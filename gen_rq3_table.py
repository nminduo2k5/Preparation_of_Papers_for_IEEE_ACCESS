import csv

csv_path = r"k:\1\Preparation_of_Papers_for_IEEE_ACCESS\metrics_summary.csv"

# Structure: data[model][arch][horizon] = {'MAE': x, 'MAPE (%)': y, 'RMSE': z}
data = {}
horizons = ['Short-term', 'Medium-term', 'Long-term']
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        model = row['Model']
        arch = row['Architecture']
        horizon = row['Horizon']
        
        if model not in data:
            data[model] = {}
        if arch not in data[model]:
            data[model][arch] = {}
            
        data[model][arch][horizon] = {
            'MAE': row['MAE'],
            'MAPE': row['MAPE (%)'],
            'RMSE': row['RMSE']
        }

latex_table = r'''
\begin{table*}[t]
\centering
\caption{\textbf{Comprehensive Comparison of Single-Agent Baselines vs. Multi-Agent Architectures (RQ3).} Values represent the average error across all evaluated stocks.}
\label{tab:rq3_baselines_vs_mas}
\resizebox{\textwidth}{!}{
\begin{tabular}{@{}ll | ccc | ccc | ccc@{}}
\toprule
\multirow{2}{*}{\textbf{Model}} & \multirow{2}{*}{\textbf{Architecture}} & \multicolumn{3}{c|}{\textbf{Short-term}} & \multicolumn{3}{c|}{\textbf{Medium-term}} & \multicolumn{3}{c}{\textbf{Long-term}} \\
\cmidrule(lr){3-5} \cmidrule(lr){6-8} \cmidrule(l){9-11}
& & \textbf{MAE} & \textbf{MAPE (\%)} & \textbf{RMSE} & \textbf{MAE} & \textbf{MAPE (\%)} & \textbf{RMSE} & \textbf{MAE} & \textbf{MAPE (\%)} & \textbf{RMSE} \\
\midrule
'''

# Define order of models
model_order = [
    'LSTM', 'TRANSFORMER', 
    'LLAMA', 'LLAMA + LSTM', 'LLAMA + TRANSFORMER',
    'GPT', 'GPT + LSTM', 'GPT + TRANSFORMER',
    'GEMINI', 'GEMINI + LSTM', 'GEMINI + TRANSFORMER'
]
arch_order = ['Baseline', 'Hierarchical', 'Round Robin', 'Ensemble']

for i, model in enumerate(model_order):
    if model not in data:
        continue
        
    latex_table += f"\\multirow{{{len(data[model])}}}{{*}}{{\\textbf{{{model}}}}} \n"
    
    for arch in arch_order:
        if arch in data[model]:
            row_str = f"& {arch} "
            for h in horizons:
                if h in data[model][arch]:
                    metrics = data[model][arch][h]
                    row_str += f"& {metrics['MAE']} & {metrics['MAPE']} & {metrics['RMSE']} "
                else:
                    row_str += "& - & - & - "
            row_str += r"\\" + "\n"
            latex_table += row_str
            
    if i < len(model_order) - 1:
        latex_table += r"\midrule" + "\n"

latex_table += r'''\bottomrule
\end{tabular}
}
\end{table*}
'''

with open(r"k:\1\Preparation_of_Papers_for_IEEE_ACCESS\rq3_table.tex", 'w', encoding='utf-8') as f:
    f.write(latex_table)

print("Generated RQ3 table successfully.")
