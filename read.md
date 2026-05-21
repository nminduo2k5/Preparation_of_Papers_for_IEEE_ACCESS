cd C:\Users\HP\Desktop\ck
pdflatex -interaction=nonstopmode -file-line-error access.tex
bibtex access
pdflatex -interaction=nonstopmode -file-line-error access.tex
pdflatex -interaction=nonstopmode -file-line-error access.tex


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