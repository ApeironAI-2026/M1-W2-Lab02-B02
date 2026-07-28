# ============================================================
#  SOLUTION p05 -- The Smudged Takings Book
#  The Cozy Bean  |  M1-W2 Lab02
#
#  How to run it: python solutions/p05_smudged_takings.py
#                 (run it from inside the M1-W2-Lab02 folder)
# ============================================================

import pandas as pd

takings = pd.read_csv("data/cozybean_takings.csv")

print("Gaps in each column:")
print(takings.isna().sum())

muffin_average = takings['muffins_sold'].mean()
print("Average muffins on counted days:", muffin_average)

filled = takings.copy()
filled['muffins_sold'] = filled['muffins_sold'].fillna(muffin_average)
print("Gaps in muffins_sold after filling:",
      int(filled['muffins_sold'].isna().sum()))

dropped = takings.dropna()
print(f"Rows kept after dropping damaged ones: "
      f"{dropped.shape[0]} of {takings.shape[0]}")

# .mean() ignores the gaps rather than treating them as zero --
# which is exactly what you want. If it counted them as zero,
# the average would be dragged down and the fill would be a lie.
