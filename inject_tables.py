import re

with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\access.tex', 'r', encoding='utf-8') as f:
    content = f.read()

with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\table1_generated.tex', 'r', encoding='utf-8') as f:
    t1 = f.read()
    
with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\table2_generated.tex', 'r', encoding='utf-8') as f:
    t2 = f.read()

with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\table3_generated.tex', 'r', encoding='utf-8') as f:
    t3 = f.read()

# Replace Table 1
pattern_t1 = r'\\begin\{table\*\}.*?\\label\{tab:aggregated_performance\}.*?\\end\{table\*\}'
content = re.sub(pattern_t1, lambda m: t1, content, flags=re.DOTALL)

# Replace Table 2
pattern_t2 = r'\\begin\{table\*\}.*?\\label\{tab:aggregate_performance_summary\}.*?\\end\{table\*\}'
content = re.sub(pattern_t2, lambda m: t2, content, flags=re.DOTALL)

# Replace Table 3
pattern_t3 = r'\\begin\{table\}.*?\\label\{tab:llm_aggregate_comparison\}.*?\\end\{table\}'
content = re.sub(pattern_t3, lambda m: t3, content, flags=re.DOTALL)

with open(r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS\access.tex', 'w', encoding='utf-8') as f:
    f.write(content)

print("Tables injected successfully into access.tex.")
