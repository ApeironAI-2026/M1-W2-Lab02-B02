# ============================================================
#  The Cozy Bean -- Script 04: Finding the Big Bills
#  Lab STEPs 10-12.
#  Shows: boolean filtering, why Week-1's `and` does not work
#         here, and sorting.
#  Run:   python scripts/04_the_big_bills.py  (from M1-W2-Lab02/)
# ============================================================

import pandas as pd

df = pd.read_csv("data/tips.csv")

# ---- Section 1  (STEP 10): show me only the big bills -----
filtered_df = df[df['total_bill'] > 20]
print("\nFiltered rows where total_bill > 20:")
print(filtered_df.head())
print()

# How many of the 244 were big ones?
print("Big bills:", filtered_df.shape)
print()

# ---- Section 2  (STEP 11): two conditions at once ---------
# ⚠️ Week 1's `and` does NOT work inside df[...]. Uncomment
# the next line to meet the error in person:
#
# filtered_data = df[df['size'] == 3 and df['tip'] > 3]
#
# ValueError: The truth value of a Series is ambiguous.
# Use a.empty, a.bool(), a.item(), a.any() or a.all().
#
# Inside df[...] you are combining whole COLUMNS of True/False
# at once, not two single answers. So use & (and) and | (or),
# and wrap each condition in its own brackets.
filtered_data = df[(df['size'] == 3) & (df['tip'] > 3)]
print("Tables of 3 who tipped over $3:")
print(filtered_data.head())
print("How many:", filtered_data.shape)
print()

# ---- Section 3  (STEP 12): restack the receipts -----------
sorted_df = df.sort_values(by='total_bill', ascending=False)
print("\nData sorted by total_bill in descending order:")
print(sorted_df.head())
print()

# Two keys: day first (A-Z), then biggest bill first within
# each day.
sorted_df_multi = df.sort_values(by=['day', 'total_bill'],
                                 ascending=[True, False])
print("Sorted by day, then biggest bill first:")
print(sorted_df_multi.head())
