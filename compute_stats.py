import re
import math
import csv

tex_file = r"k:\1\Preparation_of_Papers_for_IEEE_ACCESS\access.tex"

with open(tex_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

models = ["gemini", "gpt", "llama", "lstm", "transformer"]
current_model = None
current_stock = None
current_arch = None

results = {}

in_table = False
in_appendix = False

for line in lines:
    if r'\appendix' in line:
        in_appendix = True
        
    if not in_appendix:
        continue

    if r'\label{tab:full_forecast_' in line:
        m = re.search(r'tab:full_forecast_([a-z_]+)', line)
        if m:
            raw_model = m.group(1).upper()
            if raw_model == 'LSTM':
                current_model = 'LSTM'
            elif raw_model == 'TRANSFORMER':
                current_model = 'TRANSFORMER'
            elif raw_model in ['GEMINI', 'GPT', 'LLAMA']:
                current_model = raw_model
            elif raw_model.endswith('_LSTM'):
                current_model = f"{raw_model.split('_')[0]} + LSTM"
            elif raw_model.endswith('_TRANS'):
                current_model = f"{raw_model.split('_')[0]} + TRANSFORMER"
            else:
                current_model = raw_model
                
            if current_model not in results:
                results[current_model] = {}
                
    if r'\begin{longtable}' in line:
        in_table = True
        
    if in_table:
        m_stock = re.search(r'\\multirow\{\d+\}\{\*\}\{\\textbf\{([A-Z]+)\}', line)
        if m_stock:
            current_stock = m_stock.group(1)
            
        m_arch = re.search(r'&\s*\\textbf\{([A-Za-z\s]+)\}', line)
        if m_arch and current_model:
            arch_raw = m_arch.group(1).strip()
            # Normalize Round Robin
            if arch_raw.replace(" ", "").upper() == "ROUNDROBIN":
                current_arch = "Round Robin"
            else:
                current_arch = arch_raw
                
            if current_arch not in results[current_model]:
                results[current_model][current_arch] = {
                    'Short-term': {'abs_err': [], 'pct_err': [], 'sq_err': []},
                    'Medium-term': {'abs_err': [], 'pct_err': [], 'sq_err': []},
                    'Long-term': {'abs_err': [], 'pct_err': [], 'sq_err': []}
                }
                
        if current_model and current_stock and current_arch and r'\\' in line and line.strip().startswith('&'):
            parts = line.split('&')
            if len(parts) >= 15:
                shift = 1 if parts[1].strip() == '' else 0
                
                try:
                    s_pred = float(re.search(r'([\d\.]+)', parts[4 + shift]).group(1))
                    s_act = float(re.search(r'([\d\.]+)', parts[5 + shift]).group(1))
                    
                    m_pred = float(re.search(r'([\d\.]+)', parts[8 + shift]).group(1))
                    m_act = float(re.search(r'([\d\.]+)', parts[9 + shift]).group(1))
                    
                    l_pred = float(re.search(r'([\d\.]+)', parts[12 + shift]).group(1))
                    l_act = float(re.search(r'([\d\.]+)', parts[13 + shift]).group(1))
                    
                    if s_act > 0:
                        results[current_model][current_arch]['Short-term']['abs_err'].append(abs(s_pred - s_act))
                        results[current_model][current_arch]['Short-term']['pct_err'].append(abs(s_pred - s_act) / s_act)
                        results[current_model][current_arch]['Short-term']['sq_err'].append((s_pred - s_act)**2)
                        
                    if m_act > 0:
                        results[current_model][current_arch]['Medium-term']['abs_err'].append(abs(m_pred - m_act))
                        results[current_model][current_arch]['Medium-term']['pct_err'].append(abs(m_pred - m_act) / m_act)
                        results[current_model][current_arch]['Medium-term']['sq_err'].append((m_pred - m_act)**2)
                        
                    if l_act > 0:
                        results[current_model][current_arch]['Long-term']['abs_err'].append(abs(l_pred - l_act))
                        results[current_model][current_arch]['Long-term']['pct_err'].append(abs(l_pred - l_act) / l_act)
                        results[current_model][current_arch]['Long-term']['sq_err'].append((l_pred - l_act)**2)
                        
                except Exception as e:
                    pass

    if r'\end{longtable}' in line:
        in_table = False
        current_stock = None
        current_arch = None

csv_path = r"k:\1\Preparation_of_Papers_for_IEEE_ACCESS\metrics_summary.csv"
with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Model', 'Architecture', 'Horizon', 'MAE', 'MAPE (%)', 'RMSE'])
    
    for model in sorted(results.keys()):
        for arch in sorted(results[model].keys()):
            for horizon in ['Short-term', 'Medium-term', 'Long-term']:
                data = results[model][arch][horizon]
                n = len(data['abs_err'])
                if n > 0:
                    mae = sum(data['abs_err']) / n
                    mape = (sum(data['pct_err']) / n) * 100
                    rmse = math.sqrt(sum(data['sq_err']) / n)
                    
                    writer.writerow([model, arch, horizon, f"{mae:.3f}", f"{mape:.3f}", f"{rmse:.3f}"])

print(f"Fixed spacing and rewritten to {csv_path}")
