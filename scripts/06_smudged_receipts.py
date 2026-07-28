# ============================================================
#  The Cozy Bean -- Script 06: Smudged Entries
#  Lab STEPs 16-17.
#  Shows: checking for missing values on a perfect file, then
#         on a file with real holes in it.
#  Run:   python scripts/06_smudged_receipts.py
#         (from M1-W2-Lab02/)
# ============================================================

import pandas as pd

# ---- Section 1  (STEP 16): the till export is spotless ----
df = pd.read_csv("data/tips.csv")

print("\nCheck for missing values:")
print(df.isna().sum())
print()
print("Every number is 0. The till export has no gaps at all.")
print("Good news for the bank -- and a useless demonstration,")
print("so we need a messier book. We happen to have one.")
print()

# ---- Section 2  (STEP 17): the handwritten takings book ---
# The coffee-shop side's daily takings, typed up by whoever
# closed. Real holes in it, for real reasons.
takings = pd.read_csv("data/cozybean_takings.csv")

print("=== THE TAKINGS BOOK ===")
print(takings)
print()

print("Where are the gaps?")
print(takings.isna().sum())
print()
print("Rows with at least one gap:", int(takings.isna().any(axis=1).sum()))
print()

# ---- Option 1: fill the gaps with the average -------------
muffin_average = takings['muffins_sold'].mean()
print("Average muffins on the days we DID count:", muffin_average)

filled = takings.copy()
filled['muffins_sold'] = filled['muffins_sold'].fillna(muffin_average)

print("After filling, gaps left in muffins_sold:",
      int(filled['muffins_sold'].isna().sum()))
print()

# ---- Option 2: drop any row with a gap in it --------------
dropped = takings.dropna()
print("Rows before dropping:", takings.shape[0])
print("Rows after dropping: ", dropped.shape[0])
print()

# ---- Which one would you defend to a bank manager? --------
print("FILL when the gap is one missing number in an otherwise")
print("good row, and an average is an honest stand-in.")
print("DROP when the row is too damaged to trust -- like Friday")
print("the 18th, where the tablet died and took BOTH numbers.")
