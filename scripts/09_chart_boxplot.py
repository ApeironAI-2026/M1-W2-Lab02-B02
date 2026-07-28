# ============================================================
#  The Cozy Bean -- Script 09: Which Day Tips Best?
#  Lab STEP 20.
#  Run:   python scripts/09_chart_boxplot.py  (from M1-W2-Lab02/)
#
#  ⚠️ Pauses until you close the chart window (it may be hiding
#     behind VS Code). The PNG is saved before the window opens.
# ============================================================

import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/tips.csv")

# Boxplot for tips by day
plt.figure(figsize=(8, 6))
sns.boxplot(x='day', y='tip', data=df)
plt.title('The Cozy Bean -- Tips by Day')
plt.xlabel('Day')
plt.ylabel('Tip ($)')

plt.savefig("charts/tips_by_day.png")
print("Saved charts/tips_by_day.png")

plt.show()

print("Window closed. Script finished.")

# How to read a boxplot, in one go:
#   the line in the middle of each box = the TYPICAL tip
#   the box itself                     = the middle half of tips
#   the whiskers                       = most of the rest
#   the dots beyond them               = unusually generous tables
