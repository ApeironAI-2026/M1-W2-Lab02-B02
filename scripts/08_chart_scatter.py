# ============================================================
#  The Cozy Bean -- Script 08: Do Bigger Bills Tip More?
#  Lab STEP 19 -- your first chart.
#  Run:   python scripts/08_chart_scatter.py  (from M1-W2-Lab02/)
#
#  ⚠️ THIS SCRIPT PAUSES. A chart window opens and the terminal
#     waits until you CLOSE it. The window may open BEHIND
#     VS Code -- go and find it. Your PNG is saved either way.
# ============================================================

import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# The script builds its own display folder before pinning any
# charts to it. matplotlib will NOT create this folder for you
# -- without this line, savefig crashes with FileNotFoundError.
os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/tips.csv")

# Scatter plot for total_bill vs tip
plt.figure(figsize=(9, 6))
sns.scatterplot(x='total_bill', y='tip', data=df)
plt.title('The Cozy Bean -- Bill vs Tip (244 bills)')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')

# SAVE first, THEN show. That order matters: it means the file
# exists whether or not you ever look at the window.
plt.savefig("charts/bills_vs_tips.png")
print("Saved charts/bills_vs_tips.png")

plt.show()

print("Window closed. Script finished.")
