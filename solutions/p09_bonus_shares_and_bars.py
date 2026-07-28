# ============================================================
#  SOLUTION p09 -- 🚀 BONUS -- Shares and Bars
#  The Cozy Bean  |  M1-W2 Lab02
#
#  How to run it: python solutions/p09_bonus_shares_and_bars.py
#                 (run it from inside the M1-W2-Lab02 folder)
# ============================================================

import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/tips.csv")

shares = df['day'].value_counts(normalize=True)

print("Share of bills by day:")
print(shares)

print(f"Saturday is {shares['Sat'] * 100:.1f}% of all our bills.")

plt.figure(figsize=(8, 6))
sns.barplot(x=shares.index, y=shares.values)
plt.title('The Cozy Bean -- Share of Bills by Day')
plt.xlabel('Day')
plt.ylabel('Share of all bills')

plt.savefig("charts/share_by_day.png")
print("Saved charts/share_by_day.png")

plt.show()

# normalize=True is the whole trick: same method, one argument,
# counts become shares. Multiply by 100 when you want to say it
# out loud as a percentage.
