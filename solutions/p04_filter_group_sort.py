# ============================================================
#  SOLUTION p04 -- Filter, Group, Sort -- All in One
#  The Cozy Bean  |  M1-W2 Lab02
#
#  How to run it: python solutions/p04_filter_group_sort.py
#                 (run it from inside the M1-W2-Lab02 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/tips.csv")

# One move at a time -- this is the readable way, and it is
# what you should write first.
big = df[df['total_bill'] > 20]
by_day = big.groupby('day')[['total_bill', 'tip']].mean()
by_day = by_day.sort_values(by='total_bill', ascending=False)

print("Big tables by day, best first:")
print(by_day)
print("Best day for big tables:", by_day.index[0])

# The same three moves chained into one line. Identical result.
# Write it this way only once it already works in three.
#
# by_day = (df[df['total_bill'] > 20]
#           .groupby('day')[['total_bill', 'tip']]
#           .mean()
#           .sort_values(by='total_bill', ascending=False))
