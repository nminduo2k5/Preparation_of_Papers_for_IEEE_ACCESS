import numpy as np
import pandas as pd
import os
import re

# Model Mappings and Labels
MODEL_INFO = {
    'GPT-4o': {
        'filepath': r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\update_table1.py',
        'label': 'GPT-4o'
    },
    'Llama 3.1:8b': {
        'filepath': r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\update_table2.py',
        'label': 'Llama 3.1:8b'
    },
    'Gemini 2.0': {
        'filepath': r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\update_table3.py',
        'label': 'Gemini 2.0'
    }
}

def load_data_from_file(filepath):
    """Dynamically load the data dictionary from an update_tableX.py file without side effects."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Mock process_file to avoid rewriting TeX files during import
    globals_dict = {
        'process_file': lambda *args, **kwargs: None,
        '__name__': 'mock'
    }
    exec(content, globals_dict)
    return globals_dict['data']

def calculate_metrics(predicted, actual):
    """Calculate MAE, RMSE, and MAPE"""
    predicted = np.array(predicted)
    actual = np.array(actual)
    
    mae = np.mean(np.abs(predicted - actual))
    rmse = np.sqrt(np.mean((predicted - actual) ** 2))
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    
    return mae, rmse, mape

def main():
    # 1. Load Data
    all_data = {}
    for model_name, info in MODEL_INFO.items():
        try:
            all_data[model_name] = load_data_from_file(info['filepath'])
            print(f"Loaded {len(all_data[model_name])} keys for {model_name}.")
        except Exception as e:
            print(f"Error loading {model_name}: {e}")
            return

    # 2. Calculate Metrics for All Combinations
    records = []
    for model_name, data_dict in all_data.items():
        for key, values in data_dict.items():
            stock, arch, horizon = key.split('_')
            mae, rmse, mape = calculate_metrics(values['pred'], values['actual'])
            records.append({
                'Model': model_name,
                'Stock': stock,
                'Architecture': arch,
                'Horizon': horizon,
                'MAE': mae,
                'RMSE': rmse,
                'MAPE': mape
            })
            
    df = pd.DataFrame(records)
    
    # 3. Print General Verification Results
    print("=" * 80)
    print("DYNAMIC PERFORMANCE METRICS CALCULATION COMPLETE")
    print("=" * 80)
    print(f"Total calculated combinations: {len(df)}")
    
    stocks = sorted(df['Stock'].unique())
    architectures = ['Hierarchical', 'RoundRobin', 'Ensemble']
    horizons = ['Short', 'Medium', 'Long']
    models = ['Llama 3.1:8b', 'GPT-4o', 'Gemini 2.0'] # Ordering for tables
    
    # 4. Generate Table 1: RQ1 - Architecture Performance across Horizons
    print("\n" + "=" * 80)
    print("RESEARCH QUESTION 1 (RQ1) ANALYSIS")
    print("=" * 80)
    print("Average MAPE (%) of Coordination Architectures across all Stocks and LLMs:")
    print("-" * 65)
    print(f"{'Horizon':<12} | {'Hierarchical':<14} | {'Round Robin':<14} | {'Ensemble Voting':<15}")
    print("-" * 65)
    for horizon in horizons:
        row_str = f"{horizon:<12}"
        for arch in architectures:
            mean_mape = df[(df['Horizon'] == horizon) & (df['Architecture'] == arch)]['MAPE'].mean()
            row_str += f" | {mean_mape:12.2f}%"
        print(row_str)
    print("-" * 65)
    
    # 5. Generate Table 2: RQ2 - LLM Performance across Horizons
    print("\n" + "=" * 80)
    print("RESEARCH QUESTION 2 (RQ2) ANALYSIS")
    print("=" * 80)
    print("Average MAPE (%) of underlying LLMs across all Stocks and Architectures:")
    print("-" * 55)
    print(f"{'Horizon':<12} | {'Llama 3.1:8b':<14} | {'GPT-4o':<12} | {'Gemini 2.0':<12}")
    print("-" * 55)
    for horizon in horizons:
        row_str = f"{horizon:<12}"
        for model in models:
            mean_mape = df[(df['Horizon'] == horizon) & (df['Model'] == model)]['MAPE'].mean()
            row_str += f" | {mean_mape:10.2f}%"
        print(row_str)
    print("-" * 55)

    # 6. Generate LaTeX code for llm_comparison.tex style (one table per horizon)
    print("\n" + "=" * 80)
    print("LATEX HORIZON-SPECIFIC COMPARISON TABLES (llm_comparison.tex style)")
    print("=" * 80)
    
    for horizon in horizons:
        print(f"\n% {horizon.upper()}-TERM COMPARISON TABLE")
        print(r"\begin{table}[h!]")
        print(r"\centering")
        print(f"\\caption{{{horizon.capitalize()}-term Performance Comparison Across LLMs (Best values in bold)}}")
        print(r"\resizebox{\textwidth}{!}{")
        print(r"\begin{tabular}{c|c|ccc|ccc|ccc}")
        print(r"\toprule")
        print(r"\multirow{2}{*}{\textbf{Stock}} & \multirow{2}{*}{\textbf{Architecture}} & ")
        print(r"\multicolumn{3}{c|}{\textbf{Llama 3.1:8b}} & ")
        print(r"\multicolumn{3}{c|}{\textbf{GPT-4o}} & ")
        print(r"\multicolumn{3}{c}{\textbf{Google Gemini 2.0}} \\")
        print(r"\cmidrule(lr){3-5} \cmidrule(lr){6-8} \cmidrule(lr){9-11}")
        print(r"& & MAE & RMSE & MAPE & MAE & RMSE & MAPE & MAE & RMSE & MAPE \\")
        print(r"\midrule")
        
        for stock in stocks:
            print("\n\\multirow{3}{*}{\\textbf{" + stock + "}}")
            for arch in architectures:
                # Retrieve metrics for each model
                metrics_by_model = {}
                for model in models:
                    sub = df[(df['Model'] == model) & (df['Stock'] == stock) & 
                             (df['Architecture'] == arch) & (df['Horizon'] == horizon)]
                    if not sub.empty:
                        metrics_by_model[model] = (sub.iloc[0]['MAE'], sub.iloc[0]['RMSE'], sub.iloc[0]['MAPE'])
                    else:
                        metrics_by_model[model] = (0.0, 0.0, 0.0)
                
                # Determine min metrics for bolding
                min_mae = min(metrics_by_model[m][0] for m in models)
                min_rmse = min(metrics_by_model[m][1] for m in models)
                min_mape = min(metrics_by_model[m][2] for m in models)
                
                # Build TeX format strings
                tex_parts = []
                for model in models:
                    mae, rmse, mape = metrics_by_model[model]
                    
                    mae_str = f"\\textbf{{{mae:.2f}}}" if mae == min_mae else f"{mae:.2f}"
                    rmse_str = f"\\textbf{{{rmse:.2f}}}" if rmse == min_rmse else f"{rmse:.2f}"
                    mape_str = f"\\textbf{{{mape:.1f}\\%}}" if mape == min_mape else f"{mape:.1f}\\%"
                    
                    tex_parts.append(f"{mae_str} & {rmse_str} & {mape_str}")
                
                arch_label = "Hierarchical" if arch == "Hierarchical" else ("Round Robin" if arch == "RoundRobin" else "Ensemble")
                print(f"& {arch_label} & " + " & ".join(tex_parts) + " \\\\")
            print(r"\midrule")
            
        print(r"\bottomrule")
        print(r"\end{tabular}")
        print(r"}")
        print(r"\end{table}")

    # 7. Generate a Compact Performance Comparison Table (compact_performance_table.tex style)
    print("\n" + "=" * 80)
    print("LATEX COMPACT ALL-IN-ONE PERFORMANCE TABLE (compact_performance_table.tex style)")
    print("=" * 80)
    print(r"\begin{table*}[!h]")
    print(r"\centering")
    print(r"\caption{Performance Comparison Across Forecasting Horizons and LLMs}")
    print(r"\label{tab:full_performance_all}")
    print(r"\setlength{\tabcolsep}{1.5pt}")
    print(r"\renewcommand{\arraystretch}{0.9}")
    print(r"\tiny")
    print(r"\resizebox{0.95\textwidth}{!}{")
    print(r"\begin{tabular}{c|c|c|ccc|ccc|ccc}")
    print(r"\toprule")
    print(r"\multirow{2}{*}{\textbf{Horizon}} &")
    print(r"\multirow{2}{*}{\textbf{Stock}} &")
    print(r"\multirow{2}{*}{\textbf{Arch}} &")
    print(r"\multicolumn{3}{c|}{\textbf{Llama 3.1:8b}} &")
    print(r"\multicolumn{3}{c|}{\textbf{GPT-4o}} &")
    print(r"\multicolumn{3}{c}{\textbf{Gemini 2.0}} \\")
    print(r"\cmidrule(lr){4-6} \cmidrule(lr){7-9} \cmidrule(lr){10-12}")
    print(r"& & & MAE & RMSE & MAPE & MAE & RMSE & MAPE & MAE & RMSE & MAPE \\")
    print(r"\midrule")
    
    for h_idx, horizon in enumerate(horizons):
        print(f"\n% {horizon.upper()}")
        print("\\multirow{36}{*}{\\rotatebox{90}{\\textbf{" + horizon + "}}}")
        
        for stock in stocks:
            print("& \\multirow{3}{*}{" + stock + "}")
            for arch in architectures:
                metrics_by_model = {}
                for model in models:
                    sub = df[(df['Model'] == model) & (df['Stock'] == stock) & 
                             (df['Architecture'] == arch) & (df['Horizon'] == horizon)]
                    if not sub.empty:
                        metrics_by_model[model] = (sub.iloc[0]['MAE'], sub.iloc[0]['RMSE'], sub.iloc[0]['MAPE'])
                    else:
                        metrics_by_model[model] = (0.0, 0.0, 0.0)
                
                min_mae = min(metrics_by_model[m][0] for m in models)
                min_rmse = min(metrics_by_model[m][1] for m in models)
                min_mape = min(metrics_by_model[m][2] for m in models)
                
                tex_parts = []
                for model in models:
                    mae, rmse, mape = metrics_by_model[model]
                    mae_str = f"\\textbf{{{mae:.2f}}}" if mae == min_mae else f"{mae:.2f}"
                    rmse_str = f"\\textbf{{{rmse:.2f}}}" if rmse == min_rmse else f"{rmse:.2f}"
                    # Compact version usually uses decimals without %
                    mape_str = f"\\textbf{{{mape:.1f}}}" if mape == min_mape else f"{mape:.1f}"
                    
                    tex_parts.append(f"{mae_str} & {rmse_str} & {mape_str}")
                
                arch_letter = "H" if arch == "Hierarchical" else ("R" if arch == "RoundRobin" else "E")
                print(f"& & {arch_letter} & " + " & ".join(tex_parts) + " \\\\")
            print(r"")
        print(r"\midrule")
        
    print(r"\bottomrule")
    print(r"\end{tabular}")
    print(r"}")
    print(r"\end{table*}")

    print("\n" + "=" * 80)
    print("METRICS COMPUTATION AND LATEX GENERATION SUCCESSFUL")
    print("=" * 80)

if __name__ == '__main__':
    main()