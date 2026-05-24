import re
import numpy as np

with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\table_content.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

data = []
current_horizon = ''

for line in lines:
    line = line.strip()
    if not line or line.startswith('%') or line.startswith(r'\toprule') or line.startswith(r'\midrule') or line.startswith(r'\bottomrule') or line.startswith(r'\cmidrule') or line.startswith(r'\multirow') or line.startswith(r'\multicolumn') or line.startswith(r'\caption') or line.startswith(r'\label') or line.startswith(r'\begin') or line.startswith(r'\end') or line.startswith('&'):
        # wait, some rows start with & like: & & Round Robin & ...
        if line.startswith('&') and 'Round Robin' in line or 'Ensemble' in line or 'Hierarchical' in line:
            pass # we need to parse this
        else:
            if 'Short-term' in line and '&' not in line: continue
            if 'Medium-term' in line and '&' not in line: continue
            if 'Long-term' in line and '&' not in line: continue
            if 'textbf' in line and 'MAE' in line: continue
            
    # Remove latex commands like \cellcolor{...}, \textbf{...}
    clean_line = re.sub(r'\\cellcolor\{[^\}]+\}', '', line)
    clean_line = re.sub(r'\\textbf\{([^\}]+)\}', r'\1', clean_line)
    
    parts = [p.strip() for p in clean_line.split('&')]
    if len(parts) >= 21:
        if parts[0]:
            current_horizon = parts[0].replace('multirow{36}{*}{', '').replace('}', '').strip()
        
        stock = parts[1].replace('multirow{3}{*}{', '').replace('}', '').strip()
        arch = parts[2].strip()
        
        try:
            values = [float(x.replace(r'\\', '').strip()) for x in parts[3:21]]
            data.append({
                'Horizon': current_horizon,
                'Stock': stock,
                'Architecture': arch,
                'values': values
            })
        except ValueError as e:
            pass

results = {}
for row in data:
    horizon = row['Horizon']
    if 'Short-term' in horizon: horizon = 'Short-term'
    elif 'Medium-term' in horizon: horizon = 'Medium-term'
    elif 'Long-term' in horizon: horizon = 'Long-term'
        
    arch = row['Architecture']
    key = (horizon, arch)
    if key not in results:
        results[key] = []
    results[key].append(row['values'])

out = ''
for key, vals in results.items():
    avg_vals = np.mean(vals, axis=0)
    avg_vals_str = ['{:.2f}'.format(v) for v in avg_vals]
    out += f"{key[0]} | {key[1]} | {' | '.join(avg_vals_str)}\n"

with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\parsed_agg.txt', 'w', encoding='utf-8') as f:
    f.write(out)
