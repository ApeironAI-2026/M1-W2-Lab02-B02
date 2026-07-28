# ============================================================
#  The Cozy Bean -- Script 11: Does the Claim Hold Up?
#  Lab STEP 22.
#  Shows: a one-sample t-test, read in one sentence.
#  Run:   python scripts/11_the_claim.py  (from M1-W2-Lab02/)
# ============================================================

import pandas as pd
from scipy import stats

df = pd.read_csv("data/tips.csv")

# Your loan application says: "the average bill is about $20."
# The loan officer asks: do these 244 receipts back that up?
t_stat, p_value = stats.ttest_1samp(df['total_bill'], popmean=20)

print(f"T-test for total_bill: t-stat = {t_stat}, p-value = {p_value}")
print()

print("What the actual average is:", df['total_bill'].mean())
print()

# ---- Reading it, in one sentence --------------------------
# The p-value answers ONE question: "if the true average
# really were $20, how surprising would these 244 receipts
# be?"  A big p-value means "not surprising at all."
#
# Ours is about 0.71 -- very unsurprising. So the receipts
# give us NO reason to doubt the $20 claim. Your application
# is safe.
#
# (A small p-value -- under 0.05 is the usual line -- would
# have meant the opposite: these receipts would be hard to
# explain if the average really were $20.)
print("p-value is large, so the receipts do not contradict")
print("the $20 claim. The application stands.")
