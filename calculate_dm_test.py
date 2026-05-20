import numpy as np
import scipy.stats
import os

def dm_test(actual, pred1, pred2, h=1, crit="MSE"):
    """
    Computes the Diebold-Mariano test statistic.
    """
    e1 = np.array(actual) - np.array(pred1)
    e2 = np.array(actual) - np.array(pred2)
    
    if len(e1) != len(e2) or len(e1) == 0:
        return np.nan, np.nan
        
    if crit == "MSE":
        d = e1**2 - e2**2
    elif crit == "MAD":
        d = np.abs(e1) - np.abs(e2)
    elif crit == "MAPE":
        actual_arr = np.array(actual)
        actual_arr = np.where(actual_arr == 0, 1e-5, actual_arr)
        d = np.abs(e1 / actual_arr) - np.abs(e2 / actual_arr)
    else:
        raise ValueError("Invalid criterion")
        
    d_mean = np.mean(d)
    
    # Calculate autocovariance of d
    gamma = []
    for lag in range(0, h):
        if len(d) > lag:
            cov_val = np.cov(d[lag:], d[:len(d)-lag], ddof=0)[0, 1]
            gamma.append(cov_val)
        else:
            gamma.append(0)
            
    # Calculate V_d (variance of d_mean)
    V_d = gamma[0] + 2 * sum(gamma[1:])
    
    if V_d <= 1e-8:
        return 0, 1.0
        
    DM_stat = d_mean / np.sqrt(V_d / len(d))
    p_value = 2 * scipy.stats.norm.sf(abs(DM_stat))
    
    return DM_stat, p_value

def load_data_from_file(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return {}
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    globals_dict = {}
    try:
        exec(content, globals_dict)
        return globals_dict.get('data', {})
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return {}

def print_res(comp, horizon, dm, p):
    sig = ""
    if np.isnan(p):
        sig = "N/A"
    elif p < 0.01:
        sig = "***"
    elif p < 0.05:
        sig = "**"
    elif p < 0.1:
        sig = "*"
    print(f"{comp:<45} | {horizon:<12} | {dm:<15.4f} | {p:<10.4f} | {sig}")

def run_dm_tests():
    # Load all tables
    base_dir = r'k:\1\Preparation_of_Papers_for_IEEE_ACCESS'
    gemini_lstm = load_data_from_file(os.path.join(base_dir, 'update_table0.py'))
    gemini_trans = load_data_from_file(os.path.join(base_dir, 'update_table0_5.py'))
    
    gpt_lstm = load_data_from_file(os.path.join(base_dir, 'update_table0_1.py'))
    gpt_trans = load_data_from_file(os.path.join(base_dir, 'update_table1.py'))
    
    llama_lstm = load_data_from_file(os.path.join(base_dir, 'update_table2.py'))
    llama_trans = load_data_from_file(os.path.join(base_dir, 'update_table3.py'))

    stocks = ['CMG', 'DGC', 'DXG', 'FPT', 'HPG', 'KDH', 'MBB', 'MWG', 'TCB', 'VCB', 'VCS', 'VHM']
    horizons = ['Short', 'Medium', 'Long']
    architectures = ['Hierarchical', 'RoundRobin', 'Ensemble']
    
    for crit in ["MSE", "MAPE"]:
        print("\n" + "=" * 100)
        if crit == "MSE":
            print("TABLE 10: DIEBOLD-MARIANO TEST STATISTICS (MSE CRITERION)")
        else:
            print("ROBUSTNESS CHECK: DIEBOLD-MARIANO TEST STATISTICS (MAPE CRITERION)")
        print("=" * 100)
        print(f"{'Comparison Pair (Model 1 vs. Model 2)':<45} | {'Horizon':<12} | {'DM Statistic':<15} | {'p-value':<10} | {'Significance'}")
        print("-" * 100)
            
        # Transformer vs LSTM (Overall) - All
        act_overall = []
        pred_lstm_overall = []
        pred_trans_overall = []
        for lstm, trans in [(gemini_lstm, gemini_trans), (gpt_lstm, gpt_trans), (llama_lstm, llama_trans)]:
            for stock in stocks:
                for horizon in horizons:
                    for arch in architectures:
                        key = f"{stock}_{arch}_{horizon}"
                        if key in lstm and key in trans:
                            act_overall.extend(lstm[key]['actual'])
                            pred_lstm_overall.extend(lstm[key]['pred'])
                            pred_trans_overall.extend(trans[key]['pred'])
        dm_all, p_all = dm_test(act_overall, pred_trans_overall, pred_lstm_overall, h=1, crit=crit)
        print_res("Transformer vs. LSTM (Overall)", "All", dm_all, p_all)
        
        # Transformer vs LSTM (Overall) - Per Horizon
        for horizon in horizons:
            act_h = []
            pred_lstm_h = []
            pred_trans_h = []
            for lstm, trans in [(gemini_lstm, gemini_trans), (gpt_lstm, gpt_trans), (llama_lstm, llama_trans)]:
                for stock in stocks:
                    for arch in architectures:
                        key = f"{stock}_{arch}_{horizon}"
                        if key in lstm and key in trans:
                            act_h.extend(lstm[key]['actual'])
                            pred_lstm_h.extend(lstm[key]['pred'])
                            pred_trans_h.extend(trans[key]['pred'])
            dm_h, p_h = dm_test(act_h, pred_trans_h, pred_lstm_h, h=1, crit=crit)
            print_res("Transformer vs. LSTM (Overall)", f"{horizon}-term", dm_h, p_h)
            
        # Architecture comparisons (Gemini-LSTM only)
        for horizon in ['Medium', 'Long']:
            act_arch = []
            pred_hier = []
            pred_rr = []
            pred_ens = []
            for stock in stocks:
                key_hier = f"{stock}_Hierarchical_{horizon}"
                key_rr = f"{stock}_RoundRobin_{horizon}"
                key_ens = f"{stock}_Ensemble_{horizon}"
                if key_hier in gemini_lstm and key_rr in gemini_lstm and key_ens in gemini_lstm:
                    act_arch.extend(gemini_lstm[key_hier]['actual'])
                    pred_hier.extend(gemini_lstm[key_hier]['pred'])
                    pred_rr.extend(gemini_lstm[key_rr]['pred'])
                    pred_ens.extend(gemini_lstm[key_ens]['pred'])
            
            dm_h_e, p_h_e = dm_test(act_arch, pred_hier, pred_ens, h=1, crit=crit)
            dm_r_e, p_r_e = dm_test(act_arch, pred_rr, pred_ens, h=1, crit=crit)
            
            print_res("Hierarchical vs. Ensemble (LSTM)", f"{horizon}-term", dm_h_e, p_h_e)
            print_res("Round Robin vs. Ensemble (LSTM)", f"{horizon}-term", dm_r_e, p_r_e)

    print("\n" + "=" * 100)
    print("DETAILED BREAKDOWN PER LLM FAMILY (MSE CRITERION)")
    print("=" * 100)
    print(f"{'Comparison Pair (Model 1 vs. Model 2)':<45} | {'Horizon':<12} | {'DM Statistic':<15} | {'p-value':<10} | {'Significance'}")
    print("-" * 100)
    
    families = [
        ('Gemini-LSTM vs Gemini-Transformer', gemini_lstm, gemini_trans),
        ('GPT-LSTM vs GPT-Transformer', gpt_lstm, gpt_trans),
        ('LLaMA-LSTM vs LLaMA-Transformer', llama_lstm, llama_trans)
    ]
    for comp_name, lstm, trans in families:
        # Overall
        act_o = []
        pred_l_o = []
        pred_t_o = []
        for stock in stocks:
            for horizon in horizons:
                for arch in architectures:
                    key = f"{stock}_{arch}_{horizon}"
                    if key in lstm and key in trans:
                        act_o.extend(lstm[key]['actual'])
                        pred_l_o.extend(lstm[key]['pred'])
                        pred_t_o.extend(trans[key]['pred'])
        dm_o, p_o = dm_test(act_o, pred_t_o, pred_l_o, h=1, crit="MSE")
        print_res(comp_name, "All", dm_o, p_o)
        
        # Horizons
        for horizon in horizons:
            act_h = []
            pred_l_h = []
            pred_t_h = []
            for stock in stocks:
                for arch in architectures:
                    key = f"{stock}_{arch}_{horizon}"
                    if key in lstm and key in trans:
                        act_h.extend(lstm[key]['actual'])
                        pred_l_h.extend(lstm[key]['pred'])
                        pred_t_h.extend(trans[key]['pred'])
            dm_h, p_h = dm_test(act_h, pred_t_h, pred_l_h, h=1, crit="MSE")
            print_res(comp_name, f"{horizon}-term", dm_h, p_h)

if __name__ == "__main__":
    run_dm_tests()
