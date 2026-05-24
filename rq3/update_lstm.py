import re
import os

# LSTM BASELINE
data = {
    'CMG_Baseline_Long': {'pred': [45.8, 32.05, 28.4, 39.75], 'actual': [41.9, 35.1, 35.2, 35.2]},
    'CMG_Baseline_Medium': {'pred': [34.32, 45.32, 31.39, 35.86], 'actual': [40.8, 41.3, 39.6, 39.3]},
    'CMG_Baseline_Short': {'pred': [38.16, 41.38, 46.93, 43.38], 'actual': [41.85, 37.3, 38.75, 38.75]},
    'DGC_Baseline_Long': {'pred': [106.36, 74.21, 61.11, 58.86], 'actual': [96.0, 93.0, 70.2, 70.2]},
    'DGC_Baseline_Medium': {'pred': [91.17, 109.68, 80.39, 115.75], 'actual': [99.5, 93.6, 94.6, 95.0]},
    'DGC_Baseline_Short': {'pred': [118.39, 74.01, 81.73, 99.88], 'actual': [99.3, 93.2, 92.4, 92.4]},
    'DXG_Baseline_Long': {'pred': [18.72, 18.41, 19.71, 14.9], 'actual': [21.2, 16.3, 17.8, 17.8]},
    'DXG_Baseline_Medium': {'pred': [26.86, 17.48, 15.94, 17.47], 'actual': [24.05, 21.2, 20.15, 20.1]},
    'DXG_Baseline_Short': {'pred': [19.22, 26.77, 23.26, 19.2], 'actual': [24.0, 22.6, 20.9, 20.9]},
    'FPT_Baseline_Long': {'pred': [85.5, 106.43, 109.95, 107.01], 'actual': [103.9, 93.8, 93.9, 93.9]},
    'FPT_Baseline_Medium': {'pred': [82.2, 123.51, 124.96, 118.95], 'actual': [101.9, 102.7, 103.3, 100.9]},
    'FPT_Baseline_Short': {'pred': [122.95, 105.94, 87.92, 86.66], 'actual': [105.0, 88.1, 97.7, 97.7]},
    'HPG_Baseline_Long': {'pred': [21.66, 30.73, 29.28, 29.28], 'actual': [26.7, 26.25, 26.7, 26.7]},
    'HPG_Baseline_Medium': {'pred': [36.61, 23.59, 23.82, 31.75], 'actual': [30.35, 26.9, 26.75, 26.3]},
    'HPG_Baseline_Short': {'pred': [34.92, 32.15, 30.39, 29.71], 'actual': [29.85, 28.0, 26.4, 26.4]},
    'KDH_Baseline_Long': {'pred': [31.28, 24.06, 27.56, 36.39], 'actual': [35.85, 29.6, 32.65, 32.65]},
    'KDH_Baseline_Medium': {'pred': [29.03, 42.61, 27.78, 41.76], 'actual': [34.85, 35.85, 35.6, 34.95]},
    'KDH_Baseline_Short': {'pred': [39.92, 27.43, 27.24, 29.19], 'actual': [36.75, 33.9, 33.8, 33.8]},
    'MBB_Baseline_Long': {'pred': [19.84, 19.39, 21.02, 29.27], 'actual': [23.6, 23.75, 24.7, 24.7]},
    'MBB_Baseline_Medium': {'pred': [23.9, 21.49, 21.16, 20.56], 'actual': [26.85, 23.95, 24.0, 23.9]},
    'MBB_Baseline_Short': {'pred': [33.4, 30.85, 28.15, 28.81], 'actual': [28.25, 27.1, 24.4, 24.4]},
    'MWG_Baseline_Long': {'pred': [71.47, 85.92, 93.04, 100.2], 'actual': [82.6, 77.7, 82.9, 82.9]},
    'MWG_Baseline_Medium': {'pred': [70.32, 92.2, 74.72, 65.36], 'actual': [79.5, 83.9, 81.8, 80.2]},
    'MWG_Baseline_Short': {'pred': [87.66, 98.91, 78.08, 100.27], 'actual': [77.5, 84.5, 85.7, 85.7]},
    'TCB_Baseline_Long': {'pred': [42.03, 34.74, 39.83, 30.47], 'actual': [35.1, 32.0, 33.6, 33.6]},
    'TCB_Baseline_Medium': {'pred': [43.1, 39.16, 42.14, 39.38], 'actual': [39.0, 35.7, 35.0, 34.1]},
    'TCB_Baseline_Short': {'pred': [46.83, 45.86, 29.75, 41.36], 'actual': [39.6, 40.65, 36.1, 36.1]},
    'VCB_Baseline_Long': {'pred': [47.38, 62.23, 63.47, 46.71], 'actual': [60.7, 56.8, 57.5, 57.5]},
    'VCB_Baseline_Medium': {'pred': [79.34, 49.08, 54.82, 51.18], 'actual': [65.8, 60.6, 60.1, 60.8]},
    'VCB_Baseline_Short': {'pred': [80.32, 69.79, 47.89, 65.98], 'actual': [68.6, 61.9, 59.5, 59.5]},
    'VCS_Baseline_Long': {'pred': [39.19, 39.28, 35.82, 35.48], 'actual': [47.6, 46.5, 43.0, 43.0]},
    'VCS_Baseline_Medium': {'pred': [45.28, 53.7, 50.94, 39.02], 'actual': [50.0, 47.4, 47.1, 46.9]},
    'VCS_Baseline_Short': {'pred': [54.87, 42.57, 41.78, 40.17], 'actual': [48.8, 46.8, 46.2, 46.2]},
    'VHM_Baseline_Long': {'pred': [110.2, 103.1, 112.05, 110.69], 'actual': [99.2, 93.9, 101.5, 101.5]},
    'VHM_Baseline_Medium': {'pred': [82.13, 84.91, 120.26, 111.01], 'actual': [104.5, 104.0, 100.2, 99.6]},
    'VHM_Baseline_Short': {'pred': [114.69, 99.38, 135.0, 92.03], 'actual': [102.3, 116.0, 114.5, 114.5]},
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

file_path = r"k:\\1\\Preparation_of_Papers_for_IEEE_ACCESS\\rq3\\lstm.tex"
if os.path.exists(file_path):
    process_file(file_path)
    print(f"Successfully processed {os.path.basename(file_path)}")
else:
    print(f"File not found: {file_path}")
