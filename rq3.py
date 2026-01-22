import numpy as np
import pandas as pd

# 1. SỬA DỮ LIỆU ĐẦU VÀO: Làm sạch tên cột (bỏ khoảng trắng thừa)
data = {
    'Stock': ['VCB', 'FPT', 'VCS', 'DXG'],
    'Actual': [57.30, 94.0, 43.00, 16.65],
    'Single-Agent': [58.40, 95.80, 47.20, 18.45],   # Đã sửa tên
    'Ensemble': [58.77, 96.82, 44.01, 17.62],       # Đã sửa tên
    'Hierarchical': [59.04, 95.37, 43.29, 17.46],   # Đã sửa tên
    'RoundRobin': [58.95, 95.94, 45.58, 19.06],     # Đã sửa tên
    'Base LSTM': [54.21, 96.89, 49.54, 15.37]       # Đã sửa tên
}

df = pd.DataFrame(data).set_index('Stock')

# Hàm tính metrics
def calc_metrics(actual, predicted):
    actual = float(actual)
    predicted = float(predicted)
    mae = abs(predicted - actual)
    # Lưu ý: Với 1 điểm dữ liệu, RMSE chính là MAE (căn bậc 2 của bình phương sai số)
    rmse = np.sqrt((predicted - actual) ** 2) 
    mape = abs((actual - predicted) / actual) * 100 if actual != 0 else float('inf')
    return mae, rmse, mape

# 2. SỬA DANH SÁCH PHƯƠNG PHÁP: Phải khớp chính xác 100% với tên cột ở trên
methods = [
    'Single-Agent',
    'Ensemble',
    'Hierarchical',
    'RoundRobin',
    'Base LSTM'
]

# ────────────────────────────────────────────────
# In kết quả chi tiết từng mã
# ────────────────────────────────────────────────
print("\nKẾT QUẢ ĐÁNH GIÁ DỰ BÁO - CHI TIẾT TỪNG MÃ\n")
print(f"{'Mã':<6} {'Phương pháp':<22} {'MAE':>8}  {'RMSE':>8}  {'MAPE (%)':>10}")
print("-" * 70)

all_rows = []

for stock in df.index:
    actual = df.loc[stock, 'Actual']
    print(f"\n{stock}   Actual: {actual:>6,} VND")
    print("-" * 70)
    
    stock_results = []
    for method in methods:
        # Lấy dữ liệu dự báo
        pred = df.loc[stock, method]
        
        # Tính toán
        mae, rmse, mape = calc_metrics(actual, pred)
        stock_results.append((method, mae, rmse, mape))
        
        print(f"  {method:<22} {mae:8,.2f}  {rmse:8,.2f}  {mape:10.2f}")
    
    # Tìm phương pháp tốt nhất cho mã này (theo MAPE)
    best = min(stock_results, key=lambda x: x[3])
    print(f"  → Tốt nhất (MAPE): {best[0]}   {best[3]:.2f}%   (MAE {best[1]:,.2f})")
    
    all_rows.extend([(stock, m, mae, rmse, mape) for m, mae, rmse, mape in stock_results])

# ────────────────────────────────────────────────
# Tổng hợp trung bình trên 4 mã
# ────────────────────────────────────────────────
print("\n" + "=" * 70)
print("TỔNG HỢP TRUNG BÌNH TRÊN 4 MÃ CHỨNG KHOÁN\n")

result_df = pd.DataFrame(all_rows, columns=['Stock', 'Method', 'MAE', 'RMSE', 'MAPE'])

# Groupby để tính trung bình
agg = result_df.groupby('Method').agg({
    'MAE': 'mean',
    'RMSE': 'mean',
    'MAPE': 'mean'
}).round(2).sort_values('MAPE')

print(agg[['MAE', 'RMSE', 'MAPE']])
print("\nPhương pháp tốt nhất trung bình (MAPE thấp nhất):", agg.index[0], f"({agg.iloc[0]['MAPE']}% )")