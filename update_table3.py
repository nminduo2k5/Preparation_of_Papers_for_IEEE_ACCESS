#LLama-Transformer
import re

data = {   'DXG_Hierarchical_Short': {'pred': [23.64, 23.57, 19.44, 21.40], 'actual': [24, 22.60, 20.90, 20.90]},
    'DXG_Hierarchical_Medium': {'pred': [21.06, 24.10, 21.26, 21.27], 'actual': [24.05, 21.20, 20.15, 20.10]},
    'DXG_Hierarchical_Long': {'pred': [23.76, 26.53, 20.78, 17.66], 'actual': [21.20, 16.30, 17.80, 17.80]},
    'DXG_RoundRobin_Short': {'pred': [21.77, 22.18, 20.79, 19.99], 'actual': [24, 22.60, 20.90, 20.90]},
    'DXG_RoundRobin_Medium': {'pred': [22.45, 22.12, 21.63, 20.04], 'actual': [24.05, 21.20, 20.15, 20.10]},
    'DXG_RoundRobin_Long': {'pred': [22.71, 16.55, 19.53, 22.34], 'actual': [21.20, 16.30, 17.80, 17.80]},
    'DXG_Ensemble_Short': {'pred': [25.26, 23.47, 20.34, 20.43], 'actual': [24, 22.60, 20.90, 20.90]},
    'DXG_Ensemble_Medium': {'pred': [22.07, 21.63, 20.97, 19.22], 'actual': [24.05, 21.20, 20.15, 20.10]},
    'DXG_Ensemble_Long': {'pred': [24.53, 16.87, 20.93, 20.95], 'actual': [21.20, 16.30, 17.80, 17.80]},
    'FPT_Hierarchical_Short': {'pred': [103.42, 89.22, 90.92, 97.44], 'actual': [105, 88.10, 97.70, 97.70]},
    'FPT_Hierarchical_Medium': {'pred': [102.82, 91.62, 102.65, 93.93], 'actual': [101.90, 102.70, 103.30, 100.90]},
    'FPT_Hierarchical_Long': {'pred': [101.14, 92.18, 94.20, 100.24], 'actual': [103.90, 93.80, 93.90, 93.90]},
    'FPT_RoundRobin_Short': {'pred': [101.65, 88.96, 90.80, 97.90], 'actual': [105, 88.10, 97.70, 97.70]},
    'FPT_RoundRobin_Medium': {'pred': [101.39, 83.64, 94.23, 94.45], 'actual': [101.90, 102.70, 103.30, 100.90]},
    'FPT_RoundRobin_Long': {'pred': [103.54, 90.52, 92.91, 96.67], 'actual': [103.90, 93.80, 93.90, 93.90]},
    'FPT_Ensemble_Short': {'pred': [98.49, 87.63, 91.67, 98.20], 'actual': [105, 88.10, 97.70, 97.70]},
    'FPT_Ensemble_Medium': {'pred': [100.94, 95.87, 82.46, 100.37], 'actual': [101.90, 102.70, 103.30, 100.90]},
    'FPT_Ensemble_Long': {'pred': [100.20, 90.66, 93.35, 99.31], 'actual': [103.90, 93.80, 93.90, 93.90]},
    'VCB_Hierarchical_Short': {'pred': [69.61, 64.60, 59.13, 58.67], 'actual': [68.60, 61.90, 59.50, 59.50]},
    'VCB_Hierarchical_Medium': {'pred': [70.49, 64.26, 60.01, 58.62], 'actual': [65.80, 60.60, 60.10, 60.80]},
    'VCB_Hierarchical_Long': {'pred': [76.50, 56.59, 56.92, 59.32], 'actual': [60.70, 56.80, 57.50, 57.50]},
    'VCB_RoundRobin_Short': {'pred': [68.25, 63.06, 60.34, 60.44], 'actual': [68.60, 61.90, 59.50, 59.50]},
    'VCB_RoundRobin_Medium': {'pred': [71.33, 61.08, 60.70, 61.02], 'actual': [65.80, 60.60, 60.10, 60.80]},
    'VCB_RoundRobin_Long': {'pred': [74.21, 65.22, 58.02, 61.16], 'actual': [60.70, 56.80, 57.50, 57.50]},
    'VCB_Ensemble_Short': {'pred': [70.09, 61.82, 59.78, 60.22], 'actual': [68.60, 61.90, 59.50, 59.50]},
    'VCB_Ensemble_Medium': {'pred': [67.52, 65.17, 58.25, 58.40], 'actual': [65.80, 60.60, 60.10, 60.80]},
    'VCB_Ensemble_Long': {'pred': [64.14, 65.72, 55.53, 59.02], 'actual': [60.70, 56.80, 57.50, 57.50]},
    'VCS_Hierarchical_Short': {'pred': [47.69, 46.56, 44.33, 47.32], 'actual': [48.80, 46.80, 46.20, 46.20]},
    'VCS_Hierarchical_Medium': {'pred': [49.45, 45.96, 44.86, 43.82], 'actual': [50, 47.40, 47.10, 46.90]},
    'VCS_Hierarchical_Long': {'pred': [50.47, 46.36, 43.56, 48.23], 'actual': [47.60, 46.50, 43, 43]},
    'VCS_RoundRobin_Short': {'pred': [48.21, 46.30, 43.94, 45.78], 'actual': [48.80, 46.80, 46.20, 46.20]},
    'VCS_RoundRobin_Medium': {'pred': [49.29, 46.77, 45.38, 43.01], 'actual': [50, 47.40, 47.10, 46.90]},
    'VCS_RoundRobin_Long': {'pred': [48.72, 46.73, 43.26, 47.73], 'actual': [47.60, 46.50, 43, 43]},
    'VCS_Ensemble_Short': {'pred': [49.98, 45.52, 44.42, 46.30], 'actual': [48.80, 46.80, 46.20, 46.20]},
    'VCS_Ensemble_Medium': {'pred': [46.68, 48.23, 47.16, 43.90], 'actual': [50, 47.40, 47.10, 46.90]},
    'VCS_Ensemble_Long': {'pred': [48.22, 47.75, 44.45, 44.91], 'actual': [47.60, 46.50, 43, 43]},
    'HPG_Hierarchical_Short': {'pred': [25.39, 28.12, 27.09, 28.31], 'actual': [29.85, 28, 26.40, 26.40]},
    'HPG_Hierarchical_Medium': {'pred': [24.37, 28.03, 26.37, 24.87], 'actual': [30.35, 26.90, 26.75, 26.30]},
    'HPG_Hierarchical_Long': {'pred': [26.56, 27.91, 27.25, 27.39], 'actual': [26.70, 26.25, 26.70, 26.70]},
    'HPG_RoundRobin_Short': {'pred': [27.98, 28.68, 28.11, 27.01], 'actual': [29.85, 28, 26.40, 26.40]},
    'HPG_RoundRobin_Medium': {'pred': [28.77, 26.28, 27.01, 27.11], 'actual': [30.35, 26.90, 26.75, 26.30]},
    'HPG_RoundRobin_Long': {'pred': [27.74, 27.70, 25.46, 26.15], 'actual': [26.70, 26.25, 26.70, 26.70]},
    'HPG_Ensemble_Short': {'pred': [28.00, 27.56, 27.38, 25.55], 'actual': [29.85, 28, 26.40, 26.40]},
    'HPG_Ensemble_Medium': {'pred': [25.13, 29.63, 28.08, 25.71], 'actual': [30.35, 26.90, 26.75, 26.30]},
    'HPG_Ensemble_Long': {'pred': [26.60, 28.89, 27.73, 26.86], 'actual': [26.70, 26.25, 26.70, 26.70]},
    'TCB_Hierarchical_Short': {'pred': [38.68, 41.13, 35.61, 40.05], 'actual': [39.60, 40.65, 36.10, 36.10]},
    'TCB_Hierarchical_Medium': {'pred': [39.72, 37.49, 36.21, 35.82], 'actual': [39, 35.70, 35, 34.10]},
    'TCB_Hierarchical_Long': {'pred': [42.55, 50.84, 35.67, 42.05], 'actual': [35.10, 32, 33.60, 33.60]},
    'TCB_RoundRobin_Short': {'pred': [40.57, 41.70, 37.52, 37.57], 'actual': [39.60, 40.65, 36.10, 36.10]},
    'TCB_RoundRobin_Medium': {'pred': [40.81, 43.55, 39.51, 35.11], 'actual': [39, 35.70, 35, 34.10]},
    'TCB_RoundRobin_Long': {'pred': [37.60, 50.39, 39.10, 32.63], 'actual': [35.10, 32, 33.60, 33.60]},
    'TCB_Ensemble_Short': {'pred': [38.30, 40.02, 38.67, 39.99], 'actual': [39.60, 40.65, 36.10, 36.10]},
    'TCB_Ensemble_Medium': {'pred': [37.17, 41.73, 35.72, 33.09], 'actual': [39, 35.70, 35, 34.10]},
    'TCB_Ensemble_Long': {'pred': [42.30, 43.06, 36.90, 40.75], 'actual': [35.10, 32, 33.60, 33.60]},
    'VHM_Hierarchical_Short': {'pred': [102.10, 121.05, 110.41, 113.74], 'actual': [102.30, 116, 114.50, 114.50]},
    'VHM_Hierarchical_Medium': {'pred': [104.26, 133.99, 105.07, 115.12], 'actual': [104.50, 104, 100.20, 99.60]},
    'VHM_Hierarchical_Long': {'pred': [101.31, 114.42, 102.86, 116.11], 'actual': [99.20, 93.90, 101.50, 101.50]},
    'VHM_RoundRobin_Short': {'pred': [105.86, 127.05, 110.18, 116.10], 'actual': [102.30, 116, 114.50, 114.50]},
    'VHM_RoundRobin_Medium': {'pred': [103.65, 128.94, 108.69, 122.83], 'actual': [104.50, 104, 100.20, 99.60]},
    'VHM_RoundRobin_Long': {'pred': [107.88, 106.58, 108.94, 117.16], 'actual': [99.20, 93.90, 101.50, 101.50]},
    'VHM_Ensemble_Short': {'pred': [105.62, 123.97, 111.98, 113.42], 'actual': [102.30, 116, 114.50, 114.50]},
    'VHM_Ensemble_Medium': {'pred': [105.51, 124.45, 106.74, 124.21], 'actual': [104.50, 104, 100.20, 99.60]},
    'VHM_Ensemble_Long': {'pred': [105.58, 103.94, 105.24, 106.51], 'actual': [99.20, 93.90, 101.50, 101.50]},
    'MWG_Hierarchical_Short': {'pred': [78.93, 85.45, 82.00, 85.80], 'actual': [77.50, 84.50, 85.70, 85.70]},
    'MWG_Hierarchical_Medium': {'pred': [76.03, 84.30, 83.48, 80.59], 'actual': [79.50, 83.90, 81.80, 80.20]},
    'MWG_Hierarchical_Long': {'pred': [74.05, 83.40, 82.16, 84.24], 'actual': [82.60, 77.70, 82.90, 82.90]},
    'MWG_RoundRobin_Short': {'pred': [77.86, 83.83, 84.77, 83.51], 'actual': [77.50, 84.50, 85.70, 85.70]},
    'MWG_RoundRobin_Medium': {'pred': [77.22, 83.17, 81.90, 87.20], 'actual': [79.50, 83.90, 81.80, 80.20]},
    'MWG_RoundRobin_Long': {'pred': [72.59, 83.46, 82.02, 83.27], 'actual': [82.60, 77.70, 82.90, 82.90]},
    'MWG_Ensemble_Short': {'pred': [77.26, 85.28, 83.67, 82.73], 'actual': [77.50, 84.50, 85.70, 85.70]},
    'MWG_Ensemble_Medium': {'pred': [78.11, 84.10, 81.47, 84.57], 'actual': [79.50, 83.90, 81.80, 80.20]},
    'MWG_Ensemble_Long': {'pred': [77.73, 79.13, 83.38, 85.74], 'actual': [82.60, 77.70, 82.90, 82.90]},
    'CMG_Hierarchical_Short': {'pred': [38.59, 37.58, 38.98, 37.35], 'actual': [41.85, 37.30, 38.75, 38.75]},
    'CMG_Hierarchical_Medium': {'pred': [39.86, 39.28, 40.15, 37.20], 'actual': [40.80, 41.30, 39.60, 39.30]},
    'CMG_Hierarchical_Long': {'pred': [41.22, 37.73, 38.59, 38.32], 'actual': [41.90, 35.10, 35.20, 35.20]},
    'CMG_RoundRobin_Short': {'pred': [42.68, 39.04, 39.08, 37.67], 'actual': [41.85, 37.30, 38.75, 38.75]},
    'CMG_RoundRobin_Medium': {'pred': [39.96, 35.47, 38.21, 38.59], 'actual': [40.80, 41.30, 39.60, 39.30]},
    'CMG_RoundRobin_Long': {'pred': [40.79, 40.43, 36.25, 37.97], 'actual': [41.90, 35.10, 35.20, 35.20]},
    'CMG_Ensemble_Short': {'pred': [40.72, 39.45, 38.63, 39.76], 'actual': [41.85, 37.30, 38.75, 38.75]},
    'CMG_Ensemble_Medium': {'pred': [41.63, 38.96, 37.09, 37.60], 'actual': [40.80, 41.30, 39.60, 39.30]},
    'CMG_Ensemble_Long': {'pred': [41.34, 39.36, 41.25, 38.65], 'actual': [41.90, 35.10, 35.20, 35.20]},
    'KDH_Hierarchical_Short': {'pred': [36.87, 34.61, 30.55, 30.35], 'actual': [36.75, 33.90, 33.80, 33.80]},
    'KDH_Hierarchical_Medium': {'pred': [33.90, 35.80, 27.85, 34.53], 'actual': [34.85, 35.85, 35.60, 34.95]},
    'KDH_Hierarchical_Long': {'pred': [38.05, 30.76, 31.58, 31.57], 'actual': [35.85, 29.60, 32.65, 32.65]},
    'KDH_RoundRobin_Short': {'pred': [35.73, 33.21, 30.46, 30.73], 'actual': [36.75, 33.90, 33.80, 33.80]},
    'KDH_RoundRobin_Medium': {'pred': [37.40, 33.87, 27.90, 32.66], 'actual': [34.85, 35.85, 35.60, 34.95]},
    'KDH_RoundRobin_Long': {'pred': [37.89, 30.14, 30.59, 30.94], 'actual': [35.85, 29.60, 32.65, 32.65]},
    'KDH_Ensemble_Short': {'pred': [36.84, 35.93, 34.55, 32.82], 'actual': [36.75, 33.90, 33.80, 33.80]},
    'KDH_Ensemble_Medium': {'pred': [37.45, 31.26, 32.00, 33.40], 'actual': [34.85, 35.85, 35.60, 34.95]},
    'KDH_Ensemble_Long': {'pred': [37.07, 29.37, 31.05, 29.86], 'actual': [35.85, 29.60, 32.65, 32.65]},
    'DGC_Hierarchical_Short': {'pred': [98.40, 96.61, 92.64, 91.59], 'actual': [99.30, 93.20, 92.40, 92.40]},
    'DGC_Hierarchical_Medium': {'pred': [100.23, 93.89, 87.83, 92.70], 'actual': [99.50, 93.60, 94.60, 95.00]},
    'DGC_Hierarchical_Long': {'pred': [98.66, 92.87, 97.49, 93.66], 'actual': [96.00, 93.00, 70.20, 70.20]},
    'DGC_RoundRobin_Short': {'pred': [99.15, 94.26, 86.76, 90.89], 'actual': [99.30, 93.20, 92.40, 92.40]},
    'DGC_RoundRobin_Medium': {'pred': [97.04, 95.48, 90.60, 93.18], 'actual': [99.50, 93.60, 94.60, 95.00]},
    'DGC_RoundRobin_Long': {'pred': [96.98, 97.13, 83.38, 101.42], 'actual': [96.00, 93.00, 70.20, 70.20]},
    'DGC_Ensemble_Short': {'pred': [96.96, 97.00, 86.98, 93.42], 'actual': [99.30, 93.20, 92.40, 92.40]},
    'DGC_Ensemble_Medium': {'pred': [99.20, 94.51, 89.57, 89.50], 'actual': [99.50, 93.60, 94.60, 95.00]},
    'DGC_Ensemble_Long': {'pred': [100.58, 93.21, 99.67, 105.37], 'actual': [96.00, 93.00, 70.20, 70.20]},
    'MBB_Hierarchical_Short': {'pred': [28.97, 26.43, 23.20, 26.63], 'actual': [28.25, 27.10, 24.40, 24.40]},
    'MBB_Hierarchical_Medium': {'pred': [26.97, 28.56, 23.24, 23.20], 'actual': [26.85, 23.95, 24.00, 23.90]},
    'MBB_Hierarchical_Long': {'pred': [23.43, 27.96, 24.44, 26.58], 'actual': [23.60, 23.75, 24.70, 24.70]},
    'MBB_RoundRobin_Short': {'pred': [28.56, 28.23, 24.12, 26.34], 'actual': [28.25, 27.10, 24.40, 24.40]},
    'MBB_RoundRobin_Medium': {'pred': [28.70, 25.34, 26.26, 25.85], 'actual': [26.85, 23.95, 24.00, 23.90]},
    'MBB_RoundRobin_Long': {'pred': [28.38, 28.85, 25.87, 24.59], 'actual': [23.60, 23.75, 24.70, 24.70]},
    'MBB_Ensemble_Short': {'pred': [25.36, 27.34, 25.18, 27.73], 'actual': [28.25, 27.10, 24.40, 24.40]},
    'MBB_Ensemble_Medium': {'pred': [27.43, 30.23, 25.04, 24.10], 'actual': [26.85, 23.95, 24.00, 23.90]},
    'MBB_Ensemble_Long': {'pred': [32.17, 22.97, 25.93, 25.04], 'actual': [23.60, 23.75, 24.70, 24.70]}}

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
process_file(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\test4.tex')

print("Successfully processed test4.tex")
