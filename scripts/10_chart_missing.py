# ============================================================
#  The Cozy Bean -- Script 10: A Picture of the Gaps
#  Lab STEP 21.
#  Run:   python scripts/10_chart_missing.py  (from M1-W2-Lab02/)
#
#  ⚠️ Pauses until you close the chart window. PNG saved first.
# ============================================================

import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("charts", exist_ok=True)

# The takings book -- the one with real holes in it.
takings = pd.read_csv("data/cozybean_takings.csv")

# isna() turns the whole table into True/False: True wherever a
# value is missing. A heatmap of that is a MAP of the damage.
plt.figure(figsize=(8, 6))
sns.heatmap(takings.isna(), cbar=False, cmap='viridis')
plt.title('The Cozy Bean -- Where the Takings Book is Smudged')

plt.savefig("charts/takings_gaps.png")
print("Saved charts/takings_gaps.png")

plt.show()

print("Window closed. Script finished.")

# Bright stripes = missing. You should see gaps in
# muffins_sold (3 of them) and takings (2 of them) -- and one
# row, Friday the 18th, that is missing BOTH.
