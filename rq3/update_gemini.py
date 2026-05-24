import re
import os

# Gemini BASELINE
data = {
    'CMG_Baseline_Long': {'pred': [51.11, 29.06, 31.6, 40.77], 'actual': [41.9, 35.1, 35.2, 35.2]},
    'CMG_Baseline_Medium': {'pred': [47.47, 46.48, 44.91, 43.89], 'actual': [40.8, 41.3, 39.6, 39.3]},
    'CMG_Baseline_Short': {'pred': [49.7, 29.81, 45.0, 44.46], 'actual': [41.85, 37.3, 38.75, 38.75]},
    'DGC_Baseline_Long': {'pred': [107.62, 78.38, 61.95, 56.27], 'actual': [96.0, 93.0, 70.2, 70.2]},
    'DGC_Baseline_Medium': {'pred': [108.2, 107.49, 106.67, 103.04], 'actual': [99.5, 93.6, 94.6, 95.0]},
    'DGC_Baseline_Short': {'pred': [116.27, 103.39, 112.49, 78.48], 'actual': [99.3, 93.2, 92.4, 92.4]},
    'DXG_Baseline_Long': {'pred': [19.44, 19.59, 21.13, 21.22], 'actual': [21.2, 16.3, 17.8, 17.8]},
    'DXG_Baseline_Medium': {'pred': [26.58, 17.67, 23.12, 16.87], 'actual': [24.05, 21.2, 20.15, 20.1]},
    'DXG_Baseline_Short': {'pred': [19.66, 24.9, 17.19, 23.08], 'actual': [24.0, 22.6, 20.9, 20.9]},
    'FPT_Baseline_Long': {'pred': [118.85, 113.8, 80.35, 113.37], 'actual': [103.9, 93.8, 93.9, 93.9]},
    'FPT_Baseline_Medium': {'pred': [116.1, 86.54, 89.48, 118.73], 'actual': [101.9, 102.7, 103.3, 100.9]},
    'FPT_Baseline_Short': {'pred': [90.02, 104.49, 86.85, 105.66], 'actual': [105.0, 88.1, 97.7, 97.7]},
    'HPG_Baseline_Long': {'pred': [20.94, 23.08, 32.25, 31.25], 'actual': [26.7, 26.25, 26.7, 26.7]},
    'HPG_Baseline_Medium': {'pred': [24.52, 22.43, 22.53, 22.65], 'actual': [30.35, 26.9, 26.75, 26.3]},
    'HPG_Baseline_Short': {'pred': [25.29, 25.28, 21.22, 23.04], 'actual': [29.85, 28.0, 26.4, 26.4]},
    'KDH_Baseline_Long': {'pred': [29.97, 32.05, 35.41, 28.46], 'actual': [35.85, 29.6, 32.65, 32.65]},
    'KDH_Baseline_Medium': {'pred': [27.21, 28.76, 40.78, 27.86], 'actual': [34.85, 35.85, 35.6, 34.95]},
    'KDH_Baseline_Short': {'pred': [30.68, 40.84, 40.46, 39.6], 'actual': [36.75, 33.9, 33.8, 33.8]},
    'MBB_Baseline_Long': {'pred': [26.96, 28.65, 21.88, 27.34], 'actual': [23.6, 23.75, 24.7, 24.7]},
    'MBB_Baseline_Medium': {'pred': [29.07, 19.14, 28.51, 27.08], 'actual': [26.85, 23.95, 24.0, 23.9]},
    'MBB_Baseline_Short': {'pred': [34.2, 24.05, 21.04, 19.96], 'actual': [28.25, 27.1, 24.4, 24.4]},
    'MWG_Baseline_Long': {'pred': [64.88, 66.05, 72.98, 101.11], 'actual': [82.6, 77.7, 82.9, 82.9]},
    'MWG_Baseline_Medium': {'pred': [70.13, 75.49, 71.02, 72.13], 'actual': [79.5, 83.9, 81.8, 80.2]},
    'MWG_Baseline_Short': {'pred': [93.56, 68.91, 93.06, 99.08], 'actual': [77.5, 84.5, 85.7, 85.7]},
    'TCB_Baseline_Long': {'pred': [42.56, 35.34, 38.54, 29.64], 'actual': [35.1, 32.0, 33.6, 33.6]},
    'TCB_Baseline_Medium': {'pred': [44.42, 39.85, 31.89, 39.18], 'actual': [39.0, 35.7, 35.0, 34.1]},
    'TCB_Baseline_Short': {'pred': [43.81, 35.24, 43.31, 30.25], 'actual': [39.6, 40.65, 36.1, 36.1]},
    'VCB_Baseline_Long': {'pred': [55.04, 50.75, 69.44, 47.77], 'actual': [60.7, 56.8, 57.5, 57.5]},
    'VCB_Baseline_Medium': {'pred': [80.08, 65.79, 71.71, 52.38], 'actual': [65.8, 60.6, 60.1, 60.8]},
    'VCB_Baseline_Short': {'pred': [74.74, 51.34, 52.59, 69.68], 'actual': [68.6, 61.9, 59.5, 59.5]},
    'VCS_Baseline_Long': {'pred': [40.58, 55.26, 37.83, 47.14], 'actual': [47.6, 46.5, 43.0, 43.0]},
    'VCS_Baseline_Medium': {'pred': [60.71, 37.11, 37.88, 37.61], 'actual': [50.0, 47.4, 47.1, 46.9]},
    'VCS_Baseline_Short': {'pred': [43.43, 55.76, 41.34, 42.48], 'actual': [48.8, 46.8, 46.2, 46.2]},
    'VHM_Baseline_Long': {'pred': [78.59, 104.11, 85.35, 91.06], 'actual': [99.2, 93.9, 101.5, 101.5]},
    'VHM_Baseline_Medium': {'pred': [113.37, 94.2, 109.41, 113.85], 'actual': [104.5, 104.0, 100.2, 99.6]},
    'VHM_Baseline_Short': {'pred': [92.87, 140.94, 94.85, 131.42], 'actual': [102.3, 116.0, 114.5, 114.5]},
}

def format_gap_new(start, pred, act):
    error = round(abs(act - pred), 2)
    if error == 0:
        return f"\\textcolor{{yellow}}{{0.00}}"
    
    # Determine trend (1 for up, -1 for down, 0 for flat)
    trend_p = 1 if pred > start else (-1 if pred < start else 0)
    trend_a = 1 if act > start else (-1 if act < start else 0)
    
    if trend_p == trend_a:
        # Same direction -> Green +
        return f"\\textcolor{{green}}{{\\(\\uparrow\\)+{error:.2f}}}"
    else:
        # Opposite direction -> Red -
        return f"\\textcolor{{red}}{{\\(\\downarrow\\)-{error:.2f}}}"

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    current_stock = None
    current_arch = None
    row_idx = 0
    new_lines = []

    in_table = False
    for line in lines:
        if '\\begin{longtable}' in line:
            in_table = True
        
        if in_table:
            m_stock = re.search(r'\\multirow\{6\}\{\*\}\{\\textbf\{([A-Z]+)\}', line)
            if m_stock:
                current_stock = m_stock.group(1)
            
            m_arch = re.search(r'&\s*\\textbf\{([A-Za-z\s]+)\}', line)
            if m_arch:
                current_arch = m_arch.group(1).strip()
                row_idx = 0
            
            if current_stock and current_arch and r'\\' in line and line.strip().startswith('&'):
                key_prefix = f"{current_stock}_{current_arch}"
                short_key = f"{key_prefix}_Short"
                
                if short_key in data and row_idx < 4:
                    parts = line.split('&')
                    
                    if len(parts) >= 15:
                        shift = 1 if parts[1].strip() == '' else 0
                        
                        try:
                            start_price = float(parts[2 + shift].strip())
                        except ValueError:
                            row_idx += 1
                            continue
                            
                        if start_price > 1000:
                            start_price = start_price / 1000.0
                            parts[2 + shift] = f" {start_price:.2f} "
                        
                        # Update Short
                        short_pred = data[f"{key_prefix}_Short"]['pred'][row_idx]
                        short_act = data[f"{key_prefix}_Short"]['actual'][row_idx]
                        short_gap = format_gap_new(start_price, short_pred, short_act)
                        parts[4 + shift] = f" {short_pred:.2f} "
                        parts[5 + shift] = f" {short_act:.2f} "
                        parts[6 + shift] = f" {short_gap} "
                        
                        # Update Medium
                        med_pred = data[f"{key_prefix}_Medium"]['pred'][row_idx]
                        med_act = data[f"{key_prefix}_Medium"]['actual'][row_idx]
                        med_gap = format_gap_new(start_price, med_pred, med_act)
                        parts[8 + shift] = f" {med_pred:.2f} "
                        parts[9 + shift] = f" {med_act:.2f} "
                        parts[10 + shift] = f" {med_gap} "
                        
                        # Update Long
                        long_pred = data[f"{key_prefix}_Long"]['pred'][row_idx]
                        long_act = data[f"{key_prefix}_Long"]['actual'][row_idx]
                        long_gap = format_gap_new(start_price, long_pred, long_act)
                        parts[12 + shift] = f" {long_pred:.2f} "
                        parts[13 + shift] = f" {long_act:.2f} "
                        parts[14 + shift] = f" {long_gap} \\\\\n"
                        
                        line = "&".join(parts)
                    
                    row_idx += 1

        new_lines.append(line)
        
        if '\\end{longtable}' in line:
            in_table = False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

file_path = r"k:\\1\\Preparation_of_Papers_for_IEEE_ACCESS\\rq3\\gemini.tex"
if os.path.exists(file_path):
    process_file(file_path)
    print(f"Successfully processed {os.path.basename(file_path)}")
else:
    print(f"File not found: {file_path}")
