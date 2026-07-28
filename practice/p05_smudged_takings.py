# ============================================================
#  PRACTICE p05 -- The Smudged Takings Book
#  The Cozy Bean  |  M1-W2 Lab02
#
#  YOUR TASK:
#    Before the takings book goes anywhere near the bank, it
#    needs cleaning up.
#      1. Count the gaps in each column.
#      2. Fill the missing muffin counts with the average of
#         the days that WERE counted.
#      3. Make a version with every damaged row dropped, and
#         say how many rows survived.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Gaps in each column:
#    date            0
#    day             0
#    barista         0
#    cups_sold       0
#    muffins_sold    3
#    takings         2
#    dtype: int64
#    Average muffins on counted days: 29.0
#    Gaps in muffins_sold after filling: 0
#    Rows kept after dropping damaged ones: 10 of 14
#
#  HINT: isna().sum() counts the gaps. fillna(value) fills
#        them. dropna() removes any row with a gap in it.
#        Work on a copy so you do not clobber the original:
#        filled = takings.copy()
#
#  How to run it: python practice/p05_smudged_takings.py
#                 (run it from inside the M1-W2-Lab02 folder)
# ============================================================

import pandas as pd

takings = pd.read_csv("data/cozybean_takings.csv")

# TODO 1: print "Gaps in each column:" then the count per column
print("Gaps in each column:")
print("(not counted yet)")

# TODO 2: work out the average of the muffin counts we DO have
print("Average muffins on counted days: (not worked out yet)")

# TODO 3: fill the missing muffin counts with that average,
#         then confirm there are no gaps left in that column
print("Gaps in muffins_sold after filling: (not filled yet)")

# TODO 4: drop every row that has any gap, and report how many
#         rows survived out of how many
print(f"Rows kept after dropping damaged ones: ? of {takings.shape[0]}")
