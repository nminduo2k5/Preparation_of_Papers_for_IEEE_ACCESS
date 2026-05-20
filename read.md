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