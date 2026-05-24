import numpy as np
import pandas as pd
#GPT-LSTM
# Data extracted from the large table
data = {
    # DXG - Hierarchical
    'DXG_Hierarchical_Short': {'pred': [23.01, 22.70, 20.20, 20.67], 'actual': [24, 22.6, 20.9, 20.9]},
    'DXG_Hierarchical_Medium': {'pred': [23.30, 22.96, 20.34, 20.85], 'actual': [24.05, 21.2, 20.15, 20.1]},
    'DXG_Hierarchical_Long': {'pred': [23.78, 23.39, 19.91, 21.32], 'actual': [21.2, 16.3, 17.8, 17.8]},
    
    # DXG - Round Robin
    'DXG_RoundRobin_Short': {'pred': [23.09, 22.75, 20.16, 20.68], 'actual': [24, 22.6, 20.9, 20.9]},
    'DXG_RoundRobin_Medium': {'pred': [23.36, 23.07, 20.33, 20.90], 'actual': [24.05, 21.2, 20.15, 20.1]},
    'DXG_RoundRobin_Long': {'pred': [23.99, 23.87, 20.69, 21.33], 'actual': [21.2, 16.3, 17.8, 17.8]},
    
    # DXG - Ensemble
    'DXG_Ensemble_Short': {'pred': [22.98, 22.65, 20.16, 20.65], 'actual': [24, 22.6, 20.9, 20.9]},
    'DXG_Ensemble_Medium': {'pred': [23.15, 22.84, 20.32, 20.44], 'actual': [24.05, 21.2, 20.15, 20.1]},
    'DXG_Ensemble_Long': {'pred': [23.54, 23.32, 20.63, 21.07], 'actual': [21.2, 16.3, 17.8, 17.8]},
    
    # FPT - Hierarchical
    'FPT_Hierarchical_Short': {'pred': [104.66, 89.40, 92.33, 96.54], 'actual': [105, 88.1, 97.7, 97.7]},
    'FPT_Hierarchical_Medium': {'pred': [101.96, 89.93, 93.26, 97.43], 'actual': [101.9, 102.7, 103.3, 100.9]},
    'FPT_Hierarchical_Long': {'pred': [103.27, 91.24, 94.66, 98.91], 'actual': [103.9, 93.8, 93.9, 93.9]},
    
    # FPT - Round Robin
    'FPT_RoundRobin_Short': {'pred': [101.29, 89.32, 92.67, 96.67], 'actual': [105, 88.1, 97.7, 97.7]},
    'FPT_RoundRobin_Medium': {'pred': [102.08, 89.95, 93.04, 97.51], 'actual': [101.9, 102.7, 103.3, 100.9]},
    'FPT_RoundRobin_Long': {'pred': [103.92, 90.85, 94.19, 96.55], 'actual': [103.9, 93.8, 93.9, 93.9]},
    
    # FPT - Ensemble
    'FPT_Ensemble_Short': {'pred': [101.71, 89.30, 92.49, 96.48], 'actual': [105, 88.1, 97.7, 97.7]},
    'FPT_Ensemble_Medium': {'pred': [101.60, 89.98, 93.10, 97.25], 'actual': [101.9, 102.7, 103.3, 100.9]},
    'FPT_Ensemble_Long': {'pred': [103.01, 91.14, 94.25, 98.46], 'actual': [103.9, 93.8, 93.9, 93.9]},
    
    # VCB - Hierarchical
    'VCB_Hierarchical_Short': {'pred': [69.12, 63.21, 59.59, 59.88], 'actual': [68.6, 61.9, 59.5, 59.5]},
    'VCB_Hierarchical_Medium': {'pred': [68.64, 61.92, 61.77, 60.20], 'actual': [65.8, 60.6, 60.1, 60.8]},
    'VCB_Hierarchical_Long': {'pred': [69.15, 64.33, 55.62, 60.66], 'actual': [60.7, 56.8, 57.5, 57.5]},
    
    # VCB - Round Robin
    'VCB_RoundRobin_Short': {'pred': [68.50, 62.51, 59.45, 59.79], 'actual': [68.6, 61.9, 59.5, 59.5]},
    'VCB_RoundRobin_Medium': {'pred': [68.83, 64.03, 59.68, 60.17], 'actual': [65.8, 60.6, 60.1, 60.8]},
    'VCB_RoundRobin_Long': {'pred': [68.44, 64.57, 60.29, 59.55], 'actual': [60.7, 56.8, 57.5, 57.5]},
    
    # VCB - Ensemble
    'VCB_Ensemble_Short': {'pred': [68.38, 63.12, 59.53, 59.86], 'actual': [68.6, 61.9, 59.5, 59.5]},
    'VCB_Ensemble_Medium': {'pred': [68.67, 63.35, 59.76, 63.78], 'actual': [65.8, 60.6, 60.1, 60.8]},
    'VCB_Ensemble_Long': {'pred': [69.38, 59.44, 60.43, 60.74], 'actual': [60.7, 56.8, 57.5, 57.5]},
    
    # VCS - Hierarchical
    'VCS_Hierarchical_Short': {'pred': [47.25, 45.68, 44.01, 44.03], 'actual': [48.8, 46.8, 46.2, 46.2]},
    'VCS_Hierarchical_Medium': {'pred': [47.65, 46.05, 44.43, 44.46], 'actual': [50, 47.4, 47.1, 46.9]},
    'VCS_Hierarchical_Long': {'pred': [48.33, 46.90, 44.98, 45.21], 'actual': [47.6, 46.5, 43, 43]},
    
    # VCS - Round Robin
    'VCS_RoundRobin_Short': {'pred': [47.18, 45.69, 43.98, 43.98], 'actual': [48.8, 46.8, 46.2, 46.2]},
    'VCS_RoundRobin_Medium': {'pred': [47.42, 46.10, 47.22, 44.28], 'actual': [50, 47.4, 47.1, 46.9]},
    'VCS_RoundRobin_Long': {'pred': [48.32, 46.56, 44.71, 44.78], 'actual': [47.6, 46.5, 43, 43]},
    
    # VCS - Ensemble
    'VCS_Ensemble_Short': {'pred': [47.19, 45.63, 43.97, 45.95], 'actual': [48.8, 46.8, 46.2, 46.2]},
    'VCS_Ensemble_Medium': {'pred': [47.47, 46.03, 44.25, 47.55], 'actual': [50, 47.4, 47.1, 46.9]},
    'VCS_Ensemble_Long': {'pred': [48.18, 46.79, 45.02, 44.89], 'actual': [47.6, 46.5, 43, 43]}
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