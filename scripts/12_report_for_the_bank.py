# ============================================================
#  The Cozy Bean -- Script 12: The Report for the Bank
#  Lab STEP 23 -- the capstone walkthrough.
#  Shows: everything in this lab, doing one useful job.
#  Run:   python scripts/12_report_for_the_bank.py
#         (from M1-W2-Lab02/)
#
#  ⚠️ Pauses until you close the chart window. PNG saved first.
# ============================================================

import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("charts", exist_ok=True)

# ---- 1. Open the ledger -----------------------------------
df = pd.read_csv("data/tips.csv")

# ---- 2. Keep the big bills --------------------------------
big = df[df['total_bill'] > 20]

# ---- 3. Pile them by day ----------------------------------
by_day = big.groupby('day')[['total_bill', 'tip']].mean()

# ---- 4. Restack: best average bill first ------------------
by_day = by_day.sort_values(by='total_bill', ascending=False)

# ---- 5. Write the findings, in Week-1 f-strings -----------
best_day = by_day.index[0]
best_avg = by_day['total_bill'].iloc[0]

print("=" * 52)
print("   THE COZY BEAN -- SECOND BRANCH LOAN APPLICATION")
print("=" * 52)
print()
print(f"Evidence: {df.shape[0]} bills from the trial table-service season.")
print(f"Average bill across the whole season: ${df['total_bill'].mean():.2f}")
print(f"Average tip across the whole season:  ${df['tip'].mean():.2f}")
print()
print(f"Bills over $20: {big.shape[0]} of {df.shape[0]}"
      f" ({big.shape[0] / df.shape[0] * 100:.1f}% of all bills)")
print()
print("Big-bill days, best first:")
print(by_day)
print()
print(f"FINDING: {best_day} is our strongest day for big tables,")
print(f"averaging ${best_avg:.2f} per bill over $20.")
print()
print("=" * 52)

# ---- 6. One chart for the folder --------------------------
plt.figure(figsize=(8, 6))
sns.barplot(x=by_day.index, y=by_day['total_bill'])
plt.title('The Cozy Bean -- Average Big Bill by Day')
plt.xlabel('Day')
plt.ylabel('Average bill over $20 ($)')

plt.savefig("charts/report_bills_by_day.png")
print("Saved charts/report_bills_by_day.png")

plt.show()

print("Report complete. Take it to the bank.")
