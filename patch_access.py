import re

# Parse gemini_lstm.txt
data = {}
with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\ketqua\gemini_lstm.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

current_horizon = None
current_stock = None
for line in lines:
    line = line.strip()
    if line == 'SHORT-TERM PERFORMANCE':
        current_horizon = 'Short-term'
    elif line == 'MEDIUM-TERM PERFORMANCE':
        current_horizon = 'Medium-term'
    elif line == 'LONG-TERM PERFORMANCE':
        current_horizon = 'Long-term'
    elif re.match(r'^[A-Z]{3}:$', line):
        current_stock = line[:-1]
    elif '| MAE:' in line:
        parts = line.split('|')
        arch = parts[0].strip()
        if arch == 'RoundRobin': arch = 'Round Robin'
        elif arch == 'Ensemble': arch = 'Ensemble'
        mae = parts[1].split(':')[1].strip()
        rmse = parts[2].split(':')[1].strip()
        mape = parts[3].split(':')[1].strip().replace('%', '')
        if current_horizon and current_stock:
            data.setdefault(current_horizon, {}).setdefault(current_stock, {})[arch] = (mae, rmse, mape)

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

    if line.strip().startswith('& \multirow{3}{*}{\textbf{') or line.strip().startswith('\multirow{36}{*}{\textbf{'):
        m = re.search(r'\\textbf\{([A-Z]{3})\}', line)
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
                    return re.sub(r'[0-9]+\.[0-9]+', new_val, part)
                
                parts[-12] = replace_val(parts[-12], mae)
                parts[-11] = replace_val(parts[-11], rmse)
                parts[-10] = replace_val(parts[-10], mape)
                
                line = '&'.join(parts)
    out_lines.append(line)

with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\access.tex', 'w', encoding='utf-8') as f:
    f.writelines(out_lines)

print("Patch applied.")
