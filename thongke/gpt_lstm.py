import numpy as np
import pandas as pd
#GPT-LSTM
# Data extracted from the large table
data = {
    'CMG_Ensemble_Long': {'pred': [40.23, 34.58, 37.93, 36.07], 'actual': [41.9, 35.1, 35.2, 35.2]},
    'CMG_Ensemble_Medium': {'pred': [39.31, 41.27, 39.67, 39.52], 'actual': [40.8, 41.3, 39.6, 39.3]},
    'CMG_Ensemble_Short': {'pred': [40.23, 39.99, 38.53, 38.0], 'actual': [41.85, 37.3, 38.75, 38.75]},
    'CMG_Hierarchical_Long': {'pred': [34.09, 34.0, 32.58, 32.59], 'actual': [41.9, 35.1, 35.2, 35.2]},
    'CMG_Hierarchical_Medium': {'pred': [35.52, 32.84, 31.65, 34.01], 'actual': [40.8, 41.3, 39.6, 39.3]},
    'CMG_Hierarchical_Short': {'pred': [34.06, 32.06, 33.23, 33.23], 'actual': [41.85, 37.3, 38.75, 38.75]},
    'CMG_RoundRobin_Long': {'pred': [39.43, 30.15, 29.13, 29.32], 'actual': [41.9, 35.1, 35.2, 35.2]},
    'CMG_RoundRobin_Medium': {'pred': [39.46, 38.89, 31.54, 38.18], 'actual': [40.8, 41.3, 39.6, 39.3]},
    'CMG_RoundRobin_Short': {'pred': [39.51, 39.55, 38.04, 30.06], 'actual': [41.85, 37.3, 38.75, 38.75]},
    'DGC_Ensemble_Long': {'pred': [95.81, 92.59, 74.65, 77.61], 'actual': [96.0, 93.0, 70.2, 70.2]},
    'DGC_Ensemble_Medium': {'pred': [96.05, 98.86, 94.94, 98.27], 'actual': [99.5, 93.6, 94.6, 95.0]},
    'DGC_Ensemble_Short': {'pred': [99.82, 92.82, 95.26, 97.89], 'actual': [99.3, 93.2, 92.4, 92.4]},
    'DGC_Hierarchical_Long': {'pred': [96.9, 94.05, 78.04, 70.04], 'actual': [96.0, 93.0, 70.2, 70.2]},
    'DGC_Hierarchical_Medium': {'pred': [97.04, 93.22, 87.01, 87.5], 'actual': [99.5, 93.6, 94.6, 95.0]},
    'DGC_Hierarchical_Short': {'pred': [96.52, 93.01, 86.68, 88.0], 'actual': [99.3, 93.2, 92.4, 92.4]},
    'DGC_RoundRobin_Long': {'pred': [96.73, 94.16, 78.47, 72.2], 'actual': [96.0, 93.0, 70.2, 70.2]},
    'DGC_RoundRobin_Medium': {'pred': [86.87, 84.17, 96.27, 93.3], 'actual': [99.5, 93.6, 94.6, 95.0]},
    'DGC_RoundRobin_Short': {'pred': [86.46, 94.18, 88.88, 94.7], 'actual': [99.3, 93.2, 92.4, 92.4]},
    'DXG_Ensemble_Long': {'pred': [23.54, 23.32, 20.63, 21.07], 'actual': [21.2, 16.3, 17.8, 17.8]},
    'DXG_Ensemble_Medium': {'pred': [23.15, 22.84, 20.32, 20.44], 'actual': [24.05, 21.2, 20.15, 20.1]},
    'DXG_Ensemble_Short': {'pred': [22.98, 22.65, 20.16, 20.65], 'actual': [24.0, 22.6, 20.9, 20.9]},
    'DXG_Hierarchical_Long': {'pred': [23.78, 23.39, 19.91, 21.32], 'actual': [21.2, 16.3, 17.8, 17.8]},
    'DXG_Hierarchical_Medium': {'pred': [23.3, 22.96, 20.34, 20.85], 'actual': [24.05, 21.2, 20.15, 20.1]},
    'DXG_Hierarchical_Short': {'pred': [23.01, 22.7, 20.2, 20.67], 'actual': [24.0, 22.6, 20.9, 20.9]},
    'DXG_RoundRobin_Long': {'pred': [23.99, 23.87, 20.69, 21.33], 'actual': [21.2, 16.3, 17.8, 17.8]},
    'DXG_RoundRobin_Medium': {'pred': [23.36, 23.07, 20.33, 20.9], 'actual': [24.05, 21.2, 20.15, 20.1]},
    'DXG_RoundRobin_Short': {'pred': [23.09, 22.75, 20.16, 20.68], 'actual': [24.0, 22.6, 20.9, 20.9]},
    'FPT_Ensemble_Long': {'pred': [103.01, 91.14, 94.25, 98.46], 'actual': [103.9, 93.8, 93.9, 93.9]},
    'FPT_Ensemble_Medium': {'pred': [101.6, 89.98, 93.1, 97.25], 'actual': [101.9, 102.7, 103.3, 100.9]},
    'FPT_Ensemble_Short': {'pred': [101.71, 89.3, 92.49, 96.48], 'actual': [105.0, 88.1, 97.7, 97.7]},
    'FPT_Hierarchical_Long': {'pred': [103.27, 91.24, 94.66, 98.91], 'actual': [103.9, 93.8, 93.9, 93.9]},
    'FPT_Hierarchical_Medium': {'pred': [101.96, 89.93, 93.26, 97.43], 'actual': [101.9, 102.7, 103.3, 100.9]},
    'FPT_Hierarchical_Short': {'pred': [104.66, 89.4, 92.33, 96.54], 'actual': [105.0, 88.1, 97.7, 97.7]},
    'FPT_RoundRobin_Long': {'pred': [103.92, 90.85, 94.19, 96.55], 'actual': [103.9, 93.8, 93.9, 93.9]},
    'FPT_RoundRobin_Medium': {'pred': [102.08, 89.95, 93.04, 97.51], 'actual': [101.9, 102.7, 103.3, 100.9]},
    'FPT_RoundRobin_Short': {'pred': [101.29, 89.32, 92.67, 96.67], 'actual': [105.0, 88.1, 97.7, 97.7]},
    'HPG_Ensemble_Long': {'pred': [25.07, 25.8, 26.26, 26.55], 'actual': [26.7, 26.25, 26.7, 26.7]},
    'HPG_Ensemble_Medium': {'pred': [30.12, 25.67, 26.87, 26.22], 'actual': [30.35, 26.9, 26.75, 26.3]},
    'HPG_Ensemble_Short': {'pred': [25.0, 25.73, 26.98, 26.77], 'actual': [29.85, 28.0, 26.4, 26.4]},
    'HPG_Hierarchical_Long': {'pred': [26.25, 28.83, 26.58, 23.82], 'actual': [26.7, 26.25, 26.7, 26.7]},
    'HPG_Hierarchical_Medium': {'pred': [28.93, 23.15, 29.95, 24.18], 'actual': [30.35, 26.9, 26.75, 26.3]},
    'HPG_Hierarchical_Short': {'pred': [24.28, 28.21, 26.18, 26.83], 'actual': [29.85, 28.0, 26.4, 26.4]},
    'HPG_RoundRobin_Long': {'pred': [27.82, 29.22, 27.12, 27.55], 'actual': [26.7, 26.25, 26.7, 26.7]},
    'HPG_RoundRobin_Medium': {'pred': [29.37, 29.15, 27.66, 27.01], 'actual': [30.35, 26.9, 26.75, 26.3]},
    'HPG_RoundRobin_Short': {'pred': [27.89, 29.15, 27.12, 27.55], 'actual': [29.85, 28.0, 26.4, 26.4]},
    'KDH_Ensemble_Long': {'pred': [34.11, 39.42, 31.64, 32.54], 'actual': [35.85, 29.6, 32.65, 32.65]},
    'KDH_Ensemble_Medium': {'pred': [35.13, 32.61, 34.48, 32.54], 'actual': [34.85, 35.85, 35.6, 34.95]},
    'KDH_Ensemble_Short': {'pred': [31.55, 32.74, 31.23, 31.26], 'actual': [36.75, 33.9, 33.8, 33.8]},
    'KDH_Hierarchical_Long': {'pred': [38.72, 27.66, 31.42, 35.65], 'actual': [35.85, 29.6, 32.65, 32.65]},
    'KDH_Hierarchical_Medium': {'pred': [31.78, 36.82, 34.42, 35.15], 'actual': [34.85, 35.85, 35.6, 34.95]},
    'KDH_Hierarchical_Short': {'pred': [31.13, 34.21, 32.12, 32.15], 'actual': [36.75, 33.9, 33.8, 33.8]},
    'KDH_RoundRobin_Long': {'pred': [35.21, 29.52, 29.56, 30.54], 'actual': [35.85, 29.6, 32.65, 32.65]},
    'KDH_RoundRobin_Medium': {'pred': [34.88, 34.61, 32.14, 33.45], 'actual': [34.85, 35.85, 35.6, 34.95]},
    'KDH_RoundRobin_Short': {'pred': [32.25, 34.89, 33.45, 33.24], 'actual': [36.75, 33.9, 33.8, 33.8]},
    'MBB_Ensemble_Long': {'pred': [21.52, 25.43, 23.42, 25.31], 'actual': [23.6, 23.75, 24.7, 24.7]},
    'MBB_Ensemble_Medium': {'pred': [27.42, 23.81, 24.93, 25.72], 'actual': [26.85, 23.95, 24.0, 23.9]},
    'MBB_Ensemble_Short': {'pred': [27.93, 24.92, 26.93, 26.37], 'actual': [28.25, 27.1, 24.4, 24.4]},
    'MBB_Hierarchical_Long': {'pred': [20.91, 27.05, 26.13, 25.03], 'actual': [23.6, 23.75, 24.7, 24.7]},
    'MBB_Hierarchical_Medium': {'pred': [27.61, 24.34, 23.21, 22.72], 'actual': [26.85, 23.95, 24.0, 23.9]},
    'MBB_Hierarchical_Short': {'pred': [28.05, 25.23, 25.63, 23.29], 'actual': [28.25, 27.1, 24.4, 24.4]},
    'MBB_RoundRobin_Long': {'pred': [27.53, 22.05, 23.53, 25.58], 'actual': [23.6, 23.75, 24.7, 24.7]},
    'MBB_RoundRobin_Medium': {'pred': [27.51, 23.01, 24.66, 23.68], 'actual': [26.85, 23.95, 24.0, 23.9]},
    'MBB_RoundRobin_Short': {'pred': [24.24, 25.31, 23.93, 26.33], 'actual': [28.25, 27.1, 24.4, 24.4]},
    'MWG_Ensemble_Long': {'pred': [81.77, 77.67, 82.6, 79.5], 'actual': [82.6, 77.7, 82.9, 82.9]},
    'MWG_Ensemble_Medium': {'pred': [71.8, 87.86, 75.55, 78.36], 'actual': [79.5, 83.9, 81.8, 80.2]},
    'MWG_Ensemble_Short': {'pred': [71.76, 87.77, 86.12, 81.0], 'actual': [77.5, 84.5, 85.7, 85.7]},
    'MWG_Hierarchical_Long': {'pred': [85.03, 74.98, 75.71, 77.75], 'actual': [82.6, 77.7, 82.9, 82.9]},
    'MWG_Hierarchical_Medium': {'pred': [70.65, 79.88, 76.07, 77.66], 'actual': [79.5, 83.9, 81.8, 80.2]},
    'MWG_Hierarchical_Short': {'pred': [66.76, 75.55, 74.96, 77.54], 'actual': [77.5, 84.5, 85.7, 85.7]},
    'MWG_RoundRobin_Long': {'pred': [73.69, 68.65, 76.64, 78.76], 'actual': [82.6, 77.7, 82.9, 82.9]},
    'MWG_RoundRobin_Medium': {'pred': [65.82, 78.47, 76.93, 78.12], 'actual': [79.5, 83.9, 81.8, 80.2]},
    'MWG_RoundRobin_Short': {'pred': [64.18, 78.11, 76.62, 79.21], 'actual': [77.5, 84.5, 85.7, 85.7]},
    'TCB_Ensemble_Long': {'pred': [34.87, 32.72, 33.24, 33.25], 'actual': [35.1, 32.0, 33.6, 33.6]},
    'TCB_Ensemble_Medium': {'pred': [33.8, 35.62, 32.74, 30.57], 'actual': [39.0, 35.7, 35.0, 34.1]},
    'TCB_Ensemble_Short': {'pred': [37.5, 39.97, 36.54, 36.27], 'actual': [39.6, 40.65, 36.1, 36.1]},
    'TCB_Hierarchical_Long': {'pred': [39.61, 33.0, 31.19, 32.02], 'actual': [35.1, 32.0, 33.6, 33.6]},
    'TCB_Hierarchical_Medium': {'pred': [38.81, 39.06, 36.03, 36.51], 'actual': [39.0, 35.7, 35.0, 34.1]},
    'TCB_Hierarchical_Short': {'pred': [38.63, 40.77, 37.3, 37.67], 'actual': [39.6, 40.65, 36.1, 36.1]},
    'TCB_RoundRobin_Long': {'pred': [30.86, 33.0, 30.12, 30.4], 'actual': [35.1, 32.0, 33.6, 33.6]},
    'TCB_RoundRobin_Medium': {'pred': [34.36, 36.06, 32.25, 32.97], 'actual': [39.0, 35.7, 35.0, 34.1]},
    'TCB_RoundRobin_Short': {'pred': [37.63, 40.08, 36.42, 36.86], 'actual': [39.6, 40.65, 36.1, 36.1]},
    'VCB_Ensemble_Long': {'pred': [69.38, 59.44, 60.43, 60.74], 'actual': [60.7, 56.8, 57.5, 57.5]},
    'VCB_Ensemble_Medium': {'pred': [68.67, 63.35, 59.76, 63.78], 'actual': [65.8, 60.6, 60.1, 60.8]},
    'VCB_Ensemble_Short': {'pred': [68.38, 63.12, 59.53, 59.86], 'actual': [68.6, 61.9, 59.5, 59.5]},
    'VCB_Hierarchical_Long': {'pred': [69.15, 64.33, 55.62, 60.66], 'actual': [60.7, 56.8, 57.5, 57.5]},
    'VCB_Hierarchical_Medium': {'pred': [68.64, 61.92, 61.77, 60.2], 'actual': [65.8, 60.6, 60.1, 60.8]},
    'VCB_Hierarchical_Short': {'pred': [69.12, 63.21, 59.59, 59.88], 'actual': [68.6, 61.9, 59.5, 59.5]},
    'VCB_RoundRobin_Long': {'pred': [68.44, 64.57, 60.29, 59.55], 'actual': [60.7, 56.8, 57.5, 57.5]},
    'VCB_RoundRobin_Medium': {'pred': [68.83, 64.03, 59.68, 60.17], 'actual': [65.8, 60.6, 60.1, 60.8]},
    'VCB_RoundRobin_Short': {'pred': [68.5, 62.51, 59.45, 59.79], 'actual': [68.6, 61.9, 59.5, 59.5]},
    'VCS_Ensemble_Long': {'pred': [48.18, 46.79, 45.02, 44.89], 'actual': [47.6, 46.5, 43.0, 43.0]},
    'VCS_Ensemble_Medium': {'pred': [47.47, 46.03, 44.25, 47.55], 'actual': [50.0, 47.4, 47.1, 46.9]},
    'VCS_Ensemble_Short': {'pred': [47.19, 45.63, 43.97, 45.95], 'actual': [48.8, 46.8, 46.2, 46.2]},
    'VCS_Hierarchical_Long': {'pred': [48.33, 46.9, 44.98, 45.21], 'actual': [47.6, 46.5, 43.0, 43.0]},
    'VCS_Hierarchical_Medium': {'pred': [47.65, 46.05, 44.43, 44.46], 'actual': [50.0, 47.4, 47.1, 46.9]},
    'VCS_Hierarchical_Short': {'pred': [47.25, 45.68, 44.01, 44.03], 'actual': [48.8, 46.8, 46.2, 46.2]},
    'VCS_RoundRobin_Long': {'pred': [48.32, 46.56, 44.71, 44.78], 'actual': [47.6, 46.5, 43.0, 43.0]},
    'VCS_RoundRobin_Medium': {'pred': [47.42, 46.1, 47.22, 44.28], 'actual': [50.0, 47.4, 47.1, 46.9]},
    'VCS_RoundRobin_Short': {'pred': [47.18, 45.69, 43.98, 43.98], 'actual': [48.8, 46.8, 46.2, 46.2]},
    'VHM_Ensemble_Long': {'pred': [93.6, 97.6, 98.72, 100.4], 'actual': [99.2, 93.9, 101.5, 101.5]},
    'VHM_Ensemble_Medium': {'pred': [105.98, 104.92, 103.54, 91.78], 'actual': [104.5, 104.0, 100.2, 99.6]},
    'VHM_Ensemble_Short': {'pred': [100.22, 116.89, 116.18, 114.07], 'actual': [102.3, 116.0, 114.5, 114.5]},
    'VHM_Hierarchical_Long': {'pred': [111.13, 100.87, 105.0, 101.9], 'actual': [99.2, 93.9, 101.5, 101.5]},
    'VHM_Hierarchical_Medium': {'pred': [106.01, 104.02, 104.04, 105.02], 'actual': [104.5, 104.0, 100.2, 99.6]},
    'VHM_Hierarchical_Short': {'pred': [104.82, 122.43, 111.57, 113.43], 'actual': [102.3, 116.0, 114.5, 114.5]},
    'VHM_RoundRobin_Long': {'pred': [107.83, 101.56, 105.05, 107.41], 'actual': [99.2, 93.9, 101.5, 101.5]},
    'VHM_RoundRobin_Medium': {'pred': [107.47, 105.47, 101.05, 106.21], 'actual': [104.5, 104.0, 100.2, 99.6]},
    'VHM_RoundRobin_Short': {'pred': [105.13, 122.73, 114.27, 113.68], 'actual': [102.3, 116.0, 114.5, 114.5]}
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
print("OVERALL ARCHITECTURE AVERAGES ACROSS ALL STOCKS (LLM: GPT-4o)")
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