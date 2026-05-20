import numpy as np
import pandas as pd
#GEMINI TRANSFORMER CODE
# Data extracted from the large table
data = {
    'CMG_Ensemble_Long': {'pred': [42.88, 36.78, 39.52, 39.13], 'actual': [41.9, 35.1, 35.2, 35.2]},
    'CMG_Ensemble_Medium': {'pred': [33.51, 41.94, 39.42, 39.59], 'actual': [40.8, 41.3, 39.6, 39.3]},
    'CMG_Ensemble_Short': {'pred': [41.94, 33.97, 34.36, 34.47], 'actual': [41.85, 37.3, 38.75, 38.75]},
    'CMG_Hierarchical_Long': {'pred': [49.31, 37.64, 37.93, 38.0], 'actual': [41.9, 35.1, 35.2, 35.2]},
    'CMG_Hierarchical_Medium': {'pred': [34.13, 32.06, 32.52, 32.22], 'actual': [40.8, 41.3, 39.6, 39.3]},
    'CMG_Hierarchical_Short': {'pred': [36.08, 34.0, 34.38, 39.12], 'actual': [41.85, 37.3, 38.75, 38.75]},
    'CMG_RoundRobin_Long': {'pred': [39.31, 27.64, 27.93, 36.74], 'actual': [41.9, 35.1, 35.2, 35.2]},
    'CMG_RoundRobin_Medium': {'pred': [41.18, 39.46, 38.88, 38.22], 'actual': [40.8, 41.3, 39.6, 39.3]},
    'CMG_RoundRobin_Short': {'pred': [35.39, 33.39, 33.52, 33.57], 'actual': [41.85, 37.3, 38.75, 38.75]},
    'DGC_Ensemble_Long': {'pred': [95.27, 92.82, 69.98, 71.6], 'actual': [96.0, 93.0, 70.2, 70.2]},
    'DGC_Ensemble_Medium': {'pred': [94.86, 91.06, 91.57, 94.59], 'actual': [99.5, 93.6, 94.6, 95.0]},
    'DGC_Ensemble_Short': {'pred': [99.03, 88.79, 94.61, 89.62], 'actual': [99.3, 93.2, 92.4, 92.4]},
    'DGC_Hierarchical_Long': {'pred': [95.27, 92.82, 68.37, 69.75], 'actual': [96.0, 93.0, 70.2, 70.2]},
    'DGC_Hierarchical_Medium': {'pred': [94.33, 99.7, 92.19, 91.18], 'actual': [99.5, 93.6, 94.6, 95.0]},
    'DGC_Hierarchical_Short': {'pred': [99.9, 88.47, 82.43, 93.48], 'actual': [99.3, 93.2, 92.4, 92.4]},
    'DGC_RoundRobin_Long': {'pred': [100.02, 96.33, 68.37, 70.35], 'actual': [96.0, 93.0, 70.2, 70.2]},
    'DGC_RoundRobin_Medium': {'pred': [95.27, 92.82, 98.37, 99.75], 'actual': [99.5, 93.6, 94.6, 95.0]},
    'DGC_RoundRobin_Short': {'pred': [98.86, 86.2, 91.14, 83.09], 'actual': [99.3, 93.2, 92.4, 92.4]},
    'DXG_Ensemble_Long': {'pred': [23.58, 23.33, 20.66, 21.19], 'actual': [21.2, 16.3, 17.8, 17.8]},
    'DXG_Ensemble_Medium': {'pred': [23.18, 22.91, 20.36, 20.79], 'actual': [24.05, 21.2, 20.15, 20.1]},
    'DXG_Ensemble_Short': {'pred': [23.97, 22.65, 20.15, 20.65], 'actual': [24.0, 22.6, 20.9, 20.9]},
    'DXG_Hierarchical_Long': {'pred': [23.86, 23.61, 20.92, 21.35], 'actual': [21.2, 16.3, 17.8, 17.8]},
    'DXG_Hierarchical_Medium': {'pred': [23.31, 20.94, 18.13, 20.94], 'actual': [24.05, 21.2, 20.15, 20.1]},
    'DXG_Hierarchical_Short': {'pred': [23.0, 21.69, 19.89, 17.66], 'actual': [24.0, 22.6, 20.9, 20.9]},
    'DXG_RoundRobin_Long': {'pred': [24.01, 23.92, 20.74, 21.4], 'actual': [21.2, 16.3, 17.8, 17.8]},
    'DXG_RoundRobin_Medium': {'pred': [19.38, 23.1, 18.34, 20.89], 'actual': [24.05, 21.2, 20.15, 20.1]},
    'DXG_RoundRobin_Short': {'pred': [23.07, 22.77, 20.17, 18.35], 'actual': [24.0, 22.6, 20.9, 20.9]},
    'FPT_Ensemble_Long': {'pred': [103.14, 93.09, 94.23, 98.15], 'actual': [103.9, 93.8, 93.9, 93.9]},
    'FPT_Ensemble_Medium': {'pred': [101.63, 101.88, 103.09, 96.52], 'actual': [101.9, 102.7, 103.3, 100.9]},
    'FPT_Ensemble_Short': {'pred': [101.08, 89.37, 92.53, 96.48], 'actual': [105.0, 88.1, 97.7, 97.7]},
    'FPT_Hierarchical_Long': {'pred': [103.71, 91.69, 94.59, 98.65], 'actual': [103.9, 93.8, 93.9, 93.9]},
    'FPT_Hierarchical_Medium': {'pred': [101.91, 90.01, 93.36, 97.22], 'actual': [101.9, 102.7, 103.3, 100.9]},
    'FPT_Hierarchical_Short': {'pred': [101.09, 89.47, 92.61, 96.6], 'actual': [105.0, 88.1, 97.7, 97.7]},
    'FPT_RoundRobin_Long': {'pred': [104.16, 90.96, 94.52, 98.65], 'actual': [103.9, 93.8, 93.9, 93.9]},
    'FPT_RoundRobin_Medium': {'pred': [102.01, 89.19, 93.29, 97.28], 'actual': [101.9, 102.7, 103.3, 100.9]},
    'FPT_RoundRobin_Short': {'pred': [101.16, 89.35, 92.59, 93.48], 'actual': [105.0, 88.1, 97.7, 97.7]},
    'HPG_Ensemble_Long': {'pred': [28.11, 27.98, 26.5, 27.35], 'actual': [26.7, 26.25, 26.7, 26.7]},
    'HPG_Ensemble_Medium': {'pred': [27.8, 28.58, 27.06, 26.5], 'actual': [30.35, 26.9, 26.75, 26.3]},
    'HPG_Ensemble_Short': {'pred': [27.65, 28.4, 26.93, 26.83], 'actual': [29.85, 28.0, 26.4, 26.4]},
    'HPG_Hierarchical_Long': {'pred': [28.17, 29.12, 26.42, 27.37], 'actual': [26.7, 26.25, 26.7, 26.7]},
    'HPG_Hierarchical_Medium': {'pred': [27.83, 28.68, 27.1, 26.97], 'actual': [30.35, 26.9, 26.75, 26.3]},
    'HPG_Hierarchical_Short': {'pred': [27.67, 28.44, 26.94, 26.55], 'actual': [29.85, 28.0, 26.4, 26.4]},
    'HPG_RoundRobin_Long': {'pred': [26.41, 29.3, 27.41, 27.23], 'actual': [26.7, 26.25, 26.7, 26.7]},
    'HPG_RoundRobin_Medium': {'pred': [28.84, 29.01, 26.06, 26.89], 'actual': [30.35, 26.9, 26.75, 26.3]},
    'HPG_RoundRobin_Short': {'pred': [28.84, 29.63, 26.29, 26.79], 'actual': [29.85, 28.0, 26.4, 26.4]},
    'KDH_Ensemble_Long': {'pred': [35.32, 30.02, 34.05, 32.85], 'actual': [35.85, 29.6, 32.65, 32.65]},
    'KDH_Ensemble_Medium': {'pred': [32.59, 35.96, 36.9, 34.41], 'actual': [34.85, 35.85, 35.6, 34.95]},
    'KDH_Ensemble_Short': {'pred': [35.62, 33.48, 31.12, 31.58], 'actual': [36.75, 33.9, 33.8, 33.8]},
    'KDH_Hierarchical_Long': {'pred': [39.2, 27.36, 35.21, 35.56], 'actual': [35.85, 29.6, 32.65, 32.65]},
    'KDH_Hierarchical_Medium': {'pred': [33.52, 31.46, 29.22, 34.52], 'actual': [34.85, 35.85, 35.6, 34.95]},
    'KDH_Hierarchical_Short': {'pred': [35.84, 33.59, 31.19, 31.16], 'actual': [36.75, 33.9, 33.8, 33.8]},
    'KDH_RoundRobin_Long': {'pred': [35.88, 29.12, 25.4, 35.76], 'actual': [35.85, 29.6, 32.65, 32.65]},
    'KDH_RoundRobin_Medium': {'pred': [32.2, 30.45, 37.01, 36.98], 'actual': [34.85, 35.85, 35.6, 34.95]},
    'KDH_RoundRobin_Short': {'pred': [35.53, 33.12, 33.67, 31.0], 'actual': [36.75, 33.9, 33.8, 33.8]},
    'MBB_Ensemble_Long': {'pred': [24.22, 23.42, 26.31, 24.98], 'actual': [23.6, 23.75, 24.7, 24.7]},
    'MBB_Ensemble_Medium': {'pred': [27.11, 23.14, 25.25, 22.39], 'actual': [26.85, 23.95, 24.0, 23.9]},
    'MBB_Ensemble_Short': {'pred': [28.35, 26.15, 24.3, 24.47], 'actual': [28.25, 27.1, 24.4, 24.4]},
    'MBB_Hierarchical_Long': {'pred': [24.22, 22.19, 27.22, 26.14], 'actual': [23.6, 23.75, 24.7, 24.7]},
    'MBB_Hierarchical_Medium': {'pred': [28.23, 23.43, 24.19, 21.42], 'actual': [26.85, 23.95, 24.0, 23.9]},
    'MBB_Hierarchical_Short': {'pred': [28.87, 27.41, 24.98, 23.41], 'actual': [28.25, 27.1, 24.4, 24.4]},
    'MBB_RoundRobin_Long': {'pred': [20.43, 24.14, 24.43, 24.88], 'actual': [23.6, 23.75, 24.7, 24.7]},
    'MBB_RoundRobin_Medium': {'pred': [28.42, 22.94, 26.13, 22.43], 'actual': [26.85, 23.95, 24.0, 23.9]},
    'MBB_RoundRobin_Short': {'pred': [29.43, 27.35, 25.21, 26.22], 'actual': [28.25, 27.1, 24.4, 24.4]},
    'MWG_Ensemble_Long': {'pred': [80.38, 76.79, 85.31, 86.68], 'actual': [82.6, 77.7, 82.9, 82.9]},
    'MWG_Ensemble_Medium': {'pred': [79.0, 85.64, 83.92, 85.52], 'actual': [79.5, 83.9, 81.8, 80.2]},
    'MWG_Ensemble_Short': {'pred': [78.49, 85.06, 83.48, 84.95], 'actual': [77.5, 84.5, 85.7, 85.7]},
    'MWG_Hierarchical_Long': {'pred': [80.53, 87.25, 85.63, 87.32], 'actual': [82.6, 77.7, 82.9, 82.9]},
    'MWG_Hierarchical_Medium': {'pred': [79.14, 85.93, 84.26, 85.82], 'actual': [79.5, 83.9, 81.8, 80.2]},
    'MWG_Hierarchical_Short': {'pred': [78.54, 85.09, 83.53, 85.15], 'actual': [77.5, 84.5, 85.7, 85.7]},
    'MWG_RoundRobin_Long': {'pred': [81.67, 85.75, 81.22, 87.7], 'actual': [82.6, 77.7, 82.9, 82.9]},
    'MWG_RoundRobin_Medium': {'pred': [79.76, 86.44, 84.31, 85.85], 'actual': [79.5, 83.9, 81.8, 80.2]},
    'MWG_RoundRobin_Short': {'pred': [78.8, 85.31, 83.63, 85.2], 'actual': [77.5, 84.5, 85.7, 85.7]},
    'TCB_Ensemble_Long': {'pred': [39.43, 42.14, 38.43, 33.02], 'actual': [35.1, 32.0, 33.6, 33.6]},
    'TCB_Ensemble_Medium': {'pred': [39.03, 41.77, 38.08, 34.41], 'actual': [39.0, 35.7, 35.0, 34.1]},
    'TCB_Ensemble_Short': {'pred': [38.78, 41.5, 37.88, 35.2], 'actual': [39.6, 40.65, 36.1, 36.1]},
    'TCB_Hierarchical_Long': {'pred': [39.68, 38.43, 38.52, 34.09], 'actual': [35.1, 32.0, 33.6, 33.6]},
    'TCB_Hierarchical_Medium': {'pred': [39.09, 41.85, 35.23, 36.59], 'actual': [39.0, 35.7, 35.0, 34.1]},
    'TCB_Hierarchical_Short': {'pred': [38.84, 41.52, 37.88, 38.25], 'actual': [39.6, 40.65, 36.1, 36.1]},
    'TCB_RoundRobin_Long': {'pred': [39.88, 32.71, 38.6, 38.87], 'actual': [35.1, 32.0, 33.6, 33.6]},
    'TCB_RoundRobin_Medium': {'pred': [39.23, 41.97, 38.12, 38.49], 'actual': [39.0, 35.7, 35.0, 34.1]},
    'TCB_RoundRobin_Short': {'pred': [38.85, 41.54, 36.27, 38.27], 'actual': [39.6, 40.65, 36.1, 36.1]},
    'VCB_Ensemble_Long': {'pred': [69.33, 55.87, 60.25, 60.69], 'actual': [60.7, 56.8, 57.5, 57.5]},
    'VCB_Ensemble_Medium': {'pred': [68.66, 63.41, 59.86, 60.11], 'actual': [65.8, 60.6, 60.1, 60.8]},
    'VCB_Ensemble_Short': {'pred': [68.36, 63.14, 59.52, 59.83], 'actual': [68.6, 61.9, 59.5, 59.5]},
    'VCB_Hierarchical_Long': {'pred': [69.41, 64.05, 60.44, 58.79], 'actual': [60.7, 56.8, 57.5, 57.5]},
    'VCB_Hierarchical_Medium': {'pred': [68.7, 63.43, 59.87, 60.18], 'actual': [65.8, 60.6, 60.1, 60.8]},
    'VCB_Hierarchical_Short': {'pred': [68.37, 63.19, 59.56, 61.88], 'actual': [68.6, 61.9, 59.5, 59.5]},
    'VCB_RoundRobin_Long': {'pred': [69.99, 54.31, 60.37, 60.55], 'actual': [60.7, 56.8, 57.5, 57.5]},
    'VCB_RoundRobin_Medium': {'pred': [68.89, 63.6, 59.79, 60.08], 'actual': [65.8, 60.6, 60.1, 60.8]},
    'VCB_RoundRobin_Short': {'pred': [68.44, 63.19, 59.53, 59.82], 'actual': [68.6, 61.9, 59.5, 59.5]},
    'VCS_Ensemble_Long': {'pred': [48.86, 46.57, 44.85, 44.9], 'actual': [47.6, 46.5, 43.0, 43.0]},
    'VCS_Ensemble_Medium': {'pred': [52.54, 47.16, 44.28, 44.28], 'actual': [50.0, 47.4, 47.1, 46.9]},
    'VCS_Ensemble_Short': {'pred': [47.19, 45.64, 43.99, 43.97], 'actual': [48.8, 46.8, 46.2, 46.2]},
    'VCS_Hierarchical_Long': {'pred': [48.32, 46.59, 44.97, 45.11], 'actual': [47.6, 46.5, 43.0, 43.0]},
    'VCS_Hierarchical_Medium': {'pred': [47.72, 46.07, 44.37, 42.31], 'actual': [50.0, 47.4, 47.1, 46.9]},
    'VCS_Hierarchical_Short': {'pred': [47.26, 45.67, 44.06, 44.05], 'actual': [48.8, 46.8, 46.2, 46.2]},
    'VCS_RoundRobin_Long': {'pred': [48.05, 47.39, 45.88, 45.77], 'actual': [47.6, 46.5, 43.0, 43.0]},
    'VCS_RoundRobin_Medium': {'pred': [47.58, 47.99, 48.21, 46.33], 'actual': [50.0, 47.4, 47.1, 46.9]},
    'VCS_RoundRobin_Short': {'pred': [47.23, 45.71, 43.98, 44.01], 'actual': [48.8, 46.8, 46.2, 46.2]},
    'VHM_Ensemble_Long': {'pred': [97.62, 95.53, 104.03, 105.83], 'actual': [99.2, 93.9, 101.5, 101.5]},
    'VHM_Ensemble_Medium': {'pred': [106.03, 103.8, 102.32, 99.5], 'actual': [104.5, 104.0, 100.2, 99.6]},
    'VHM_Ensemble_Short': {'pred': [101.14, 122.91, 111.53, 113.67], 'actual': [102.3, 116.0, 114.5, 114.5]},
    'VHM_Hierarchical_Long': {'pred': [97.97, 107.0, 114.76, 106.61], 'actual': [99.2, 93.9, 101.5, 101.5]},
    'VHM_Hierarchical_Medium': {'pred': [106.31, 104.43, 112.53, 104.52], 'actual': [104.5, 104.0, 100.2, 99.6]},
    'VHM_Hierarchical_Short': {'pred': [105.28, 123.23, 111.77, 113.8], 'actual': [102.3, 116.0, 114.5, 114.5]},
    'VHM_RoundRobin_Long': {'pred': [108.85, 100.95, 105.22, 106.08], 'actual': [99.2, 93.9, 101.5, 101.5]},
    'VHM_RoundRobin_Medium': {'pred': [106.72, 105.79, 103.0, 104.64], 'actual': [104.5, 104.0, 100.2, 99.6]},
    'VHM_RoundRobin_Short': {'pred': [105.54, 123.89, 111.92, 113.88], 'actual': [102.3, 116.0, 114.5, 114.5]},
}

def calculate_metrics(predicted, actual):
    """Calculate MAE, RMSE, and MAPE"""
    predicted = np.array(predicted)
    actual = np.array(actual)
    
    # MAE
    mae = np.mean(np.abs(predicted - actual))
    
    # RMSE
    rmse = np.sqrt(np.mean((predicted - actual) ** 2))
    
    # MAPE
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    
    return mae, rmse, mape

# Calculate metrics for each combination
results = {}
for key, values in data.items():
    mae, rmse, mape = calculate_metrics(values['pred'], values['actual'])
    results[key] = {'MAE': mae, 'RMSE': rmse, 'MAPE': mape}

# Group results by stock and time horizon
# Dynamically extract all stock symbols from the data keys to support any number of stocks
stocks = []
for key in data.keys():
    stock = key.split('_')[0]
    if stock not in stocks:
        stocks.append(stock)

architectures = ['Hierarchical', 'RoundRobin', 'Ensemble']
horizons = ['Short', 'Medium', 'Long']

print("="*80)
print("PERFORMANCE METRICS CALCULATION RESULTS")
print("="*80)

for horizon in horizons:
    print(f"\n{horizon.upper()}-TERM PERFORMANCE")
    print("-" * 50)
    
    for stock in stocks:
        print(f"\n{stock}:")
        arch_results = []
        
        for arch in architectures:
            key = f"{stock}_{arch}_{horizon}"
            if key in results:
                mae = results[key]['MAE']
                rmse = results[key]['RMSE']
                mape = results[key]['MAPE']
                arch_results.append((arch, mae, rmse, mape))
                print(f"  {arch:12} | MAE: {mae:5.2f} | RMSE: {rmse:5.2f} | MAPE: {mape:5.2f}%")
        
        # Find best architecture for this stock and horizon
        if arch_results:
            best_arch = min(arch_results, key=lambda x: x[3])  # Sort by MAPE
            print(f"  {'BEST':12} | {best_arch[0]} (MAPE: {best_arch[3]:.2f}%)")

# Generate LaTeX table format
print("\n" + "="*80)
print("LATEX TABLE FORMAT")
print("="*80)

for horizon in horizons:
    print(f"\n\\subsubsection{{{horizon.capitalize()}-term Performance}}")
    print("\\begin{table}[!h]")
    print("\\centering")
    print(f"\\caption{{Average {horizon.capitalize()}-term Performance of Prediction Architectures Across Stocks}}")
    print("\\resizebox{\\columnwidth}{!}{")
    print("\\begin{tabular}{c c c c c}")
    print("\\hline")
    print("\\textbf{Stock} & \\textbf{Architecture} & \\textbf{Avg MAE} & \\textbf{Avg RMSE} & \\textbf{Avg MAPE} \\\\")
    print("\\hline")
    
    for stock in stocks:
        print(f"\n\\multirow{{3}}{{*}}{{\\textbf{{{stock}}}}}")
        
        # Get results for this stock and horizon
        stock_results = []
        for arch in architectures:
            key = f"{stock}_{arch}_{horizon}"
            if key in results:
                mae = results[key]['MAE']
                rmse = results[key]['RMSE']
                mape = results[key]['MAPE']
                arch_name = "Ensemble Voting" if arch == "Ensemble" else arch
                stock_results.append((arch_name, mae, rmse, mape))
        
        # Sort by MAPE to put best first
        stock_results.sort(key=lambda x: x[3])
        
        for i, (arch_name, mae, rmse, mape) in enumerate(stock_results):
            if i == 0:  # Best performance - bold
                print(f"& {arch_name:15} & \\textbf{{{mae:.2f}}} & \\textbf{{{rmse:.2f}}} & \\textbf{{{mape:.1f}\\%}} \\\\")
            else:
                print(f"& {arch_name:15} & {mae:.2f} & {rmse:.2f} & {mape:.1f}\\% \\\\")
        
        print("\\hline")
    
    print("\n\\end{tabular}")
    print("}")
    print("\\end{table}")

print("\n" + "="*80)
print("OVERALL ARCHITECTURE AVERAGES ACROSS ALL STOCKS (LLM: Gemini 2.0 Flash)")
print("="*80)
for horizon in horizons:
    print(f"\n{horizon.upper()}-TERM GLOBAL AVERAGES:")
    print("-" * 65)
    print(f"{'Architecture':<15} | {'Avg MAE':<10} | {'Avg RMSE':<10} | {'Avg MAPE':<10}")
    print("-" * 65)
    for arch in architectures:
        maes, rmses, mapes = [], [], []
        for stock in stocks:
            key = f"{stock}_{arch}_{horizon}"
            if key in results:
                maes.append(results[key]['MAE'])
                rmses.append(results[key]['RMSE'])
                mapes.append(results[key]['MAPE'])
        if mapes:
            print(f"{arch:<15} | {np.mean(maes):<10.2f} | {np.mean(rmses):<10.2f} | {np.mean(mapes):<9.2f}%")
    print("-" * 65)

print("\n" + "="*80)
print("CALCULATION COMPLETE!")
print("="*80)