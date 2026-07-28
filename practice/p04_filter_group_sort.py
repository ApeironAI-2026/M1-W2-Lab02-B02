# ============================================================
#  PRACTICE p04 -- Filter, Group, Sort -- All in One
#  The Cozy Bean  |  M1-W2 Lab02
#
#  ⭐ This is the one that makes you feel like a data person.
#
#  YOUR TASK:
#    The officer asks the real question: "Forget the small
#    tables. On your BIG tables, which day earns you most?"
#
#    Three moves, in order:
#      1. FILTER   -- keep only bills over $20
#      2. GROUP    -- pile them by day, averaging total_bill
#                     and tip
#      3. SORT     -- best average bill first
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Big tables by day, best first:
#          total_bill       tip
#    day
#    Sun    28.582162  3.980000
#    Sat    28.476579  3.842368
#    Thur   28.433125  4.150625
#    Fri    27.111667  3.580000
#    Best day for big tables: Sun
#
#  HINT: do it in three separate lines first, each one storing
#        its result in a variable. Once it works, you can chain
#        them into one long line if you like -- but working
#        beats clever.
#        The day name at the end is by_day.index[0].
#
#  How to run it: python practice/p04_filter_group_sort.py
#                 (run it from inside the M1-W2-Lab02 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/tips.csv")

# TODO 1: keep only bills over $20

# TODO 2: group what is left by 'day', taking the mean of
#         ['total_bill', 'tip']

# TODO 3: sort by 'total_bill', biggest first
by_day = df.groupby('day')[['total_bill', 'tip']].mean()

print("Big tables by day, best first:")
print(by_day)

# TODO 4: print "Best day for big tables:" and the top day
print("Best day for big tables: (not sorted yet)")
