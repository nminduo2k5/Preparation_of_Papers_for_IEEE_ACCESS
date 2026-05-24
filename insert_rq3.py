import os
import re

access_path = r"k:\1\Preparation_of_Papers_for_IEEE_ACCESS\access.tex"
table_path = r"k:\1\Preparation_of_Papers_for_IEEE_ACCESS\rq3_table.tex"

with open(table_path, 'r', encoding='utf-8') as f:
    table_content = f.read()

analysis_text = r'''
To address RQ3, we evaluate whether the proposed Multi-Agent System (MAS) empirically outperforms traditional deep learning approaches and single-agent LLM baselines. Table~\ref{tab:rq3_baselines_vs_mas} presents a comprehensive macro-level comparison across all 12 evaluated stocks, contrasting traditional time-series models (LSTM and Transformer) against single-agent LLMs (Baseline) and multi-agent coordination architectures (Hierarchical, Round Robin, and Ensemble) driven by Llama-3.1-8B, GPT-4o, and Gemini 2.0 Flash.

\subsection{Limitations of Traditional Baselines}
The empirical results expose significant limitations in traditional quantitative models when applied to Vietnam's volatile, retail-driven stock market. Both the LSTM and Transformer baselines exhibit high error rates across all forecasting horizons. Specifically, the LSTM baseline records a Mean Absolute Percentage Error (MAPE) of 14.63\% in the short-term, degrading to 15.33\% in the medium-term. The Transformer baseline performs similarly, with MAPE values ranging from 13.97\% (short-term) to a peak of 15.45\% (long-term). These substantial errors highlight the inability of pure historical price-sequence models to adapt to abrupt, sentiment-driven market fluctuations and complex exogenous shocks.

Similarly, deploying LLMs as solitary "Single-Agent" forecasters (denoted as the Baseline rows for LLAMA, GPT, and GEMINI) fails to yield meaningful improvements over LSTM or Transformer. For instance, the Gemini Single-Agent Baseline yields a short-term MAPE of 15.17\% and a long-term MAPE of 15.33\%, mirroring the struggles of traditional deep learning models. This indicates that raw reasoning capability, when isolated, is insufficient to overcome financial market noise.

\subsection{Superiority of Multi-Agent Architectures}
In stark contrast, transitioning from single-agent baselines to coordinated multi-agent architectures results in a dramatic reduction in forecasting error. The integration of specialized roles (e.g., Sentiment Agent, Technical Agent, Fundamental Agent) coupled with coordination mechanisms effectively filters noise and synthesizes heterogeneous data streams.

\textbf{Massive Error Reduction:} The \textit{Ensemble} and \textit{Hierarchical} architectures consistently deliver the lowest errors. For example, using Gemini 2.0 Flash as the core LLM, the \textit{Ensemble} architecture achieves an extraordinary short-term MAPE of just 2.92\% (an approximate 80\% reduction in error compared to the LSTM baseline of 14.63\%). Even at the extended 60-day horizon, the Gemini Ensemble maintains a robust MAPE of 5.91\%, vastly outperforming the Transformer baseline's 15.45\%.

\textbf{Consistency Across LLMs:} This structural superiority is not limited to a single LLM. When powered by GPT-4o, the Ensemble architecture reduces medium-term MAPE to 4.75\% (compared to GPT Baseline's 15.55\%). Similarly, Llama-3.1-8B in a Hierarchical setup achieves a short-term MAPE of 3.20\% (versus Llama Baseline's 14.63\%). The Multi-Agent framework consistently transforms highly inaccurate single-agent outputs into highly precise, actionable forecasts.

\subsection{Conclusion for RQ3}
The evidence overwhelmingly supports the superiority of the proposed Multi-Agent framework over traditional deep learning baselines and solitary LLM approaches. By embedding deliberative reasoning, cross-validation, and consensus-building among specialized agents, the MAS successfully bridges the gap between qualitative market sentiment and quantitative price dynamics. Traditional models (LSTM/Transformer) are constrained by their reliance on historical numerical patterns, rendering them fragile in emerging markets like Vietnam. Ultimately, the Multi-Agent approach is not merely an incremental improvement, but a paradigm shift that reduces forecasting errors by up to 80\%, proving its empirical effectiveness.
'''

with open(access_path, 'r', encoding='utf-8') as f:
    access_content = f.read()

pattern = r"(\\section\{RQ3: Multi-Agent vs\. Traditional Baselines\}).*?(\\section\{Discussion\})"

new_access_content = re.sub(
    pattern, 
    lambda m: m.group(1) + "\n\n" + analysis_text + "\n\n" + table_content + "\n\n" + m.group(2), 
    access_content, 
    flags=re.DOTALL
)

with open(access_path, 'w', encoding='utf-8') as f:
    f.write(new_access_content)

print("Insertion complete.")
