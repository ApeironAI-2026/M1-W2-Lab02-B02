# ============================================================
#  PRACTICE p01 -- Open the Ledger
#  The Cozy Bean  |  M1-W2 Lab02
#
#  YOUR TASK:
#    The loan officer starts gently. Three warm-up questions
#    about the till export:
#      1. How many bills are there, and how many columns?
#      2. What are the columns called?
#      3. Show me the first five.
#
#  WHEN YOU ARE DONE, running this file should print EXACTLY:
#    Bills and columns: (244, 7)
#    Columns: ['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']
#    First five bills:
#       total_bill   tip     sex smoker  day    time  size
#    0       16.99  1.01  Female     No  Sun  Dinner     2
#    1       10.34  1.66    Male     No  Sun  Dinner     3
#    2       21.01  3.50    Male     No  Sun  Dinner     3
#    3       23.68  3.31    Male     No  Sun  Dinner     2
#    4       24.59  3.61  Female     No  Sun  Dinner     4
#
#  HINT: .shape and .columns are ATTRIBUTES -- no brackets.
#        .head() is a METHOD -- brackets.
#        list(df.columns) turns the column names into a plain
#        Week-1 list so they print on one line.
#
#  How to run it: python practice/p01_open_the_ledger.py
#                 (run it from inside the M1-W2-Lab02 folder)
# ============================================================

import pandas as pd

df = pd.read_csv("data/tips.csv")

# TODO 1: print "Bills and columns:" followed by the shape
print("Bills and columns: (not checked yet)")

# TODO 2: print "Columns:" followed by list(df.columns)
print("Columns: (not checked yet)")

# TODO 3: print "First five bills:" then the first five rows
print("First five bills:")
print("(not shown yet)")
