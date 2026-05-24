import re
import numpy as np
import os

tex_path = r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\access.tex'

with open(tex_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

data = []
current_horizon = ''
current_stock = ''

parsing = False
for line in lines:
    if r'\label{tab:full_performance_all}' in line:
        parsing = True
        continue
    
    if parsing and r'\end{longtable}' in line:
        break
        
    if not parsing:
        continue

    line = line.strip()
    if not line or line.startswith('%') or line.startswith(r'\toprule') or line.startswith(r'\midrule') or line.startswith(r'\bottomrule') or line.startswith(r'\cmidrule') or line.startswith(r'\multicolumn') or line.startswith(r'\caption') or line.startswith(r'\label') or line.startswith(r'\begin') or line.startswith(r'\end') or line.startswith(r'\table'):
        if line.startswith('&') and ('Round Robin' in line or 'Ensemble' in line or 'Hierarchical' in line):
            pass # we need to parse this
        else:
            continue
            
    # Clean latex
    clean_line = re.sub(r'\\cellcolor\{[^\}]+\}', '', line)
    clean_line = re.sub(r'\\textbf\{([^\}]+)\}', r'\1', clean_line)
    clean_line = clean_line.replace(r'\\', '')
    
    parts = [p.strip() for p in clean_line.split('&')]
    if len(parts) >= 21:
        # Parse Horizon
        if parts[0] != '':
            if 'multirow' in parts[0]:
                h_match = re.findall(r'\{([^}]+)\}', parts[0])
                if h_match: current_horizon = h_match[-1].strip()
            else:
                current_horizon = parts[0]
        
        # Parse Stock
        if parts[1] != '':
            if 'multirow' in parts[1]:
                s_match = re.findall(r'\{([^}]+)\}', parts[1])
                if s_match: current_stock = s_match[-1].strip()
            else:
                current_stock = parts[1]
                
        arch = parts[2].strip()
        
        h = 'Short-term' if 'Short' in current_horizon else 'Medium-term' if 'Medium' in current_horizon else 'Long-term' if 'Long' in current_horizon else current_horizon
        
        try:
            values = [float(x.strip()) for x in parts[3:21]]
            data.append({
                'Horizon': h,
                'Stock': current_stock,
                'Architecture': arch,
                'values': values
            })
        except ValueError:
            pass

print(f"Extracted {len(data)} rows from access.tex.")

# ---------------------------------------------------------
# COMPUTE TABLE 1: Aggregated Performance (RQ1)
# Groups by Horizon and Architecture, average over all 12 stocks and all 3 LLMs (Llama, GPT, Gemini) for LSTM vs Transformer
# columns in values:
# 0-2: Llama-LSTM (MAE, RMSE, MAPE)
# 3-5: GPT-LSTM
# 6-8: Gemini-LSTM
# 9-11: Llama-Trans
# 12-14: GPT-Trans
# 15-17: Gemini-Trans
# ---------------------------------------------------------

results_table1 = {}
for row in data:
    h = row['Horizon']
    arch = row['Architecture']
    key = (h, arch)
    if key not in results_table1:
        results_table1[key] = {'lstm': [], 'trans': []}
    
    v = row['values']
    # LSTM metrics: avg over 3 LLMs (Llama, GPT, Gemini)
    lstm_mae = (v[0] + v[3] + v[6]) / 3
    lstm_rmse = (v[1] + v[4] + v[7]) / 3
    lstm_mape = (v[2] + v[5] + v[8]) / 3
    
    # Trans metrics: avg over 3 LLMs
    trans_mae = (v[9] + v[12] + v[15]) / 3
    trans_rmse = (v[10] + v[13] + v[16]) / 3
    trans_mape = (v[11] + v[14] + v[17]) / 3
    
    results_table1[key]['lstm'].append([lstm_mae, lstm_rmse, lstm_mape])
    results_table1[key]['trans'].append([trans_mae, trans_rmse, trans_mape])

# Generate Table 1 LaTeX
table1_latex = r'''\begin{table*}[t]
\centering
\caption{Aggregated Performance Comparison Across Forecasting Horizons, Architectures, and LLMs.}
\label{tab:aggregated_performance}
\resizebox{\textwidth}{!}{
\begin{tabular}{llccc|ccc}
\toprule
\multirow{2}{*}{\textbf{Horizon}} & \multirow{2}{*}{\textbf{Architecture}} & \multicolumn{3}{c|}{\textbf{LSTM-based Multi-Agent}} & \multicolumn{3}{c}{\textbf{Transformer-based Multi-Agent}} \\
\cmidrule(lr){3-5} \cmidrule(lr){6-8}
& & \textbf{MAE} & \textbf{RMSE} & \textbf{MAPE (\%)} & \textbf{MAE} & \textbf{RMSE} & \textbf{MAPE (\%)} \\ \midrule
'''

horizons = ['Short-term', 'Medium-term', 'Long-term']
archs = ['Hierarchical', 'Round Robin', 'Ensemble']

for h in horizons:
    table1_latex += f"\\multirow{{3}}{{*}}{{\\textbf{{{h}}}}} \n"
    for arch in archs:
        key = (h, arch)
        if key in results_table1:
            lstm_mean = np.mean(results_table1[key]['lstm'], axis=0)
            trans_mean = np.mean(results_table1[key]['trans'], axis=0)
            
            # Format and bold minimums row-wise
            l_vals = list(lstm_mean)
            t_vals = list(trans_mean)
            
            # MAE
            if l_vals[0] < t_vals[0]: l_mae = f"\\textbf{{{l_vals[0]:.4f}}}"; t_mae = f"{t_vals[0]:.4f}"
            else: l_mae = f"{l_vals[0]:.4f}"; t_mae = f"\\textbf{{{t_vals[0]:.4f}}}"
            
            # RMSE
            if l_vals[1] < t_vals[1]: l_rmse = f"\\textbf{{{l_vals[1]:.4f}}}"; t_rmse = f"{t_vals[1]:.4f}"
            else: l_rmse = f"{l_vals[1]:.4f}"; t_rmse = f"\\textbf{{{t_vals[1]:.4f}}}"
            
            # MAPE
            if l_vals[2] < t_vals[2]: l_mape = f"\\textbf{{{l_vals[2]:.2f}}}"; t_mape = f"{t_vals[2]:.2f}"
            else: l_mape = f"{l_vals[2]:.2f}"; t_mape = f"\\textbf{{{t_vals[2]:.2f}}}"
            
            table1_latex += f"& {arch} & {l_mae} & {l_rmse} & {l_mape} & {t_mae} & {t_rmse} & {t_mape} \\\\\n"
    table1_latex += "\\midrule\n"

table1_latex += r'''\bottomrule
\end{tabular}
}
\end{table*}'''

# ---------------------------------------------------------
# COMPUTE TABLE 2: Summary of Aggregate Performance Metrics
# ---------------------------------------------------------
lstm_mae_all, lstm_mape_all = [], []
trans_mae_all, trans_mape_all = [], []

arch_lstm_mae = {'Hierarchical': [], 'Round Robin': [], 'Ensemble': []}
arch_lstm_mape = {'Hierarchical': [], 'Round Robin': [], 'Ensemble': []}

for row in data:
    v = row['values']
    arch = row['Architecture']
    
    # LSTM overall (all 3 LLMs)
    l_m = [v[0], v[3], v[6]]
    l_ma = [v[2], v[5], v[8]]
    lstm_mae_all.extend(l_m)
    lstm_mape_all.extend(l_ma)
    
    # Trans overall (all 3 LLMs)
    t_m = [v[9], v[12], v[15]]
    t_ma = [v[11], v[14], v[17]]
    trans_mae_all.extend(t_m)
    trans_mape_all.extend(t_ma)
    
    arch_lstm_mae[arch].extend(l_m)
    arch_lstm_mape[arch].extend(l_ma)

table2_latex = r'''\begin{table*}[t]
\centering
\caption{Summary of Aggregate Performance Metrics Across Models and Coordination Architectures.}
\label{tab:aggregate_performance_summary}
\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}llcc@{}}
\toprule
\textbf{Dimension} & \textbf{Configuration} & \textbf{Mean MAE} & \textbf{Mean MAPE (\%)} \\ \midrule
\multirow{2}{*}{\textbf{Base Model (Overall)}} & LSTM-based Multi-Agent & ''' + f"{np.mean(lstm_mae_all):.4f} & \\textbf{{{np.mean(lstm_mape_all):.2f}\\%}} \\\\\n" + \
r'''                                             & Transformer-based Multi-Agent & ''' + f"\\textbf{{{np.mean(trans_mae_all):.4f}}} & {np.mean(trans_mape_all):.2f}\\% \\\\ \\midrule\n" + \
r'''\multirow{3}{*}{\textbf{Architecture (under LSTM)}} & Hierarchical Architecture & ''' + f"{np.mean(arch_lstm_mae['Hierarchical']):.4f} & {np.mean(arch_lstm_mape['Hierarchical']):.2f}\\% \\\\\n" + \
r'''                                                      & Round Robin Architecture & ''' + f"{np.mean(arch_lstm_mae['Round Robin']):.4f} & {np.mean(arch_lstm_mape['Round Robin']):.2f}\\% \\\\\n" + \
r'''                                                      & Ensemble Voting Architecture & ''' + f"\\textbf{{{np.mean(arch_lstm_mae['Ensemble']):.4f}}} & \\textbf{{{np.mean(arch_lstm_mape['Ensemble']):.2f}\\%}} \\\\ \\bottomrule\n" + \
r'''\end{tabular*}
\end{table*}'''

# ---------------------------------------------------------
# COMPUTE TABLE 3: LLM Aggregate Comparison
# ---------------------------------------------------------
llm_map = {'Llama-3.1-8B': ([0, 3, 6], [9, 12, 15]), 'GPT-4o': ([3, 4, 5], [12, 13, 14]), 'Gemini 2.0 Flash': ([6, 7, 8], [15, 16, 17])}
# Wait, the indices for LLM columns:
# Llama-LSTM: 0(MAE), 1(RMSE), 2(MAPE)
# GPT-LSTM: 3(MAE), 4(RMSE), 5(MAPE)
# Gemini-LSTM: 6(MAE), 7(RMSE), 8(MAPE)
# Llama-Trans: 9(MAE), 10(RMSE), 11(MAPE)
# GPT-Trans: 12(MAE), 13(RMSE), 14(MAPE)
# Gemini-Trans: 15(MAE), 16(RMSE), 17(MAPE)

table3_data = {llm: {h: {'MAE': [], 'RMSE': [], 'MAPE': []} for h in horizons} for llm in ['Llama-3.1-8B', 'GPT-4o', 'Gemini 2.0 Flash']}

for row in data:
    h = row['Horizon']
    v = row['values']
    
    # Llama
    table3_data['Llama-3.1-8B'][h]['MAE'].extend([v[0], v[9]])
    table3_data['Llama-3.1-8B'][h]['RMSE'].extend([v[1], v[10]])
    table3_data['Llama-3.1-8B'][h]['MAPE'].extend([v[2], v[11]])
    
    # GPT
    table3_data['GPT-4o'][h]['MAE'].extend([v[3], v[12]])
    table3_data['GPT-4o'][h]['RMSE'].extend([v[4], v[13]])
    table3_data['GPT-4o'][h]['MAPE'].extend([v[5], v[14]])
    
    # Gemini
    table3_data['Gemini 2.0 Flash'][h]['MAE'].extend([v[6], v[15]])
    table3_data['Gemini 2.0 Flash'][h]['RMSE'].extend([v[7], v[16]])
    table3_data['Gemini 2.0 Flash'][h]['MAPE'].extend([v[8], v[17]])

table3_latex = r'''\begin{table}[h!]
\centering
\caption{\textbf{Aggregate Performance Comparison Across Foundation LLM Families (Averaged Over All Stocks and Coordination Architectures).}}
\label{tab:llm_aggregate_comparison}
\resizebox{\columnwidth}{!}{
\begin{tabular}{llccc}
\toprule
\textbf{Horizon} & \textbf{Metric} & \textbf{Llama-3.1-8B} & \textbf{GPT-4o} & \textbf{Gemini 2.0 Flash} \\ \midrule
'''

for h in horizons:
    h_label = "Short-term (3-day)" if h == "Short-term" else "Medium-term (14-day)" if h == "Medium-term" else "Long-term (60-day)"
    table3_latex += f"\\multirow{{3}}{{*}}{{\\textbf{{{h_label}}}}} \n"
    for m in ['MAE', 'RMSE', 'MAPE']:
        l_v = np.mean(table3_data['Llama-3.1-8B'][h][m])
        g_v = np.mean(table3_data['GPT-4o'][h][m])
        gem_v = np.mean(table3_data['Gemini 2.0 Flash'][h][m])
        
        vals = [l_v, g_v, gem_v]
        min_idx = vals.index(min(vals))
        fmts = [f"{v:.4f}" if m != 'MAPE' else f"{v:.2f}\\%" for v in vals]
        fmts[min_idx] = f"\\textbf{{{fmts[min_idx]}}}"
        
        m_label = "MAPE (\\%)" if m == "MAPE" else m
        table3_latex += f" & \\textbf{{{m_label}}} & {fmts[0]} & {fmts[1]} & {fmts[2]} \\\\\n"
    table3_latex += "\\midrule\n"

table3_latex += "\\multirow{3}{*}{\\textbf{Overall Average}} \n"
for m in ['MAE', 'RMSE', 'MAPE']:
    l_vals, g_vals, gem_vals = [], [], []
    for h in horizons:
        l_vals.extend(table3_data['Llama-3.1-8B'][h][m])
        g_vals.extend(table3_data['GPT-4o'][h][m])
        gem_vals.extend(table3_data['Gemini 2.0 Flash'][h][m])
    
    l_v = np.mean(l_vals)
    g_v = np.mean(g_vals)
    gem_v = np.mean(gem_vals)
    
    vals = [l_v, g_v, gem_v]
    min_idx = vals.index(min(vals))
    fmts = [f"{v:.4f}" if m != 'MAPE' else f"{v:.2f}\\%" for v in vals]
    fmts[min_idx] = f"\\textbf{{{fmts[min_idx]}}}"
    
    m_label = "MAPE (\\%)" if m == "MAPE" else m
    table3_latex += f" & \\textbf{{{m_label}}} & {fmts[0]} & {fmts[1]} & {fmts[2]} \\\\\n"

table3_latex += r'''\bottomrule
\end{tabular}
}
\end{table}'''

with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\table1_generated.tex', 'w', encoding='utf-8') as f:
    f.write(table1_latex)

with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\table2_generated.tex', 'w', encoding='utf-8') as f:
    f.write(table2_latex)

with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\table3_generated.tex', 'w', encoding='utf-8') as f:
    f.write(table3_latex)

print("SUCCESS: Tables 1, 2, and 3 have been generated.")
