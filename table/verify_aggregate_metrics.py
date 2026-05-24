import re
import pandas as pd
import numpy as np
import os

def clean_value(val):
    # Remove LaTeX formatting like \cellcolor{...}, \textbf{...}, \textit{...}, spaces, etc.
    val = val.strip()
    val = re.sub(r'\\cellcolor\{[^}]+\}', '', val)
    val = re.sub(r'\\textbf\{([^}]+)\}', r'\1', val)
    val = re.sub(r'\\textit\{([^}]+)\}', r'\1', val)
    val = re.sub(r'\\textcolor\{[^}]+\}\{([^}]+)\}', r'\1', val)
    val = val.replace('\\', '').replace('%', '').strip()
    if not val or val == '-':
        return None
    try:
        return float(val)
    except ValueError:
        return None

def parse_latex_table(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where 'tab:full_performance_all' or 'Performance Comparison Across Forecasting Horizons' is located
    label_match = re.search(r'\\label\{tab:full_performance_all\}', content)
    if not label_match:
        label_match = re.search(r'Performance Comparison Across Forecasting Horizons', content)
        
    if not label_match:
        print("Could not find label tab:full_performance_all or caption in the file.")
        return []
        
    pos = label_match.start()
    
    # Search backwards for \begin{longtable}
    begin_matches = list(re.finditer(r'\\begin\{longtable\}', content[:pos]))
    if not begin_matches:
        print("Could not find \\begin{longtable} before label.")
        return []
    start_pos = begin_matches[-1].start()
    
    # Search forwards for \end{longtable}
    end_match = re.search(r'\\end\{longtable\}', content[pos:])
    if not end_match:
        print("Could not find \\end{longtable} after label.")
        return []
    end_pos = pos + end_match.end()
    
    table_content = content[start_pos:end_pos]
    lines = table_content.split('\n')
    
    records = []
    
    current_horizon = None
    current_stock = None
    
    for line in lines:
        line = line.strip()
        
        # Skip comment lines and formatting lines
        if not line or line.startswith('%') or line.startswith('\\toprule') or line.startswith('\\midrule') or line.startswith('\\bottomrule') or line.startswith('\\end{longtable}') or line.startswith('\\begin{longtable}') or line.startswith('\\caption') or line.startswith('\\label') or line.startswith('\\hfill') or line.startswith('\\cmidrule'):
            continue
            
        # Determine Horizon
        if 'Short-term' in line:
            current_horizon = 'Short-term'
        elif 'Medium-term' in line:
            current_horizon = 'Medium-term'
        elif 'Long-term' in line:
            current_horizon = 'Long-term'
            
        # Determine Stock
        m_stock = re.search(r'\\multirow\{\d+\}\{\*\}\{\\textbf\{([A-Z]+)\}\}', line)
        if m_stock:
            current_stock = m_stock.group(1)
            
        # Check if line contains architecture row
        parts = [p.strip() for p in line.split('&')]
        if len(parts) >= 21:
            arch_raw = parts[2]
            current_arch = None
            if 'Hierarchical' in arch_raw:
                current_arch = 'Hierarchical'
            elif 'Round' in arch_raw:
                current_arch = 'Round Robin'
            elif 'Ensemble' in arch_raw:
                current_arch = 'Ensemble'
                
            if current_arch:
                # LSTM is columns index 3 to 11 (inclusive)
                lstm_vals = [clean_value(v) for v in parts[3:12]]
                # Transformer is columns index 12 to 20 (inclusive)
                trans_vals = [clean_value(v) for v in parts[12:21]]
                
                if len(lstm_vals) == 9 and len(trans_vals) == 9:
                    records.append({
                        'Horizon': current_horizon,
                        'Stock': current_stock,
                        'Architecture': current_arch,
                        'Model': 'LSTM',
                        'Llama_MAE': lstm_vals[0], 'Llama_RMSE': lstm_vals[1], 'Llama_MAPE': lstm_vals[2],
                        'GPT_MAE': lstm_vals[3], 'GPT_RMSE': lstm_vals[4], 'GPT_MAPE': lstm_vals[5],
                        'Gemini_MAE': lstm_vals[6], 'Gemini_RMSE': lstm_vals[7], 'Gemini_MAPE': lstm_vals[8]
                    })
                    records.append({
                        'Horizon': current_horizon,
                        'Stock': current_stock,
                        'Architecture': current_arch,
                        'Model': 'Transformer',
                        'Llama_MAE': trans_vals[0], 'Llama_RMSE': trans_vals[1], 'Llama_MAPE': trans_vals[2],
                        'GPT_MAE': trans_vals[3], 'GPT_RMSE': trans_vals[4], 'GPT_MAPE': trans_vals[5],
                        'Gemini_MAE': trans_vals[6], 'Gemini_RMSE': trans_vals[7], 'Gemini_MAPE': trans_vals[8]
                    })
                else:
                    print(f"Warning: parts length mismatch for row: {line}")
                    print(f"LSTM values parsed ({len(lstm_vals)}): {lstm_vals}")
                    print(f"Transformer values parsed ({len(trans_vals)}): {trans_vals}")
                    
    return records

def calculate_aggregates(records):
    df = pd.DataFrame(records)
    if df.empty:
        print("No data parsed.")
        return
        
    print(f"Successfully parsed {len(df)} records ({len(df)//2} rows of LSTM & Transformer each).")
    
    # Melting columns to compute aggregates
    melted = []
    for _, row in df.iterrows():
        for llm in ['Llama', 'GPT', 'Gemini']:
            melted.append({
                'Horizon': row['Horizon'],
                'Stock': row['Stock'],
                'Architecture': row['Architecture'],
                'Model': row['Model'],
                'LLM': llm,
                'MAE': row[f'{llm}_MAE'],
                'RMSE': row[f'{llm}_RMSE'],
                'MAPE': row[f'{llm}_MAPE']
            })
            
    mdf = pd.DataFrame(melted)
    
    # Verify that MAE and MAPE have no NaN values
    missing_mae = mdf['MAE'].isnull().sum()
    missing_mape = mdf['MAPE'].isnull().sum()
    if missing_mae > 0 or missing_mape > 0:
        print(f"Warning: {missing_mae} missing MAE values and {missing_mape} missing MAPE values found!")
        print("Here are some of the records with missing values:")
        print(mdf[mdf['MAE'].isnull() | mdf['MAPE'].isnull()].head(15))
    
    print("\n--- CALCULATING OVERALL MODEL PERFORMANCE ---")
    overall_model = mdf.groupby('Model')[['MAE', 'MAPE']].mean()
    print(overall_model)
    
    print("\n--- CALCULATING ARCHITECTURE PERFORMANCE (UNDER LSTM) ---")
    lstm_arch = mdf[mdf['Model'] == 'LSTM'].groupby('Architecture')[['MAE', 'MAPE']].mean()
    print(lstm_arch)
    
    print("\n--- DETAILED SUMMARY TABLE ---")
    print(f"LSTM Overall: Mean MAE = {overall_model.loc['LSTM', 'MAE']:.4f}, Mean MAPE = {overall_model.loc['LSTM', 'MAPE']:.4f}%")
    print(f"Transformer Overall: Mean MAE = {overall_model.loc['Transformer', 'MAE']:.4f}, Mean MAPE = {overall_model.loc['Transformer', 'MAPE']:.4f}%")
    
    print(f"Hierarchical under LSTM: Mean MAE = {lstm_arch.loc['Hierarchical', 'MAE']:.4f}, Mean MAPE = {lstm_arch.loc['Hierarchical', 'MAPE']:.4f}%")
    print(f"Round Robin under LSTM: Mean MAE = {lstm_arch.loc['Round Robin', 'MAE']:.4f}, Mean MAPE = {lstm_arch.loc['Round Robin', 'MAPE']:.4f}%")
    print(f"Ensemble under LSTM: Mean MAE = {lstm_arch.loc['Ensemble', 'MAE']:.4f}, Mean MAPE = {lstm_arch.loc['Ensemble', 'MAPE']:.4f}%")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(base_dir, 'access.tex')
    records = parse_latex_table(filepath)
    calculate_aggregates(records)
