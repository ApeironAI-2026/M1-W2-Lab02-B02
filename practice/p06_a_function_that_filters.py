# ============================================================
#  PRACTICE p06 -- A Recipe Card for the Bank
#  The Cozy Bean  |  M1-W2 Lab02
#
#  YOUR TASK:
#    The officer keeps moving the goalposts: "show me over $20
#    ... no, over $30 ... actually, over $40." Rather than
#    rewriting the filter every time, write it ONCE as a
#    function and call it three times.
#
#    Write big_bills(data, floor) so that it:
#      - takes a DataFrame and a number
#      - RETURNS the rows whose total_bill is above that number
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Over $20: 97 bills, average tip $3.93
#    Over $30: 32 bills, average tip $4.58
#    Over $40: 10 bills, average tip $5.45
#
#  HINT: 🔙 Week 1 -- this is an ordinary function with two
#        parameters and a `return`. The only new part is that
#        the thing it returns is a DataFrame. Because it IS a
#        DataFrame, .shape and .mean() work on the result just
#        as they do on the original.
#
#  How to run it: python practice/p06_a_function_that_filters.py
#                 (run it from inside the M1-W2-Lab02 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/tips.csv")


def big_bills(data, floor):
    # TODO 1: return only the rows where total_bill is above
    #         `floor`
    return data


for floor in [20, 30, 40]:
    result = big_bills(df, floor)
    # TODO 2: fix this line so it reports the count and the
    #         average tip, to 2 decimal places
    print(f"Over ${floor}: {result.shape[0]} bills, average tip $?")
