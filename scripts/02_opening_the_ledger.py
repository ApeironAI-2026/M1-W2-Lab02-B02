# ============================================================
#  The Cozy Bean -- Script 02: Opening the Ledger
#  Lab STEPs 3-6.
#  Shows: read_csv, head/tail, info/shape, columns/dtypes, and
#         the attributes-vs-methods rule.
#  Run:   python scripts/02_opening_the_ledger.py
#         (from M1-W2-Lab02/)
# ============================================================

import pandas as pd

# ---- Section 1  (STEP 3): open the ledger -----------------
# 📌 In class this was read straight from a web address:
#    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
#    df = pd.read_csv(url)
# We use the local copy so the lab works with no internet.
df = pd.read_csv("data/tips.csv")

# ---- Section 2  (STEP 4): peek at the first pages ---------
print("First 5 records of the dataset:")
print(df.head())
print()

print("Just the first 2:")
print(df.head(2))
print()

print("The last 3 bills of the season:")
print(df.tail(3))
print()

# ---- Section 3  (STEP 5): how big is this book? -----------
print("Shape (rows, columns):", df.shape)
print()

print("The full inventory:")
df.info()
print()

# ---- Section 4  (STEP 6): names and types -----------------
# NOTE: no brackets on these two -- they are ATTRIBUTES, facts
# the table carries. df.head() has brackets: it is a METHOD.
print("Column names:")
print(df.columns)
print()

print("What kind of thing is in each column:")
print(df.dtypes)
