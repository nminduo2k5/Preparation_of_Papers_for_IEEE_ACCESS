# Gap Calculation Logic

## Logic Rules:
1. **Màu sắc dựa trên hướng của Actual so với Start:**
   - Nếu Actual > Start → 🟢 (xanh lá)
   - Nếu Actual < Start → 🔴 (đỏ)
   - Nếu Actual ≈ Start → 🟡 (vàng)

2. **Giá trị Gap = |Actual - Predicted|**

3. **Ví dụ:**
   - Start=21, Pred=22, Actual=22.5 → Cùng tăng → 🟢 0.5
   - Start=21, Pred=20, Actual=20.2 → Cùng giảm → 🟢 0.2
   - Start=21, Pred=20, Actual=21.2 → Không cùng tăng/giảm → 🔴 1.2
   - Start=21, Pred=22, Actual=20.8 → Không cùng tăng/giảm → 🔴 1.2

## Recalculated Values:

### DXG - Hierarchical
1. Start=22.8, Pred=22.25, Act=24 → Act>Start → 🟢 +1.75
2. Start=22.45, Pred=22.10, Act=22.6 → Act>Start → 🟢 +0.50
3. Start=20.0, Pred=20.51, Act=20.9 → Act>Start → 🟢 +0.39
4. Start=20.5, Pred=21.10, Act=20.9 → Act>Start → 🟢 -0.20

### DXG - Round Robin
1. Start=22.8, Pred=22.25, Act=24 → Act>Start → 🟢 +1.75
2. Start=22.45, Pred=22.15, Act=22.6 → Act>Start → 🟢 +0.45
3. Start=20.0, Pred=20.34, Act=20.9 → Act>Start → 🟢 +0.56
4. Start=20.5, Pred=20.48, Act=20.9 → Act>Start → 🟢 +0.42

### DXG - Ensemble
1. Start=22.8, Pred=22.11, Act=24 → Act>Start → 🟢 +1.89
2. Start=22.45, Pred=21.92, Act=22.6 → Act>Start → 🟢 +0.68
3. Start=20.0, Pred=20.07, Act=20.9 → Act>Start → 🟢 +0.83
4. Start=20.5, Pred=21.05, Act=20.9 → Act>Start → 🟢 -0.15

### FPT - Hierarchical
1. Start=101.6, Pred=103.60, Act=105 → Act>Start → 🟢 +1.40
2. Start=89.8, Pred=90.83, Act=88.1 → Act<Start → 🔴 -2.73
3. Start=93, Pred=95.37, Act=97.7 → Act>Start → 🟢 +2.33
4. Start=97, Pred=93.5, Act=97.7 → Act>Start → 🟢 +4.20

### FPT - Round Robin
1. Start=101.6, Pred=104.42, Act=105 → Act>Start → 🟢 +0.58
2. Start=89.8, Pred=90.46, Act=88.1 → Act<Start → 🔴 -2.36
3. Start=93, Pred=96.00, Act=97.7 → Act>Start → 🟢 +1.70
4. Start=97, Pred=93.68, Act=97.7 → Act>Start → 🟢 +4.02

### FPT - Ensemble
1. Start=101.6, Pred=103.60, Act=105 → Act>Start → 🟢 +1.40
2. Start=89.8, Pred=88.55, Act=88.1 → Act<Start → 🔴 -0.45
3. Start=93, Pred=95.14, Act=97.7 → Act>Start → 🟢 +2.56
4. Start=97, Pred=96.59, Act=97.7 → Act>Start → 🟢 +1.11

### VCB - Hierarchical
1. Start=68.6, Pred=68.66, Act=68.6 → Act=Start → 🟡 -0.06
2. Start=62.9, Pred=63.29, Act=61.9 → Act<Start → 🔴 -1.39
3. Start=59.3, Pred=61.68, Act=59.5 → Act>Start → 🟢 -2.18
4. Start=59.6, Pred=61.21, Act=59.5 → Act<Start → 🔴 -1.71

### VCB - Round Robin
1. Start=68.6, Pred=68.46, Act=68.6 → Act=Start → 🟡 +0.14
2. Start=62.9, Pred=62.51, Act=61.9 → Act<Start → 🔴 -0.61
3. Start=59.3, Pred=61.15, Act=59.5 → Act>Start → 🟢 -1.65
4. Start=59.6, Pred=61.46, Act=59.5 → Act<Start → 🔴 -1.96

### VCB - Ensemble
1. Start=68.6, Pred=67.64, Act=68.6 → Act=Start → 🟡 +0.96
2. Start=62.9, Pred=63.65, Act=61.9 → Act<Start → 🔴 -1.75
3. Start=59.3, Pred=62.58, Act=59.5 → Act>Start → 🟢 -3.08
4. Start=59.6, Pred=60.88, Act=59.5 → Act<Start → 🔴 -1.38

### VCS - Hierarchical
1. Start=48.8, Pred=47.97, Act=48.8 → Act=Start → 🟡 +0.83
2. Start=47.2, Pred=47.86, Act=46.8 → Act<Start → 🔴 -1.06
3. Start=45.5, Pred=47.12, Act=46.2 → Act>Start → 🟢 -0.92
4. Start=45.5, Pred=46.38, Act=46.2 → Act>Start → 🟢 -0.18

### VCS - Round Robin
1. Start=48.8, Pred=48.62, Act=48.8 → Act=Start → 🟡 +0.18
2. Start=47.2, Pred=47.55, Act=46.8 → Act<Start → 🔴 -0.75
3. Start=45.5, Pred=47.43, Act=46.2 → Act>Start → 🟢 -1.23
4. Start=45.5, Pred=46.92, Act=46.2 → Act>Start → 🟢 -0.72

### VCS - Ensemble
1. Start=48.8, Pred=48.66, Act=48.8 → Act=Start → 🟡 +0.14
2. Start=47.2, Pred=45.48, Act=46.8 → Act<Start → 🔴 +1.32
3. Start=45.5, Pred=46.95, Act=46.2 → Act>Start → 🟢 -0.75
4. Start=45.5, Pred=45.70, Act=46.2 → Act>Start → 🟢 +0.50

## Medium-term Examples:

### DXG - Hierarchical (Medium-term)
1. Start=22.8, Pred=23.38, Act=24.05 → Act>Start → 🟢 +0.67
2. Start=22.45, Pred=23.34, Act=21.2 → Act<Start → 🔴 -2.14
3. Start=20.0, Pred=20.52, Act=20.15 → Act>Start → 🟢 -0.37
4. Start=20.5, Pred=28.88, Act=20.1 → Act<Start → 🔴 -8.78

### DXG - Round Robin (Medium-term)
1. Start=22.8, Pred=21.98, Act=24.05 → Act>Start → 🟢 +2.07
2. Start=22.45, Pred=22.28, Act=21.2 → Act<Start → 🔴 -1.08
3. Start=20.0, Pred=20.79, Act=20.15 → Act>Start → 🟢 -0.64
4. Start=20.5, Pred=23.68, Act=20.1 → Act<Start → 🔴 -3.58

### DXG - Ensemble (Medium-term)
1. Start=22.8, Pred=22.98, Act=24.05 → Act>Start → 🟢 +1.07
2. Start=22.45, Pred=21.75, Act=21.2 → Act<Start → 🔴 -0.55
3. Start=20.0, Pred=20.52, Act=20.15 → Act>Start → 🟢 -0.37
4. Start=20.5, Pred=26.35, Act=20.1 → Act<Start → 🔴 -6.25