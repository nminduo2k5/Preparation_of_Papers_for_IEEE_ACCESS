import re
import pandas as pd
import numpy as np
#Tính bảng MAE và MAPE
def clean_value(val):
    # Remove LaTeX formatting like \textbf{...}, \textit{...}, spaces, etc.
    val = val.strip()
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

    # Find where 'tab:full_performance_all' or 'Performance Comparison Across Forecasting Horizons and LLMs' is located
    label_match = re.search(r'\\label\{tab:full_performance_all\}', content)
    if not label_match:
        label_match = re.search(r'Performance Comparison Across Forecasting Horizons and LLMs', content)
        
    if not label_match:
        print("Could not find label tab:full_performance_all in the file.")
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
    current_arch = None
    
    row_line_1 = None
    row_line_2 = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
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
            
        # Determine Architecture and get the first line (LSTM)
        # Match lines starting with & followed by Hierarchical, RoundRobin, or Ensemble
        # Note: sometimes they have spaces or \textbf
        m_arch = re.search(r'&\s*(Hierarchical|RoundRobin|Ensemble|Round\s+Robin|Ensemble\s+Voting)\s*&', line)
        if m_arch:
            arch_raw = m_arch.group(1).strip()
            if 'Hierarchical' in arch_raw:
                current_arch = 'Hierarchical'
            elif 'Round' in arch_raw:
                current_arch = 'Round Robin'
            elif 'Ensemble' in arch_raw:
                current_arch = 'Ensemble'
                
            # This line contains LSTM metrics.
            row_line_1 = line
            
            # The next line should contain Transformer metrics.
            i += 1
            if i < len(lines):
                row_line_2 = lines[i].strip()
                
            # Process the two lines
            parts_1 = [p.strip() for p in row_line_1.split('&')]
            
            try:
                arch_idx = -1
                for idx, p in enumerate(parts_1):
                    if current_arch in p or (current_arch == 'Round Robin' and 'Round' in p) or (current_arch == 'Ensemble' and 'Ensemble' in p):
                        arch_idx = idx
                        break
                
                if arch_idx != -1:
                    lstm_vals = parts_1[arch_idx+1:]
                    # Clean the values
                    cleaned_lstm = [clean_value(v) for v in lstm_vals]
                    
                    # Line 2: & Llama_MAE & Llama_RMSE & Llama_MAPE & GPT_MAE & GPT_RMSE & GPT_MAPE & Gemini_MAE & Gemini_RMSE & Gemini_MAPE \\
                    parts_2 = [p.strip() for p in row_line_2.split('&')]
                    cleaned_trans = [clean_value(v) for v in parts_2[1:]]
                    
                    # Ensure we have at least 9 values
                    if len(cleaned_lstm) >= 9 and len(cleaned_trans) >= 9:
                        # LSTM
                        records.append({
                            'Horizon': current_horizon,
                            'Stock': current_stock,
                            'Architecture': current_arch,
                            'Model': 'LSTM',
                            'Llama_MAE': cleaned_lstm[0], 'Llama_RMSE': cleaned_lstm[1], 'Llama_MAPE': cleaned_lstm[2],
                            'GPT_MAE': cleaned_lstm[3], 'GPT_RMSE': cleaned_lstm[4], 'GPT_MAPE': cleaned_lstm[5],
                            'Gemini_MAE': cleaned_lstm[6], 'Gemini_RMSE': cleaned_lstm[7], 'Gemini_MAPE': cleaned_lstm[8]
                        })
                        # Transformer
                        records.append({
                            'Horizon': current_horizon,
                            'Stock': current_stock,
                            'Architecture': current_arch,
                            'Model': 'Transformer',
                            'Llama_MAE': cleaned_trans[0], 'Llama_RMSE': cleaned_trans[1], 'Llama_MAPE': cleaned_trans[2],
                            'GPT_MAE': cleaned_trans[3], 'GPT_RMSE': cleaned_trans[4], 'GPT_MAPE': cleaned_trans[5],
                            'Gemini_MAE': cleaned_trans[6], 'Gemini_RMSE': cleaned_trans[7], 'Gemini_MAPE': cleaned_trans[8]
                        })
                    else:
                        print(f"Warning: line mismatch at {current_horizon} {current_stock} {current_arch}")
                        print(f"LSTM parts ({len(cleaned_lstm)}): {cleaned_lstm}")
                        print(f"Trans parts ({len(cleaned_trans)}): {cleaned_trans}")
            except Exception as ex:
                print(f"Error parsing row: {ex}")
                
        i += 1
        
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
        # Let's inspect where the missing values are
        print(mdf[mdf['MAE'].isnull() | mdf['MAPE'].isnull()])
    
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
    filepath = r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\access.tex'
    records = parse_latex_table(filepath)
    calculate_aggregates(records)
