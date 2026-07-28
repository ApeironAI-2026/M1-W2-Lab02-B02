# ============================================================
#  PRACTICE p07 -- One More Page for the Folder
#  The Cozy Bean  |  M1-W2 Lab02
#
#  YOUR TASK:
#    The folder needs one more chart: do lunch tables or dinner
#    tables spend more? Build a boxplot of total_bill by time,
#    give it a title and axis labels, SAVE it, then show it.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Saved charts/bills_by_service.png
#    Window closed. Script finished.
#
#    ...and charts/bills_by_service.png should exist. Open it!
#
#  ⚠️ The script PAUSES when the chart window opens, and the
#     window may be hiding behind VS Code. Find it, admire it,
#     close it, and the script finishes. Your PNG is already
#     saved either way, because savefig runs first.
#
#  HINT: sns.boxplot(x='time', y='total_bill', data=df)
#        Keep the savefig BEFORE the show. Always that order.
#
#  How to run it: python practice/p07_your_own_chart.py
#                 (run it from inside the M1-W2-Lab02 folder)
# ============================================================

import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# The script builds its own display folder first. matplotlib
# will not create it for you.
os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/tips.csv")

plt.figure(figsize=(8, 6))

# TODO 1: draw a boxplot of total_bill split by time

# TODO 2: add a title, an x label and a y label

# TODO 3: save it to charts/bills_by_service.png, then print
#         "Saved charts/bills_by_service.png"
print("(nothing saved yet)")

# TODO 4: show it
print("Window closed. Script finished.")
