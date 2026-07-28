# ============================================================
#  PRACTICE p08 -- CAPSTONE -- Your Report for the Bank
#  The Cozy Bean  |  M1-W2 Lab02
#
#  This is the CAPSTONE. Everything in this lab, doing one
#  real job: the evidence page of your loan application.
#
#  YOUR TASK:
#    Write five findings, in your own f-strings, and save the
#    chart that backs them up.
#
#      1. How many bills, over how many trading days
#      2. The average bill and the average tip
#      3. How many bills were over $20, and what share that is
#      4. Which day had the highest average bill (all bills,
#         not just big ones)
#      5. A bar chart of average bill by day, saved to
#         charts/my_report.png
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    ==============================================
#       THE COZY BEAN -- EVIDENCE FOR THE BANK
#    ==============================================
#    244 bills across 4 trading days.
#    Average bill: $19.79
#    Average tip:  $3.00
#    Bills over $20: 97 (39.8%)
#    Best day by average bill: Sun ($21.41)
#    Saved charts/my_report.png
#
#  HINT: you have done every one of these pieces already --
#        p01 (shape), p02 (nunique), p03 (filter + mean),
#        p04 (groupby + sort), p07 (chart + savefig).
#        This is assembly, not invention.
#        :.2f gives two decimals; :.1f gives one.
#
#  How to run it: python practice/p08_capstone_report_for_the_bank.py
#                 (run it from inside the M1-W2-Lab02 folder)
#
#  Stuck? See solutions/p08_capstone_report_for_the_bank.py --
#  but give it a real try first. This one is worth it.
# ============================================================

import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/tips.csv")

print("=" * 46)
print("   THE COZY BEAN -- EVIDENCE FOR THE BANK")
print("=" * 46)

# TODO 1: how many bills, across how many trading days
print("? bills across ? trading days.")

# TODO 2: the average bill and the average tip, to 2 decimals
print("Average bill: $?")
print("Average tip:  $?")

# TODO 3: how many bills were over $20, and what percentage
print("Bills over $20: ? (?%)")

# TODO 4: group ALL bills by day, average them, sort biggest
#         first, and report the winner and its average
print("Best day by average bill: ? ($?)")

# TODO 5: bar chart of average bill by day -> charts/my_report.png
plt.figure(figsize=(8, 6))
print("(no chart saved yet)")
