import re

table_data = {}
with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\table_content.txt', 'r', encoding='utf-8') as f:
    current_horizon = ""
    for line in f:
        line = line.strip()
        if not line or line.startswith('%') or line.startswith('\\') and not line.startswith('\\multirow') and not line.startswith('&'):
            if line.startswith('&') and ('Round Robin' in line or 'Ensemble' in line or 'Hierarchical' in line):
                pass
            else:
                continue
                
        clean_line = re.sub(r'\\cellcolor\{[^\}]+\}', '', line)
        clean_line = re.sub(r'\\textbf\{([^\}]+)\}', r'\1', clean_line)
        clean_line = clean_line.replace(r'\\', '')
        
        parts = [p.strip() for p in clean_line.split('&')]
        if len(parts) >= 21:
            if parts[0] != '':
                if 'multirow' in parts[0]:
                    h_match = re.search(r'\}\{([^}]+)\}', parts[0])
                    if h_match: current_horizon = h_match.group(1).replace(r'\textbf{', '').replace('}', '').strip()
                else:
                    current_horizon = parts[0]
            
            h = 'Short-term' if 'Short' in current_horizon else 'Medium-term' if 'Medium' in current_horizon else 'Long-term' if 'Long' in current_horizon else current_horizon
            if h not in table_data: table_data[h] = []
            table_data[h].append(1)

print(table_data.keys())
