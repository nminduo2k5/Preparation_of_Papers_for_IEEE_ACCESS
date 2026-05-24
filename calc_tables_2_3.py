import numpy as np
import re

table_data = {}
with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\table_content.txt', 'r', encoding='utf-8') as f:
    current_horizon = ""
    current_stock = ""
    for line in f:
        line = line.strip()
        if not line or line.startswith('%') or line.startswith('\\') and not line.startswith('\\multirow') and not line.startswith('&'):
            if line.startswith('&') and ('Round Robin' in line or 'Ensemble' in line or 'Hierarchical' in line):
                pass
            else:
                continue
                
        clean_line = re.sub(r'\\cellcolor\{[^\}]+\}', '', line)
        clean_line = re.sub(r'\\textbf\{([^\}]+)\}', r'\1', clean_line)
        clean_line = clean_line.replace(r'\\', '')
        
        parts = [p.strip() for p in clean_line.split('&')]
        if len(parts) >= 21:
            if parts[0] != '':
                if 'multirow' in parts[0]:
                    h_match = re.findall(r'\{([^}]+)\}', parts[0])
                    if h_match: current_horizon = h_match[-1].strip()
                else:
                    current_horizon = parts[0]
            
            if parts[1] != '':
                if 'multirow' in parts[1]:
                    s_match = re.findall(r'\{([^}]+)\}', parts[1])
                    if s_match: current_stock = s_match[-1].strip()
                else:
                    current_stock = parts[1]
            
            arch = parts[2].strip()
            
            h = 'Short-term' if 'Short' in current_horizon else 'Medium-term' if 'Medium' in current_horizon else 'Long-term' if 'Long' in current_horizon else current_horizon
            
            if h not in table_data: table_data[h] = {}
            if current_stock not in table_data[h]: table_data[h][current_stock] = {}
            
            try:
                values = [float(x.replace(r'\\', '').strip()) for x in parts[3:21]]
                table_data[h][current_stock][arch] = {
                    'lstm_llama': values[0:3], 'lstm_gpt': values[3:6], 'lstm_gemini': values[6:9],
                    'trans_llama': values[9:12], 'trans_gpt': values[12:15], 'trans_gemini': values[15:18]
                }
            except ValueError:
                pass

# --- TABLE 2: Summary of Aggregate Performance Metrics ---
lstm_mae, lstm_mape = [], []
trans_mae, trans_mape = [], []

for h in table_data:
    for s in table_data[h]:
        for arch in table_data[h][s]:
            row = table_data[h][s][arch]
            for llm in ['lstm_llama', 'lstm_gpt', 'lstm_gemini']:
                lstm_mae.append(row[llm][0])
                lstm_mape.append(row[llm][2])
            for llm in ['trans_llama', 'trans_gpt', 'trans_gemini']:
                trans_mae.append(row[llm][0])
                trans_mape.append(row[llm][2])

arch_lstm_mae = {'Hierarchical': [], 'Round Robin': [], 'Ensemble': []}
arch_lstm_mape = {'Hierarchical': [], 'Round Robin': [], 'Ensemble': []}

for h in table_data:
    for s in table_data[h]:
        for arch in table_data[h][s]:
            row = table_data[h][s][arch]
            for llm in ['lstm_llama', 'lstm_gpt', 'lstm_gemini']:
                arch_lstm_mae[arch].append(row[llm][0])
                arch_lstm_mape[arch].append(row[llm][2])

table2_latex = r'''\begin{table*}[t]
\centering
\caption{Summary of Aggregate Performance Metrics Across Models and Coordination Architectures.}
\label{tab:aggregate_performance_summary}
\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}llcc@{}}
\toprule
\textbf{Dimension} & \textbf{Configuration} & \textbf{Mean MAE} & \textbf{Mean MAPE (\%)} \\ \midrule
\multirow{2}{*}{\textbf{Base Model (Overall)}} & LSTM-based Multi-Agent & ''' + f"{np.mean(lstm_mae):.4f} & \\textbf{{{np.mean(lstm_mape):.2f}\\%}} \\\\\n" + \
r'''                                             & Transformer-based Multi-Agent & ''' + f"\\textbf{{{np.mean(trans_mae):.4f}}} & {np.mean(trans_mape):.2f}\\% \\\\ \\midrule\n" + \
r'''\multirow{3}{*}{\textbf{Architecture (under LSTM)}} & Hierarchical Architecture & ''' + f"{np.mean(arch_lstm_mae['Hierarchical']):.4f} & {np.mean(arch_lstm_mape['Hierarchical']):.2f}\\% \\\\\n" + \
r'''                                                      & Round Robin Architecture & ''' + f"{np.mean(arch_lstm_mae['Round Robin']):.4f} & {np.mean(arch_lstm_mape['Round Robin']):.2f}\\% \\\\\n" + \
r'''                                                      & Ensemble Voting Architecture & ''' + f"\\textbf{{{np.mean(arch_lstm_mae['Ensemble']):.4f}}} & \\textbf{{{np.mean(arch_lstm_mape['Ensemble']):.2f}\\%}} \\\\ \\bottomrule\n" + \
r'''\end{tabular*}
\end{table*}'''

# --- TABLE 3: Aggregate Performance Comparison Across Foundation LLM Families ---
llm_map = {'Llama-3.1-8B': ['lstm_llama', 'trans_llama'], 'GPT-4o': ['lstm_gpt', 'trans_gpt'], 'Gemini 2.0 Flash': ['lstm_gemini', 'trans_gemini']}
horizons = ['Short-term', 'Medium-term', 'Long-term']

table3_data = {llm: {h: {m: [] for m in ['MAE', 'RMSE', 'MAPE']} for h in horizons} for llm in llm_map}

for h in horizons:
    for s in table_data[h]:
        for arch in table_data[h][s]:
            row = table_data[h][s][arch]
            for llm_name, keys in llm_map.items():
                for key in keys:
                    table3_data[llm_name][h]['MAE'].append(row[key][0])
                    table3_data[llm_name][h]['RMSE'].append(row[key][1])
                    table3_data[llm_name][h]['MAPE'].append(row[key][2])

table3_latex = r'''\begin{table}[h!]
\centering
\caption{\textbf{Aggregate Performance Comparison Across Foundation LLM Families (Averaged Over All Stocks and Coordination Architectures).}}
\label{tab:llm_aggregate_comparison}
\resizebox{\columnwidth}{!}{
\begin{tabular}{llccc}
\toprule
\textbf{Horizon} & \textbf{Metric} & \textbf{Llama-3.1-8B} & \textbf{GPT-4o} & \textbf{Gemini 2.0 Flash} \\ \midrule
'''

for h_idx, h in enumerate(horizons):
    h_label = "Short-term (3-day)" if h == "Short-term" else "Medium-term (14-day)" if h == "Medium-term" else "Long-term (60-day)"
    table3_latex += f"\\multirow{{3}}{{*}}{{{h_label}}} \n"
    for m in ['MAE', 'RMSE', 'MAPE']:
        l_v = np.mean(table3_data['Llama-3.1-8B'][h][m])
        g_v = np.mean(table3_data['GPT-4o'][h][m])
        gem_v = np.mean(table3_data['Gemini 2.0 Flash'][h][m])
        
        vals = [l_v, g_v, gem_v]
        min_idx = vals.index(min(vals))
        fmts = [f"{v:.4f}" if m != 'MAPE' else f"{v:.2f}\\%" for v in vals]
        fmts[min_idx] = f"\\textbf{{{fmts[min_idx]}}}"
        
        m_label = "MAPE (\\%)" if m == "MAPE" else m
        table3_latex += f" & {m_label} & {fmts[0]} & {fmts[1]} & {fmts[2]} \\\\\n"
    table3_latex += "\\midrule\n"

table3_latex += "\\multirow{3}{*}{\\textbf{Overall Average}} \n"
for m in ['MAE', 'RMSE', 'MAPE']:
    l_vals = []
    g_vals = []
    gem_vals = []
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
    table3_latex += f" & {m_label} & {fmts[0]} & {fmts[1]} & {fmts[2]} \\\\\n"

table3_latex += r'''\bottomrule
\end{tabular}
}
\end{table}'''

with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\table2_generated.tex', 'w', encoding='utf-8') as f:
    f.write(table2_latex)

with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\table3_generated.tex', 'w', encoding='utf-8') as f:
    f.write(table3_latex)

print("Tables generated successfully.")

