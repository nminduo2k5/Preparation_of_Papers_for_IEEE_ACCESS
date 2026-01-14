import re

def calculate_gap(pred, act):
    """Calculate absolute gap |Act - Pred|"""
    return abs(float(act) - float(pred))

def process_latex_table(content):
    """Process LaTeX table and update Gap values with |Act - Pred|"""
    
    # Pattern to match table rows with Pred, Act, and Gap values
    pattern = r'(\d+\.?\d*)\s*&\s*(\d+\.?\d*)\s*&\s*\\textcolor\{[^}]+\}\{[^}]*\}'
    
    def replace_gap(match):
        pred = float(match.group(1))
        act = float(match.group(2))
        gap = calculate_gap(pred, act)
        
        # Format gap value
        gap_str = f"{gap:.2f}"
        
        # Return the replacement with absolute gap value
        return f"{pred} & {act} & {gap_str}"
    
    # Find and replace all Gap values
    lines = content.split('\n')
    updated_lines = []
    
    for line in lines:
        # Look for lines with Pred & Act & Gap pattern
        if '&' in line and 'textcolor' in line:
            # Extract numbers before textcolor
            parts = line.split('&')
            if len(parts) >= 3:
                # Find Pred and Act values (usually the last two numbers before textcolor)
                pred_part = parts[-3].strip()
                act_part = parts[-2].strip()
                
                # Extract numeric values
                pred_match = re.search(r'(\d+\.?\d*)$', pred_part)
                act_match = re.search(r'(\d+\.?\d*)$', act_part)
                
                if pred_match and act_match:
                    pred = float(pred_match.group(1))
                    act = float(act_match.group(1))
                    gap = calculate_gap(pred, act)
                    
                    # Replace the textcolor part with simple gap value
                    gap_str = f"{gap:.2f}"
                    line = re.sub(r'\\textcolor\{[^}]+\}\{[^}]*\}', gap_str, line)
        
        updated_lines.append(line)
    
    return '\n'.join(updated_lines)

# Read the current file content
with open(r'c:\Users\HP\Desktop\Preparation_of_Papers_for_IEEE_ACCESS\access.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Process and update the content
updated_content = process_latex_table(content)

# Write back to file
with open(r'c:\Users\HP\Desktop\Preparation_of_Papers_for_IEEE_ACCESS\access_updated.tex', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("Gap values have been updated to |Act - Pred| format")