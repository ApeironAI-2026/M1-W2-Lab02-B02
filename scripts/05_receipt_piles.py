# ============================================================
#  The Cozy Bean -- Script 05: Piles of Receipts
#  Lab STEPs 13-15.
#  Shows: groupby, agg, and describe -- the three things the
#         bank actually wants to see.
#  Run:   python scripts/05_receipt_piles.py  (from M1-W2-Lab02/)
# ============================================================

import pandas as pd

df = pd.read_csv("data/tips.csv")

# ---- Section 1  (STEP 13): sort the receipts into piles ---
# 📌 This is the cell from class. Note what it actually
# computes: the SMALLEST bill and tip in each pile.
grouped_df = df.groupby('day')[['total_bill', 'tip']].min()
print("\nSmallest bill and tip on each day:")
print(grouped_df)
print()

# And the number the bank actually asked for -- the AVERAGE:
grouped_mean = df.groupby('day')[['total_bill', 'tip']].mean()
print("Average bill and tip on each day:")
print(grouped_mean)
print()

# ---- Section 2  (STEP 14): several numbers at once --------
grouped_agg = df.groupby('day').agg({
    'total_bill': ['mean', 'sum', 'max'],
    'tip': ['mean', 'sum']
})
print("\nGrouped data by 'day' with multiple aggregations:")
print(grouped_agg)
print()

# Single brackets -> a Series. Double brackets -> a DataFrame.
print("Single brackets gives a", type(df.groupby('day')['tip'].mean()).__name__)
print("Double brackets gives a", type(df.groupby('day')[['tip']].mean()).__name__)
print()

# ---- Section 3  (STEP 15): the summary page ---------------
print("\nDescriptive statistics for numeric columns:")
print(df.describe())
