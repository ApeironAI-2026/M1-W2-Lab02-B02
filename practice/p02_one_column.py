# ============================================================
#  PRACTICE p02 -- One Column at a Time
#  The Cozy Bean  |  M1-W2 Lab02
#
#  YOUR TASK:
#    The officer wants to understand the trading pattern.
#      1. How many different days did we trade?
#      2. How many bills fell on each day?
#      3. How many were lunches and how many dinners?
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Different days: 4
#    Bills per day:
#    day
#    Sat     87
#    Sun     76
#    Thur    62
#    Fri     19
#    Name: count, dtype: int64
#    Lunch vs dinner:
#    time
#    Dinner    176
#    Lunch      68
#    Name: count, dtype: int64
#
#  HINT: nunique() counts how many DIFFERENT values a column
#        has. value_counts() counts how many of each.
#        Use square brackets to name a column: df['day']
#
#  How to run it: python practice/p02_one_column.py
#                 (run it from inside the M1-W2-Lab02 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/tips.csv")

# TODO 1: print "Different days:" and how many different days
print("Different days: (not counted yet)")

# TODO 2: print "Bills per day:" then the count for each day
print("Bills per day:")
print("(not counted yet)")

# TODO 3: print "Lunch vs dinner:" then the count for each
print("Lunch vs dinner:")
print("(not counted yet)")
