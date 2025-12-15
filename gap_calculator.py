#!/usr/bin/env python3
"""
Gap Calculator for Stock Forecast Table
Calculates Gap = Actual - Predicted
"""

def calculate_gap(predicted, actual):
    """Calculate gap between actual and predicted values"""
    if actual == "--" or predicted == "--":
        return "--"
    return round(float(actual) - float(predicted), 2)

def format_gap_display(gap, start_price, actual_price):
    """Format gap display with direction indicators"""
    if gap == "--":
        return "--"
    
    # Gap direction
    gap_direction = "uparrow" if gap > 0 else "downarrow"
    gap_sign = "+" if gap > 0 else ""
    
    color = "green" if gap > 0 else "red"
    return f"\\textcolor{{{color}}}{{\\({gap_direction}\\){gap_sign}{gap}}}"

# Example calculations for your table
print("=== CORRECTED GAP CALCULATIONS ===\n")

# DXG Hierarchical examples
print("DXG - Hierarchical:")
print("Row 1 Short-term: Start=22.8, Pred=22.25, Act=24")
gap1 = calculate_gap(22.25, 24)
print(f"Gap = {24} - {22.25} = {gap1}")
print(f"Formatted: {format_gap_display(gap1, 22.8, 24)}")

print("\nRow 1 Medium-term: Start=22.8, Pred=23.38, Act=24.05")
gap2 = calculate_gap(23.38, 24.05)
print(f"Gap = {24.05} - {23.38} = {gap2}")
print(f"Formatted: {format_gap_display(gap2, 22.8, 24.05)}")

print("\nRow 1 Long-term: Start=22.8, Pred=21.83, Act=21.2")
gap3 = calculate_gap(21.83, 21.2)
print(f"Gap = {21.2} - {21.83} = {gap3}")
print(f"Formatted: {format_gap_display(gap3, 22.8, 21.2)}")

print("\n" + "="*50)

# FPT Hierarchical examples
print("FPT - Hierarchical:")
print("Row 1 Short-term: Start=101.6, Pred=103.60, Act=105")
gap4 = calculate_gap(103.60, 105)
print(f"Gap = {105} - {103.60} = {gap4}")
print(f"Formatted: {format_gap_display(gap4, 101.6, 105)}")

print("\nRow 1 Medium-term: Start=101.6, Pred=106.07, Act=101.9")
gap5 = calculate_gap(106.07, 101.9)
print(f"Gap = {101.9} - {106.07} = {gap5}")
print(f"Formatted: {format_gap_display(gap5, 101.6, 101.9)}")

print("\n" + "="*50)
print("\nCORRECTED LATEX TABLE ENTRIES:")
print("Replace your current Gap columns with these corrected values:")
print()

# Generate corrected entries for key rows
corrections = [
    ("DXG Hierarchical Row 1", "22.8", "22.25", "24", "23.38", "24.05", "21.83", "21.2"),
    ("DXG Hierarchical Row 4", "20.5", "21.10", "20.9", "28.88", "20.1", "26.71", "--"),
    ("FPT Hierarchical Row 1", "101.6", "103.60", "105", "106.07", "101.9", "105.57", "103.9"),
]

for name, start, pred_s, act_s, pred_m, act_m, pred_l, act_l in corrections:
    print(f"\n{name}:")
    
    # Short-term
    gap_s = calculate_gap(pred_s, act_s)
    gap_s_formatted = format_gap_display(gap_s, start, act_s)
    print(f"Short-term Gap: {gap_s_formatted}")
    
    # Medium-term  
    gap_m = calculate_gap(pred_m, act_m)
    gap_m_formatted = format_gap_display(gap_m, start, act_m)
    print(f"Medium-term Gap: {gap_m_formatted}")
    
    # Long-term
    if act_l != "--":
        gap_l = calculate_gap(pred_l, act_l)
        gap_l_formatted = format_gap_display(gap_l, start, act_l)
        print(f"Long-term Gap: {gap_l_formatted}")
    else:
        print(f"Long-term Gap: --")