# ============================================================
#  The Cozy Bean -- Script 07: Labels vs Positions
#  Lab STEP 18.
#  Shows: .loc (by label) and .iloc (by position), and the one
#         way they differ that catches everybody.
#  Run:   python scripts/07_labels_vs_positions.py
#         (from M1-W2-Lab02/)
# ============================================================

import pandas as pd

df = pd.read_csv("data/tips.csv")

# ---- Section 1  (STEP 18): by POSITION, with iloc ---------
# "the first 10 rows" -- counted, like a stack of receipts
subset_iloc = df.iloc[:10, df.columns.get_loc('total_bill')]
print("\nFirst 10 rows of 'total_bill' column using .iloc[]:")
print(subset_iloc)
print()

# ---- Section 2  (STEP 18): by LABEL, with loc -------------
# "the pages labelled 0 to 9" -- looked up, like page numbers
subset_loc = df.loc[0:9, 'total_bill']
print("\nFirst 10 rows of 'total_bill' column using .loc[]:")
print(subset_loc)
print()

# ---- Section 3  (STEP 18): the difference that bites ------
# 🔙 Week 1: a list slice LEAVES OUT the end.
week1_list = ["Sara", "Ben", "Aisha", "Marcus"]
print("Week-1 list slice [1:3] ->", week1_list[1:3], "(2 names, 3 left out)")

# iloc follows the SAME Week-1 rule: end left out.
print("iloc[0:10] gives", len(df.iloc[0:10]), "rows (10 left out)")

# loc does NOT. Its end label is INCLUDED.
print("loc[0:9]  gives", len(df.loc[0:9]), "rows (9 included)")
print()
print("Both gave 10 rows -- for two completely different reasons.")
