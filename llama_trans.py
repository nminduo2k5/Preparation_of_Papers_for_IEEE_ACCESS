import numpy as np
import pandas as pd
#LLAMA TRANSFORMER CODE
# Data extracted from the large table
data = {
    # DXG - Hierarchical
    'DXG_Hierarchical_Short': {'pred': [22.92, 22.58, 20.12, 20.61], 'actual': [24, 22.6, 20.9, 20.9]},
    'DXG_Hierarchical_Medium': {'pred': [23.13, 22.80, 20.31, 20.79], 'actual': [24.05, 21.2, 20.15, 20.1]},
    'DXG_Hierarchical_Long': {'pred': [23.73, 23.43, 20.88, 21.33], 'actual': [21.2, 16.3, 17.8, 17.8]},
    
    # DXG - Round Robin
    'DXG_RoundRobin_Short': {'pred': [23.07, 22.75, 20.17, 20.68], 'actual': [24, 22.6, 20.9, 20.9]},
    'DXG_RoundRobin_Medium': {'pred': [23.44, 23.08, 20.38, 20.88], 'actual': [24.05, 21.2, 20.15, 20.1]},
    'DXG_RoundRobin_Long': {'pred': [24.10, 23.83, 20.82, 21.42], 'actual': [21.2, 16.3, 17.8, 17.8]},
    
    # DXG - Ensemble
    'DXG_Ensemble_Short': {'pred': [22.91, 22.57, 20.12, 20.60], 'actual': [24, 22.6, 20.9, 20.9]},
    'DXG_Ensemble_Medium': {'pred': [23.10, 22.75, 20.27, 20.75], 'actual': [24.05, 21.2, 20.15, 20.1]},
    'DXG_Ensemble_Long': {'pred': [23.59, 23.23, 20.74, 21.12], 'actual': [21.2, 16.3, 17.8, 17.8]},
    
    # FPT - Hierarchical
    'FPT_Hierarchical_Short': {'pred': [101.20, 89.35, 92.62, 96.53], 'actual': [105, 88.1, 97.7, 97.7]},
    'FPT_Hierarchical_Medium': {'pred': [101.91, 90.08, 93.14, 97.05], 'actual': [101.9, 102.7, 103.3, 100.9]},
    'FPT_Hierarchical_Long': {'pred': [101.75, 98.55, 94.50, 98.87], 'actual': [103.9, 93.8, 93.9, 93.9]},
    
    # FPT - Round Robin
    'FPT_RoundRobin_Short': {'pred': [101.21, 89.39, 92.64, 96.67], 'actual': [105, 88.1, 97.7, 97.7]},
    'FPT_RoundRobin_Medium': {'pred': [102.09, 90.03, 93.12, 97.38], 'actual': [101.9, 102.7, 103.3, 100.9]},
    'FPT_RoundRobin_Long': {'pred': [104.11, 91.13, 94.41, 105.33], 'actual': [103.9, 93.8, 93.9, 93.9]},
    
    # FPT - Ensemble
    'FPT_Ensemble_Short': {'pred': [101.04, 89.31, 92.50, 96.46], 'actual': [105, 88.1, 97.7, 97.7]},
    'FPT_Ensemble_Medium': {'pred': [103.6, 89.86, 93.03, 97.11], 'actual': [101.9, 102.7, 103.3, 100.9]},
    'FPT_Ensemble_Long': {'pred': [103.23, 90.94, 94.04, 98.49], 'actual': [103.9, 93.8, 93.9, 93.9]},
    
    # VCB - Hierarchical
    'VCB_Hierarchical_Short': {'pred': [68.32, 63.09, 63.42, 59.82], 'actual': [68.6, 61.9, 59.5, 59.5]},
    'VCB_Hierarchical_Medium': {'pred': [68.75, 61.59, 59.95, 60.24], 'actual': [65.8, 60.6, 60.1, 60.8]},
    'VCB_Hierarchical_Long': {'pred': [70.15, 64.82, 61.30, 61.58], 'actual': [60.7, 56.8, 57.5, 57.5]},
    
    # VCB - Round Robin
    'VCB_RoundRobin_Short': {'pred': [68.43, 63.21, 59.61, 59.94], 'actual': [68.6, 61.9, 59.5, 59.5]},
    'VCB_RoundRobin_Medium': {'pred': [68.95, 63.73, 60.09, 60.40], 'actual': [65.8, 60.6, 60.1, 60.8]},
    'VCB_RoundRobin_Long': {'pred': [70.37, 65.19, 61.47, 61.87], 'actual': [60.7, 56.8, 57.5, 57.5]},
    
    # VCB - Ensemble
    'VCB_Ensemble_Short': {'pred': [47.22, 45.75, 59.50, 59.80], 'actual': [68.6, 61.9, 59.5, 59.5]},
    'VCB_Ensemble_Medium': {'pred': [68.64, 63.36, 59.81, 60.18], 'actual': [65.8, 60.6, 60.1, 60.8]},
    'VCB_Ensemble_Long': {'pred': [69.80, 64.47, 60.91, 61.11], 'actual': [60.7, 56.8, 57.5, 57.5]},
    
    # VCS - Hierarchical
    'VCS_Hierarchical_Short': {'pred': [47.22, 45.75, 44.04, 44.06], 'actual': [48.8, 46.8, 46.2, 46.2]},
    'VCS_Hierarchical_Medium': {'pred': [47.65, 46.09, 44.34, 44.39], 'actual': [50, 47.4, 47.1, 46.9]},
    'VCS_Hierarchical_Long': {'pred': [48.52, 46.79, 45.06, 45.02], 'actual': [47.6, 46.5, 43, 43]},
    
    # VCS - Round Robin
    'VCS_RoundRobin_Short': {'pred': [47.19, 45.64, 44.01, 43.98], 'actual': [48.8, 46.8, 46.2, 46.2]},
    'VCS_RoundRobin_Medium': {'pred': [47.56, 46.03, 44.62, 44.32], 'actual': [50, 47.4, 47.1, 46.9]},
    'VCS_RoundRobin_Long': {'pred': [48.00, 46.69, 44.81, 44.74], 'actual': [47.6, 46.5, 43, 43]},
    
    # VCS - Ensemble
    'VCS_Ensemble_Short': {'pred': [45.35, 45.63, 43.97, 43.99], 'actual': [48.8, 46.8, 46.2, 46.2]},
    'VCS_Ensemble_Medium': {'pred': [47.48, 46.04, 44.33, 44.34], 'actual': [50, 47.4, 47.1, 46.9]},
    'VCS_Ensemble_Long': {'pred': [48.26, 46.65, 44.98, 44.96], 'actual': [47.6, 46.5, 43, 43]}
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
stocks = ['DXG', 'FPT', 'VCB', 'VCS']
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
print("CALCULATION COMPLETE!")
print("="*80)