import re
#GPT-Transformer
data = {   'DXG_Hierarchical_Short': {'pred': [23.03, 21.50, 17.21, 19.67], 'actual': [24, 22.60, 20.90, 20.90]},
    'DXG_Hierarchical_Medium': {'pred': [23.14, 22.83, 19.95, 18.80], 'actual': [24.05, 21.20, 20.15, 20.10]},
    'DXG_Hierarchical_Long': {'pred': [23.91, 19.03, 18.69, 18.61], 'actual': [21.20, 16.30, 17.80, 17.80]},
    'DXG_RoundRobin_Short': {'pred': [22.86, 22.28, 18.51, 20.59], 'actual': [24, 22.60, 20.90, 20.90]},
    'DXG_RoundRobin_Medium': {'pred': [23.87, 22.79, 20.22, 21.19], 'actual': [24.05, 21.20, 20.15, 20.10]},
    'DXG_RoundRobin_Long': {'pred': [20.26, 26.57, 16.78, 21.00], 'actual': [21.20, 16.30, 17.80, 17.80]},
    'DXG_Ensemble_Short': {'pred': [22.15, 25.15, 19.84, 18.93], 'actual': [24, 22.60, 20.90, 20.90]},
    'DXG_Ensemble_Medium': {'pred': [22.91, 20.10, 21.80, 20.70], 'actual': [24.05, 21.20, 20.15, 20.10]},
    'DXG_Ensemble_Long': {'pred': [25.54, 21.53, 20.29, 22.49], 'actual': [21.20, 16.30, 17.80, 17.80]},
    'FPT_Hierarchical_Short': {'pred': [101.82, 94.05, 93.21, 96.76], 'actual': [105, 88.10, 97.70, 97.70]},
    'FPT_Hierarchical_Medium': {'pred': [102.40, 93.77, 99.68, 94.24], 'actual': [101.90, 102.70, 103.30, 100.90]},
    'FPT_Hierarchical_Long': {'pred': [101.45, 94.24, 92.13, 94.70], 'actual': [103.90, 93.80, 93.90, 93.90]},
    'FPT_RoundRobin_Short': {'pred': [101.27, 87.11, 91.76, 96.93], 'actual': [105, 88.10, 97.70, 97.70]},
    'FPT_RoundRobin_Medium': {'pred': [101.08, 101.65, 80.81, 100.57], 'actual': [101.90, 102.70, 103.30, 100.90]},
    'FPT_RoundRobin_Long': {'pred': [99.11, 85.43, 93.79, 99.93], 'actual': [103.90, 93.80, 93.90, 93.90]},
    'FPT_Ensemble_Short': {'pred': [103.76, 91.28, 96.74, 98.58], 'actual': [105, 88.10, 97.70, 97.70]},
    'FPT_Ensemble_Medium': {'pred': [101.74, 87.00, 96.43, 102.92], 'actual': [101.90, 102.70, 103.30, 100.90]},
    'FPT_Ensemble_Long': {'pred': [100.99, 88.74, 90.97, 96.20], 'actual': [103.90, 93.80, 93.90, 93.90]},
    'VCB_Hierarchical_Short': {'pred': [68.01, 60.40, 58.32, 59.80], 'actual': [68.60, 61.90, 59.50, 59.50]},
    'VCB_Hierarchical_Medium': {'pred': [69.85, 61.01, 59.87, 58.53], 'actual': [65.80, 60.60, 60.10, 60.80]},
    'VCB_Hierarchical_Long': {'pred': [81.38, 67.82, 59.41, 58.91], 'actual': [60.70, 56.80, 57.50, 57.50]},
    'VCB_RoundRobin_Short': {'pred': [68.98, 61.05, 58.76, 58.83], 'actual': [68.60, 61.90, 59.50, 59.50]},
    'VCB_RoundRobin_Medium': {'pred': [68.15, 63.09, 60.61, 61.07], 'actual': [65.80, 60.60, 60.10, 60.80]},
    'VCB_RoundRobin_Long': {'pred': [72.46, 53.50, 57.26, 62.50], 'actual': [60.70, 56.80, 57.50, 57.50]},
    'VCB_Ensemble_Short': {'pred': [69.08, 63.22, 59.17, 59.34], 'actual': [68.60, 61.90, 59.50, 59.50]},
    'VCB_Ensemble_Medium': {'pred': [68.53, 58.67, 59.86, 58.66], 'actual': [65.80, 60.60, 60.10, 60.80]},
    'VCB_Ensemble_Long': {'pred': [75.07, 59.85, 59.08, 57.58], 'actual': [60.70, 56.80, 57.50, 57.50]},
    'VCS_Hierarchical_Short': {'pred': [49.07, 46.41, 44.52, 44.40], 'actual': [48.80, 46.80, 46.20, 46.20]},
    'VCS_Hierarchical_Medium': {'pred': [48.43, 48.26, 44.42, 43.00], 'actual': [50, 47.40, 47.10, 46.90]},
    'VCS_Hierarchical_Long': {'pred': [51.44, 45.44, 42.58, 47.30], 'actual': [47.60, 46.50, 43, 43]},
    'VCS_RoundRobin_Short': {'pred': [48.31, 47.45, 46.08, 45.20], 'actual': [48.80, 46.80, 46.20, 46.20]},
    'VCS_RoundRobin_Medium': {'pred': [47.65, 46.40, 46.87, 43.89], 'actual': [50, 47.40, 47.10, 46.90]},
    'VCS_RoundRobin_Long': {'pred': [48.89, 47.56, 41.81, 48.18], 'actual': [47.60, 46.50, 43, 43]},
    'VCS_Ensemble_Short': {'pred': [50.26, 48.01, 45.80, 44.64], 'actual': [48.80, 46.80, 46.20, 46.20]},
    'VCS_Ensemble_Medium': {'pred': [46.13, 47.99, 42.40, 44.36], 'actual': [50, 47.40, 47.10, 46.90]},
    'VCS_Ensemble_Long': {'pred': [47.75, 49.06, 47.57, 42.76], 'actual': [47.60, 46.50, 43, 43]},
    'HPG_Hierarchical_Short': {'pred': [23.78, 29.70, 26.22, 24.88], 'actual': [29.85, 28, 26.40, 26.40]},
    'HPG_Hierarchical_Medium': {'pred': [29.96, 27.68, 28.49, 26.63], 'actual': [30.35, 26.90, 26.75, 26.30]},
    'HPG_Hierarchical_Long': {'pred': [27.05, 27.12, 27.77, 26.43], 'actual': [26.70, 26.25, 26.70, 26.70]},
    'HPG_RoundRobin_Short': {'pred': [25.77, 29.22, 26.27, 26.00], 'actual': [29.85, 28, 26.40, 26.40]},
    'HPG_RoundRobin_Medium': {'pred': [27.79, 27.53, 27.19, 26.25], 'actual': [30.35, 26.90, 26.75, 26.30]},
    'HPG_RoundRobin_Long': {'pred': [27.06, 21.61, 27.20, 26.62], 'actual': [26.70, 26.25, 26.70, 26.70]},
    'HPG_Ensemble_Short': {'pred': [29.26, 29.28, 26.26, 26.50], 'actual': [29.85, 28, 26.40, 26.40]},
    'HPG_Ensemble_Medium': {'pred': [26.98, 26.84, 28.02, 25.47], 'actual': [30.35, 26.90, 26.75, 26.30]},
    'HPG_Ensemble_Long': {'pred': [26.93, 28.54, 27.16, 26.42], 'actual': [26.70, 26.25, 26.70, 26.70]},
    'TCB_Hierarchical_Short': {'pred': [38.70, 42.16, 34.15, 39.08], 'actual': [39.60, 40.65, 36.10, 36.10]},
    'TCB_Hierarchical_Medium': {'pred': [40.61, 40.14, 36.45, 36.57], 'actual': [39, 35.70, 35, 34.10]},
    'TCB_Hierarchical_Long': {'pred': [37.34, 42.99, 38.94, 43.97], 'actual': [35.10, 32, 33.60, 33.60]},
    'TCB_RoundRobin_Short': {'pred': [37.66, 40.49, 38.24, 39.26], 'actual': [39.60, 40.65, 36.10, 36.10]},
    'TCB_RoundRobin_Medium': {'pred': [40.64, 44.17, 37.02, 37.32], 'actual': [39, 35.70, 35, 34.10]},
    'TCB_RoundRobin_Long': {'pred': [40.68, 43.14, 37.13, 40.09], 'actual': [35.10, 32, 33.60, 33.60]},
    'TCB_Ensemble_Short': {'pred': [38.95, 41.18, 36.85, 39.73], 'actual': [39.60, 40.65, 36.10, 36.10]},
    'TCB_Ensemble_Medium': {'pred': [38.67, 43.02, 38.11, 38.55], 'actual': [39, 35.70, 35, 34.10]},
    'TCB_Ensemble_Long': {'pred': [40.53, 39.46, 37.72, 42.78], 'actual': [35.10, 32, 33.60, 33.60]},
    'VHM_Hierarchical_Short': {'pred': [102.17, 122.60, 115.51, 113.50], 'actual': [102.30, 116, 114.50, 114.50]},
    'VHM_Hierarchical_Medium': {'pred': [103.53, 126.31, 115.77, 84.63], 'actual': [104.50, 104, 100.20, 99.60]},
    'VHM_Hierarchical_Long': {'pred': [108.73, 100.29, 115.81, 113.47], 'actual': [99.20, 93.90, 101.50, 101.50]},
    'VHM_RoundRobin_Short': {'pred': [103.32, 128.13, 113.14, 111.56], 'actual': [102.30, 116, 114.50, 114.50]},
    'VHM_RoundRobin_Medium': {'pred': [103.59, 135.55, 101.53, 119.26], 'actual': [104.50, 104, 100.20, 99.60]},
    'VHM_RoundRobin_Long': {'pred': [104.88, 105.51, 114.54, 103.27], 'actual': [99.20, 93.90, 101.50, 101.50]},
    'VHM_Ensemble_Short': {'pred': [103.06, 118.75, 111.05, 111.22], 'actual': [102.30, 116, 114.50, 114.50]},
    'VHM_Ensemble_Medium': {'pred': [105.01, 106.66, 95.32, 125.40], 'actual': [104.50, 104, 100.20, 99.60]},
    'VHM_Ensemble_Long': {'pred': [105.34, 148.10, 108.70, 129.43], 'actual': [99.20, 93.90, 101.50, 101.50]},
    'MWG_Hierarchical_Short': {'pred': [78.24, 82.77, 84.52, 82.67], 'actual': [77.50, 84.50, 85.70, 85.70]},
    'MWG_Hierarchical_Medium': {'pred': [80.65, 83.10, 82.30, 86.36], 'actual': [79.50, 83.90, 81.80, 80.20]},
    'MWG_Hierarchical_Long': {'pred': [77.37, 90.67, 83.66, 83.90], 'actual': [82.60, 77.70, 82.90, 82.90]},
    'MWG_RoundRobin_Short': {'pred': [76.98, 83.77, 84.26, 81.96], 'actual': [77.50, 84.50, 85.70, 85.70]},
    'MWG_RoundRobin_Medium': {'pred': [77.93, 82.21, 84.82, 80.02], 'actual': [79.50, 83.90, 81.80, 80.20]},
    'MWG_RoundRobin_Long': {'pred': [80.00, 79.25, 84.54, 85.06], 'actual': [82.60, 77.70, 82.90, 82.90]},
    'MWG_Ensemble_Short': {'pred': [78.34, 83.27, 84.50, 84.93], 'actual': [77.50, 84.50, 85.70, 85.70]},
    'MWG_Ensemble_Medium': {'pred': [77.52, 87.70, 83.31, 80.60], 'actual': [79.50, 83.90, 81.80, 80.20]},
    'MWG_Ensemble_Long': {'pred': [75.39, 88.21, 82.37, 85.00], 'actual': [82.60, 77.70, 82.90, 82.90]},
    'CMG_Hierarchical_Short': {'pred': [42.26, 38.52, 39.74, 37.33], 'actual': [41.85, 37.30, 38.75, 38.75]},
    'CMG_Hierarchical_Medium': {'pred': [42.26, 35.02, 36.82, 38.68], 'actual': [40.80, 41.30, 39.60, 39.30]},
    'CMG_Hierarchical_Long': {'pred': [40.96, 38.16, 36.41, 41.03], 'actual': [41.90, 35.10, 35.20, 35.20]},
    'CMG_RoundRobin_Short': {'pred': [38.57, 37.15, 37.70, 38.43], 'actual': [41.85, 37.30, 38.75, 38.75]},
    'CMG_RoundRobin_Medium': {'pred': [38.49, 42.26, 38.51, 38.87], 'actual': [40.80, 41.30, 39.60, 39.30]},
    'CMG_RoundRobin_Long': {'pred': [40.92, 41.63, 41.55, 35.32], 'actual': [41.90, 35.10, 35.20, 35.20]},
    'CMG_Ensemble_Short': {'pred': [41.13, 37.62, 38.66, 38.29], 'actual': [41.85, 37.30, 38.75, 38.75]},
    'CMG_Ensemble_Medium': {'pred': [41.01, 41.51, 37.68, 38.08], 'actual': [40.80, 41.30, 39.60, 39.30]},
    'CMG_Ensemble_Long': {'pred': [41.52, 34.85, 40.41, 41.48], 'actual': [41.90, 35.10, 35.20, 35.20]},
    'KDH_Hierarchical_Short': {'pred': [38.19, 33.58, 29.82, 34.27], 'actual': [36.75, 33.90, 33.80, 33.80]},
    'KDH_Hierarchical_Medium': {'pred': [37.75, 32.82, 33.28, 30.38], 'actual': [34.85, 35.85, 35.60, 34.95]},
    'KDH_Hierarchical_Long': {'pred': [35.80, 32.31, 29.97, 32.44], 'actual': [35.85, 29.60, 32.65, 32.65]},
    'KDH_RoundRobin_Short': {'pred': [36.95, 34.85, 33.34, 28.33], 'actual': [36.75, 33.90, 33.80, 33.80]},
    'KDH_RoundRobin_Medium': {'pred': [37.47, 36.31, 35.81, 29.88], 'actual': [34.85, 35.85, 35.60, 34.95]},
    'KDH_RoundRobin_Long': {'pred': [35.63, 36.91, 32.33, 33.14], 'actual': [35.85, 29.60, 32.65, 32.65]},
    'KDH_Ensemble_Short': {'pred': [36.23, 33.66, 30.07, 32.74], 'actual': [36.75, 33.90, 33.80, 33.80]},
    'KDH_Ensemble_Medium': {'pred': [34.71, 36.08, 30.10, 33.27], 'actual': [34.85, 35.85, 35.60, 34.95]},
    'KDH_Ensemble_Long': {'pred': [36.65, 35.87, 33.92, 33.20], 'actual': [35.85, 29.60, 32.65, 32.65]},
    'DGC_Hierarchical_Short': {'pred': [96.81, 96.43, 96.52, 89.31], 'actual': [99.30, 93.20, 92.40, 92.40]},
    'DGC_Hierarchical_Medium': {'pred': [99.87, 96.65, 94.94, 99.70], 'actual': [99.50, 93.60, 94.60, 95.00]},
    'DGC_Hierarchical_Long': {'pred': [99.54, 94.19, 94.72, 78.79], 'actual': [96.00, 93.00, 70.20, 70.20]},
    'DGC_RoundRobin_Short': {'pred': [98.45, 93.94, 88.21, 93.86], 'actual': [99.30, 93.20, 92.40, 92.40]},
    'DGC_RoundRobin_Medium': {'pred': [97.09, 93.81, 87.80, 86.25], 'actual': [99.50, 93.60, 94.60, 95.00]},
    'DGC_RoundRobin_Long': {'pred': [96.95, 94.66, 96.51, 94.93], 'actual': [96.00, 93.00, 70.20, 70.20]},
    'DGC_Ensemble_Short': {'pred': [98.99, 96.98, 89.64, 91.68], 'actual': [99.30, 93.20, 92.40, 92.40]},
    'DGC_Ensemble_Medium': {'pred': [99.11, 95.20, 92.07, 92.48], 'actual': [99.50, 93.60, 94.60, 95.00]},
    'DGC_Ensemble_Long': {'pred': [98.54, 98.38, 94.71, 73.49], 'actual': [96.00, 93.00, 70.20, 70.20]},
    'MBB_Hierarchical_Short': {'pred': [28.74, 27.51, 25.40, 26.77], 'actual': [28.25, 27.10, 24.40, 24.40]},
    'MBB_Hierarchical_Medium': {'pred': [27.92, 23.49, 29.13, 23.99], 'actual': [26.85, 23.95, 24.00, 23.90]},
    'MBB_Hierarchical_Long': {'pred': [31.87, 29.55, 24.99, 25.78], 'actual': [23.60, 23.75, 24.70, 24.70]},
    'MBB_RoundRobin_Short': {'pred': [27.04, 26.77, 25.96, 25.18], 'actual': [28.25, 27.10, 24.40, 24.40]},
    'MBB_RoundRobin_Medium': {'pred': [29.21, 29.85, 25.19, 26.41], 'actual': [26.85, 23.95, 24.00, 23.90]},
    'MBB_RoundRobin_Long': {'pred': [26.43, 30.02, 24.24, 23.81], 'actual': [23.60, 23.75, 24.70, 24.70]},
    'MBB_Ensemble_Short': {'pred': [26.94, 25.99, 24.64, 24.66], 'actual': [28.25, 27.10, 24.40, 24.40]},
    'MBB_Ensemble_Medium': {'pred': [28.43, 28.56, 24.77, 22.02], 'actual': [26.85, 23.95, 24.00, 23.90]},
    'MBB_Ensemble_Long': {'pred': [28.64, 27.36, 26.38, 25.40], 'actual': [23.60, 23.75, 24.70, 24.70]}}

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

    # Only process table lines within longtable
    in_table = False
    for line in lines:
        if '\\begin{longtable}' in line:
            in_table = True
        
        if in_table:
            m_stock = re.search(r'\\multirow\{12\}\{\*\}\{\\textbf\{([A-Z]+)\}\}', line)
            if m_stock:
                current_stock = m_stock.group(1)
            
            m_arch = re.search(r'&\s*\\textbf\{([A-Za-z\s]+)\}', line)
            if m_arch:
                arch_raw = m_arch.group(1).strip()
                if arch_raw == 'Round Robin' or arch_raw == 'RoundRobin':
                    current_arch = 'RoundRobin'
                else:
                    current_arch = arch_raw
                row_idx = 0
            
            if current_stock and current_arch and r'\\' in line and line.strip().startswith('&'):
                key_prefix = f"{current_stock}_{current_arch}"
                short_key = f"{key_prefix}_Short"
                
                if short_key in data and row_idx < 4:
                    parts = line.split('&')
                    
                    if len(parts) >= 15:
                        start_price = float(parts[2].strip())
                        
                        # Update Short
                        short_pred = data[f"{key_prefix}_Short"]['pred'][row_idx]
                        short_act = data[f"{key_prefix}_Short"]['actual'][row_idx]
                        short_gap = format_gap_new(start_price, short_pred, short_act)
                        parts[4] = f" {short_pred} "
                        parts[6] = f" {short_gap} "
                        
                        # Update Medium
                        med_pred = data[f"{key_prefix}_Medium"]['pred'][row_idx]
                        med_act = data[f"{key_prefix}_Medium"]['actual'][row_idx]
                        med_gap = format_gap_new(start_price, med_pred, med_act)
                        parts[8] = f" {med_pred} "
                        parts[10] = f" {med_gap} "
                        
                        # Update Long
                        long_pred = data[f"{key_prefix}_Long"]['pred'][row_idx]
                        long_act = data[f"{key_prefix}_Long"]['actual'][row_idx]
                        long_gap = format_gap_new(start_price, long_pred, long_act)
                        parts[12] = f" {long_pred} "
                        parts[14] = f" {long_gap} \\\\\n"
                        
                        line = "&".join(parts)
                    
                    row_idx += 1

        new_lines.append(line)
        
        if '\\end{longtable}' in line:
            in_table = False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

# Process both test1.tex and access.tex to ensure they are synchronized
process_file(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\table\test2.tex')

print("Successfully processed test2.tex")
