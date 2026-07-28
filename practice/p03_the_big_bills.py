# ============================================================
#  PRACTICE p03 -- The Big Bills
#  The Cozy Bean  |  M1-W2 Lab02
#
#  YOUR TASK:
#    The bank calls anything over $30 a "big table". They want
#    to know how many we served, and what those tables tipped.
#      1. Keep only the bills over $30.
#      2. Print how many there are (rows and columns).
#      3. Print the average tip on those tables.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Big tables (over $30): (32, 7)
#    That is 32 of 244 bills.
#    Average tip on a big table: $4.58
#
#  HINT: the filter is df[df['total_bill'] > 30].
#        For the last line, .mean() on the tip column of the
#        FILTERED table -- and :.2f inside an f-string rounds
#        it to two decimal places like money.
#
#  How to run it: python practice/p03_the_big_bills.py
#                 (run it from inside the M1-W2-Lab02 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/tips.csv")

# TODO 1: keep only the bills over $30
big = df

# TODO 2: print "Big tables (over $30):" and the shape
print("Big tables (over $30): (not filtered yet)")

print(f"That is {big.shape[0]} of {df.shape[0]} bills.")

# TODO 3: print the average tip on those tables, to 2 decimals
print("Average tip on a big table: (not worked out yet)")
