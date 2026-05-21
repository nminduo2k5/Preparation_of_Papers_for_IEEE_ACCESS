# Hướng Dẫn Chi Tiết Về Kiểm Định Diebold-Mariano (DM Test) Trong Table 10

Tài liệu này giải thích chi tiết toán học, logic lập luận và ý nghĩa thực tế của các con số xuất hiện trong **Table 10 (Diebold-Mariano Test)** của bài báo, đặc biệt là ý nghĩa của dòng **"Transformer vs. LSTM (Overall) - Horizon: All"**.

---

## 1. Bản Chất Của Kiểm Định Diebold-Mariano (DM Test)

Kiểm định Diebold-Mariano (1995) là một công nghệ kiểm định thống kê chuẩn mực được dùng để so sánh **độ chính xác dự báo** của hai mô hình khác nhau. 

Giả sử ta có chuỗi giá trị thực tế $y_t$ và hai chuỗi dự báo tương ứng $\hat{y}_{1,t}$ (Mô hình 1) và $\hat{y}_{2,t}$ (Mô hình 2).
1. **Sai số dự báo:**
   $$e_{1,t} = y_t - \hat{y}_{1,t}, \quad e_{2,t} = y_t - \hat{y}_{2,t}$$
2. **Hàm mất mát (Loss Function):**
   * **MSE (Mean Squared Error):** $L(e_t) = e_t^2$
   * **MAPE (Mean Absolute Percentage Error):** $L(e_t) = \left|\frac{e_t}{y_t}\right|$
3. **Chuỗi chênh lệch mất mát (Loss Differential):**
   $$d_t = L(e_{1,t}) - L(e_{2,t})$$
4. **Giả thuyết kiểm định:**
   * **Giả thuyết Không ($H_0$):** $E[d_t] = 0$ (Hai mô hình có độ chính xác như nhau).
   * **Giả thuyết Đối ($H_1$):** $E[d_t] \neq 0$ (Một mô hình có độ chính xác vượt trội mô hình kia).
5. **Thống kê kiểm định DM:**
   $$DM = \frac{\bar{d}}{\sqrt{\hat{V}(\bar{d})/N}} \sim N(0,1)$$
   * Trong đó $\bar{d}$ là trung bình mẫu của chuỗi chênh lệch $d_t$, và $\hat{V}(\bar{d})$ là phương sai tiệm cận của $\bar{d}$ (đã hiệu chỉnh tự tương quan).

> [!IMPORTANT]
> **Quy ước về Dấu của DM Statistic:**
> Theo công thức $d_t = L(\text{Transformer}) - L(\text{LSTM})$:
> * **DM > 0:** Sai số của Transformer lớn hơn LSTM $\rightarrow$ **LSTM dự báo tốt hơn**.
> * **DM < 0:** Sai số của LSTM lớn hơn Transformer $\rightarrow$ **Transformer dự báo tốt hơn**.
> * **$p$-value < mức ý nghĩa (0.01, 0.05, 0.1):** Sự vượt trội này có ý nghĩa thống kê (không phải do ngẫu nhiên).

---

## 2. Giải Thích Chi Tiết Về p-value Và Các Mức Ý Nghĩa Thống Kê (1%, 5%, 10%)

Để hiểu sâu sắc và bảo vệ bài báo một cách chặt chẽ trước các phản biện (Reviewers), chúng ta cần nắm vững cơ chế khoa học đứng sau **$p$-value** và các ký hiệu ngôi sao ($^{***}$, $^{**}$, $^{*}$) tương ứng với các mức ý nghĩa **1%**, **5%**, và **10%**.

### 2.1. Bản Chất của $p$-value là gì?
Trong thống kê, $p$-value (Probability Value - Giá trị xác suất) trả lời câu hỏi:
> *"Nếu thực tế hai mô hình hoàn toàn giống nhau về hiệu năng (Giả thuyết Không $H_0$ là đúng), thì xác suất để chúng ta thu được sự chênh lệch hiệu năng lớn như kết quả quan sát này (do yếu tố ngẫu nhiên) là bao nhiêu?"*

* **$p$-value nhỏ (ví dụ $p < 0.05$):** Khả năng xảy ra chênh lệch do ngẫu nhiên là vô cùng thấp (dưới 5%). Vì thế, ta bác bỏ giả thuyết $H_0$, công nhận hai mô hình thực sự có sự chênh lệch hiệu năng thực tế.
* **$p$-value lớn (ví dụ $p > 0.10$):** Chênh lệch hiệu năng quan sát được rất có thể chỉ là do nhiễu ngẫu nhiên của thị trường. Ta không thể kết luận mô hình nào tốt hơn một cách có cơ sở khoa học.

### 2.2. Các Mức Ý Nghĩa (1%, 5%, 10%) và Ký Hiệu Sao ở đâu ra?
Trong nghiên cứu khoa học chuẩn mực, chúng ta định sẵn các rào cản xác suất (Mức ý nghĩa $\alpha$) để đưa ra quyết định bác bỏ $H_0$. Cụ thể:

1. **Mức ý nghĩa 1% ($\alpha = 0.01$) — Ký hiệu $^{***}$:**
   * **Điều kiện:** $p\text{-value} < 0.01$
   * **Độ tin cậy (Confidence Level):** $99\%$ (Chúng ta tin tưởng $99\%$ rằng mô hình chiến thắng thực sự tốt hơn, chỉ có $1\%$ khả năng đây là kết quả ngẫu nhiên).
   * **Ngưỡng điểm DM (Z-score tương ứng):** $|DM| > 2.576$
   
2. **Mức ý nghĩa 5% ($\alpha = 0.05$) — Ký hiệu $^{**}$:**
   * **Điều kiện:** $0.01 \le p\text{-value} < 0.05$
   * **Độ tin cậy:** $95\%$ (Mức chuẩn mực vàng được chấp nhận rộng rãi nhất trong khoa học).
   * **Ngưỡng điểm DM:** $|DM| > 1.960$

3. **Mức ý nghĩa 10% ($\alpha = 0.10$) — Ký hiệu $^{*}$:**
   * **Điều kiện:** $0.05 \le p\text{-value} < 0.10$
   * **Độ tin cậy:** $90\%$ (Còn được gọi là **ý nghĩa thống kê biên - marginal significance**). Thường được chấp nhận trong các dữ liệu tài chính độ nhiễu cao.
   * **Ngưỡng điểm DM:** $|DM| > 1.645$

* **Không có sao (Không có ý nghĩa thống kê):**
   * **Điều kiện:** $p\text{-value} \ge 0.10$ (Xác suất xảy ra sai sót ngẫu nhiên lớn hơn $10\%$, không đủ độ tin cậy khoa học).

---

### 2.3. Phân tích cụ thể từng con số trong Table 10

#### Ví dụ 1: Dòng `Hierarchical vs. Ensemble (LSTM)` - Horizon: `Medium-term`
* **Số liệu:** DM Statistic = `3.9140`, $p$-value = `0.0001`
* **Giải nghĩa:**
  * **Giải thích dấu:** DM mang dấu dương (`3.9140` > 0) $\rightarrow$ Mô hình 2 (Ensemble) có sai số nhỏ hơn Mô hình 1 (Hierarchical).
  * **Giải thích $p$-value:** Giá trị $p = 0.0001 < 0.01$, nằm dưới ngưỡng 1%.
  * **Kết luận khoa học:** Ký hiệu **$^{***}$** (Ý nghĩa thống kê ở mức 1%). Có độ tin cậy đến **$99.99\%$** rằng Ensemble vượt trội Hierarchical ở kỳ trung hạn. Sự chênh lệch này là thực tế do thiết kế kiến trúc, không phải do stochastic variation (biến động ngẫu nhiên).

#### Ví dụ 2: Dòng `Round Robin vs. Ensemble (LSTM)` - Horizon: `Medium-term`
* **Số liệu:** DM Statistic = `1.7069`, $p$-value = `0.0878`
* **Giải nghĩa:**
  * **Giải thích dấu:** DM mang dấu dương (`1.7069` > 0) $\rightarrow$ Ensemble dự báo tốt hơn Round Robin.
  * **Giải thích $p$-value:** Giá trị $p = 0.0878$. Nó lớn hơn $0.05$ nhưng nhỏ hơn $0.10$. Do đó nó rơi vào khoảng ý nghĩa biên 10%.
  * **Kết luận khoa học:** Ký hiệu **$^{*}$** (Ý nghĩa thống kê ở mức 10%). Chúng ta có độ tin cậy **$91.22\%$** ($100\% - 8.78\%$) rằng Ensemble tốt hơn Round Robin. Kết quả này được xem là có ý nghĩa chấp nhận được trong dự báo chuỗi thời gian tài chính phức tạp.

#### Ví dụ 3: Dòng `Transformer vs. LSTM (Overall)` - Horizon: `Short-term`
* **Số liệu:** DM Statistic = `-2.3918`, $p$-value = `0.0168`
* **Giải nghĩa:**
  * **Giải thích dấu:** DM mang dấu âm (`-2.3918` < 0) $\rightarrow$ Mô hình 1 (Transformer) có sai số nhỏ hơn Mô hình 2 (LSTM).
  * **Giải thích $p$-value:** Giá trị $p = 0.0168$. Số này nằm trong khoảng $[0.01, 0.05)$ (dưới ngưỡng 5% nhưng chưa đạt tới mức 1%).
  * **Kết luận khoa học:** Ký hiệu **$^{**}$** (Ý nghĩa thống kê mức 5%). Ta tin tưởng **$98.32\%$** rằng Transformer thực sự thắng LSTM ở kỳ hạn ngắn.

#### Ví dụ 4: Dòng `Transformer vs. LSTM (Overall)` - Horizon: `All`
* **Số liệu:** DM Statistic = `0.5659`, $p$-value = `0.5714`
* **Giải nghĩa:**
  * **Giải thích $p$-value:** Giá trị $p = 0.5714 > 0.10$.
  * **Kết luận khoa học:** Không có ký hiệu sao (Không có ý nghĩa thống kê). Xác suất sự chênh lệch này là ngẫu nhiên lên tới **$57.14\%$**. Do đó, về mặt khoa học, LSTM và Transformer có năng lực dự báo tổng thể tương đương nhau.

---

## 3. Giải Nghĩa "Transformer vs. LSTM (Overall) - All"

### Dòng này nghĩa là gì?
Dòng **`Transformer vs. LSTM (Overall)`** tại Horizon **`All`** là kết quả của kiểm định gộp (pooled DM test) trên toàn bộ không gian dữ liệu dự báo của cả nghiên cứu để đưa ra kết luận chung nhất: **"Nhìn chung, mạng LSTM hay mạng Transformer làm mô hình nền tảng tốt hơn?"**

### Cách tập hợp chuỗi dữ liệu để tính toán:
Để có được số liệu này, chương trình gộp toàn bộ các điểm dự báo lại:
* **3 Dòng LLM:** Gemini 2.0 Flash, GPT-4o, LLaMA-3.
* **12 Mã cổ phiếu:** CMG, DGC, DXG, FPT, HPG, KDH, MBB, MWG, TCB, VCB, VCS, VHM.
* **3 Kiến trúc phối hợp:** Hierarchical, Round Robin, Ensemble.
* **3 Kỳ hạn dự báo:** Short-term (3 ngày), Medium-term (14 ngày), Long-term (60 ngày).
* **4 Ngày dự báo test** cho mỗi chuỗi.

Tổng số chuỗi dự báo gộp là:
$$3 \text{ LLMs} \times 12 \text{ Stocks} \times 3 \text{ Architectures} \times 3 \text{ Horizons} = 324 \text{ chuỗi}$$
Mỗi chuỗi có 4 điểm dữ liệu thời gian $\rightarrow$ Tổng số điểm mẫu gộp là $324 \times 4 = 1296$ điểm sai số dự báo.

### Kết quả tính toán thực tế (MSE):
* **DM Statistic:** `0.5659`
* **$p$-value:** `0.5714` (Không có ý nghĩa thống kê)

### Tại sao lại không có ý nghĩa thống kê ($p > 0.1$)?
Logic này hoàn toàn nhất quán với bản chất hoạt động của hai mô hình nền tảng:
1. **Transformer** hoạt động cực kỳ tốt ở **kỳ ngắn hạn (Short-term)** nhờ khả năng nắm bắt nhanh các xu hướng tức thời (DM Statistic ở Short-term là **`-2.3918`**, vô cùng có ý nghĩa $p = 0.0168^{**}$).
2. **LSTM** lại tỏ ra ổn định hơn khi dự báo **kỳ dài hạn (Long-term)** nhờ cơ chế nhớ dài hạn qua các cổng nhớ tuần hoàn (DM Statistic ở Long-term là **`0.7343`** - thiên về LSTM).
3. **Khi gộp chung tất cả các kỳ hạn (All):** Sự vượt trội của Transformer ở kỳ ngắn hạn đã triệt tiêu sự vượt trội của LSTM ở kỳ dài hạn. Do đó, xét trên toàn bộ tổng thể, không có mô hình nào chiến thắng tuyệt đối một cách có ý nghĩa thống kê. 

Điều này giải thích tại sao việc **bổ sung per-horizon breakdown (Short, Medium, Long)** vào Table 10 là cực kỳ quan trọng. Nó giúp Reviewer thấy được bức tranh đa chiều: LSTM không thắng Transformer ở mọi mặt trận, mà mỗi kiến trúc có một thế mạnh riêng theo kỳ hạn.

---

## 3. Phân Tích Chi Tiết Toàn Bộ Các Dòng Trong Table 10

Dưới đây là bảng số liệu kiểm định thực tế (MSE) và logic giải thích cho từng dòng:

| So sánh (Mô hình 1 vs 2) | Horizon | DM Stat | $p$-value | Ý nghĩa thống kê | Logic giải thích |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Transformer vs. LSTM** | **All** | `0.5659` | `0.5714` | Không có ý nghĩa | Hai mô hình tự triệt tiêu thế mạnh của nhau khi gộp chung tất cả các kỳ hạn. |
| **Transformer vs. LSTM** | **Short-term** | `-2.3918` | `0.0168` | **Có ý nghĩa (5%)** | Transformer tốt hơn rõ rệt nhờ cơ chế self-attention nhạy bén với biến động ngắn hạn. |
| **Transformer vs. LSTM** | **Medium-term** | `0.1590` | `0.8737` | Không có ý nghĩa | Giai đoạn chuyển giao thế trận, hiệu năng hai mô hình tương đương nhau. |
| **Transformer vs. LSTM** | **Long-term** | `0.7343` | `0.4628` | Không có ý nghĩa | LSTM tốt hơn trên trung bình MAE/MAPE nhưng độ nhiễu dài hạn cao khiến kiểm định không đạt ý nghĩa thống kê. |
| **Hierarchical vs. Ensemble** | **Medium-term** | `3.9140` | `0.0001` | **Cực kỳ ý nghĩa (1%)** | Cơ chế bỏ phiếu trọng số động của Ensemble vượt trội hoàn toàn cấu hình phân cấp cứng nhắc. |
| **Round Robin vs. Ensemble** | **Medium-term** | `1.7069` | `0.0878` | **Có ý nghĩa biên (10%)** | Ensemble nhỉnh hơn nhờ tích hợp đồng thời thay vì cập nhật tuần tự mất thời gian của Round Robin. |
| **Hierarchical vs. Ensemble** | **Long-term** | `2.8200` | `0.0048` | **Cực kỳ ý nghĩa (1%)** | Trong dài hạn, Ensemble giảm thiểu rủi ro sai số tích lũy tốt hơn Hierarchical. |
| **Round Robin vs. Ensemble** | **Long-term** | `1.6602` | `0.0969` | **Có ý nghĩa biên (10%)** | Round Robin bị suy giảm thông tin qua các vòng lặp dài hạn, Ensemble giữ độ ổn định tốt hơn. |

---

## 4. Tại Sao Phải Có "Robustness Check" Với Tiêu Chí MAPE?

### Vấn đề của tiêu chí MSE (Mean Squared Error):
Kiểm định DM truyền thống sử dụng mất mát MSE (bình phương sai số). Tuy nhiên, khi gộp chung 12 mã cổ phiếu có **thị giá chênh lệch lớn**, MSE sẽ bị bóp méo nghiêm trọng:
* Ví dụ: Cổ phiếu FPT giá trị ~100,000 VND, biến động 5% tạo ra sai số bình phương rất lớn.
* Cổ phiếu DXG giá trị ~20,000 VND, biến động 5% tạo ra sai số bình phương cực nhỏ.
$\Rightarrow$ Kết quả kiểm định DM sử dụng MSE bị **thao túng chủ yếu bởi FPT và VHM** (các cổ phiếu giá cao).

### Giải pháp dùng MAPE (Robustness Check):
Mất mát phần trăm tuyệt đối trung bình (MAPE) chia sai số cho chính giá trị thực tế của cổ phiếu tại thời điểm đó:
$$L(e_t) = \left|\frac{y_t - \hat{y}_t}{y_t}\right|$$
Điều này chuẩn hóa sai số của tất cả các cổ phiếu về cùng một tỷ lệ phần trăm (vô hiệu hóa sự thống trị của thị giá cổ phiếu).

### Nhận xét tính nhất quán của kết quả MAPE:
Khi chạy tệp `calculate_dm_test.py` với tùy chọn `crit="MAPE"`, kết quả cho thấy:
* Thứ tự xếp hạng hiệu năng của các mô hình hoàn toàn **đồng nhất** với bảng MSE.
* Việc này chứng minh rằng kết luận khoa học của bài báo là **đáng tin cậy và bền vững** (robust), không phụ thuộc vào cách tính toán hàm mất mát hay do ảnh hưởng cá biệt của các cổ phiếu vốn hóa lớn.
