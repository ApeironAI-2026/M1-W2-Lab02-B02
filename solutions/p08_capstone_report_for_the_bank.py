# ============================================================
#  SOLUTION p08 -- CAPSTONE -- Your Report for the Bank
#  The Cozy Bean  |  M1-W2 Lab02
#
#  This is the reference answer. Compare it with yours -- if
#  yours is different but prints the same thing, yours is also
#  correct.
#
#  How to run it: python solutions/p08_capstone_report_for_the_bank.py
#                 (run it from inside the M1-W2-Lab02 folder)
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

# 1. Size of the evidence
print(f"{df.shape[0]} bills across {df['day'].nunique()} trading days.")

# 2. The headline averages
print(f"Average bill: ${df['total_bill'].mean():.2f}")
print(f"Average tip:  ${df['tip'].mean():.2f}")

# 3. The big tables
big = df[df['total_bill'] > 20]
share = big.shape[0] / df.shape[0] * 100
print(f"Bills over $20: {big.shape[0]} ({share:.1f}%)")

# 4. The best day -- filter nothing, group, sort
by_day = df.groupby('day')[['total_bill']].mean()
by_day = by_day.sort_values(by='total_bill', ascending=False)
best_day = by_day.index[0]
best_avg = by_day['total_bill'].iloc[0]
print(f"Best day by average bill: {best_day} (${best_avg:.2f})")

# 5. The chart that backs it up
plt.figure(figsize=(8, 6))
sns.barplot(x=by_day.index, y=by_day['total_bill'])
plt.title('The Cozy Bean -- Average Bill by Day')
plt.xlabel('Day')
plt.ylabel('Average bill ($)')

plt.savefig("charts/my_report.png")
print("Saved charts/my_report.png")

plt.show()
