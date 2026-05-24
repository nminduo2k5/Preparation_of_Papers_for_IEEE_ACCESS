import os
import re

# 1. Parse table_content.txt
table_data = {}
with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\table_content.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('%') or line.startswith('\\') and not line.startswith('\\multirow') and not line.startswith('&'):
            if line.startswith('&') and ('Round Robin' in line or 'Ensemble' in line or 'Hierarchical' in line):
                pass
            else:
                continue
                
        # Clean latex
        clean_line = re.sub(r'\\cellcolor\{[^\}]+\}', '', line)
        clean_line = re.sub(r'\\textbf\{([^\}]+)\}', r'\1', clean_line)
        clean_line = clean_line.replace(r'\\', '')
        
        parts = [p.strip() for p in clean_line.split('&')]
        if len(parts) >= 21:
            if parts[0] and 'multirow' in parts[0]:
                horizon_match = re.search(r'\}\{([^}]+)\}', parts[0])
                if horizon_match:
                    current_horizon = horizon_match.group(1).strip()
            
            stock_col = parts[1]
            if 'multirow' in stock_col:
                stock_match = re.search(r'\}\{([^}]+)\}', stock_col)
                if stock_match:
                    current_stock = stock_match.group(1).strip()
            
            arch = parts[2].strip()
            
            if current_horizon not in table_data: table_data[current_horizon] = {}
            if current_stock not in table_data[current_horizon]: table_data[current_horizon][current_stock] = {}
            
            try:
                values = [float(x.replace(r'\\', '').strip()) for x in parts[3:21]]
                table_data[current_horizon][current_stock][arch] = {
                    'llama_lstm': values[0:3],
                    'gpt_lstm': values[3:6],
                    'gemini_lstm': values[6:9],
                    'llama_trans': values[9:12],
                    'gpt_trans': values[12:15],
                    'gemini_trans': values[15:18]
                }
            except ValueError:
                pass

# 2. Parse ketqua folder
raw_data = {}

def parse_ketqua_file(filepath, llm, base):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    current_horizon = None
    current_stock = None
    
    for line in lines:
        line = line.strip()
        if "SHORT-TERM PERFORMANCE" in line: current_horizon = "Short-term"
        elif "MEDIUM-TERM PERFORMANCE" in line: current_horizon = "Medium-term"
        elif "LONG-TERM PERFORMANCE" in line: current_horizon = "Long-term"
        
        # Match stock
        stock_match = re.match(r'^([A-Z]{3}):$', line)
        if stock_match:
            current_stock = stock_match.group(1)
            
        # Match arch
        arch_match = re.match(r'^(Hierarchical|RoundRobin|Ensemble)\s*\|\s*MAE:\s*([\d\.]+)\s*\|\s*RMSE:\s*([\d\.]+)\s*\|\s*MAPE:\s*([\d\.]+)%$', line)
        if arch_match and current_horizon and current_stock:
            arch = arch_match.group(1)
            if arch == 'RoundRobin': arch = 'Round Robin'
            
            mae = float(arch_match.group(2))
            rmse = float(arch_match.group(3))
            mape = float(arch_match.group(4))
            
            if current_horizon not in raw_data: raw_data[current_horizon] = {}
            if current_stock not in raw_data[current_horizon]: raw_data[current_horizon][current_stock] = {}
            if arch not in raw_data[current_horizon][current_stock]: raw_data[current_horizon][current_stock][arch] = {}
            
            key = f"{llm}_{base}"
            raw_data[current_horizon][current_stock][arch][key] = [mae, rmse, mape]

files_map = {
    'gemini_lstm.txt': ('gemini', 'lstm'),
    'gemini_trans.py.txt': ('gemini', 'trans'),
    'gpt_lstm.txt': ('gpt', 'lstm'),
    'gpt_trans.py.txt': ('gpt', 'trans'),
    'llama_lstm.txt': ('llama', 'lstm'),
    'llama_trans.txt': ('llama', 'trans')
}

ketqua_dir = r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\ketqua'
for fname, (llm, base) in files_map.items():
    parse_ketqua_file(os.path.join(ketqua_dir, fname), llm, base)

# 3. Compare
mismatches = []
for horizon in table_data:
    for stock in table_data[horizon]:
        for arch in table_data[horizon][stock]:
            t_row = table_data[horizon][stock][arch]
            
            if horizon in raw_data and stock in raw_data[horizon] and arch in raw_data[horizon][stock]:
                r_row = raw_data[horizon][stock][arch]
                
                for key in ['llama_lstm', 'gpt_lstm', 'gemini_lstm', 'llama_trans', 'gpt_trans', 'gemini_trans']:
                    t_vals = t_row[key]
                    if key in r_row:
                        r_vals = r_row[key]
                        
                        # Compare
                        for i, metric in enumerate(['MAE', 'RMSE', 'MAPE']):
                            if abs(t_vals[i] - r_vals[i]) > 0.001:
                                mismatches.append(f"{horizon} | {stock} | {arch} | {key} | {metric} : Table={t_vals[i]}, Raw={r_vals[i]}")

if len(mismatches) == 0:
    print("SUCCESS: table_content.txt perfectly matches the files in ketqua!")
else:
    print(f"FOUND {len(mismatches)} MISMATCHES:")
    for m in mismatches[:20]:
        print(m)
    if len(mismatches) > 20:
        print(f"... and {len(mismatches) - 20} more.")

