import re

tex_file = r"k:\1\Preparation_of_Papers_for_IEEE_ACCESS\table\test4.tex"
with open(tex_file, 'r', encoding='utf-8') as f:
    content = f.read()

# We want to extract actual prices for each stock.
# The table has blocks like: \multirow{12}{*}{\textbf{DXG}}
stocks = ["DXG", "FPT", "VCB", "VCS", "HPG", "TCB", "VHM", "MWG", "CMG", "KDH", "DGC", "MBB"]

actuals = {}
for stock in stocks:
    # find the block for the stock
    idx = content.find(f"\\multirow{{12}}{{*}}{{\\textbf{{{stock}}}}}")
    if idx == -1:
        continue
    
    # Extract the next 4 rows for the first architecture (Hierarchical)
    # Each row ends with \\
    # The actual prices are in columns:
    # 7 (Short Act), 11 (Med Act), 15 (Long Act)
    
    block = content[idx:idx+1500]
    lines = block.split('\\\\')
    
    short_acts = []
    med_acts = []
    long_acts = []
    
    for line in lines[:4]:
        parts = line.split('&')
        if len(parts) >= 15:
            # Short act is parts[6]
            # Med act is parts[10]
            # Long act is parts[14]
            short_act = float(re.search(r'([\d\.]+)', parts[6]).group(1))
            med_act = float(re.search(r'([\d\.]+)', parts[10]).group(1))
            long_act = float(re.search(r'([\d\.]+)', parts[14]).group(1))
            
            short_acts.append(short_act)
            med_acts.append(med_act)
            long_acts.append(long_act)
            
    actuals[stock] = {
        "Short": short_acts,
        "Medium": med_acts,
        "Long": long_acts
    }

for k, v in actuals.items():
    print(k, v)
