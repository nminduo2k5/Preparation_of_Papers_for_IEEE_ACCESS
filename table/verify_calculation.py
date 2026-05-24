import numpy as np
import pandas as pd
import os

# Define the file paths for each of the 6 configurations using relative paths
base_dir = os.path.dirname(os.path.abspath(__file__))
CONFIGS = [
    {'Model': 'LSTM', 'LLM': 'Llama', 'filepath': os.path.join(base_dir, 'update_table2.py')},
    {'Model': 'LSTM', 'LLM': 'GPT', 'filepath': os.path.join(base_dir, 'update_table0_1.py')},
    {'Model': 'LSTM', 'LLM': 'Gemini', 'filepath': os.path.join(base_dir, 'update_table0.py')},
    {'Model': 'Transformer', 'LLM': 'Llama', 'filepath': os.path.join(base_dir, 'update_table3.py')},
    {'Model': 'Transformer', 'LLM': 'GPT', 'filepath': os.path.join(base_dir, 'update_table1.py')},
    {'Model': 'Transformer', 'LLM': 'Gemini', 'filepath': os.path.join(base_dir, 'update_table0_5.py')},
]

def load_data_from_file(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    globals_dict = {
        'process_file': lambda *args, **kwargs: None,
        '__name__': 'mock'
    }
    exec(content, globals_dict)
    return globals_dict['data']

def calculate_metrics(predicted, actual):
    predicted = np.array(predicted)
    actual = np.array(actual)
    mae = np.mean(np.abs(predicted - actual))
    rmse = np.sqrt(np.mean((predicted - actual) ** 2))
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    return mae, rmse, mape

def main():
    records = []
    for cfg in CONFIGS:
        try:
            data_dict = load_data_from_file(cfg['filepath'])
            print(f"Loaded {len(data_dict)} keys for {cfg['Model']} + {cfg['LLM']}.")
            for key, values in data_dict.items():
                parts = key.split('_')
                stock, arch, horizon = parts[0], parts[1], parts[2]
                mae, rmse, mape = calculate_metrics(values['pred'], values['actual'])
                records.append({
                    'Model': cfg['Model'],
                    'LLM': cfg['LLM'],
                    'Stock': stock,
                    'Architecture': arch,
                    'Horizon': horizon,
                    'MAE': mae,
                    'RMSE': rmse,
                    'MAPE': mape
                })
        except Exception as e:
            print(f"Error loading {cfg['Model']} + {cfg['LLM']} from {cfg['filepath']}: {e}")
            return
            
    df = pd.DataFrame(records)
    print("=" * 80)
    print("ALL CONFIGURATIONS LOADED AND COMPUTED")
    print("=" * 80)
    
    print("\n--- BASE MODEL (OVERALL) ---")
    overall_model = df.groupby('Model')[['MAE', 'MAPE']].mean()
    print(overall_model)
    
    print("\n--- ARCHITECTURE (UNDER LSTM) ---")
    lstm_arch = df[df['Model'] == 'LSTM'].groupby('Architecture')[['MAE', 'MAPE']].mean()
    print(lstm_arch)

if __name__ == '__main__':
    main()
