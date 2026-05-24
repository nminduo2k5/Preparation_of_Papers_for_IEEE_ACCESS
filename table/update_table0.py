import re
#GEMINI-LSTM-BASELINE
data = {'CMG_Ensemble_Long': {'actual': [41.9, 35.1, 35.2, 35.2], 'pred': [42.88, 35.52, 31.21, 39.41]},
 'CMG_Ensemble_Medium': {'actual': [40.8, 41.3, 39.6, 39.3], 'pred': [42.21, 39.25, 38.87, 41.26]},
 'CMG_Ensemble_Short': {'actual': [41.85, 37.3, 38.75, 38.75], 'pred': [42.15, 39.85, 38.66, 39.62]},
 'CMG_Hierarchical_Long': {'actual': [41.9, 35.1, 35.2, 35.2], 'pred': [33.24, 33.63, 31.82, 31.21]},
 'CMG_Hierarchical_Medium': {'actual': [40.8, 41.3, 39.6, 39.3], 'pred': [33.28, 38.14, 35.82, 37.44]},
 'CMG_Hierarchical_Short': {'actual': [41.85, 37.3, 38.75, 38.75], 'pred': [39.13, 37.52, 38.12, 35.33]},
 'CMG_RoundRobin_Long': {'actual': [41.9, 35.1, 35.2, 35.2], 'pred': [36.88, 32.52, 31.29, 33.11]},
 'CMG_RoundRobin_Medium': {'actual': [40.8, 41.3, 39.6, 39.3], 'pred': [36.84, 36.58, 36.72, 38.83]},
 'CMG_RoundRobin_Short': {'actual': [41.85, 37.3, 38.75, 38.75], 'pred': [37.27, 39.28, 36.22, 35.82]},
 'DGC_Ensemble_Long': {'actual': [96.0, 93.0, 70.2, 70.2], 'pred': [95.31, 93.6, 77.25, 72.95]},
 'DGC_Ensemble_Medium': {'actual': [99.5, 93.6, 94.6, 95.0], 'pred': [100.97, 93.84, 95.11, 95.13]},
 'DGC_Ensemble_Short': {'actual': [99.3, 93.2, 92.4, 92.4], 'pred': [94.36, 93.35, 94.82, 93.78]},
 'DGC_Hierarchical_Long': {'actual': [96.0, 93.0, 70.2, 70.2], 'pred': [95.0, 92.01, 76.0, 77.8]},
 'DGC_Hierarchical_Medium': {'actual': [99.5, 93.6, 94.6, 95.0], 'pred': [94.5, 92.82, 86.0, 89.02]},
 'DGC_Hierarchical_Short': {'actual': [99.3, 93.2, 92.4, 92.4], 'pred': [96.01, 93.52, 87.01, 90.3]},
 'DGC_RoundRobin_Long': {'actual': [96.0, 93.0, 70.2, 70.2], 'pred': [95.82, 94.36, 78.52, 77.92]},
 'DGC_RoundRobin_Medium': {'actual': [99.5, 93.6, 94.6, 95.0], 'pred': [99.77, 95.12, 91.06, 96.4]},
 'DGC_RoundRobin_Short': {'actual': [99.3, 93.2, 92.4, 92.4], 'pred': [95.27, 92.82, 98.37, 97.22]},
 'DXG_Ensemble_Long': {'actual': [21.2, 16.3, 17.8, 17.8], 'pred': [21.47, 23.36, 20.81, 20.45]},
 'DXG_Ensemble_Medium': {'actual': [24.05, 21.2, 20.15, 20.1], 'pred': [22.98, 21.75, 20.52, 26.35]},
 'DXG_Ensemble_Short': {'actual': [24.0, 22.6, 20.9, 20.9], 'pred': [22.11, 21.92, 20.07, 21.05]},
 'DXG_Hierarchical_Long': {'actual': [21.2, 16.3, 17.8, 17.8], 'pred': [21.83, 24.46, 20.81, 20.42]},
 'DXG_Hierarchical_Medium': {'actual': [24.05, 21.2, 20.15, 20.1], 'pred': [23.38, 23.34, 20.52, 28.88]},
 'DXG_Hierarchical_Short': {'actual': [24.0, 22.6, 20.9, 20.9], 'pred': [22.25, 22.1, 20.51, 21.1]},
 'DXG_RoundRobin_Long': {'actual': [21.2, 16.3, 17.8, 17.8], 'pred': [24.47, 25.63, 20.96, 20.96]},
 'DXG_RoundRobin_Medium': {'actual': [24.05, 21.2, 20.15, 20.1], 'pred': [21.98, 22.28, 20.79, 23.68]},
 'DXG_RoundRobin_Short': {'actual': [24.0, 22.6, 20.9, 20.9], 'pred': [22.25, 22.15, 20.34, 20.48]},
 'FPT_Ensemble_Long': {'actual': [103.9, 93.8, 93.9, 93.9], 'pred': [102.77, 92.24, 97.22, 105.33]},
 'FPT_Ensemble_Medium': {'actual': [101.9, 102.7, 103.3, 100.9], 'pred': [103.6, 91.17, 96.26, 97.93]},
 'FPT_Ensemble_Short': {'actual': [105.0, 88.1, 97.7, 97.7], 'pred': [103.6, 88.55, 95.14, 96.59]},
 'FPT_Hierarchical_Long': {'actual': [103.9, 93.8, 93.9, 93.9], 'pred': [105.57, 92.13, 97.56, 108.92]},
 'FPT_Hierarchical_Medium': {'actual': [101.9, 102.7, 103.3, 100.9], 'pred': [106.07, 89.32, 95.8, 97.6]},
 'FPT_Hierarchical_Short': {'actual': [105.0, 88.1, 97.7, 97.7], 'pred': [103.6, 90.83, 95.37, 93.5]},
 'FPT_RoundRobin_Long': {'actual': [103.9, 93.8, 93.9, 93.9], 'pred': [104.27, 90.7, 97.48, 108.92]},
 'FPT_RoundRobin_Medium': {'actual': [101.9, 102.7, 103.3, 100.9], 'pred': [105.66, 91.28, 95.25, 93.6]},
 'FPT_RoundRobin_Short': {'actual': [105.0, 88.1, 97.7, 97.7], 'pred': [104.42, 90.46, 96.0, 93.68]},
 'HPG_Ensemble_Long': {'actual': [26.7, 26.25, 26.7, 26.7], 'pred': [25.3, 25.86, 23.6, 21.55]},
 'HPG_Ensemble_Medium': {'actual': [30.35, 26.9, 26.75, 26.3], 'pred': [25.24, 25.78, 24.3, 22.21]},
 'HPG_Ensemble_Short': {'actual': [29.85, 28.0, 26.4, 26.4], 'pred': [25.22, 25.92, 22.63, 21.75]},
 'HPG_Hierarchical_Long': {'actual': [26.7, 26.25, 26.7, 26.7], 'pred': [28.1, 25.11, 28.03, 27.33]},
 'HPG_Hierarchical_Medium': {'actual': [30.35, 26.9, 26.75, 26.3], 'pred': [28.0, 29.01, 27.2, 27.0]},
 'HPG_Hierarchical_Short': {'actual': [29.85, 28.0, 26.4, 26.4], 'pred': [28.29, 28.6, 28.02, 27.61]},
 'HPG_RoundRobin_Long': {'actual': [26.7, 26.25, 26.7, 26.7], 'pred': [26.41, 30.22, 28.11, 27.86]},
 'HPG_RoundRobin_Medium': {'actual': [30.35, 26.9, 26.75, 26.3], 'pred': [28.84, 29.01, 27.2, 27.0]},
 'HPG_RoundRobin_Short': {'actual': [29.85, 28.0, 26.4, 26.4], 'pred': [28.84, 29.63, 26.6, 28.0]},
 'KDH_Ensemble_Long': {'actual': [35.85, 29.6, 32.65, 32.65], 'pred': [34.97, 28.92, 34.16, 27.99]},
 'KDH_Ensemble_Medium': {'actual': [34.85, 35.85, 35.6, 34.95], 'pred': [35.71, 37.51, 37.04, 33.4]},
 'KDH_Ensemble_Short': {'actual': [36.75, 33.9, 33.8, 33.8], 'pred': [39.25, 32.39, 35.55, 32.59]},
 'KDH_Hierarchical_Long': {'actual': [35.85, 29.6, 32.65, 32.65], 'pred': [33.47, 31.44, 28.95, 26.64]},
 'KDH_Hierarchical_Medium': {'actual': [34.85, 35.85, 35.6, 34.95], 'pred': [33.38, 31.44, 29.07, 25.76]},
 'KDH_Hierarchical_Short': {'actual': [36.75, 33.9, 33.8, 33.8], 'pred': [33.18, 31.31, 28.48, 27.76]},
 'KDH_RoundRobin_Long': {'actual': [35.85, 29.6, 32.65, 32.65], 'pred': [35.21, 29.52, 29.56, 30.54]},
 'KDH_RoundRobin_Medium': {'actual': [34.85, 35.85, 35.6, 34.95], 'pred': [34.61, 34.61, 32.14, 33.45]},
 'KDH_RoundRobin_Short': {'actual': [36.75, 33.9, 33.8, 33.8], 'pred': [32.25, 34.89, 33.45, 33.24]},
 'MBB_Ensemble_Long': {'actual': [23.6, 23.75, 24.7, 24.7], 'pred': [24.48, 23.02, 24.73, 24.34]},
 'MBB_Ensemble_Medium': {'actual': [26.85, 23.95, 24.0, 23.9], 'pred': [25.61, 23.1, 24.35, 23.55]},
 'MBB_Ensemble_Short': {'actual': [28.25, 27.1, 24.4, 24.4], 'pred': [29.65, 26.97, 24.97, 24.94]},
 'MBB_Hierarchical_Long': {'actual': [23.6, 23.75, 24.7, 24.7], 'pred': [22.21, 26.95, 24.96, 26.44]},
 'MBB_Hierarchical_Medium': {'actual': [26.85, 23.95, 24.0, 23.9], 'pred': [29.54, 21.58, 25.18, 24.58]},
 'MBB_Hierarchical_Short': {'actual': [28.25, 27.1, 24.4, 24.4], 'pred': [26.77, 26.81, 24.78, 23.54]},
 'MBB_RoundRobin_Long': {'actual': [23.6, 23.75, 24.7, 24.7], 'pred': [25.93, 22.67, 24.07, 22.94]},
 'MBB_RoundRobin_Medium': {'actual': [26.85, 23.95, 24.0, 23.9], 'pred': [25.51, 26.78, 24.41, 22.99]},
 'MBB_RoundRobin_Short': {'actual': [28.25, 27.1, 24.4, 24.4], 'pred': [28.2, 27.7, 24.7, 23.13]},
 'MWG_Ensemble_Long': {'actual': [82.6, 77.7, 82.9, 82.9], 'pred': [76.21, 77.09, 81.82, 83.53]},
 'MWG_Ensemble_Medium': {'actual': [79.5, 83.9, 81.8, 80.2], 'pred': [75.71, 82.79, 80.18, 81.39]},
 'MWG_Ensemble_Short': {'actual': [77.5, 84.5, 85.7, 85.7], 'pred': [77.31, 77.04, 79.49, 87.54]},
 'MWG_Hierarchical_Long': {'actual': [82.6, 77.7, 82.9, 82.9], 'pred': [78.64, 81.35, 81.23, 87.42]},
 'MWG_Hierarchical_Medium': {'actual': [79.5, 83.9, 81.8, 80.2], 'pred': [73.42, 88.18, 86.08, 83.14]},
 'MWG_Hierarchical_Short': {'actual': [77.5, 84.5, 85.7, 85.7], 'pred': [73.12, 87.88, 86.4, 87.6]},
 'MWG_RoundRobin_Long': {'actual': [82.6, 77.7, 82.9, 82.9], 'pred': [78.62, 77.81, 82.69, 78.35]},
 'MWG_RoundRobin_Medium': {'actual': [79.5, 83.9, 81.8, 80.2], 'pred': [71.86, 77.72, 80.45, 79.27]},
 'MWG_RoundRobin_Short': {'actual': [77.5, 84.5, 85.7, 85.7], 'pred': [71.61, 87.75, 85.63, 87.2]},
 'TCB_Ensemble_Long': {'actual': [35.1, 32.0, 33.6, 33.6], 'pred': [35.42, 37.97, 34.76, 35.1]},
 'TCB_Ensemble_Medium': {'actual': [39.0, 35.7, 35.0, 34.1], 'pred': [35.1, 37.94, 34.67, 35.14]},
 'TCB_Ensemble_Short': {'actual': [39.6, 40.65, 36.1, 36.1], 'pred': [35.28, 37.9, 34.78, 35.1]},
 'TCB_Hierarchical_Long': {'actual': [35.1, 32.0, 33.6, 33.6], 'pred': [40.03, 41.2, 38.0, 37.03]},
 'TCB_Hierarchical_Medium': {'actual': [39.0, 35.7, 35.0, 34.1], 'pred': [39.82, 42.27, 38.82, 38.5]},
 'TCB_Hierarchical_Short': {'actual': [39.6, 40.65, 36.1, 36.1], 'pred': [40.02, 42.0, 37.5, 39.01]},
 'TCB_RoundRobin_Long': {'actual': [35.1, 32.0, 33.6, 33.6], 'pred': [36.91, 36.03, 33.59, 36.93]},
 'TCB_RoundRobin_Medium': {'actual': [39.0, 35.7, 35.0, 34.1], 'pred': [38.25, 36.07, 36.08, 38.62]},
 'TCB_RoundRobin_Short': {'actual': [39.6, 40.65, 36.1, 36.1], 'pred': [37.81, 42.81, 36.73, 37.22]},
 'VCB_Ensemble_Long': {'actual': [60.7, 56.8, 57.5, 57.5], 'pred': [67.9, 61.94, 63.01, 62.29]},
 'VCB_Ensemble_Medium': {'actual': [65.8, 60.6, 60.1, 60.8], 'pred': [68.85, 64.34, 62.36, 61.78]},
 'VCB_Ensemble_Short': {'actual': [68.6, 61.9, 59.5, 59.5], 'pred': [67.64, 63.65, 62.58, 60.88]},
 'VCB_Hierarchical_Long': {'actual': [60.7, 56.8, 57.5, 57.5], 'pred': [67.6, 64.47, 58.5, 62.76]},
 'VCB_Hierarchical_Medium': {'actual': [65.8, 60.6, 60.1, 60.8], 'pred': [68.52, 64.29, 62.37, 62.37]},
 'VCB_Hierarchical_Short': {'actual': [68.6, 61.9, 59.5, 59.5], 'pred': [68.66, 63.29, 61.68, 61.21]},
 'VCB_RoundRobin_Long': {'actual': [60.7, 56.8, 57.5, 57.5], 'pred': [77.81, 64.57, 63.0, 62.45]},
 'VCB_RoundRobin_Medium': {'actual': [65.8, 60.6, 60.1, 60.8], 'pred': [68.9, 64.03, 62.37, 61.96]},
 'VCB_RoundRobin_Short': {'actual': [68.6, 61.9, 59.5, 59.5], 'pred': [68.46, 62.51, 61.15, 61.46]},
 'VCS_Ensemble_Long': {'actual': [47.6, 46.5, 43.0, 43.0], 'pred': [49.65, 41.33, 47.43, 46.53]},
 'VCS_Ensemble_Medium': {'actual': [50.0, 47.4, 47.1, 46.9], 'pred': [49.2, 45.74, 46.78, 46.66]},
 'VCS_Ensemble_Short': {'actual': [48.8, 46.8, 46.2, 46.2], 'pred': [48.66, 45.48, 46.95, 45.7]},
 'VCS_Hierarchical_Long': {'actual': [47.6, 46.5, 43.0, 43.0], 'pred': [50.51, 42.13, 47.66, 47.56]},
 'VCS_Hierarchical_Medium': {'actual': [50.0, 47.4, 47.1, 46.9], 'pred': [50.2, 49.74, 47.06, 47.27]},
 'VCS_Hierarchical_Short': {'actual': [48.8, 46.8, 46.2, 46.2], 'pred': [47.97, 47.86, 47.12, 46.38]},
 'VCS_RoundRobin_Long': {'actual': [47.6, 46.5, 43.0, 43.0], 'pred': [50.51, 45.5, 44.16, 44.15]},
 'VCS_RoundRobin_Medium': {'actual': [50.0, 47.4, 47.1, 46.9], 'pred': [46.2, 46.94, 46.12, 46.6]},
 'VCS_RoundRobin_Short': {'actual': [48.8, 46.8, 46.2, 46.2], 'pred': [48.62, 47.55, 47.43, 46.92]},
 'VHM_Ensemble_Long': {'actual': [99.2, 93.9, 101.5, 101.5], 'pred': [95.79, 102.3, 99.62, 94.42]},
 'VHM_Ensemble_Medium': {'actual': [104.5, 104.0, 100.2, 99.6], 'pred': [105.31, 112.0, 101.29, 95.86]},
 'VHM_Ensemble_Short': {'actual': [102.3, 116.0, 114.5, 114.5], 'pred': [105.18, 111.7, 111.66, 117.23]},
 'VHM_Hierarchical_Long': {'actual': [99.2, 93.9, 101.5, 101.5], 'pred': [106.01, 105.04, 102.01, 106.45]},
 'VHM_Hierarchical_Medium': {'actual': [104.5, 104.0, 100.2, 99.6], 'pred': [107.54, 115.5, 113.84, 105.49]},
 'VHM_Hierarchical_Short': {'actual': [102.3, 116.0, 114.5, 114.5], 'pred': [105.5, 124.69, 114.33, 114.64]},
 'VHM_RoundRobin_Long': {'actual': [99.2, 93.9, 101.5, 101.5], 'pred': [107.83, 100.56, 105.05, 105.71]},
 'VHM_RoundRobin_Medium': {'actual': [104.5, 104.0, 100.2, 99.6], 'pred': [107.47, 105.23, 104.05, 106.21]},
 'VHM_RoundRobin_Short': {'actual': [102.3, 116.0, 114.5, 114.5], 'pred': [105.13, 122.73, 111.57, 113.68]}}

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
process_file(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\table\test6.tex')

print("Successfully processed test6.tex")
