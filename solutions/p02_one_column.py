# ============================================================
#  SOLUTION p02 -- One Column at a Time
#  The Cozy Bean  |  M1-W2 Lab02
#
#  How to run it: python solutions/p02_one_column.py
#                 (run it from inside the M1-W2-Lab02 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/tips.csv")

print("Different days:", df['day'].nunique())

print("Bills per day:")
print(df['day'].value_counts())

print("Lunch vs dinner:")
print(df['time'].value_counts())

# value_counts() sorts biggest first by default, which is
# almost always what you want when you are about to say
# "our busiest day is..."
