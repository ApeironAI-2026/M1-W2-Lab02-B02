# ============================================================
#  PRACTICE p09 -- 🚀 BONUS -- Shares and Bars
#  The Cozy Bean  |  M1-W2 Lab02
#
#  🚀 THIS IS BONUS MATERIAL, BEYOND CLASS. Nothing else in the
#  lab depends on it. Skip it guilt-free -- or do it, because
#  banks think in percentages and this is how you give them
#  percentages.
#
#  YOUR TASK:
#    1. value_counts() gives counts. Add normalize=True and it
#       gives SHARES instead -- 0.36 meaning 36%. Print the
#       share of bills falling on each day.
#    2. Draw those shares as a bar chart and save it.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Share of bills by day:
#    day
#    Sat     0.356557
#    Sun     0.311475
#    Thur    0.254098
#    Fri     0.077869
#    Name: proportion, dtype: float64
#    Saturday is 35.7% of all our bills.
#    Saved charts/share_by_day.png
#
#  HINT: shares = df['day'].value_counts(normalize=True)
#        For the chart: sns.barplot(x=shares.index, y=shares.values)
#        For the sentence: shares['Sat'] * 100, with :.1f
#
#  How to run it: python practice/p09_bonus_shares_and_bars.py
#                 (run it from inside the M1-W2-Lab02 folder)
# ============================================================

import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/tips.csv")

# TODO 1: print "Share of bills by day:" then the shares
print("Share of bills by day:")
print("(not worked out yet)")

# TODO 2: print the Saturday share as a percentage, 1 decimal
print("Saturday is ?% of all our bills.")

# TODO 3: bar chart of the shares -> charts/share_by_day.png
plt.figure(figsize=(8, 6))
print("(no chart saved yet)")
