import csv
import numpy as np

csv_path = r"k:\1\Preparation_of_Papers_for_IEEE_ACCESS\metrics_summary.csv"

llms = ['LLAMA', 'GPT', 'GEMINI']
horizons = ['Short-term', 'Medium-term', 'Long-term']
metrics = ['MAE', 'MAPE', 'RMSE']

# data[llm][horizon][metric] = list of values
data = {llm: {h: {m: [] for m in metrics} for h in horizons} for llm in llms}

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        model = row['Model']
        arch = row['Architecture']
        horizon = row['Horizon']
        
        if model in llms:
            # According to the old table, it was "Averaged Over All Stocks and Coordination Architectures"
            # Since metrics_summary already averaged over stocks, we now average over architectures
            # Including Baseline, Hierarchical, Round Robin, Ensemble
            data[model][horizon]['MAE'].append(float(row['MAE']))
            data[model][horizon]['MAPE'].append(float(row['MAPE (%)']))
            data[model][horizon]['RMSE'].append(float(row['RMSE']))

# Calculate averages
table3_results = {llm: {h: {} for h in horizons} for llm in llms}
for llm in llms:
    for h in horizons:
        table3_results[llm][h]['MAE'] = np.mean(data[llm][h]['MAE'])
        table3_results[llm][h]['MAPE'] = np.mean(data[llm][h]['MAPE'])
        table3_results[llm][h]['RMSE'] = np.mean(data[llm][h]['RMSE'])

# Also calculate Overall Average
for llm in llms:
    all_mae = []
    all_mape = []
    all_rmse = []
    for h in horizons:
        all_mae.extend(data[llm][h]['MAE'])
        all_mape.extend(data[llm][h]['MAPE'])
        all_rmse.extend(data[llm][h]['RMSE'])
    
    table3_results[llm]['Overall'] = {
        'MAE': np.mean(all_mae),
        'MAPE': np.mean(all_mape),
        'RMSE': np.mean(all_rmse)
    }

# Print the results to see
print("Table 3: Aggregate Performance Comparison Across Foundation LLM Families")
print(f"{'Horizon':<15} | {'Metric':<10} | {'LLAMA':<10} | {'GPT':<10} | {'GEMINI':<10}")
print("-" * 65)

for h in horizons + ['Overall']:
    for m in metrics:
        llama_val = table3_results['LLAMA'][h][m]
        gpt_val = table3_results['GPT'][h][m]
        gemini_val = table3_results['GEMINI'][h][m]
        print(f"{h:<15} | {m:<10} | {llama_val:.4f}     | {gpt_val:.4f}     | {gemini_val:.4f}")
    print("-" * 65)

