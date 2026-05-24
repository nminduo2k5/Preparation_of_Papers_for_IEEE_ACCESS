import numpy as np
import re

table_data = {}
with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\table_content.txt', 'r', encoding='utf-8') as f:
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
            print("Row:", parts[0:3])

