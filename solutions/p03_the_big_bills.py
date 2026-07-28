# ============================================================
#  SOLUTION p03 -- The Big Bills
#  The Cozy Bean  |  M1-W2 Lab02
#
#  How to run it: python solutions/p03_the_big_bills.py
#                 (run it from inside the M1-W2-Lab02 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/tips.csv")

big = df[df['total_bill'] > 30]

print("Big tables (over $30):", big.shape)
print(f"That is {big.shape[0]} of {df.shape[0]} bills.")
print(f"Average tip on a big table: ${big['tip'].mean():.2f}")

# Note the filtered table is a DataFrame just like the original
# -- so every method you know still works on it. That is why
# you can chain a .mean() straight onto a filter's result.
