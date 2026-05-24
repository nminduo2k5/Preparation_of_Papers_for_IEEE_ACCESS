# Hướng Dẫn Chi Tiết Quy Trình Tính Toán Dữ Liệu Cho RQ1 và RQ2

Tài liệu này giải thích chi tiết nguồn gốc dữ liệu, logic trích xuất và các công thức toán học đằng sau quá trình tạo Bảng 1, 2 (phục vụ RQ1) và Bảng 3 (phục vụ RQ2) trong bài báo IEEE Access.

---

## 1. Nguồn Dữ Liệu Gốc (Data Source)
Toàn bộ dữ liệu tính toán đều bắt nguồn từ **một nguồn duy nhất**: Các bảng Phụ lục (Appendix) nằm ở phần cuối của file `access.tex` (ví dụ: khu vực bên dưới nhãn `\label{tab:full_performance_all}`).

Trong các bảng phụ lục này, dữ liệu thô được trình bày dưới dạng:
- **Cổ phiếu:** 12 mã đại diện cho 4 nhóm ngành (VCB, FPT, DXG, VCS...).
- **Cấu trúc (Architecture):** Hierarchical, Round Robin, Ensemble.
- **Dữ liệu mốc thời gian:** 
  - **Short-term** (3 ngày)
  - **Medium-term** (14 ngày)
  - **Long-term** (60 ngày)
- Ở mỗi mốc thời gian đều có cặp giá: **Giá Dự đoán (Predicted Price)** và **Giá Thực tế (Actual Price)**.

---

## 2. Quá Trình Trích Xuất Dữ Liệu (Parsing)
Script Python (`tinhtoanrq1.py`) thực hiện việc lấy dữ liệu một cách tự động để tránh sai sót khi làm thủ công:
1. Mở file `access.tex`, duyệt từng dòng của các bảng phụ lục.
2. Sử dụng **Biểu thức chính quy (Regex)** để nhận diện tên Cổ phiếu và tên Cấu trúc (Arch).
3. Tại mỗi dòng, script tách cột (split theo ký tự `&`) và bóc tách ra các con số:
   - `s_pred`, `s_act` (Cho Short-term)
   - `m_pred`, `m_act` (Cho Medium-term)
   - `l_pred`, `l_act` (Cho Long-term)
4. Dữ liệu này được lưu trữ tạm thời vào cấu trúc dictionary trong Python, phân loại theo LLM, Architecture và Horizon.

---

## 3. Các Công Thức Tính Sai Số Cơ Bản
Với mỗi cặp `(pred, act)` thu thập được, hệ thống tính toán 3 thành phần trung gian:
- **Sai số tuyệt đối (Absolute Error - AE):** $AE = |pred - act|$
- **Sai số phần trăm (Percentage Error - PE):** $PE = \frac{|pred - act|}{act}$
- **Bình phương sai số (Squared Error - SE):** $SE = (pred - act)^2$

---

## 4. Các Bước Tính Toán Cho RQ1 (Đánh giá Cấu trúc Multi-Agent)
RQ1 yêu cầu trả lời câu hỏi: *Cấu trúc phối hợp nào (Hierarchical, Round Robin, Ensemble) là hiệu quả nhất?*

Để trả lời, `tinhtoanrq1.py` thực hiện các bước sau để tạo ra **Bảng 1** và **Bảng 2**:
- **Bước 1 (Gom nhóm dữ liệu Bảng 1):** Script chia dữ liệu thành 2 nhánh lớn là LSTM-based và Transformer-based. Trong mỗi nhánh, dữ liệu được gom theo 3 cấu trúc (Hierarchical, Round Robin, Ensemble) tại từng mốc thời gian (Short/Medium/Long).
- **Bước 2 (Tính toán Bảng 1):** Tại mỗi ô trong Bảng 1 (ví dụ: LSTM - Ensemble - Short-term), script cộng dồn sai số tuyệt đối ($AE$), sai số phần trăm ($PE$), và sai số bình phương ($SE$) của **toàn bộ 12 cổ phiếu**. Sau đó tính trung bình:
  - $\text{MAE} = \frac{\sum AE}{12}$
  - $\text{MAPE} = \left(\frac{\sum PE}{12}\right) \times 100\%$
  - $\text{RMSE} = \sqrt{\frac{\sum SE}{12}}$
- **Bước 3 (Gom nhóm dữ liệu Bảng 2):** Để có cái nhìn tổng quan nhất (Overall), script gom toàn bộ dữ liệu của cả 3 mốc thời gian (Short + Medium + Long) lại thành một tập dữ liệu lớn.
- **Bước 4 (Tính toán Bảng 2):** Áp dụng lại công thức MAE và MAPE cho tập dữ liệu khổng lồ này để đại diện cho hiệu suất tổng thể của từng Cấu trúc (độc lập với mốc thời gian). Cấu trúc có sai số nhỏ nhất (Ensemble) sẽ được in đậm.

---

## 5. Các Bước Tính Toán Cho RQ2 (Tác động của LLM)
RQ2 yêu cầu trả lời: *Việc lựa chọn LLM (Llama, GPT, Gemini) ảnh hưởng thế nào đến độ chính xác?*

Để tạo ra **Bảng 3** (`tab:llm_aggregate_comparison`), script `tinhtoanrq1.py` tiếp tục đóng vai trò xử lý và thực hiện theo các bước:
- **Bước 1 (Đổi trục gom nhóm):** Thay vì gom theo cấu trúc Agent như RQ1, script gom dữ liệu theo **Họ LLM** (Llama-3.1-8B, GPT-4o, Gemini 2.0 Flash).
- **Bước 2 (Gộp dữ liệu cấu trúc):** Tập dữ liệu của 1 LLM (ví dụ: Gemini) tại 1 mốc thời gian (ví dụ: Short-term) sẽ là sự kết hợp của: 12 mã cổ phiếu $\times$ 3 cấu trúc (Hierarchical + Round Robin + Ensemble) = 36 điểm dữ liệu.
- **Bước 3 (Tính toán thành phần):** Tính MAE, RMSE, MAPE trung bình cho 36 điểm dữ liệu này. Cách tính này giúp đánh giá năng lực thuần túy của bộ não LLM, loại bỏ sự thiên vị do một cấu trúc Agent cụ thể mang lại.
- **Bước 4 (Tính Overall Average):** Để ra được dòng cuối cùng của Bảng 3, script gộp toàn bộ dữ liệu của cả 3 mốc thời gian (Short+Medium+Long) thành 108 điểm dữ liệu và tính trung bình MAE, RMSE, MAPE tổng thể cho từng LLM.

---

## 6. Tính Nhất Quán (Consistency)
Nhờ sử dụng chung một kịch bản trích xuất và tính toán, dữ liệu trong bài thỏa mãn 3 tính chất:
- **Traceability (Có thể truy xuất):** Các con số ở bảng RQ1 và RQ2 (Bảng 1, 2, 3) không phải là con số tự sinh ra, mà hoàn toàn có thể tính ngược lại bằng cách lấy trung bình cộng từ bảng phụ lục khổng lồ phía sau bài báo.
- **Macro-level Evaluation:** Việc tính trung bình trên toàn bộ cổ phiếu giúp báo cáo cung cấp một cái nhìn vĩ mô (tránh hiện tượng Overfitting khi chỉ nhìn vào 1 cổ phiếu dễ dự đoán).
- **Automation:** Nếu sau này người dùng có cập nhật hay sửa lại một con số `pred/act` bất kỳ trong phụ lục, việc chạy lại `tinhtoanrq1.py` sẽ lập tức update hàng loạt Bảng 1, Bảng 2 và Bảng 3 một cách chính xác tuyệt đối.

---

## 7. Các Bước Tính Toán Cho RQ3 (So sánh Multi-Agent và Single-Agent Baselines)
RQ3 yêu cầu trả lời: *Hệ thống Multi-Agent có thực sự vượt trội hơn các mô hình truyền thống (LSTM/Transformer) và Single-Agent LLM hay không?*

Hệ thống tạo ra **Bảng RQ3** (`tab:rq3_baselines_vs_mas`) thông qua quy trình 4 bước:

- **Bước 1 (Trích xuất toàn diện):** Chạy script `compute_stats.py`. Khác với RQ1/RQ2, script này lấy THÊM dữ liệu của cấu trúc **Baseline** (đại diện cho Single-Agent LLM tự hoạt động không có agent phối hợp) và các mô hình deep learning truyền thống (**LSTM, TRANSFORMER**).
- **Bước 2 (Tính toán ghi ra CSV):** Script tính toán MAE, MAPE, RMSE trung bình (trên toàn bộ 12 cổ phiếu) cho MỌI tổ hợp (Model + Architecture + Horizon). Toàn bộ kết quả này được lưu vào file trung gian `metrics_summary.csv`.
- **Bước 3 (Đọc và Định dạng bảng):** Chạy script `gen_rq3_table.py`. Script này đọc file CSV, sắp xếp các mô hình theo nhóm: Nhóm mô hình truyền thống (LSTM/Transformer Baseline) lên đầu, tiếp đến là nhóm LLM (Llama, GPT, Gemini).
- **Bước 4 (Xuất LaTeX):** Với mỗi nhóm LLM, script in ra dòng Baseline trước, sau đó so sánh trực tiếp với các phiên bản Multi-Agent (Hierarchical, Round Robin, Ensemble) của chính LLM đó. Kết quả được lưu vào `rq3_table.tex`.

**Kết luận:** Phương pháp tính của RQ3 hoàn toàn nhất quán với RQ1 và RQ2 (đều lấy trung bình 12 mã cổ phiếu để đảm bảo tính công bằng). Sự giảm thiểu sai số đột phá (đặc biệt là MAPE) ở RQ3 minh chứng rõ ràng sức mạnh lọc nhiễu của cơ chế Multi-Agent so với việc để LLM dự đoán đơn độc (Single-Agent).
