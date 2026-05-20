import re

with open('k:/1/Preparation_of_Papers_for_IEEE_ACCESS/access.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
in_longtable = False
current_stock = None
stock_block_count = 0

for i, line in enumerate(lines):
    if r'\begin{longtable}' in line:
        in_longtable = True
        current_stock = None
    elif r'\end{longtable}' in line:
        in_longtable = False
        current_stock = None
        
    if in_longtable:
        match = re.search(r'\\multirow\{4\}\{\*\}\{\\textbf\{([A-Z]+)\}\}', line)
        if match:
            stock = match.group(1)
            if stock != current_stock:
                current_stock = stock
                stock_block_count = 1
                line = line.replace(r'\multirow{4}', r'\multirow{12}')
                new_lines.append(line)
            else:
                stock_block_count += 1
                # Replace the preceding \midrule with \cmidrule(lr){2-16}
                for j in range(len(new_lines)-1, -1, -1):
                    if r'\midrule' in new_lines[j]:
                        new_lines[j] = new_lines[j].replace(r'\midrule', r'\cmidrule(lr){2-16}')
                        break
                # Do not append this \multirow line
                continue
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open('k:/1/Preparation_of_Papers_for_IEEE_ACCESS/access.tex', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Tables optimized successfully.")
