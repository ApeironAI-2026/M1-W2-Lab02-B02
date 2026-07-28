# ============================================================
#  SOLUTION p07 -- One More Page for the Folder
#  The Cozy Bean  |  M1-W2 Lab02
#
#  How to run it: python solutions/p07_your_own_chart.py
#                 (run it from inside the M1-W2-Lab02 folder)
# ============================================================

import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("charts", exist_ok=True)

df = pd.read_csv("data/tips.csv")

plt.figure(figsize=(8, 6))
sns.boxplot(x='time', y='total_bill', data=df)
plt.title('The Cozy Bean -- Bill Size by Service')
plt.xlabel('Service')
plt.ylabel('Total Bill ($)')

plt.savefig("charts/bills_by_service.png")
print("Saved charts/bills_by_service.png")

plt.show()

print("Window closed. Script finished.")

# savefig BEFORE show, every time. If you show first, the
# window takes over and on some setups the figure is cleared
# by the time savefig runs -- and you get a blank PNG.
