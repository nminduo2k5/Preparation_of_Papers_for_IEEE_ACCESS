import re
import os

# Transformer BASELINE
data = {
    'CMG_Baseline_Long': {'pred': [32.96, 30.22, 38.78, 28.41], 'actual': [41.9, 35.1, 35.2, 35.2]},
    'CMG_Baseline_Medium': {'pred': [35.57, 50.01, 44.48, 33.66], 'actual': [40.8, 41.3, 39.6, 39.3]},
    'CMG_Baseline_Short': {'pred': [38.24, 30.41, 30.85, 42.65], 'actual': [41.85, 37.3, 38.75, 38.75]},
    'DGC_Baseline_Long': {'pred': [109.18, 101.26, 55.11, 64.49], 'actual': [96.0, 93.0, 70.2, 70.2]},
    'DGC_Baseline_Medium': {'pred': [88.37, 108.83, 83.66, 105.04], 'actual': [99.5, 93.6, 94.6, 95.0]},
    'DGC_Baseline_Short': {'pred': [117.19, 83.47, 104.68, 75.98], 'actual': [99.3, 93.2, 92.4, 92.4]},
    'DXG_Baseline_Long': {'pred': [25.47, 12.87, 19.89, 20.05], 'actual': [21.2, 16.3, 17.8, 17.8]},
    'DXG_Baseline_Medium': {'pred': [19.26, 25.62, 23.01, 23.25], 'actual': [24.05, 21.2, 20.15, 20.1]},
    'DXG_Baseline_Short': {'pred': [21.87, 19.08, 18.93, 22.66], 'actual': [24.0, 22.6, 20.9, 20.9]},
    'FPT_Baseline_Long': {'pred': [86.81, 75.88, 107.59, 81.93], 'actual': [103.9, 93.8, 93.9, 93.9]},
    'FPT_Baseline_Medium': {'pred': [122.54, 118.46, 91.94, 117.2], 'actual': [101.9, 102.7, 103.3, 100.9]},
    'FPT_Baseline_Short': {'pred': [116.43, 72.77, 86.06, 118.3], 'actual': [105.0, 88.1, 97.7, 97.7]},
    'HPG_Baseline_Long': {'pred': [29.77, 29.01, 31.21, 31.12], 'actual': [26.7, 26.25, 26.7, 26.7]},
    'HPG_Baseline_Medium': {'pred': [27.37, 29.54, 32.33, 29.72], 'actual': [30.35, 26.9, 26.75, 26.3]},
    'HPG_Baseline_Short': {'pred': [27.17, 22.35, 24.22, 28.75], 'actual': [29.85, 28.0, 26.4, 26.4]},
    'KDH_Baseline_Long': {'pred': [29.27, 25.52, 39.18, 26.83], 'actual': [35.85, 29.6, 32.65, 32.65]},
    'KDH_Baseline_Medium': {'pred': [31.41, 30.66, 40.14, 39.71], 'actual': [34.85, 35.85, 35.6, 34.95]},
    'KDH_Baseline_Short': {'pred': [31.46, 38.16, 37.83, 29.12], 'actual': [36.75, 33.9, 33.8, 33.8]},
    'MBB_Baseline_Long': {'pred': [19.56, 19.26, 28.56, 29.58], 'actual': [23.6, 23.75, 24.7, 24.7]},
    'MBB_Baseline_Medium': {'pred': [21.18, 20.84, 28.73, 18.69], 'actual': [26.85, 23.95, 24.0, 23.9]},
    'MBB_Baseline_Short': {'pred': [32.74, 30.4, 28.01, 22.28], 'actual': [28.25, 27.1, 24.4, 24.4]},
    'MWG_Baseline_Long': {'pred': [95.31, 68.73, 99.09, 96.75], 'actual': [82.6, 77.7, 82.9, 82.9]},
    'MWG_Baseline_Medium': {'pred': [69.42, 71.86, 73.78, 68.68], 'actual': [79.5, 83.9, 81.8, 80.2]},
    'MWG_Baseline_Short': {'pred': [92.82, 76.16, 96.65, 104.45], 'actual': [77.5, 84.5, 85.7, 85.7]},
    'TCB_Baseline_Long': {'pred': [30.36, 37.39, 40.42, 28.06], 'actual': [35.1, 32.0, 33.6, 33.6]},
    'TCB_Baseline_Medium': {'pred': [45.58, 43.16, 39.0, 40.56], 'actual': [39.0, 35.7, 35.0, 34.1]},
    'TCB_Baseline_Short': {'pred': [43.84, 34.63, 28.91, 29.1], 'actual': [39.6, 40.65, 36.1, 36.1]},
    'VCB_Baseline_Long': {'pred': [50.52, 65.06, 68.11, 48.09], 'actual': [60.7, 56.8, 57.5, 57.5]},
    'VCB_Baseline_Medium': {'pred': [54.31, 69.7, 53.63, 50.39], 'actual': [65.8, 60.6, 60.1, 60.8]},
    'VCB_Baseline_Short': {'pred': [54.79, 52.25, 54.25, 49.19], 'actual': [68.6, 61.9, 59.5, 59.5]},
    'VCS_Baseline_Long': {'pred': [37.54, 52.38, 37.84, 46.59], 'actual': [47.6, 46.5, 43.0, 43.0]},
    'VCS_Baseline_Medium': {'pred': [45.85, 55.27, 38.83, 53.86], 'actual': [50.0, 47.4, 47.1, 46.9]},
    'VCS_Baseline_Short': {'pred': [53.04, 42.83, 41.92, 50.74], 'actual': [48.8, 46.8, 46.2, 46.2]},
    'VHM_Baseline_Long': {'pred': [109.88, 79.1, 90.34, 90.29], 'actual': [99.2, 93.9, 101.5, 101.5]},
    'VHM_Baseline_Medium': {'pred': [126.39, 116.97, 83.78, 113.41], 'actual': [104.5, 104.0, 100.2, 99.6]},
    'VHM_Baseline_Short': {'pred': [120.72, 138.38, 133.53, 93.74], 'actual': [102.3, 116.0, 114.5, 114.5]},
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

file_path = r"k:\\1\\Preparation_of_Papers_for_IEEE_ACCESS\\rq3\\transformer.tex"
if os.path.exists(file_path):
    process_file(file_path)
    print(f"Successfully processed {os.path.basename(file_path)}")
else:
    print(f"File not found: {file_path}")
