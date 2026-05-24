import json

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
    elif line.endswith(':'):
        import re
        if re.match(r'^[A-Z]{3}:$', line):
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

with open('debug_data.json', 'w') as f:
    json.dump(data, f, indent=2)
