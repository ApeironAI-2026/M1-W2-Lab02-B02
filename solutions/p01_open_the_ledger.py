# ============================================================
#  SOLUTION p01 -- Open the Ledger
#  The Cozy Bean  |  M1-W2 Lab02
#
#  How to run it: python solutions/p01_open_the_ledger.py
#                 (run it from inside the M1-W2-Lab02 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/tips.csv")

print("Bills and columns:", df.shape)
print("Columns:", list(df.columns))
print("First five bills:")
print(df.head())

# shape and columns are attributes (no brackets); head() is a
# method (brackets). Getting that the wrong way round is the
# most common pandas slip there is.
