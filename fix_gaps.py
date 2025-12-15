import re

def fix_gaps_in_file():
    with open('access.tex', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the extra values after / in Gap columns
    patterns = [
        (r'(\+\d+\.?\d*) / \\.*?\}', r'\1}'),
        (r'(-\d+\.?\d*) / \\.*?\}', r'\1}'),
        (r'(\+\d+\.?\d*) / \(.*?\)', r'\1'),
        (r'(-\d+\.?\d*) / \(.*?\)', r'\1'),
    ]
    
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    # Fix simple +/- format to proper LaTeX format
    content = re.sub(r'& (\+\d+\.?\d*) &', r'& \\textcolor{green}{\\(\\uparrow\\)\1} &', content)
    content = re.sub(r'& (-\d+\.?\d*) &', r'& \\textcolor{red}{\\(\\downarrow\\)\1} &', content)
    
    with open('access.tex', 'w', encoding='utf-8') as f:
        f.write(content)

fix_gaps_in_file()
print("Fixed all Gap calculations")