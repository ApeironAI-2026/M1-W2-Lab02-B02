# ============================================================
#  The Cozy Bean -- Script 03: One Column at a Time
#  Lab STEPs 7-9.
#  Shows: two ways to pull a column out, the trap in the second
#         one, and what a single column can tell you.
#  Run:   python scripts/03_one_column.py  (from M1-W2-Lab02/)
# ============================================================

import pandas as pd

df = pd.read_csv("data/tips.csv")

# ---- Section 1  (STEP 7): pulling one column --------------
# Two ways to ask for the same column:
print("Square brackets:")
print(df['day'].head())
print()

print("Dot notation -- same answer:")
print(df.day.head())
print()

# ONE column is a Series. TWO columns (double brackets) is a
# smaller DataFrame.
print("One column -> a Series:")
print(type(df['total_bill']))
print("Two columns -> a DataFrame:")
print(type(df[['total_bill', 'tip']]))
print()

# ---- Section 2  (STEP 8): when dot notation lies ----------
# This table HAS a column called 'size' (people at the table).
# But every DataFrame also has a built-in attribute called
# .size. The attribute wins -- silently.
print("df['size'] -- the column we wanted:")
print(df['size'].head(3))
print()

print("df.size -- NOT the column. No error. Just wrong:")
print(df.size)          # 1708 = 244 rows x 7 columns
print()
print("Use square brackets. Always. It is never ambiguous.")
print()

# ---- Section 3  (STEP 9): what one column can tell you ----
print("How many different days did we trade?", df['day'].nunique())
print()

print("How many bills on each day?")
print(df['day'].value_counts())
print()

print("How many bills in total?", df['total_bill'].count())
