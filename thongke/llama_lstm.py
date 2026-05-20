import numpy as np
import pandas as pd
#LLAMA LSTM
# Data extracted from the large table
data = {   'DXG_Hierarchical_Short': {'pred': [22.22, 22.85, 20.80, 20.83], 'actual': [24, 22.60, 20.90, 20.90]},
    'DXG_Hierarchical_Medium': {'pred': [23.45, 21.57, 19.83, 19.27], 'actual': [24.05, 21.20, 20.15, 20.10]},
    'DXG_Hierarchical_Long': {'pred': [20.52, 25.38, 20.44, 18.23], 'actual': [21.20, 16.30, 17.80, 17.80]},
    'DXG_RoundRobin_Short': {'pred': [23.25, 21.19, 19.65, 19.79], 'actual': [24, 22.60, 20.90, 20.90]},
    'DXG_RoundRobin_Medium': {'pred': [23.70, 22.59, 19.16, 20.37], 'actual': [24.05, 21.20, 20.15, 20.10]},
    'DXG_RoundRobin_Long': {'pred': [21.80, 22.73, 20.30, 22.54], 'actual': [21.20, 16.30, 17.80, 17.80]},
    'DXG_Ensemble_Short': {'pred': [22.36, 23.39, 20.62, 19.74], 'actual': [24, 22.60, 20.90, 20.90]},
    'DXG_Ensemble_Medium': {'pred': [21.75, 21.54, 20.38, 19.36], 'actual': [24.05, 21.20, 20.15, 20.10]},
    'DXG_Ensemble_Long': {'pred': [23.88, 22.39, 23.04, 20.04], 'actual': [21.20, 16.30, 17.80, 17.80]},
    'FPT_Hierarchical_Short': {'pred': [103.64, 90.67, 92.28, 100.01], 'actual': [105, 88.10, 97.70, 97.70]},
    'FPT_Hierarchical_Medium': {'pred': [100.74, 95.39, 91.49, 93.00], 'actual': [101.90, 102.70, 103.30, 100.90]},
    'FPT_Hierarchical_Long': {'pred': [99.52, 91.25, 91.93, 99.45], 'actual': [103.90, 93.80, 93.90, 93.90]},
    'FPT_RoundRobin_Short': {'pred': [101.11, 89.17, 92.29, 95.73], 'actual': [105, 88.10, 97.70, 97.70]},
    'FPT_RoundRobin_Medium': {'pred': [101.69, 92.83, 86.98, 98.09], 'actual': [101.90, 102.70, 103.30, 100.90]},
    'FPT_RoundRobin_Long': {'pred': [99.16, 88.84, 93.11, 100.16], 'actual': [103.90, 93.80, 93.90, 93.90]},
    'FPT_Ensemble_Short': {'pred': [100.90, 87.61, 91.74, 96.38], 'actual': [105, 88.10, 97.70, 97.70]},
    'FPT_Ensemble_Medium': {'pred': [100.37, 101.52, 83.49, 95.53], 'actual': [101.90, 102.70, 103.30, 100.90]},
    'FPT_Ensemble_Long': {'pred': [102.29, 87.69, 94.86, 97.69], 'actual': [103.90, 93.80, 93.90, 93.90]},
    'VCB_Hierarchical_Short': {'pred': [68.25, 65.30, 59.40, 59.22], 'actual': [68.60, 61.90, 59.50, 59.50]},
    'VCB_Hierarchical_Medium': {'pred': [67.85, 60.09, 60.60, 59.50], 'actual': [65.80, 60.60, 60.10, 60.80]},
    'VCB_Hierarchical_Long': {'pred': [68.02, 73.78, 60.64, 58.00], 'actual': [60.70, 56.80, 57.50, 57.50]},
    'VCB_RoundRobin_Short': {'pred': [68.05, 62.04, 59.44, 60.66], 'actual': [68.60, 61.90, 59.50, 59.50]},
    'VCB_RoundRobin_Medium': {'pred': [69.56, 58.80, 57.98, 58.22], 'actual': [65.80, 60.60, 60.10, 60.80]},
    'VCB_RoundRobin_Long': {'pred': [64.52, 63.90, 60.96, 59.70], 'actual': [60.70, 56.80, 57.50, 57.50]},
    'VCB_Ensemble_Short': {'pred': [69.67, 63.90, 58.71, 59.15], 'actual': [68.60, 61.90, 59.50, 59.50]},
    'VCB_Ensemble_Medium': {'pred': [71.32, 63.98, 57.65, 59.87], 'actual': [65.80, 60.60, 60.10, 60.80]},
    'VCB_Ensemble_Long': {'pred': [59.23, 55.02, 57.91, 63.20], 'actual': [60.70, 56.80, 57.50, 57.50]},
    'VCS_Hierarchical_Short': {'pred': [47.65, 46.45, 44.01, 44.54], 'actual': [48.80, 46.80, 46.20, 46.20]},
    'VCS_Hierarchical_Medium': {'pred': [49.17, 45.08, 42.73, 44.73], 'actual': [50, 47.40, 47.10, 46.90]},
    'VCS_Hierarchical_Long': {'pred': [49.86, 46.58, 44.76, 46.20], 'actual': [47.60, 46.50, 43, 43]},
    'VCS_RoundRobin_Short': {'pred': [49.15, 45.80, 44.65, 44.86], 'actual': [48.80, 46.80, 46.20, 46.20]},
    'VCS_RoundRobin_Medium': {'pred': [49.82, 45.74, 43.05, 44.60], 'actual': [50, 47.40, 47.10, 46.90]},
    'VCS_RoundRobin_Long': {'pred': [49.43, 49.21, 44.68, 44.05], 'actual': [47.60, 46.50, 43, 43]},
    'VCS_Ensemble_Short': {'pred': [48.87, 47.13, 44.87, 47.69], 'actual': [48.80, 46.80, 46.20, 46.20]},
    'VCS_Ensemble_Medium': {'pred': [46.80, 48.09, 48.37, 47.88], 'actual': [50, 47.40, 47.10, 46.90]},
    'VCS_Ensemble_Long': {'pred': [46.44, 48.51, 45.37, 43.33], 'actual': [47.60, 46.50, 43, 43]},
    'HPG_Hierarchical_Short': {'pred': [27.20, 27.85, 28.10, 27.47], 'actual': [29.85, 28, 26.40, 26.40]},
    'HPG_Hierarchical_Medium': {'pred': [24.00, 28.86, 26.66, 26.88], 'actual': [30.35, 26.90, 26.75, 26.30]},
    'HPG_Hierarchical_Long': {'pred': [26.64, 31.10, 27.10, 26.00], 'actual': [26.70, 26.25, 26.70, 26.70]},
    'HPG_RoundRobin_Short': {'pred': [27.87, 27.33, 25.94, 27.67], 'actual': [29.85, 28, 26.40, 26.40]},
    'HPG_RoundRobin_Medium': {'pred': [28.17, 27.92, 26.69, 28.31], 'actual': [30.35, 26.90, 26.75, 26.30]},
    'HPG_RoundRobin_Long': {'pred': [25.52, 29.51, 25.96, 25.72], 'actual': [26.70, 26.25, 26.70, 26.70]},
    'HPG_Ensemble_Short': {'pred': [27.22, 26.50, 26.66, 26.50], 'actual': [29.85, 28, 26.40, 26.40]},
    'HPG_Ensemble_Medium': {'pred': [27.71, 32.05, 25.57, 26.51], 'actual': [30.35, 26.90, 26.75, 26.30]},
    'HPG_Ensemble_Long': {'pred': [26.57, 26.11, 26.91, 26.29], 'actual': [26.70, 26.25, 26.70, 26.70]},
    'TCB_Hierarchical_Short': {'pred': [38.94, 42.52, 36.32, 40.89], 'actual': [39.60, 40.65, 36.10, 36.10]},
    'TCB_Hierarchical_Medium': {'pred': [38.79, 46.76, 38.53, 41.33], 'actual': [39, 35.70, 35, 34.10]},
    'TCB_Hierarchical_Long': {'pred': [41.55, 37.74, 33.77, 29.07], 'actual': [35.10, 32, 33.60, 33.60]},
    'TCB_RoundRobin_Short': {'pred': [39.47, 41.37, 37.16, 35.09], 'actual': [39.60, 40.65, 36.10, 36.10]},
    'TCB_RoundRobin_Medium': {'pred': [38.39, 41.63, 35.69, 35.07], 'actual': [39, 35.70, 35, 34.10]},
    'TCB_RoundRobin_Long': {'pred': [30.17, 43.44, 33.84, 34.53], 'actual': [35.10, 32, 33.60, 33.60]},
    'TCB_Ensemble_Short': {'pred': [40.52, 41.04, 38.75, 40.90], 'actual': [39.60, 40.65, 36.10, 36.10]},
    'TCB_Ensemble_Medium': {'pred': [39.85, 35.29, 36.46, 38.80], 'actual': [39, 35.70, 35, 34.10]},
    'TCB_Ensemble_Long': {'pred': [42.56, 35.59, 39.19, 41.41], 'actual': [35.10, 32, 33.60, 33.60]},
    'VHM_Hierarchical_Short': {'pred': [105.61, 115.54, 106.67, 112.08], 'actual': [102.30, 116, 114.50, 114.50]},
    'VHM_Hierarchical_Medium': {'pred': [103.60, 133.52, 101.61, 121.61], 'actual': [104.50, 104, 100.20, 99.60]},
    'VHM_Hierarchical_Long': {'pred': [99.28, 111.14, 116.28, 114.30], 'actual': [99.20, 93.90, 101.50, 101.50]},
    'VHM_RoundRobin_Short': {'pred': [110.78, 127.83, 104.09, 115.57], 'actual': [102.30, 116, 114.50, 114.50]},
    'VHM_RoundRobin_Medium': {'pred': [104.60, 129.70, 113.96, 107.31], 'actual': [104.50, 104, 100.20, 99.60]},
    'VHM_RoundRobin_Long': {'pred': [109.81, 159.50, 109.00, 115.97], 'actual': [99.20, 93.90, 101.50, 101.50]},
    'VHM_Ensemble_Short': {'pred': [104.42, 117.56, 113.67, 112.04], 'actual': [102.30, 116, 114.50, 114.50]},
    'VHM_Ensemble_Medium': {'pred': [105.57, 146.99, 126.98, 106.06], 'actual': [104.50, 104, 100.20, 99.60]},
    'VHM_Ensemble_Long': {'pred': [102.47, 105.08, 101.01, 114.13], 'actual': [99.20, 93.90, 101.50, 101.50]},
    'MWG_Hierarchical_Short': {'pred': [77.02, 85.02, 82.30, 83.65], 'actual': [77.50, 84.50, 85.70, 85.70]},
    'MWG_Hierarchical_Medium': {'pred': [78.69, 85.20, 86.72, 82.19], 'actual': [79.50, 83.90, 81.80, 80.20]},
    'MWG_Hierarchical_Long': {'pred': [74.32, 81.73, 81.64, 86.22], 'actual': [82.60, 77.70, 82.90, 82.90]},
    'MWG_RoundRobin_Short': {'pred': [77.29, 82.85, 84.54, 83.47], 'actual': [77.50, 84.50, 85.70, 85.70]},
    'MWG_RoundRobin_Medium': {'pred': [77.60, 83.08, 82.54, 90.21], 'actual': [79.50, 83.90, 81.80, 80.20]},
    'MWG_RoundRobin_Long': {'pred': [82.25, 84.71, 82.47, 85.87], 'actual': [82.60, 77.70, 82.90, 82.90]},
    'MWG_Ensemble_Short': {'pred': [76.62, 86.34, 79.51, 85.25], 'actual': [77.50, 84.50, 85.70, 85.70]},
    'MWG_Ensemble_Medium': {'pred': [77.80, 84.16, 81.62, 82.69], 'actual': [79.50, 83.90, 81.80, 80.20]},
    'MWG_Ensemble_Long': {'pred': [78.74, 89.41, 83.22, 85.48], 'actual': [82.60, 77.70, 82.90, 82.90]},
    'CMG_Hierarchical_Short': {'pred': [44.35, 36.28, 38.52, 38.39], 'actual': [41.85, 37.30, 38.75, 38.75]},
    'CMG_Hierarchical_Medium': {'pred': [41.55, 37.52, 39.13, 37.81], 'actual': [40.80, 41.30, 39.60, 39.30]},
    'CMG_Hierarchical_Long': {'pred': [40.47, 38.29, 39.24, 37.19], 'actual': [41.90, 35.10, 35.20, 35.20]},
    'CMG_RoundRobin_Short': {'pred': [41.31, 39.34, 37.67, 37.87], 'actual': [41.85, 37.30, 38.75, 38.75]},
    'CMG_RoundRobin_Medium': {'pred': [42.04, 39.45, 36.42, 39.24], 'actual': [40.80, 41.30, 39.60, 39.30]},
    'CMG_RoundRobin_Long': {'pred': [39.15, 40.82, 36.43, 39.08], 'actual': [41.90, 35.10, 35.20, 35.20]},
    'CMG_Ensemble_Short': {'pred': [40.65, 37.44, 39.90, 37.68], 'actual': [41.85, 37.30, 38.75, 38.75]},
    'CMG_Ensemble_Medium': {'pred': [40.38, 35.86, 38.51, 39.97], 'actual': [40.80, 41.30, 39.60, 39.30]},
    'CMG_Ensemble_Long': {'pred': [42.34, 40.34, 40.71, 31.80], 'actual': [41.90, 35.10, 35.20, 35.20]},
    'KDH_Hierarchical_Short': {'pred': [37.70, 33.25, 32.24, 31.55], 'actual': [36.75, 33.90, 33.80, 33.80]},
    'KDH_Hierarchical_Medium': {'pred': [36.36, 31.98, 27.13, 31.60], 'actual': [34.85, 35.85, 35.60, 34.95]},
    'KDH_Hierarchical_Long': {'pred': [37.09, 38.05, 32.43, 32.57], 'actual': [35.85, 29.60, 32.65, 32.65]},
    'KDH_RoundRobin_Short': {'pred': [37.80, 35.28, 32.17, 30.05], 'actual': [36.75, 33.90, 33.80, 33.80]},
    'KDH_RoundRobin_Medium': {'pred': [36.86, 33.55, 35.91, 31.91], 'actual': [34.85, 35.85, 35.60, 34.95]},
    'KDH_RoundRobin_Long': {'pred': [34.07, 27.90, 32.10, 32.01], 'actual': [35.85, 29.60, 32.65, 32.65]},
    'KDH_Ensemble_Short': {'pred': [36.65, 34.65, 29.22, 30.93], 'actual': [36.75, 33.90, 33.80, 33.80]},
    'KDH_Ensemble_Medium': {'pred': [35.04, 33.31, 34.80, 33.01], 'actual': [34.85, 35.85, 35.60, 34.95]},
    'KDH_Ensemble_Long': {'pred': [34.99, 35.06, 30.17, 32.01], 'actual': [35.85, 29.60, 32.65, 32.65]},
    'DGC_Hierarchical_Short': {'pred': [98.00, 91.81, 89.33, 90.15], 'actual': [99.30, 93.20, 92.40, 92.40]},
    'DGC_Hierarchical_Medium': {'pred': [97.04, 92.73, 83.28, 93.49], 'actual': [99.50, 93.60, 94.60, 95.00]},
    'DGC_Hierarchical_Long': {'pred': [98.34, 91.99, 93.05, 69.19], 'actual': [96.00, 93.00, 70.20, 70.20]},
    'DGC_RoundRobin_Short': {'pred': [98.94, 92.84, 91.04, 89.33], 'actual': [99.30, 93.20, 92.40, 92.40]},
    'DGC_RoundRobin_Medium': {'pred': [99.99, 97.48, 91.42, 93.76], 'actual': [99.50, 93.60, 94.60, 95.00]},
    'DGC_RoundRobin_Long': {'pred': [98.00, 95.66, 103.07, 109.47], 'actual': [96.00, 93.00, 70.20, 70.20]},
    'DGC_Ensemble_Short': {'pred': [99.63, 95.47, 85.62, 88.55], 'actual': [99.30, 93.20, 92.40, 92.40]},
    'DGC_Ensemble_Medium': {'pred': [94.65, 93.65, 89.57, 87.89], 'actual': [99.50, 93.60, 94.60, 95.00]},
    'DGC_Ensemble_Long': {'pred': [96.53, 94.31, 75.26, 96.04], 'actual': [96.00, 93.00, 70.20, 70.20]},
    'MBB_Hierarchical_Short': {'pred': [27.89, 26.73, 24.53, 26.84], 'actual': [28.25, 27.10, 24.40, 24.40]},
    'MBB_Hierarchical_Medium': {'pred': [28.53, 27.40, 24.20, 25.75], 'actual': [26.85, 23.95, 24.00, 23.90]},
    'MBB_Hierarchical_Long': {'pred': [26.07, 30.05, 27.13, 26.36], 'actual': [23.60, 23.75, 24.70, 24.70]},
    'MBB_RoundRobin_Short': {'pred': [30.20, 28.02, 23.18, 26.52], 'actual': [28.25, 27.10, 24.40, 24.40]},
    'MBB_RoundRobin_Medium': {'pred': [28.28, 31.26, 25.65, 24.45], 'actual': [26.85, 23.95, 24.00, 23.90]},
    'MBB_RoundRobin_Long': {'pred': [28.32, 25.73, 24.79, 23.77], 'actual': [23.60, 23.75, 24.70, 24.70]},
    'MBB_Ensemble_Short': {'pred': [27.90, 27.98, 24.25, 25.36], 'actual': [28.25, 27.10, 24.40, 24.40]},
    'MBB_Ensemble_Medium': {'pred': [29.49, 26.30, 24.99, 24.62], 'actual': [26.85, 23.95, 24.00, 23.90]},
    'MBB_Ensemble_Long': {'pred': [35.09, 21.68, 27.35, 26.54], 'actual': [23.60, 23.75, 24.70, 24.70]}}

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
print("OVERALL ARCHITECTURE AVERAGES ACROSS ALL STOCKS (LLM: Llama-3.1-8B)")
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