# ============================================================
#  SOLUTION p06 -- A Recipe Card for the Bank
#  The Cozy Bean  |  M1-W2 Lab02
#
#  How to run it: python solutions/p06_a_function_that_filters.py
#                 (run it from inside the M1-W2-Lab02 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/tips.csv")


def big_bills(data, floor):
    return data[data['total_bill'] > floor]


for floor in [20, 30, 40]:
    result = big_bills(df, floor)
    print(f"Over ${floor}: {result.shape[0]} bills, "
          f"average tip ${result['tip'].mean():.2f}")

# This is a Week-1 recipe card that happens to hand back a
# whole table. Three questions from the bank, one function,
# three calls. Change the rule once and all three answers
# update -- exactly the point of functions in the first place.
