# 📋 Lab02 Cheat Sheet — The Pandas One-Pager

**The Cozy Bean · M1-W2-Lab02 · Apeiron AI Training Academy**

*Print this one. It is the page you will still be using in a year.*

---

## Setup, once

```text
pip install pandas matplotlib seaborn scipy      # NumPy arrives automatically
py -m pip install pandas matplotlib seaborn scipy    # Windows fallback
python scripts/00_check_setup.py                 # prove it worked
```

## The four imports, every time

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

---

## Load and look

```python
df = pd.read_csv("data/tips.csv")   # path is relative to YOUR TERMINAL's folder

df.head()        # first 5 rows          df.head(20)   # first 20
df.tail()        # last 5 rows           df.tail(10)   # last 10
df.info()        # full inventory: columns, non-null counts, types
df.describe()    # count/mean/std/min/quartiles/max for numeric columns
```

> **ALWAYS look at your data before you do anything to it.** `head()` is the most-typed method in pandas for a reason.

## Attributes vs methods — the brackets rule

| No brackets (facts) | Brackets (actions) |
|---|---|
| `df.shape` → `(244, 7)` | `df.head()` |
| `df.columns` | `df.describe()` |
| `df.dtypes` | `df.mean()` |
| `df.index` | `df.sort_values(...)` |

`df.shape()` → `TypeError: 'tuple' object is not callable`. `dir(df)` lists everything.

---

## Select columns

```python
df['day']                    # one column -> a SERIES
df[['total_bill', 'tip']]    # two columns -> a DATAFRAME
df.day                       # dot notation -- works, but see below
```

> ### ⚠️ The `df.size` trap
> Our table has a `size` column, but every DataFrame also has a built-in `.size`.
> `df.size` → **1708** (244 × 7). **No error. Just wrong.**
> **Use square brackets, always.** They are never ambiguous, and they cope with spaces in names.

## Summarise one column

```python
df['day'].nunique()          # how many DIFFERENT values      -> 4
df['day'].value_counts()     # how many of each, biggest first
df['total_bill'].count()     # how many values                -> 244
df['total_bill'].mean()      # .min() .max() .sum() .std() too
```

---

## Filter — "show me only…"

```python
df[df['total_bill'] > 20]                          # -> 97 rows
df[df['total_bill'] > 20].shape                    # -> (97, 7)
df[df['day'] == 'Sat']
```

### 🔙 Week 1's `and` does NOT work here

```python
df[df['size'] == 3 and df['tip'] > 3]      # ValueError: truth value is ambiguous
df[(df['size'] == 3) & (df['tip'] > 3)]    # ✅ correct
```

| Week 1 (one answer) | pandas (whole columns) |
|---|---|
| `and` | `&` |
| `or` | `\|` |
| `not` | `~` |

**Bracket every condition, every time.**

---

## Sort

```python
df.sort_values(by='total_bill')                       # smallest first
df.sort_values(by='total_bill', ascending=False)      # biggest first
df.sort_values(by=['day', 'total_bill'],
               ascending=[True, False])               # 2 keys, 2 directions
```

> Hands back a **new** table. It does not change `df`. Catch the result.

---

## Group — "pile the receipts by…"

```python
df.groupby('day')[['total_bill', 'tip']].mean()    # one row per pile
df.groupby('day')[['total_bill', 'tip']].min()     # also .max() .sum() .count()

df.groupby('day').agg({                            # several at once
    'total_bill': ['mean', 'sum', 'max'],
    'tip': ['mean', 'sum']
})
```

- The grouping column becomes the **index** (the labels down the left).
- Get the winner after sorting with `result.index[0]`.
- Single brackets → Series. Double brackets → DataFrame.

---

## Missing values

```python
df.isna().sum()              # count gaps per column
df.isna().sum().sum()        # total gaps in the whole table

df['muffins_sold'].mean()                            # .mean() IGNORES gaps
filled = df.copy()
filled['col'] = filled['col'].fillna(filled['col'].mean())

df.dropna()                          # drop any row with any gap
df.dropna(subset=['takings'])        # drop only rows missing THIS column
```

| Choose | When |
|---|---|
| `fillna` | one number missing from an otherwise good row |
| `dropna` | the row is too damaged to trust |

Missing values print as **`NaN`**. Dropping is a decision, not the safe default.

---

## loc and iloc

```python
df.iloc[:10, 2]        # by POSITION -- i for integer
df.loc[0:9, 'total_bill']   # by LABEL
df.loc[0:9]                 # all columns
```

> ### 🔙 The endpoint rule changes
> - Week-1 list slice `[1:3]` → end **left out**
> - `iloc[0:10]` → end **left out** (same as Week 1)
> - `loc[0:9]` → end **INCLUDED**
>
> Both give 10 rows, for different reasons.

---

## Charts

```python
import os
os.makedirs("charts", exist_ok=True)     # matplotlib will NOT create it

plt.figure(figsize=(9, 6))
sns.scatterplot(x='total_bill', y='tip', data=df)      # relationship
sns.boxplot(x='day', y='tip', data=df)                 # compare groups
sns.barplot(x=s.index, y=s.values)                     # one bar per category
sns.heatmap(df.isna(), cbar=False, cmap='viridis')     # map the gaps

plt.title('...'); plt.xlabel('...'); plt.ylabel('...')

plt.savefig("charts/name.png")     # SAVE first...
plt.show()                          # ...THEN show
```

> ⚠️ **`show()` pauses the script until you close the window — and the window may open BEHIND VS Code.** Find it, close it, done. The PNG is already saved.
> ⚠️ **Never `show()` before `savefig()`** or you may write a blank PNG.

---

## A taste of statistics

```python
from scipy import stats
t_stat, p_value = stats.ttest_1samp(df['total_bill'], popmean=20)
```

**Reading the p-value:** *"if the claim were true, how surprising would this data be?"*

| p-value | Means |
|---|---|
| **large** (ours: 0.71) | not surprising — **no reason to doubt the claim** |
| **small** (under 0.05) | this data would be hard to explain if the claim were true |

A large p-value never *proves* the claim. It just fails to argue against it.

---

## Errors you have met

| Error | Means |
|---|---|
| `FileNotFoundError: 'data/tips.csv'` | **wrong folder** — check `pwd` |
| `ModuleNotFoundError: No module named 'pandas'` | not installed, or installed into a different Python |
| `ValueError: The truth value of a Series is ambiguous` | used `and` instead of `&` inside `df[...]` |
| `TypeError: 'tuple' object is not callable` | brackets on an attribute — `df.shape()` |
| `KeyError: 'count'` | no column by that name |

---

## 🚀 Bonus — beyond class

```python
df['day'].value_counts(normalize=True)      # shares, not counts (0.36 = 36%)
filtered['total_bill'].mean()               # any method works on a filtered table
sns.barplot(x=shares.index, y=shares.values)
```
