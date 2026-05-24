import numpy as np

# Data from parsed_agg.txt
data = [
    ["Short-term", "Hierarchical", 1.62, 2.03, 3.07, 2.75, 3.14, 5.11, 1.96, 2.32, 3.92, 1.55, 2.03, 3.33, 1.85, 2.23, 3.94, 1.97, 2.38, 3.87],
    ["Short-term", "Round Robin", 1.90, 2.15, 3.50, 2.58, 3.13, 4.62, 1.86, 2.19, 3.45, 1.68, 2.07, 3.17, 1.68, 2.23, 3.29, 2.12, 2.47, 4.08],
    ["Short-term", "Ensemble", 1.67, 2.07, 3.27, 1.74, 2.10, 3.69, 1.96, 2.25, 4.10, 1.77, 2.14, 3.40, 1.26, 1.48, 2.70, 1.57, 1.86, 2.93],
    ["Medium-term", "Hierarchical", 3.86, 4.92, 6.93, 3.08, 3.54, 5.83, 3.99, 4.59, 7.89, 3.08, 4.08, 5.61, 3.22, 3.88, 5.65, 3.26, 3.90, 6.24],
    ["Medium-term", "Round Robin", 3.31, 4.25, 5.67, 2.98, 3.69, 5.00, 2.63, 3.07, 5.00, 3.75, 4.67, 6.37, 3.38, 4.66, 5.84, 2.61, 3.05, 5.27],
    ["Medium-term", "Ensemble", 3.86, 5.06, 6.04, 2.44, 2.92, 4.07, 2.15, 2.58, 4.55, 3.52, 4.53, 6.24, 2.86, 3.80, 5.42, 1.64, 2.16, 3.51],
    ["Long-term", "Hierarchical", 4.33, 5.65, 9.35, 3.07, 3.68, 7.30, 3.98, 4.65, 9.20, 4.67, 6.19, 10.08, 4.60, 5.72, 9.49, 3.30, 3.83, 7.89],
    ["Long-term", "Round Robin", 6.05, 7.89, 11.02, 3.41, 3.85, 7.99, 3.61, 4.34, 8.25, 4.55, 5.75, 9.18, 4.63, 5.93, 10.34, 3.21, 3.83, 7.77],
    ["Long-term", "Ensemble", 3.96, 5.07, 9.47, 2.18, 2.73, 5.63, 3.07, 3.75, 7.06, 4.42, 5.39, 9.30, 5.62, 7.20, 10.99, 2.17, 2.57, 5.89]
]

out = r"""\begin{table*}[t]
\centering
\caption{\textbf{Aggregated Performance Comparison Across Forecasting Horizons, Architectures, and LLMs.} Values are averaged across all evaluated stocks to provide a macro-level assessment addressing RQ1 (Architectural Effectiveness) and RQ2 (LLM Impact). The best-performing model in each configuration is highlighted in bold.}
\label{tab:aggregated_performance}
\resizebox{\textwidth}{!}{
\begin{tabular}{@{}ll | ccc ccc ccc | ccc ccc ccc@{}}
\toprule
\multirow{3}{*}{\textbf{Horizon}} & \multirow{3}{*}{\textbf{Architecture}} & \multicolumn{9}{c|}{\textbf{LSTM Baseline}} & \multicolumn{9}{c}{\textbf{Transformer Baseline}} \\
\cmidrule(lr){3-11} \cmidrule(l){12-20}
& & \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{GPT-4o}} & \multicolumn{3}{c|}{\textbf{Gemini 2.0}} & \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{GPT-4o}} & \multicolumn{3}{c}{\textbf{Gemini 2.0}} \\
\cmidrule(lr){3-5} \cmidrule(lr){6-8} \cmidrule(lr){9-11} \cmidrule(lr){12-14} \cmidrule(lr){15-17} \cmidrule(lr){18-20}
& & \textbf{MAE} & \textbf{RMSE} & \textbf{MAPE} & \textbf{MAE} & \textbf{RMSE} & \textbf{MAPE} & \textbf{MAE} & \textbf{RMSE} & \textbf{MAPE} & \textbf{MAE} & \textbf{RMSE} & \textbf{MAPE} & \textbf{MAE} & \textbf{RMSE} & \textbf{MAPE} & \textbf{MAE} & \textbf{RMSE} & \textbf{MAPE} \\
\midrule
"""

current_horizon = ""
for idx, row in enumerate(data):
    horizon = row[0]
    arch = row[1]
    
    if horizon != current_horizon:
        if idx != 0:
            out += "\\midrule\n"
        out += f"\\multirow{{3}}{{*}}{{\\textbf{{{horizon}}}}}"
        current_horizon = horizon
    else:
        out += ""
        
    out += f" & {arch} "
    
    # LSTM
    lstm_llama = row[2:5]
    lstm_gpt = row[5:8]
    lstm_gemini = row[8:11]
    
    # find best MAPE in LSTM
    mapes = [lstm_llama[2], lstm_gpt[2], lstm_gemini[2]]
    min_mape_idx = mapes.index(min(mapes))
    
    lstm_blocks = [lstm_llama, lstm_gpt, lstm_gemini]
    for i, b in enumerate(lstm_blocks):
        if i == min_mape_idx:
            out += f"& \\textbf{{{b[0]:.2f}}} & \\textbf{{{b[1]:.2f}}} & \\textbf{{{b[2]:.2f}}} "
        else:
            out += f"& {b[0]:.2f} & {b[1]:.2f} & {b[2]:.2f} "
            
    # Transformer
    tr_llama = row[11:14]
    tr_gpt = row[14:17]
    tr_gemini = row[17:20]
    
    mapes_tr = [tr_llama[2], tr_gpt[2], tr_gemini[2]]
    min_mape_tr_idx = mapes_tr.index(min(mapes_tr))
    
    tr_blocks = [tr_llama, tr_gpt, tr_gemini]
    for i, b in enumerate(tr_blocks):
        if i == min_mape_tr_idx:
            out += f"& \\textbf{{{b[0]:.2f}}} & \\textbf{{{b[1]:.2f}}} & \\textbf{{{b[2]:.2f}}} "
        else:
            out += f"& {b[0]:.2f} & {b[1]:.2f} & {b[2]:.2f} "
            
    out += "\\\\\n"

out += r"""\bottomrule
\end{tabular}
}
\end{table*}
"""

with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\new_table.tex', 'w', encoding='utf-8') as f:
    f.write(out)
