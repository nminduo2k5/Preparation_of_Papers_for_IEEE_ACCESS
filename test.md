\clearpage
\onecolumn  
\begin{table*}[!h]
\centering
\caption{Comparison of Short-term, Medium-term, and Long-term Forecasts Across Architectures and Stocks (LLM: Llama3.1:8b )}
\label{tab:full_forecast}
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.05}
\scriptsize
\begin{tabular}{llcc|cccc|cccc|cccc}
\toprule
\multirow{2}{*}{\textbf{Stock}} &
\multirow{2}{*}{\textbf{Architecture}} &
\multicolumn{2}{c|}{\textbf{Start}} &
\multicolumn{4}{c|}{\textbf{Short-term}} &
\multicolumn{4}{c|}{\textbf{Medium-term}} &
\multicolumn{4}{c}{\textbf{Long-term}} \\
\cmidrule(lr){3-4}
\cmidrule(lr){5-8}
\cmidrule(lr){9-12}
\cmidrule(lr){13-16}
& &
\textbf{Date} & \textbf{Price} &
\textbf{End Date} & \textbf{Pred} & \textbf{Act} & \textbf{Gap} &
\textbf{End Date} & \textbf{Pred} & \textbf{Act} & \textbf{Gap} &
\textbf{End Date} & \textbf{Pred} & \textbf{Act} & \textbf{Gap} \\
\midrule


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ===================== DXG ======================
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\multirow{4}{*}{\textbf{DXG}} 
& \textbf{Hierarchical}
& 31/08 & 22.8 & 03/09 & 22.92 & 24 & \textcolor{green}{\(\uparrow\)+1.08} & 14/09 & 23.13 & 24.05 & \textcolor{green}{\(\uparrow\)+0.92} & 30/10 & 23.73 & 21.2 & \textcolor{red}{\(\downarrow\)-2.53} \\

& 
& 16/10 & 22.45 & 19/10 & 22.58 & 22.6 & \textcolor{green}{\(\uparrow\)+0.02} & 30/10 & 22.80 & 21.2 & \textcolor{red}{\(\downarrow\)-1.6} & 15/12 & 23.43 & 16.3 & \textcolor{red}{\(\downarrow\)-7.13} \\

& 
& 21/10 & 20.0 & 24/10 & 20.12 & 20.9 & \textcolor{green}{\(\uparrow\)+0.78} & 04/11 & 20.31 & 20.15 & \textcolor{green}{\(\uparrow\)+0.16} & 20/12 & 20.88 & 17.8 & \textcolor{red}{\(\downarrow\)-3.08} \\

&
& 22/10 & 20.5 & 25/10 & 20.61 & 20.9 & \textcolor{green}{\(\uparrow\)+0.29} & 05/11 & 20.79 & 20.1 & \textcolor{red}{\(\downarrow\)-0.69} & 21/12 & 21.33 & 17.8 & \textcolor{red}{\(\downarrow\)-3.53} \\
\midrule


\multirow{4}{*}{\textbf{DXG}} 
& \textbf{Round Robin}
& 31/08 & 22.8 & 03/09 & 23.07 & 24 & \textcolor{green}{\(\uparrow\)+0.93} & 14/09 & 23.44 & 24.05 & \textcolor{green}{\(\uparrow\)+0.61} & 30/10 & 24.10 & 21.2 & \textcolor{red}{\(\downarrow\)-2.90} \\

&
& 16/10 & 22.45 & 19/10 & 22.75 & 22.6 & \textcolor{green}{\(\uparrow\)+0.15} & 30/10 & 23.08 & 21.2 & \textcolor{red}{\(\downarrow\)-1.88} & 15/12 & 23.83 & 16.3 & \textcolor{red}{\(\downarrow\)-7.53} \\

&
& 21/10 & 20.0 & 24/10 & 20.17 & 20.9 & \textcolor{green}{\(\uparrow\)+0.73} & 04/11 & 20.38 & 20.15 & \textcolor{green}{\(\uparrow\)+0.23} & 20/12 & 20.82 & 17.8 & \textcolor{red}{\(\downarrow\)-3.02} \\

&
& 22/10 & 20.5 & 25/10 & 20.68 & 20.9 & \textcolor{green}{\(\uparrow\)+0.22} & 05/11 & 20.88 & 20.1 & \textcolor{red}{\(\downarrow\)-0.78} & 21/12 & 21.42 & 17.8 & \textcolor{red}{\(\downarrow\)-3.62} \\
\midrule


\multirow{4}{*}{\textbf{DXG}} 
& \textbf{Ensemble}
& 31/08 & 22.8 & 03/09 & 22.91 & 24 & \textcolor{red}{\(\downarrow\)-1.09} & 14/09 & 23.10 & 24.05 & \textcolor{green}{\(\uparrow\)+0.95} & 30/10 & 23.59 & 21.2 & \textcolor{red}{\(\downarrow\)-2.39} \\

&
& 16/10 & 22.45 & 19/10 & 22.57 & 22.6 & \textcolor{green}{\(\uparrow\)+0.03} & 30/10 & 22.75 & 21.2 & \textcolor{red}{\(\downarrow\)-1.55} & 15/12 & 23.23 & 16.3 & \textcolor{red}{\(\downarrow\)-6.93} \\

&
& 21/10 & 20.0 & 24/10 & 20.12 & 20.9 & \textcolor{green}{\(\uparrow\)+0.78} & 04/11 & 20.27 & 20.15 & \textcolor{green}{\(\uparrow\)+0.12} & 20/12 & 20.74 & 17.8 & \textcolor{red}{\(\downarrow\)-2.94} \\

&
& 22/10 & 20.5 & 25/10 & 20.60 & 20.9 & \textcolor{green}{\(\uparrow\)+0.3} & 05/11 & 20.75 & 20.1 & \textcolor{red}{\(\downarrow\)-0.65} & 21/12 & 21.21 & 17.8 & \textcolor{red}{\(\downarrow\)-3.41} \\
\midrule



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ===================== FPT ======================
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\multirow{4}{*}{\textbf{FPT}} 
& \textbf{Hierarchical}
& 01/09 & 101.6 & 04/09 & 101.20 & 105 & \textcolor{red}{\(\downarrow\)-3.8} & 15/09 & 101.91 & 101.9 & \textcolor{green}{\(\uparrow\)+0.01} & 31/10 & 101.75 & 103.9 & \textcolor{green}{\(\uparrow\)+1.67} \\

&
& 16/10 & 89.8 & 19/10 & 89.35 & 88.1 & \textcolor{green}{\(\uparrow\)+1.25} & 30/10 & 90.08 & 102.7 & \textcolor{green}{\(\uparrow\)-12.62} & 15/12 & 98.55 & 93.8 & \textcolor{green}{\(\uparrow\)+1.67} \\

&
& 21/10 & 93 & 24/10 & 92.62 & 97.7 & \textcolor{green}{\(\uparrow\)+2.33} & 04/11 & 93.14 & 103.3 & \textcolor{green}{\(\uparrow\)+7.50} & 20/12 & 94.50 & 93.9 &\textcolor{green}{\(\uparrow\)+3.66}\\

&
& 22/10 & 97 & 25/10 & 96.53 & 97.7 & \textcolor{red}{\(\downarrow\)-4.20} & 05/11 & 97.05 & 100.9 & \textcolor{green}{\(\uparrow\)+3.30} & 21/12 & 98.87 & 93.9 & \textcolor{red}{\(\downarrow\)-15.02} \\
\midrule


\multirow{4}{*}{\textbf{FPT}} 
& \textbf{Round Robin}
& 01/09 & 101.6 & 04/09 & 101.21 & 105 & \textcolor{green}{\(\uparrow\)+0.58} & 15/09 & 102.09 & 101.9 & \textcolor{red}{\(\downarrow\)-3.76} & 31/10 & 104.11 & 103.9 & \textcolor{green}{\(\uparrow\)+0.37} \\

&
& 16/10 & 89.8 & 19/10 & 89.39 & 88.1 & \textcolor{red}{\(\downarrow\)-2.36} & 30/10 & 90.03 & 102.7 & \textcolor{red}{\(\downarrow\)-11.42} & 15/12 & 91.13 & 93.8 & \textcolor{green}{\(\uparrow\)+3.1} \\

&
& 21/10 & 93 & 24/10 & 92.64 & 97.7 & \textcolor{green}{\(\uparrow\)+1.70} & 04/11 & 93.12 & 103.3 & \textcolor{green}{\(\uparrow\)+8.05} & 20/12 & 94.41 & 93.9 & \textcolor{green}{\(\uparrow\)+3.58} \\

&
& 22/10 & 97 & 25/10 & 96.67 & 97.7 & \textcolor{red}{\(\downarrow\)-4.02} & 05/11 & 97.38 & 100.9 & \textcolor{green}{\(\uparrow\)+7.30} & 21/12 & 105.33 & 93.9 & \textcolor{red}{\(\downarrow\)-15.02} \\
\midrule



\multirow{4}{*}{\textbf{FPT}} 
& \textbf{Ensemble}
& 01/09 & 101.6 & 04/09 & 101.04 & 105 & \textcolor{red}{\(\downarrow\)-3.96} & 15/09 & 103.6 & 101.9 & \textcolor{red}{\(\downarrow\)-1.70} & 31/10 & 103.23 & 103.9 & \textcolor{green}{\(\uparrow\)+0.67} \\

&
& 16/10 & 89.8 & 19/10 & 89.31 & 88.1 & \textcolor{green}{\(\uparrow\)+1.21} & 30/10 & 89.86 & 102.7 & \textcolor{green}{\(\uparrow\)-12.84} & 15/12 & 90.94 & 93.8 & \textcolor{green}{\(\uparrow\)+2.86} \\

&
& 21/10 & 93 & 24/10 & 92.50 & 97.7 & \textcolor{red}{\(\downarrow\)+5.2} & 04/11 & 93.03 & 103.3 & \textcolor{green}{\(\uparrow\)+10.27} & 20/12 & 94.04 & 93.9 & \textcolor{green}{\(\uparrow\)+0.14} \\

&
& 22/10 & 97 & 25/10 & 96.46 & 97.7 & \textcolor{red}{\(\downarrow\)+1.24} & 05/11 & 97.11 & 100.9 & \textcolor{green}{\(\uparrow\)+3.97} & 21/11 & 98.49 & 93.9 & \textcolor{red}{\(\downarrow\)-4.59} \\
\midrule




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ===================== VCB ======================
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\multirow{4}{*}{\textbf{VCB}} 
& \textbf{Hierarchical}
& 30/08 & 68.6 & 02/09 & 68.32 & 68.6 & \textcolor{yellow}{0.06} & 13/09 & 68.75 & 65.8 & \textcolor{red}{\(\downarrow\)-2.72} & 29/10 & 70.15 & 60.7 & \textcolor{green}{\(\uparrow\)+6.9} \\

&
& 16/10 & 62.9 & 19/10 & 63.09 & 61.9 & \textcolor{red}{\(\downarrow\)-1.39} & 30/10 & 61.59 & 60.6 & \textcolor{red}{\(\downarrow\)-3.69} & 15/12 & 64.82 & 56.8 & \textcolor{red}{\(\downarrow\)-7.67} \\

&
& 21/10 & 59.3 & 24/10 & 63.42 & 59.5 & \textcolor{green}{\(\uparrow\)-2.18} & 04/11 & 59.95 & 60.1 & \textcolor{green}{\(\uparrow\)+2.27} & 20/12 & 61.30 & 57.5 & \textcolor{green}{\(\uparrow\)+1.0} \\

&
& 22/10 & 59.6 & 25/10 & 59.82 & 59.5 & \textcolor{red}{\(\downarrow\)-1.71} & 05/11 & 60.24 & 60.8 & \textcolor{green}{\(\uparrow\)+1.57} & 21/12 & 61.58 & 57.5 & \textcolor{red}{\(\downarrow\)-5.26} \\
\midrule


\multirow{4}{*}{\textbf{VCB}} 
& \textbf{Round Robin}
& 30/08 & 68.6 & 02/09 & 68.43 & 68.6 & \textcolor{yellow}{0.14} & 13/09 & 68.95 & 65.8 & \textcolor{red}{\(\downarrow\)-3.10} & 29/10 & 70.37 & 60.7 & \textcolor{red}{\(\downarrow\)-17.11} \\

&
& 16/10 & 62.9 & 19/10 & 63.21 & 61.9 & \textcolor{green}{\(\uparrow\)+0.61} & 30/10 & 63.73 & 60.6 & \textcolor{red}{\(\downarrow\)-3.43} & 15/12 & 65.19 & 56.8 & \textcolor{red}{\(\downarrow\)-7.77} \\

&
& 21/10 & 59.3 & 24/10 & 59.61 & 59.5 & \textcolor{green}{\(\uparrow\)+1.65} & 04/11 & 60.09 & 60.1 & \textcolor{green}{\(\uparrow\)+2.27} & 20/12 & 61.47 & 57.5 & \textcolor{red}{\(\downarrow\)-5.5} \\

&
& 22/10 & 59.6 & 25/10 & 59.94 & 59.5 & \textcolor{red}{\(\downarrow\)-1.96} & 05/11 & 60.40 & 60.8 & \textcolor{green}{\(\uparrow\)+1.16} & 21/12 & 61.87 & 57.5 & \textcolor{red}{\(\downarrow\)-4.95} \\
\midrule

\multirow{4}{*}{\textbf{VCB}} 
& \textbf{Ensemble}
& 30/08 & 68.6 & 02/09 & 68.32 & 68.6 & \textcolor{yellow}{0.96} & 13/09 & 68.64 & 65.8 & \textcolor{red}{\(\downarrow\)-3.05} & 29/10 & 69.80 & 60.7 & \textcolor{green}{\(\uparrow\)+7.2} \\

&
& 16/10 & 62.9 & 19/10 & 63.09 & 61.9 & \textcolor{red}{\(\downarrow\)-1.75} & 30/10 & 63.36 & 60.6 & \textcolor{red}{\(\downarrow\)-3.74} & 15/12 & 64.47 & 56.8 & \textcolor{green}{\(\uparrow\)+5.14} \\

&
& 21/10 & 59.3 & 24/10 & 59.50 & 59.5 & \textcolor{green}{\(\uparrow\)+3.08} & 04/11 & 59.81 & 60.1 & \textcolor{green}{\(\uparrow\)+2.26} & 20/12 & 60.91 & 57.5 & \textcolor{red}{\(\downarrow\)-5.51} \\

&
& 22/10 & 59.6 & 25/10 & 59.80 & 59.5 & \textcolor{red}{\(\downarrow\)-1.38} & 05/11 & 60.18 & 60.8 & \textcolor{green}{\(\uparrow\)+0.98} & 21/12 & 61.11 & 57.5 & \textcolor{red}{\(\downarrow\)-4.79} \\
\midrule



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ===================== VCS ======================
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\multirow{4}{*}{\textbf{VCS}} 
& \textbf{Hierarchical}
& 30/08 & 48.8 & 02/09 & 47.22 & 48.8 & \textcolor{yellow}{0.83} & 13/09 & 47.65 & 50 & \textcolor{green}{\(\uparrow\)+0.20} & 29/10 & 48.52 & 47.6 & \textcolor{red}{\(\downarrow\)-2.91} \\

&
& 16/10 & 47.2 & 19/10 & 45.75 & 46.8 & \textcolor{red}{\(\downarrow\)-1.06} & 30/10 & 46.09 & 47.4 & \textcolor{green}{\(\uparrow\)+2.34} & 15/12 & 46.79 & 46.5 & \textcolor{green}{\(\uparrow\)+4.37} \\

&
& 21/10 & 45.5 & 24/10 & 44.04 & 46.2 & \textcolor{green}{\(\uparrow\)+0.92} & 04/11 & 44.34 & 47.1 & \textcolor{green}{\(\uparrow\)+0.04} & 20/12 & 45.06 & 43 & \textcolor{red}{\(\downarrow\)-4.66} \\

&
& 22/10 & 45.5 & 25/10 & 44.06 & 46.2 & \textcolor{green}{\(\uparrow\)+0.18} & 05/11 & 44.39 & 46.9 & \textcolor{green}{\(\uparrow\)+0.37} & 21/12 & 45.02 & 43 & \textcolor{red}{\(\downarrow\)-4.56} \\
\midrule


\multirow{4}{*}{\textbf{VCS}} 
& \textbf{Round Robin}
& 30/08 & 48.8 & 02/09 & 47.19 & 48.8 & \textcolor{yellow}{0.18} & 13/09 & 47.56 & 50 & \textcolor{red}{\(\downarrow\)-3.80} & 29/10 & 48.00 & 47.6 & \textcolor{red}{\(\downarrow\)-2.91} \\

&
& 16/10 & 47.2 & 19/10 & 45.64 & 46.8 & \textcolor{red}{\(\downarrow\)-0.75} & 30/10 & 46.03 & 47.4 & \textcolor{green}{\(\uparrow\)+0.46} & 15/12 & 46.69 & 46.5 & \textcolor{green}{\(\uparrow\)+1} \\

&
& 21/10 & 45.5 & 24/10 & 44.01 & 46.2 & \textcolor{green}{\(\uparrow\)+1.23} & 04/11 & 44.62 & 47.1 & \textcolor{green}{\(\uparrow\)+0.98} & 20/12 & 44.81 & 43 & \textcolor{green}{\(\uparrow\)+1.16} \\

&
& 22/10 & 45.5 & 25/10 & 43.98 & 46.2 & \textcolor{green}{\(\uparrow\)+0.72} & 05/11 & 44.32 & 46.9 & \textcolor{green}{\(\uparrow\)+0.30} & 21/12 & 44.74 & 43 & \textcolor{green}{\(\uparrow\)+1.15} \\
\midrule



\multirow{4}{*}{\textbf{VCS}} 
& \textbf{Ensemble}
& 30/08 & 48.8 & 02/09 & 45.35 & 48.8 & \textcolor{yellow}{3.45} & 13/09 & 47.48 & 50 & \textcolor{red}{\(\downarrow\)+2.52} & 29/10 & 48.26 & 47.6 & \textcolor{green}{\(\uparrow\)+0.66} \\

&
& 16/10 & 47.2 & 19/10 & 45.63 & 46.8 & \textcolor{green}{\(\uparrow\)+1.17} & 30/10 & 46.04 & 47.4 & \textcolor{red}{\(\downarrow\)-1.36} & 15/12 & 46.65 & 46.5 & \textcolor{green}{\(\uparrow\)+0.15} \\

&
& 21/10 & 45.5 & 24/10 & 43.97 & 46.2 & \textcolor{red}{\(\downarrow\)-2.23} & 04/11 & 44.33 & 47.1 & \textcolor{red}{\(\downarrow\)-2.77} & 20/12 & 44.98 & 43 & \textcolor{green}{\(\uparrow\)-1.98} \\

&
& 22/10 & 45.5 & 25/10 & 43.99 & 46.2 & \textcolor{red}{\(\downarrow\)+2.21} & 05/11 & 44.34 & 46.9 & \textcolor{red}{\(\downarrow\)-2.56} & 21/12 & 44.96 & 43 & \textcolor{green}{\(\uparrow\)+1.96}  \\


\bottomrule
\end{tabular}
\end{table*}







\clearpage
\onecolumn
\begin{table*}[!h]
\centering
\caption{Comparison of Short-term, Medium-term, and Long-term Forecasts Across Architectures and Stocks (LLM: GPT-4o)}
\label{tab:full_forecast}
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.05}
\scriptsize
\begin{tabular}{llcc|cccc|cccc|cccc}
\toprule
\multirow{2}{*}{\textbf{Stock}} &
\multirow{2}{*}{\textbf{Architecture}} &
\multicolumn{2}{c|}{\textbf{Start}} &
\multicolumn{4}{c|}{\textbf{Short-term}} &
\multicolumn{4}{c|}{\textbf{Medium-term}} &
\multicolumn{4}{c}{\textbf{Long-term}} \\
\cmidrule(lr){3-4}
\cmidrule(lr){5-8}
\cmidrule(lr){9-12}
\cmidrule(lr){13-16}
& &
\textbf{Date} & \textbf{Price} &
\textbf{End Date} & \textbf{Pred} & \textbf{Act} & \textbf{Gap} &
\textbf{End Date} & \textbf{Pred} & \textbf{Act} & \textbf{Gap} &
\textbf{End Date} & \textbf{Pred} & \textbf{Act} & \textbf{Gap} \\
\midrule


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ===================== DXG ======================
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\multirow{4}{*}{\textbf{DXG}} 
& \textbf{Hierarchical}
& 31/08 & 22.8 & 03/09 & 23.01 & 24 & \textcolor{red}{\(\downarrow\)-1.75} & 14/09 & 23.30 & 24.05 & \textcolor{green}{\(\uparrow\)+0.67} & 30/10 & 23.78 & 21.2 & \textcolor{green}{\(\uparrow\)+0.63} \\

& 
& 16/10 & 22.45 & 19/10 & 22.70 & 22.6 & \textcolor{red}{\(\downarrow\)-0.50} & 30/10 & 22.96 & 21.2 & \textcolor{green}{\(\uparrow\)+2.14} & 15/12 & 23.39 & 16.3 & \textcolor{red}{\(\downarrow\)-8.16} \\

& 
& 21/10 & 20.0 & 24/10 & 20.20 & 20.9 & \textcolor{green}{\(\uparrow\)+0.39} & 04/11 & 20.34 & 20.15 & \textcolor{green}{\(\uparrow\)+0.37} & 20/12 & 19.91 & 17.8 & \textcolor{red}{\(\downarrow\)-3.01} \\

&
& 22/10 & 20.5 & 25/10 & 20.67 & 20.9 & \textcolor{green}{\(\uparrow\)+0.20} & 05/11 & 20.85 & 20.1 & \textcolor{red}{\(\downarrow\)-8.78} & 21/12 & 21.32 & 17.8 & \textcolor{green}{\(\uparrow\)+2.62} \\
\midrule


\multirow{4}{*}{\textbf{DXG}} 
& \textbf{Round Robin}
& 31/08 & 22.8 & 03/09 & 23.09 & 24 & \textcolor{red}{\(\downarrow\)-1.75} & 14/09 & 23.36 & 24.05 & \textcolor{red}{\(\downarrow\)-2.07} & 30/10 & 23.99 & 21.2 & \textcolor{red}{\(\downarrow\)-3.27} \\

&
& 16/10 & 22.45 & 19/10 & 22.75 & 22.6 & \textcolor{red}{\(\downarrow\)-0.45} & 30/10 & 23.07 & 21.2 & \textcolor{green}{\(\uparrow\)+1.08} & 15/12 & 23.87 & 16.3 & \textcolor{red}{\(\downarrow\)-9.33} \\

&
& 21/10 & 20.0 & 24/10 & 20.16 & 20.9 & \textcolor{green}{\(\uparrow\)+0.56} & 04/11 & 20.33 & 20.15 & \textcolor{green}{\(\uparrow\)+0.64} & 20/12 & 20.69 & 17.8 & \textcolor{red}{\(\downarrow\)-3.16} \\

&
& 22/10 & 20.5 & 25/10 & 20.68 & 20.9 & \textcolor{red}{\(\downarrow\)-0.42} & 05/11 & 20.90 & 20.1 & \textcolor{red}{\(\downarrow\)-3.58} & 21/12 & 21.33 & 17.8 & \textcolor{red}{\(\downarrow\)-3.16} \\
\midrule


\multirow{4}{*}{\textbf{DXG}} 
& \textbf{Ensemble}
& 31/08 & 22.8 & 03/09 & 22.98 & 24 & \textcolor{red}{\(\downarrow\)-1.89} & 14/09 & 23.15 & 24.05 & \textcolor{green}{\(\uparrow\)+1.07} & 30/10 & 23.54 & 21.2 & \textcolor{red}{\(\downarrow\)-0.27} \\

&
& 16/10 & 22.45 & 19/10 & 22.65 & 22.6 & \textcolor{red}{\(\downarrow\)-0.68} & 30/10 & 22.84 & 21.2 & \textcolor{green}{\(\uparrow\)+0.55} & 15/12 & 23.32 & 16.3 & \textcolor{red}{\(\downarrow\)-7.06} \\

&
& 21/10 & 20.0 & 24/10 & 20.16 & 20.9 & \textcolor{green}{\(\uparrow\)+0.83} & 04/11 & 20.32 & 20.15 & \textcolor{green}{\(\uparrow\)+0.37} & 20/12 & 20.63 & 17.8 & \textcolor{red}{\(\downarrow\)-3.01} \\

&
& 22/10 & 20.5 & 25/10 & 20.65 & 20.9 & \textcolor{green}{\(\uparrow\)+0.15} & 05/11 & 20.44 & 20.1 & \textcolor{red}{\(\downarrow\)-6.25} & 21/12 & 21.07 & 17.8 & \textcolor{green}{\(\uparrow\)+2.65} \\
\midrule



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ===================== FPT ======================
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\multirow{4}{*}{\textbf{FPT}} 
& \textbf{Hierarchical}
& 01/09 & 101.6 & 04/09 & 104.66 & 105 & \textcolor{green}{\(\uparrow\)+1.40} & 15/09 & 101.96 & 101.9 & \textcolor{red}{\(\downarrow\)-4.17} & 31/10 & 103.27 & 103.9 & \textcolor{green}{\(\uparrow\)+1.67} \\

&
& 16/10 & 89.8 & 19/10 & 89.40 & 88.1 & \textcolor{red}{\(\downarrow\)-2.73} & 30/10 & 89.93 & 102.7 & \textcolor{red}{\(\downarrow\)-13.38} & 15/12 & 91.24 & 93.8 & \textcolor{green}{\(\uparrow\)+1.67} \\

&
& 21/10 & 93 & 24/10 & 92.33 & 97.7 & \textcolor{green}{\(\uparrow\)+2.33} & 04/11 & 93.26 & 103.3 & \textcolor{green}{\(\uparrow\)+7.50} & 20/12 & 94.66 & 93.9 &\textcolor{green}{\(\uparrow\)+3.66}\\

&
& 22/10 & 97 & 25/10 & 96.54 & 97.7 & \textcolor{red}{\(\downarrow\)-4.20} & 05/11 & 97.43 & 100.9 & \textcolor{green}{\(\uparrow\)+3.30} & 21/12 & 98.91 & 93.9 & \textcolor{red}{\(\downarrow\)-15.02} \\
\midrule


\multirow{4}{*}{\textbf{FPT}} 
& \textbf{Round Robin}
& 01/09 & 101.6 & 04/09 & 101.29 & 105 & \textcolor{green}{\(\uparrow\)+0.58} & 15/09 & 102.08 & 101.9 & \textcolor{red}{\(\downarrow\)-3.76} & 31/10 & 103.92 & 103.9 & \textcolor{green}{\(\uparrow\)+0.37} \\

&
& 16/10 & 89.8 & 19/10 & 89.32 & 88.1 & \textcolor{red}{\(\downarrow\)-2.36} & 30/10 & 89.95 & 102.7 & \textcolor{red}{\(\downarrow\)-11.42} & 15/12 & 90.85 & 93.8 & \textcolor{green}{\(\uparrow\)+3.1} \\

&
& 21/10 & 93 & 24/10 & 92.67 & 97.7 & \textcolor{green}{\(\uparrow\)+1.70} & 04/11 & 93.04 & 103.3 & \textcolor{green}{\(\uparrow\)+8.05} & 20/12 & 94.19 & 93.9 & \textcolor{green}{\(\uparrow\)+3.58} \\

&
& 22/10 & 97 & 25/10 & 96.67 & 97.7 & \textcolor{red}{\(\downarrow\)-4.02} & 05/11 & 97.51 & 100.9 & \textcolor{green}{\(\uparrow\)+7.30} & 21/12 & 96.55 & 93.9 & \textcolor{red}{\(\downarrow\)-15.02} \\
\midrule



\multirow{4}{*}{\textbf{FPT}} 
& \textbf{Ensemble}
& 01/09 & 101.6 & 04/09 & 101.71 & 105 & \textcolor{green}{\(\uparrow\)+1.40} & 15/09 & 101.60 & 101.9 & \textcolor{red}{\(\downarrow\)-1.70} & 31/10 & 103.01 & 103.9 & \textcolor{green}{\(\uparrow\)+1.13} \\

&
& 16/10 & 89.8 & 19/10 & 89.30 & 88.1 & \textcolor{green}{\(\uparrow\)-0.45} & 30/10 & 89.98 & 102.7 & \textcolor{red}{\(\downarrow\)-11.53} & 15/12 & 91.14 & 93.8 & \textcolor{green}{\(\uparrow\)+1.56} \\

&
& 21/10 & 93 & 24/10 & 92.49 & 97.7 & \textcolor{green}{\(\uparrow\)+2.56} & 04/11 & 93.10 & 103.3 & \textcolor{green}{\(\uparrow\)+7.04} & 20/12 & 94.25 & 93.9 & \textcolor{green}{\(\uparrow\)+3.32} \\

&
& 22/10 & 97 & 25/10 & 96.48 & 97.7 & \textcolor{green}{\(\uparrow\)+1.11} & 05/11 & 97.25 & 100.9 & \textcolor{green}{\(\uparrow\)+2.97} & 21/11 & 98.46 & 93.9 & \textcolor{red}{\(\downarrow\)-11.43} \\
\midrule




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ===================== VCB ======================
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\multirow{4}{*}{\textbf{VCB}} 
& \textbf{Hierarchical}
& 30/08 & 68.6 & 02/09 & 69.12 & 68.6 & \textcolor{yellow}{0.06} & 13/09 & 68.64 & 65.8 & \textcolor{red}{\(\downarrow\)-2.72} & 29/10 & 69.15 & 60.7 & \textcolor{green}{\(\uparrow\)+6.9} \\

&
& 16/10 & 62.9 & 19/10 & 63.21 & 61.9 & \textcolor{red}{\(\downarrow\)-1.39} & 30/10 & 61.92 & 60.6 & \textcolor{red}{\(\downarrow\)-3.69} & 15/12 & 64.33 & 56.8 & \textcolor{red}{\(\downarrow\)-7.67} \\

&
& 21/10 & 59.3 & 24/10 & 59.59 & 59.5 & \textcolor{green}{\(\uparrow\)-2.18} & 04/11 & 61.77 & 60.1 & \textcolor{green}{\(\uparrow\)+2.27} & 20/12 & 55.62 & 57.5 & \textcolor{green}{\(\uparrow\)+1.0} \\

&
& 22/10 & 59.6 & 25/10 & 59.88 & 59.5 & \textcolor{red}{\(\downarrow\)-1.71} & 05/11 & 60.20 & 60.8 & \textcolor{green}{\(\uparrow\)+1.57} & 21/12 & 60.66 & 57.5 & \textcolor{red}{\(\downarrow\)-5.26} \\
\midrule


\multirow{4}{*}{\textbf{VCB}} 
& \textbf{Round Robin}
& 30/08 & 68.6 & 02/09 & 68.50 & 68.6 & \textcolor{yellow}{0.14} & 13/09 & 68.83 & 65.8 & \textcolor{red}{\(\downarrow\)-3.10} & 29/10 & 68.44 & 60.7 & \textcolor{red}{\(\downarrow\)-17.11} \\

&
& 16/10 & 62.9 & 19/10 & 62.51 & 61.9 & \textcolor{green}{\(\uparrow\)+0.61} & 30/10 & 64.03 & 60.6 & \textcolor{red}{\(\downarrow\)-3.43} & 15/12 & 64.57 & 56.8 & \textcolor{red}{\(\downarrow\)-7.77} \\

&
& 21/10 & 59.3 & 24/10 & 59.45 & 59.5 & \textcolor{green}{\(\uparrow\)+1.65} & 04/11 & 59.68 & 60.1 & \textcolor{green}{\(\uparrow\)+2.27} & 20/12 & 60.29 & 57.5 & \textcolor{red}{\(\downarrow\)-5.5} \\

&
& 22/10 & 59.6 & 25/10 & 59.79 & 59.5 & \textcolor{red}{\(\downarrow\)-1.96} & 05/11 & 60.17 & 60.8 & \textcolor{green}{\(\uparrow\)+1.16} & 21/12 & 59.55 & 57.5 & \textcolor{red}{\(\downarrow\)-4.95} \\
\midrule

\multirow{4}{*}{\textbf{VCB}} 
& \textbf{Ensemble}
& 30/08 & 68.6 & 02/09 & 68.38 & 68.6 & \textcolor{yellow}{0.96} & 13/09 & 68.67 & 65.8 & \textcolor{red}{\(\downarrow\)-3.05} & 29/10 & 69.38 & 60.7 & \textcolor{green}{\(\uparrow\)+7.2} \\

&
& 16/10 & 62.9 & 19/10 & 63.12 & 61.9 & \textcolor{red}{\(\downarrow\)-1.75} & 30/10 & 63.35 & 60.6 & \textcolor{red}{\(\downarrow\)-3.74} & 15/12 & 59.44 & 56.8 & \textcolor{green}{\(\uparrow\)+5.14} \\

&
& 21/10 & 59.3 & 24/10 & 59.53 & 59.5 & \textcolor{green}{\(\uparrow\)+3.08} & 04/11 & 59.76 & 60.1 & \textcolor{green}{\(\uparrow\)+2.26} & 20/12 & 60.43 & 57.5 & \textcolor{red}{\(\downarrow\)-5.51} \\

&
& 22/10 & 59.6 & 25/10 & 59.86 & 59.5 & \textcolor{red}{\(\downarrow\)-1.38} & 05/11 & 63.78 & 60.8 & \textcolor{green}{\(\uparrow\)+0.98} & 21/12 & 60.74 & 57.5 & \textcolor{red}{\(\downarrow\)-4.79} \\
\midrule



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% ===================== VCS ======================
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\multirow{4}{*}{\textbf{VCS}} 
& \textbf{Hierarchical}
& 30/08 & 48.8 & 02/09 & 47.25 & 48.8 & \textcolor{yellow}{0.83} & 13/09 & 47.65 & 50 & \textcolor{green}{\(\uparrow\)+0.20} & 29/10 & 48.33 & 47.6 & \textcolor{red}{\(\downarrow\)-2.91} \\

&
& 16/10 & 47.2 & 19/10 & 45.68 & 46.8 & \textcolor{red}{\(\downarrow\)-1.06} & 30/10 & 46.05 & 47.4 & \textcolor{green}{\(\uparrow\)+2.34} & 15/12 & 46.90 & 46.5 & \textcolor{green}{\(\uparrow\)+4.37} \\

&
& 21/10 & 45.5 & 24/10 & 44.01 & 46.2 & \textcolor{green}{\(\uparrow\)+0.92} & 04/11 & 44.43 & 47.1 & \textcolor{green}{\(\uparrow\)+0.04} & 20/12 & 44.98 & 43 & \textcolor{red}{\(\downarrow\)-4.66} \\

&
& 22/10 & 45.5 & 25/10 & 44.03 & 46.2 & \textcolor{green}{\(\uparrow\)+0.18} & 05/11 & 44.46 & 46.9 & \textcolor{green}{\(\uparrow\)+0.37} & 21/12 & 45.21 & 43 & \textcolor{red}{\(\downarrow\)-4.56} \\
\midrule


\multirow{4}{*}{\textbf{VCS}} 
& \textbf{Round Robin}
& 30/08 & 48.8 & 02/09 & 47.18 & 48.8 & \textcolor{yellow}{0.18} & 13/09 & 47.42 & 50 & \textcolor{red}{\(\downarrow\)-3.80} & 29/10 & 48.32 & 47.6 & \textcolor{red}{\(\downarrow\)-2.91} \\

&
& 16/10 & 47.2 & 19/10 & 45.69 & 46.8 & \textcolor{red}{\(\downarrow\)-0.75} & 30/10 & 46.10 & 47.4 & \textcolor{green}{\(\uparrow\)+0.46} & 15/12 & 46.56 & 46.5 & \textcolor{green}{\(\uparrow\)+1} \\

&
& 21/10 & 45.5 & 24/10 & 43.98 & 46.2 & \textcolor{green}{\(\uparrow\)+1.23} & 04/11 & 47.22 & 47.1 & \textcolor{green}{\(\uparrow\)+0.98} & 20/12 & 44.71 & 43 & \textcolor{green}{\(\uparrow\)+1.16} \\

&
& 22/10 & 45.5 & 25/10 & 43.98 & 46.2 & \textcolor{green}{\(\uparrow\)+0.72} & 05/11 & 44.28 & 46.9 & \textcolor{green}{\(\uparrow\)+0.30} & 21/12 & 44.78 & 43 & \textcolor{green}{\(\uparrow\)+1.15} \\
\midrule



\multirow{4}{*}{\textbf{VCS}} 
& \textbf{Ensemble}
& 30/08 & 48.8 & 02/09 & 47.19 & 48.8 & \textcolor{yellow}{0.14} & 13/09 & 47.47 & 50 & \textcolor{green}{\(\uparrow\)+0.80} & 29/10 & 48.18 & 47.6 & \textcolor{red}{\(\downarrow\)-2.05} \\

&
& 16/10 & 47.2 & 19/10 & 45.63 & 46.8 & \textcolor{green}{\(\uparrow\)+1.32} & 30/10 & 46.03 & 47.4 & \textcolor{green}{\(\uparrow\)+1.66} & 15/12 & 46.79 & 46.5 & \textcolor{green}{\(\uparrow\)-5.17} \\

&
& 21/10 & 45.5 & 24/10 & 43.97 & 46.2 & \textcolor{green}{\(\uparrow\)+0.75} & 04/11 & 44.25 & 47.1 & \textcolor{green}{\(\uparrow\)+0.32} & 20/12 & 45.02 & 43 & \textcolor{red}{\(\downarrow\)-4.43} \\

&
& 22/10 & 45.5 & 25/10 & 45.95 & 46.2 & \textcolor{green}{\(\uparrow\)+0.50} & 05/11 & 47.55 & 46.9 & \textcolor{green}{\(\uparrow\)+0.24} & 21/12 & 44.89 & 43 & \textcolor{red}{\(\downarrow\)-3.53}  \\


\bottomrule
\end{tabular}
\end{table*}

\newpage
\twocolumn

\subsubsection{Short-term Performance}
\begin{table}[!h]
\centering
\caption{Average Short-term Performance of Prediction Architectures Across Stocks (LLM: Llama)}      
\resizebox{\columnwidth}{!}{
\begin{tabular}{c c c c c}
\hline
\textbf{Stock} & \textbf{Architecture} & \textbf{Avg MAE} & \textbf{Avg RMSE} & \textbf{Avg MAPE} \\
\hline

\multirow{3}{*}{\textbf{DXG}}
& RoundRobin      & \textbf{0.51} & \textbf{0.61} & \textbf{2.3\%} \\
& Hierarchical    & 0.54 & 0.68 & 2.4\% \\
& Ensemble Voting & 0.55 & 0.69 & 2.5\% \\
\hline

\multirow{3}{*}{\textbf{FPT}}
& RoundRobin      & \textbf{2.79} & \textbf{3.27} & \textbf{2.8\%} \\
& Hierarchical    & 2.82 & 3.29 & 2.9\% \\
& Ensemble Voting & 2.90 & 3.38 & 2.9\% \\
\hline

\multirow{3}{*}{\textbf{VCB}}
& RoundRobin      & \textbf{0.51} & \textbf{0.70} & \textbf{0.8\%} \\
& Hierarchical    & 1.43 & 2.06 & 2.4\% \\
& Ensemble Voting & 9.46 & 13.40 & 14.4\% \\
\hline

\multirow{3}{*}{\textbf{VCS}}
& Hierarchical    & \textbf{1.73} & \textbf{1.79} & \textbf{3.7\%} \\
& RoundRobin      & 1.80 & 1.85 & 3.8\% \\
& Ensemble Voting & 2.26 & 2.40 & 4.8\% \\
\hline

\end{tabular}
}
\end{table}

\subsubsection{Medium-term Performance}
\begin{table}[!h]
\centering
\caption{Average Medium-term Performance of Prediction Architectures Across Stocks (LLM: Llama)}     
\resizebox{\columnwidth}{!}{
\begin{tabular}{c c c c c}
\hline
\textbf{Stock} & \textbf{Architecture} & \textbf{Avg MAE} & \textbf{Avg RMSE} & \textbf{Avg MAPE} \\
\hline

\multirow{3}{*}{\textbf{DXG}}
& Ensemble Voting & \textbf{0.82} & \textbf{0.97} & \textbf{3.8\%} \\
& Hierarchical    & 0.84 & 0.99 & 3.9\% \\
& RoundRobin      & 0.87 & 1.07 & 4.1\% \\
\hline

\multirow{3}{*}{\textbf{FPT}}
& RoundRobin      & \textbf{6.64} & \textbf{8.32} & \textbf{6.5\%} \\
& Hierarchical    & 6.66 & 8.33 & 6.5\% \\
& Ensemble Voting & 7.15 & 8.48 & 7.0\% \\
\hline

\multirow{3}{*}{\textbf{VCB}}
& Hierarchical    & \textbf{1.16} & \textbf{1.58} & \textbf{1.8\%} \\
& Ensemble Voting & 1.63 & 2.01 & 2.6\% \\
& RoundRobin      & 1.67 & 2.23 & 2.7\% \\
\hline

\multirow{3}{*}{\textbf{VCS}}
& RoundRobin      & \textbf{2.22} & \textbf{2.27} & \textbf{4.6\%} \\
& Hierarchical    & 2.23 & 2.30 & 4.7\% \\
& Ensemble Voting & 2.30 & 2.37 & 4.8\% \\
\hline

\end{tabular}
}
\end{table}

\subsubsection{Long-term Performance}
\begin{table}[!h]
\centering
\caption{Average Long-term Performance of Prediction Architectures Across Stocks (LLM: Llama)}       
\resizebox{\columnwidth}{!}{
\begin{tabular}{c c c c c}
\hline
\textbf{Stock} & \textbf{Architecture} & \textbf{Avg MAE} & \textbf{Avg RMSE} & \textbf{Avg MAPE} \\
\hline

\multirow{3}{*}{\textbf{DXG}}
& Ensemble Voting & \textbf{3.89} & \textbf{4.28} & \textbf{22.2\%} \\
& Hierarchical    & 4.07 & 4.45 & 23.2\% \\
& RoundRobin      & 4.27 & 4.67 & 24.3\% \\
\hline

\multirow{3}{*}{\textbf{FPT}}
& Ensemble Voting & \textbf{2.06} & \textbf{2.73} & \textbf{2.2\%} \\
& Hierarchical    & 3.12 & 3.61 & 3.3\% \\
& RoundRobin      & 3.70 & 5.88 & 3.9\% \\
\hline

\multirow{3}{*}{\textbf{VCB}}
& Ensemble Voting & \textbf{5.95} & \textbf{6.45} & \textbf{10.2\%} \\
& Hierarchical    & 6.34 & 6.80 & 10.8\% \\
& RoundRobin      & 6.60 & 7.05 & 11.3\% \\
\hline

\multirow{3}{*}{\textbf{VCS}}
& RoundRobin      & \textbf{1.04} & \textbf{1.27} & \textbf{2.4\%} \\
& Ensemble Voting & 1.19 & 1.43 & 2.7\% \\
& Hierarchical    & 1.32 & 1.52 & 3.0\% \\
\hline

\end{tabular}
}
\end{table}

\subsubsection{Short-term Performance}
\begin{table}[!h]
\centering
\caption{Average Short-term Performance of Prediction Architectures Across Stocks (LLM: GPT-4)}      
\resizebox{\columnwidth}{!}{
\begin{tabular}{c c c c c}
\hline
\textbf{Stock} & \textbf{Architecture} & \textbf{Avg MAE} & \textbf{Avg RMSE} & \textbf{Avg MAPE} \\
\hline

\multirow{3}{*}{\textbf{DXG}}
& Hierarchical    & \textbf{0.50} & \textbf{0.62} & \textbf{2.3\%} \\
& RoundRobin      & 0.50 & 0.60 & 2.3\% \\
& Ensemble Voting & 0.51 & 0.64 & 2.3\% \\
\hline

\multirow{3}{*}{\textbf{FPT}}
& Hierarchical    & \textbf{2.04} & \textbf{2.83} & \textbf{2.1\%} \\
& Ensemble Voting & 2.73 & 3.20 & 2.8\% \\
& RoundRobin      & 2.75 & 3.23 & 2.8\% \\
\hline

\multirow{3}{*}{\textbf{VCB}}
& RoundRobin      & \textbf{0.26} & \textbf{0.34} & \textbf{0.4\%} \\
& Ensemble Voting & 0.46 & 0.65 & 0.7\% \\
& Hierarchical    & 0.58 & 0.73 & 0.9\% \\
\hline

\multirow{3}{*}{\textbf{VCS}}
& Ensemble Voting & \textbf{1.31} & \textbf{1.50} & \textbf{2.8\%} \\
& Hierarchical    & 1.76 & 1.81 & 3.8\% \\
& RoundRobin      & 1.79 & 1.85 & 3.8\% \\
\hline

\end{tabular}
}
\end{table}

\subsubsection{Medium-term Performance}
\begin{table}[!h]
\centering
\caption{Average Medium-term Performance of Prediction Architectures Across Stocks (LLM: GPT-4)}     
\resizebox{\columnwidth}{!}{
\begin{tabular}{c c c c c}
\hline
\textbf{Stock} & \textbf{Architecture} & \textbf{Avg MAE} & \textbf{Avg RMSE} & \textbf{Avg MAPE} \\
\hline

\multirow{3}{*}{\textbf{DXG}}
& Ensemble Voting & \textbf{0.76} & \textbf{0.95} & \textbf{3.5\%} \\
& Hierarchical    & 0.86 & 1.03 & 4.0\% \\
& RoundRobin      & 0.88 & 1.08 & 4.1\% \\
\hline

\multirow{3}{*}{\textbf{FPT}}
& Hierarchical    & \textbf{6.58} & \textbf{8.31} & \textbf{6.4\%} \\
& RoundRobin      & 6.64 & 8.36 & 6.5\% \\
& Ensemble Voting & 6.72 & 8.36 & 6.5\% \\
\hline

\multirow{3}{*}{\textbf{VCB}}
& Hierarchical    & \textbf{1.61} & \textbf{1.80} & \textbf{2.6\%} \\
& RoundRobin      & 1.88 & 2.32 & 3.0\% \\
& Ensemble Voting & 2.24 & 2.49 & 3.6\% \\
\hline

\multirow{3}{*}{\textbf{VCS}}
& RoundRobin      & \textbf{1.65} & \textbf{1.95} & \textbf{3.4\%} \\
& Ensemble Voting & 1.85 & 2.05 & 3.8\% \\
& Hierarchical    & 2.20 & 2.26 & 4.6\% \\
\hline

\end{tabular}
}
\end{table}

\subsubsection{Long-term Performance}
\begin{table}[!h]
\centering
\caption{Average Long-term Performance of Prediction Architectures Across Stocks (LLM: GPT-4)}       
\resizebox{\columnwidth}{!}{
\begin{tabular}{c c c c c}
\hline
\textbf{Stock} & \textbf{Architecture} & \textbf{Avg MAE} & \textbf{Avg RMSE} & \textbf{Avg MAPE} \\
\hline

\multirow{3}{*}{\textbf{DXG}}
& Hierarchical    & \textbf{3.83} & \textbf{4.29} & \textbf{21.8\%} \\
& Ensemble Voting & 3.86 & 4.29 & 22.1\% \\
& RoundRobin      & 4.19 & 4.63 & 23.9\% \\
\hline

\multirow{3}{*}{\textbf{FPT}}
& RoundRobin      & \textbf{1.48} & \textbf{1.99} & \textbf{1.6\%} \\
& Ensemble Voting & 2.11 & 2.68 & 2.2\% \\
& Hierarchical    & 2.24 & 2.86 & 2.4\% \\
\hline

\multirow{3}{*}{\textbf{VCB}}
& Ensemble Voting & \textbf{4.37} & \textbf{5.03} & \textbf{7.4\%} \\
& RoundRobin      & 5.09 & 5.75 & 8.7\% \\
& Hierarchical    & 5.26 & 5.95 & 9.0\% \\
\hline

\multirow{3}{*}{\textbf{VCS}}
& RoundRobin      & \textbf{1.07} & \textbf{1.29} & \textbf{2.4\%} \\
& Ensemble Voting & 1.20 & 1.42 & 2.7\% \\
& Hierarchical    & 1.33 & 1.54 & 3.0\% \\
\hline

\end{tabular}
}
\end{table}
