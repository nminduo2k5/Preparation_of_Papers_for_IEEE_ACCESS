import re
import os

# Llama BASELINE
data = {
    'CMG_Baseline_Long': {'pred': [47.66, 39.06, 28.73, 41.8], 'actual': [41.9, 35.1, 35.2, 35.2]},
    'CMG_Baseline_Medium': {'pred': [34.69, 32.37, 33.71, 32.52], 'actual': [40.8, 41.3, 39.6, 39.3]},
    'CMG_Baseline_Short': {'pred': [36.88, 43.08, 31.94, 31.86], 'actual': [41.85, 37.3, 38.75, 38.75]},
    'DGC_Baseline_Long': {'pred': [83.85, 103.99, 55.14, 62.33], 'actual': [96.0, 93.0, 70.2, 70.2]},
    'DGC_Baseline_Medium': {'pred': [83.82, 108.71, 111.82, 113.73], 'actual': [99.5, 93.6, 94.6, 95.0]},
    'DGC_Baseline_Short': {'pred': [110.36, 84.31, 107.23, 72.54], 'actual': [99.3, 93.2, 92.4, 92.4]},
    'DXG_Baseline_Long': {'pred': [23.18, 19.2, 20.57, 15.03], 'actual': [21.2, 16.3, 17.8, 17.8]},
    'DXG_Baseline_Medium': {'pred': [26.29, 17.16, 16.24, 22.66], 'actual': [24.05, 21.2, 20.15, 20.1]},
    'DXG_Baseline_Short': {'pred': [26.15, 25.46, 23.92, 23.0], 'actual': [24.0, 22.6, 20.9, 20.9]},
    'FPT_Baseline_Long': {'pred': [117.23, 110.53, 107.69, 75.51], 'actual': [103.9, 93.8, 93.9, 93.9]},
    'FPT_Baseline_Medium': {'pred': [122.02, 89.78, 86.35, 116.35], 'actual': [101.9, 102.7, 103.3, 100.9]},
    'FPT_Baseline_Short': {'pred': [126.89, 98.6, 84.76, 80.0], 'actual': [105.0, 88.1, 97.7, 97.7]},
    'HPG_Baseline_Long': {'pred': [23.13, 23.87, 28.96, 23.97], 'actual': [26.7, 26.25, 26.7, 26.7]},
    'HPG_Baseline_Medium': {'pred': [33.41, 23.97, 22.32, 23.06], 'actual': [30.35, 26.9, 26.75, 26.3]},
    'HPG_Baseline_Short': {'pred': [26.06, 33.74, 28.96, 30.63], 'actual': [29.85, 28.0, 26.4, 26.4]},
    'KDH_Baseline_Long': {'pred': [29.75, 24.6, 26.45, 36.14], 'actual': [35.85, 29.6, 32.65, 32.65]},
    'KDH_Baseline_Medium': {'pred': [27.89, 28.78, 40.66, 42.51], 'actual': [34.85, 35.85, 35.6, 34.95]},
    'KDH_Baseline_Short': {'pred': [39.81, 37.96, 38.43, 39.32], 'actual': [36.75, 33.9, 33.8, 33.8]},
    'MBB_Baseline_Long': {'pred': [21.64, 21.27, 22.48, 20.33], 'actual': [23.6, 23.75, 24.7, 24.7]},
    'MBB_Baseline_Medium': {'pred': [29.2, 27.95, 28.75, 19.07], 'actual': [26.85, 23.95, 24.0, 23.9]},
    'MBB_Baseline_Short': {'pred': [31.56, 32.07, 29.18, 27.61], 'actual': [28.25, 27.1, 24.4, 24.4]},
    'MWG_Baseline_Long': {'pred': [93.52, 61.11, 98.93, 76.02], 'actual': [82.6, 77.7, 82.9, 82.9]},
    'MWG_Baseline_Medium': {'pred': [65.18, 93.88, 68.92, 63.47], 'actual': [79.5, 83.9, 81.8, 80.2]},
    'MWG_Baseline_Short': {'pred': [85.91, 92.42, 98.17, 101.28], 'actual': [77.5, 84.5, 85.7, 85.7]},
    'TCB_Baseline_Long': {'pred': [40.12, 27.77, 28.46, 36.97], 'actual': [35.1, 32.0, 33.6, 33.6]},
    'TCB_Baseline_Medium': {'pred': [43.37, 29.41, 32.04, 28.83], 'actual': [39.0, 35.7, 35.0, 34.1]},
    'TCB_Baseline_Short': {'pred': [33.0, 45.79, 30.1, 43.98], 'actual': [39.6, 40.65, 36.1, 36.1]},
    'VCB_Baseline_Long': {'pred': [49.57, 68.09, 62.23, 50.32], 'actual': [60.7, 56.8, 57.5, 57.5]},
    'VCB_Baseline_Medium': {'pred': [58.83, 49.25, 66.97, 67.16], 'actual': [65.8, 60.6, 60.1, 60.8]},
    'VCB_Baseline_Short': {'pred': [76.01, 50.23, 54.73, 72.15], 'actual': [68.6, 61.9, 59.5, 59.5]},
    'VCS_Baseline_Long': {'pred': [42.76, 38.47, 38.93, 51.06], 'actual': [47.6, 46.5, 43.0, 43.0]},
    'VCS_Baseline_Medium': {'pred': [40.06, 39.55, 53.37, 41.42], 'actual': [50.0, 47.4, 47.1, 46.9]},
    'VCS_Baseline_Short': {'pred': [44.27, 38.76, 55.73, 37.76], 'actual': [48.8, 46.8, 46.2, 46.2]},
    'VHM_Baseline_Long': {'pred': [81.88, 79.54, 122.64, 84.24], 'actual': [99.2, 93.9, 101.5, 101.5]},
    'VHM_Baseline_Medium': {'pred': [84.19, 126.86, 112.76, 117.18], 'actual': [104.5, 104.0, 100.2, 99.6]},
    'VHM_Baseline_Short': {'pred': [91.68, 139.47, 126.81, 100.27], 'actual': [102.3, 116.0, 114.5, 114.5]},
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

file_path = r"k:\\1\\Preparation_of_Papers_for_IEEE_ACCESS\\rq3\\llama.tex"
if os.path.exists(file_path):
    process_file(file_path)
    print(f"Successfully processed {os.path.basename(file_path)}")
else:
    print(f"File not found: {file_path}")
