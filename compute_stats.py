import re

# Read access.tex
with open("k:/1/Preparation_of_Papers_for_IEEE_ACCESS/access.tex", "r", encoding="utf-8") as f:
    content = f.read()

# Find label
start_match = re.search(r"\\label\{tab:full_performance_all\}", content)
if not start_match:
    print("Table not found!")
    exit(1)

table_text = content[start_match.start():]
end_match = re.search(r"\\end\{longtable\}", table_text)
if end_match:
    table_text = table_text[:end_match.end()]

lines = table_text.split("\n")
rows = []
current_horizon = "Short-term"
current_stock = None

STOCKS = ["DXG", "FPT", "VCB", "VCS", "HPG", "TCB", "VHM", "MWG", "CMG", "KDH", "DGC", "MBB"]

for i, line in enumerate(lines):
    line = line.strip()
    if not line or line.startswith("%"):
        continue
    
    # Track horizon changes via comments or line content
    if "SHORT-TERM" in line.upper():
        current_horizon = "Short-term"
    elif "MEDIUM-TERM" in line.upper():
        current_horizon = "Medium-term"
    elif "LONG-TERM" in line.upper():
        current_horizon = "Long-term"
        
    # Check if this line is an actual data row by ampersand count
    if line.count("&") >= 15:
        parts = [p.strip() for p in line.split("&")]
        def clean_val(val):
            val = re.sub(r"\\cellcolor\{[a-zA-Z]+\}", "", val)
            val = re.sub(r"\\textbf\{([^\}]+)\}", r"\1", val)
            val = val.replace("\\\\", "").strip()
            return val
        
        parts = [clean_val(p) for p in parts]
        
        # Parse horizon
        idx = 0
        horiz_part = parts[0]
        if "short" in horiz_part.lower():
            current_horizon = "Short-term"
            idx = 1
        elif "medium" in horiz_part.lower():
            current_horizon = "Medium-term"
            idx = 1
        elif "long" in horiz_part.lower():
            current_horizon = "Long-term"
            idx = 1
        elif horiz_part == "":
            idx = 1
            
        # Parse stock
        stock_part = parts[idx]
        found_stock = False
        for s in STOCKS:
            if s in stock_part:
                current_stock = s
                found_stock = True
                break
        if found_stock or stock_part in STOCKS:
            idx += 1
        elif stock_part == "":
            idx += 1
            
        if idx < len(parts):
            arch = parts[idx]
            data_parts = parts[idx+1:]
            
            if data_parts:
                data_parts[-1] = data_parts[-1].replace("\\\\", "").strip()
                
            if len(data_parts) >= 18:
                rows.append({
                    "horizon": current_horizon,
                    "stock": current_stock,
                    "arch": arch,
                    "data": data_parts[:18]
                })

def parse_val(val):
    val = val.replace("%", "").strip()
    if not val:
        return None
    try:
        return float(val)
    except ValueError:
        return None

# Now, let's compute aggregate statistics for each LLM:
# For each LLM, we want to compute the average MAE, RMSE, and MAPE across all rows.
# There are 3 LLMs: Llama, GPT, Gemini.
# Under LSTM:
#   Llama: MAE=col0, RMSE=col1, MAPE=col2
#   GPT: MAE=col3, RMSE=col4, MAPE=col5
#   Gemini: MAE=col6, RMSE=col7, MAPE=col8
# Under Transformer:
#   Llama: MAE=col9, RMSE=col10, MAPE=col11
#   GPT: MAE=col12, RMSE=col13, MAPE=col14
#   Gemini: MAE=col15, RMSE=col16, MAPE=col17

# We can aggregate by (LLM, Framework) or just by (LLM) overall.
# Let's aggregate by LLM and Horizon! This would make a beautiful, detailed table:
# Rows: Horizon (Short-term, Medium-term, Long-term, Overall)
# Columns: Metric (MAE, RMSE, MAPE) for each of the 3 LLMs (Llama-3.1-8B, GPT-4o, Gemini 2.0 Flash)

stats = {}
for h in ["Short-term", "Medium-term", "Long-term", "Overall"]:
    stats[h] = {
        "Llama": {"MAE": [], "RMSE": [], "MAPE": []},
        "GPT": {"MAE": [], "RMSE": [], "MAPE": []},
        "Gemini": {"MAE": [], "RMSE": [], "MAPE": []}
    }

for r in rows:
    h = r["horizon"]
    
    # Extract values
    l_mae_lstm = parse_val(r["data"][0])
    l_rmse_lstm = parse_val(r["data"][1])
    l_mape_lstm = parse_val(r["data"][2])
    
    g_mae_lstm = parse_val(r["data"][3])
    g_rmse_lstm = parse_val(r["data"][4])
    g_mape_lstm = parse_val(r["data"][5])
    
    gem_mae_lstm = parse_val(r["data"][6])
    gem_rmse_lstm = parse_val(r["data"][7])
    gem_mape_lstm = parse_val(r["data"][8])
    
    l_mae_trans = parse_val(r["data"][9])
    l_rmse_trans = parse_val(r["data"][10])
    l_mape_trans = parse_val(r["data"][11])
    
    g_mae_trans = parse_val(r["data"][12])
    g_rmse_trans = parse_val(r["data"][13])
    g_mape_trans = parse_val(r["data"][14])
    
    gem_mae_trans = parse_val(r["data"][15])
    gem_rmse_trans = parse_val(r["data"][16])
    gem_mape_trans = parse_val(r["data"][17])
    
    # Let's combine LSTM and Transformer or average them?
    # Usually we want the average across all frameworks.
    # Let's add them to the lists:
    for h_key in [h, "Overall"]:
        # Llama
        if l_mae_lstm is not None: stats[h_key]["Llama"]["MAE"].append(l_mae_lstm)
        if l_rmse_lstm is not None: stats[h_key]["Llama"]["RMSE"].append(l_rmse_lstm)
        if l_mape_lstm is not None: stats[h_key]["Llama"]["MAPE"].append(l_mape_lstm)
        if l_mae_trans is not None: stats[h_key]["Llama"]["MAE"].append(l_mae_trans)
        if l_rmse_trans is not None: stats[h_key]["Llama"]["RMSE"].append(l_rmse_trans)
        if l_mape_trans is not None: stats[h_key]["Llama"]["MAPE"].append(l_mape_trans)
        
        # GPT
        if g_mae_lstm is not None: stats[h_key]["GPT"]["MAE"].append(g_mae_lstm)
        if g_rmse_lstm is not None: stats[h_key]["GPT"]["RMSE"].append(g_rmse_lstm)
        if g_mape_lstm is not None: stats[h_key]["GPT"]["MAPE"].append(g_mape_lstm)
        if g_mae_trans is not None: stats[h_key]["GPT"]["MAE"].append(g_mae_trans)
        if g_rmse_trans is not None: stats[h_key]["GPT"]["RMSE"].append(g_rmse_trans)
        if g_mape_trans is not None: stats[h_key]["GPT"]["MAPE"].append(g_mape_trans)
        
        # Gemini
        if gem_mae_lstm is not None: stats[h_key]["Gemini"]["MAE"].append(gem_mae_lstm)
        if gem_rmse_lstm is not None: stats[h_key]["Gemini"]["RMSE"].append(gem_rmse_lstm)
        if gem_mape_lstm is not None: stats[h_key]["Gemini"]["MAPE"].append(gem_mape_lstm)
        if gem_mae_trans is not None: stats[h_key]["Gemini"]["MAE"].append(gem_mae_trans)
        if gem_rmse_trans is not None: stats[h_key]["Gemini"]["RMSE"].append(gem_rmse_trans)
        if gem_mape_trans is not None: stats[h_key]["Gemini"]["MAPE"].append(gem_mape_trans)

print("\n--- AGGREGATE RESULTS BY LLM AND HORIZON ---")
for h_key in ["Short-term", "Medium-term", "Long-term", "Overall"]:
    print(f"\nHorizon: {h_key}")
    for llm in ["Llama", "GPT", "Gemini"]:
        maes = stats[h_key][llm]["MAE"]
        rmses = stats[h_key][llm]["RMSE"]
        mapes = stats[h_key][llm]["MAPE"]
        avg_mae = sum(maes)/len(maes) if maes else 0
        avg_rmse = sum(rmses)/len(rmses) if rmses else 0
        avg_mape = sum(mapes)/len(mapes) if mapes else 0
        print(f"  {llm:<8} | MAE: {avg_mae:.4f} | RMSE: {avg_rmse:.4f} | MAPE: {avg_mape:.2f}%")
