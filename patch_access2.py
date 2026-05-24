import json
import re

with open('debug_data.json', 'r') as f:
    data = json.load(f)

with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\access.tex', 'r', encoding='utf-8') as f:
    tex_lines = f.readlines()

out_lines = []
in_horizon = None
in_stock = None

for line in tex_lines:
    if r'\multirow{36}{*}{\textbf{Short-term}}' in line or '% ===================== SHORT-TERM' in line:
        in_horizon = 'Short-term'
    elif r'\multirow{36}{*}{\textbf{Medium-term}}' in line or '% ===================== MEDIUM-TERM' in line:
        in_horizon = 'Medium-term'
    elif r'\multirow{36}{*}{\textbf{Long-term}}' in line or '% ===================== LONG-TERM' in line:
        in_horizon = 'Long-term'

    # Better regex to capture stock name, e.g. & \multirow{3}{*}{\textbf{HPG}} or just \multirow{3}{*}{\textbf{HPG}}
    m = re.search(r'\\multirow\{\d+\}\{\*\}\{\\textbf\{([A-Z]{3})\}\}', line)
    if m:
        in_stock = m.group(1)

    if in_horizon and in_stock and '&' in line and '\\\\' in line:
        arch = None
        if 'Hierarchical' in line: arch = 'Hierarchical'
        elif 'Round Robin' in line: arch = 'Round Robin'
        elif 'Ensemble' in line: arch = 'Ensemble'
        
        if arch and arch in data.get(in_horizon, {}).get(in_stock, {}):
            mae, rmse, mape = data[in_horizon][in_stock][arch]
            parts = line.split('&')
            if len(parts) >= 20:
                def replace_val(part, new_val):
                    # Replace only the first sequence of numbers + decimal. 
                    # If it has \textbf{1.23}, we keep \textbf{}
                    return re.sub(r'[0-9]+\.[0-9]+', new_val, part, count=1)
                
                parts[-12] = replace_val(parts[-12], mae)
                parts[-11] = replace_val(parts[-11], rmse)
                parts[-10] = replace_val(parts[-10], mape)
                
                line = '&'.join(parts)
    out_lines.append(line)

with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\access.tex', 'w', encoding='utf-8') as f:
    f.writelines(out_lines)

print("Patch applied.")
