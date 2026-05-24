cd C:\Users\HP\Desktop\ck
pdflatex -interaction=nonstopmode -file-line-error access.tex
bibtex access
pdflatex -interaction=nonstopmode -file-line-error access.tex
pdflatex -interaction=nonstopmode -file-line-error access.tex



## Python Scripts for Aggregating Table 2

### 1. `agg_script.py` - Parsing LaTeX table and calculating mean
```python
import re
import numpy as np

with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\table_content.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

data = []
current_horizon = ''

for line in lines:
    line = line.strip()
    if not line or line.startswith('%') or line.startswith(r'\toprule') or line.startswith(r'\midrule') or line.startswith(r'\bottomrule') or line.startswith(r'\cmidrule') or line.startswith(r'\multirow') or line.startswith(r'\multicolumn') or line.startswith(r'\caption') or line.startswith(r'\label') or line.startswith(r'\begin') or line.startswith(r'\end') or line.startswith('&'):
        # wait, some rows start with & like: & & Round Robin & ...
        if line.startswith('&') and 'Round Robin' in line or 'Ensemble' in line or 'Hierarchical' in line:
            pass # we need to parse this
        else:
            if 'Short-term' in line and '&' not in line: continue
            if 'Medium-term' in line and '&' not in line: continue
            if 'Long-term' in line and '&' not in line: continue
            if 'textbf' in line and 'MAE' in line: continue
            
    # Remove latex commands like \cellcolor{...}, \textbf{...}
    clean_line = re.sub(r'\\cellcolor\{[^\}]+\}', '', line)
    clean_line = re.sub(r'\\textbf\{([^\}]+)\}', r'\1', clean_line)
    
    parts = [p.strip() for p in clean_line.split('&')]
    if len(parts) >= 21:
        if parts[0]:
            current_horizon = parts[0].replace('multirow{36}{*}{', '').replace('}', '').strip()
        
        stock = parts[1].replace('multirow{3}{*}{', '').replace('}', '').strip()
        arch = parts[2].strip()
        
        try:
            values = [float(x.replace(r'\\', '').strip()) for x in parts[3:21]]
            data.append({
                'Horizon': current_horizon,
                'Stock': stock,
                'Architecture': arch,
                'values': values
            })
        except ValueError as e:
            pass

results = {}
for row in data:
    horizon = row['Horizon']
    if 'Short-term' in horizon: horizon = 'Short-term'
    elif 'Medium-term' in horizon: horizon = 'Medium-term'
    elif 'Long-term' in horizon: horizon = 'Long-term'
        
    arch = row['Architecture']
    key = (horizon, arch)
    if key not in results:
        results[key] = []
    results[key].append(row['values'])

out = ''
for key, vals in results.items():
    avg_vals = np.mean(vals, axis=0)
    avg_vals_str = ['{:.2f}'.format(v) for v in avg_vals]
    out += f"{key[0]} | {key[1]} | {' | '.join(avg_vals_str)}\n"

with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\parsed_agg.txt', 'w', encoding='utf-8') as f:
    f.write(out)
```

### 3. `calc_summary_table.py` - Calculating the 5-line Summary Table (Table 4)
```python
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

lstm_mae, lstm_mape, trans_mae, trans_mape = [], [], [], []
arch_lstm_metrics = {"Hierarchical": {"mae": [], "mape": []},
                     "Round Robin": {"mae": [], "mape": []},
                     "Ensemble": {"mae": [], "mape": []}}

for row in data:
    arch = row[1]
    
    # LSTM metrics for this row (columns: MAE=2,5,8 | MAPE=4,7,10)
    r_lstm_mae = [row[2], row[5], row[8]]
    r_lstm_mape = [row[4], row[7], row[10]]
    lstm_mae.extend(r_lstm_mae)
    lstm_mape.extend(r_lstm_mape)
    
    # Transformer metrics for this row (columns: MAE=11,14,17 | MAPE=13,16,19)
    r_trans_mae = [row[11], row[14], row[17]]
    r_trans_mape = [row[13], row[16], row[19]]
    trans_mae.extend(r_trans_mae)
    trans_mape.extend(r_trans_mape)
    
    # Store LSTM metrics by architecture
    arch_lstm_metrics[arch]["mae"].extend(r_lstm_mae)
    arch_lstm_metrics[arch]["mape"].extend(r_lstm_mape)

print("--- Base Model (Overall) ---")
print(f"LSTM-based: Mean MAE = {np.mean(lstm_mae):.4f}, Mean MAPE = {np.mean(lstm_mape):.2f}%")
print(f"Transformer-based: Mean MAE = {np.mean(trans_mae):.4f}, Mean MAPE = {np.mean(trans_mape):.2f}%")

print("\\n--- Architecture (under LSTM) ---")
for arch in ["Hierarchical", "Round Robin", "Ensemble"]:
    print(f"{arch}: Mean MAE = {np.mean(arch_lstm_metrics[arch]['mae']):.4f}, Mean MAPE = {np.mean(arch_lstm_metrics[arch]['mape']):.2f}%")
```


### 2. gen_latex.py - Generating the new LaTeX table
`python
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
```



\begin{table}[h!]
\centering
\caption{Comparison between actual and predicted prices across three model architectures in Long-term of FPT}
\begin{tabular}{|c|c|c|c|c|c|}
\hline
\textbf{Date} & \textbf{Stock Code} & \textbf{Actual Price (VND)} &
\textbf{Hierarchical} & \textbf{Round Robin} & \textbf{Ensemble} \\ \hline

 & & & & & \\ \hline
 & & & & & \\ \hline

\end{tabular}
\end{table}

fpt 01/09 -> 04/09 
fpt 01/09 -> 15/09 , 31/10


LLM Family	LSTM (Base)	Transformer (Base)
Gemini 2.0 Flash	update_table0.py (đọc test6.tex)	update_table0_5.py (đọc test5.tex)
GPT-4o	update_table0_1.py (đọc test7.tex)	update_table1.py (đọc test2.tex)
LLaMA-3	update_table2.py (đọc test3.tex)	update_table3.py (đọc test4.tex)

[text](access.pdf)


Vị trí bảng phụ lục (Appendix)	Nội dung cấu hình Mô hình & Baseline (Caption)	Kết quả
Cặp 1	Dòng 592	Dòng 5305	LLM: Google Gemini 2.0 Flash, LSTM Baseline	Khớp 100%
Cặp 2	Dòng 1225	Dòng 5938	LLM: Google Gemini 2.0 Flash, Transformer Baseline	Khớp 100%
Cặp 3	Dòng 1862	Dòng 6575	LLM: GPT-4o, LSTM Baseline	Khớp 100%
Cặp 4	Dòng 2503	Dòng 7216	LLM: GPT-4o, Transformer Baseline	Khớp 100%
Cặp 5	Dòng 3142	Dòng 7855	LLM: Llama, LSTM Baseline	Khớp 100%
Cặp 6	Dòng 3781	Dòng 8494	LLM: Llama, Transformer Baseline	Khớp 100%




Tôi đã ghi chép lại toàn bộ cả 2 đoạn code tính toán đầy đủ vào file read.md của bạn rồi nhé (bắt đầu từ dòng số 10 trở đi, ngay dưới các dòng lệnh build LaTeX để không ảnh hưởng đến luồng làm việc của bạn).

Bây giờ trong file read.md đã có đầy đủ:

agg_script.py: Chứa toàn bộ logic trích xuất dữ liệu từ bảng latex, xử lý và dùng numpy tính trung bình cộng dọc theo các mã cổ phiếu.
gen_latex.py: Chứa code chuyển đổi các mảng giá trị trung bình đã tính được thành mã LaTeX chuẩn với việc tự động phân tích và in đậm MAPE nhỏ nhất cho mỗi LLM.




Cụ thể là các file sau:

agg_script.py: Đây là file Python dùng để gom nhóm, tính trung bình (average) các chỉ số từ dữ liệu thô (hoặc từ file text như parsed_agg.txt và table_content.txt) để tạo ra bảng hiệu suất tổng hợp (Aggregated Performance Comparison) cho RQ1 và RQ2.
calculate_dm_test.py: Chứa code tính toán và định dạng bảng thống kê Diebold-Mariano (DM test) nhằm kiểm định ý nghĩa thống kê về sự khác biệt giữa các mô hình (phục vụ đánh giá mức độ tin cậy cho RQ1 và RQ2).
gen_latex.py / optimize_table.py: Các đoạn script dùng để lấy kết quả sau khi đã tính toán (như MAE, MAPE, RMSE) rồi đắp vào khung (template) bảng LaTeX chuẩn của IEEE Access.
Ngoài ra, nếu bạn muốn xem lại các dữ liệu đầu vào hoặc output tạm thời được dùng cho các phép tính trên, bạn có thể mở các file table_content.txt, parsed_agg.txt, hoặc metrics_report.txt cũng nằm ngay trong thư mục gốc. Bạn có muốn tôi mở thử file nào trong số các file trên lên để tinh chỉnh lại logic tính toán không?

