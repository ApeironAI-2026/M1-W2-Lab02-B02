# 📖 Lab02 Glossary — every word, one plain sentence

**The Cozy Bean · M1-W2-Lab02 · Apeiron AI Training Academy**

*Week 2 Lab01's words (module, class, object, attribute, method…) are in [its glossary](../Lab01/GLOSSARY.md) and still apply — a DataFrame is an object, and `pd` is a module.*

---

## The story words

| Story | Python | Meaning |
|---|---|---|
| the big ledger book the till printed | **DataFrame** | a table of rows and columns |
| one column of figures | **Series** | a single labelled column |
| peeking at the first / last pages | **`head()` / `tail()`** | show the first or last few rows |
| "show me only the big bills" | **filtering** | keeping only the rows that match a condition |
| sorting receipts into piles by day | **`groupby`** | splitting rows into groups to summarise each |
| working out what each pile is worth | **aggregation** | reducing a group to one number, like a mean or a sum |
| restacking the receipts biggest-first | **`sort_values`** | reordering rows by a column |
| smudged entries in the takings book | **missing values** (`NaN`) | cells where no value was recorded |
| the summary page the bank reads first | **`describe()`** | the eight headline statistics per numeric column |
| what goes in the loan-application folder | **charts** | pictures saved as PNG files |
| the loan officer's raised eyebrow | **p-value** | how surprising your data would be if a claim were true |

---

## A–Z

**aggregation** — computing one summary number for a group: a mean, a sum, a count, a maximum. `agg()` does several at once.

**`agg()`** — a method taking a dictionary of `column: [what to work out]`, so you can compute several statistics per column in one call.

**alias** — the nickname a library is imported under. `import pandas as pd` makes `pd` the alias. The four standard ones are `pd`, `np`, `plt`, `sns`.

**attribute** — a fact a DataFrame carries, written with **no brackets**: `df.shape`, `df.columns`, `df.dtypes`.

**boolean indexing** — the proper name for filtering: building a column of True/False and using it to pick rows, as in `df[df['total_bill'] > 20]`.

**boxplot** — a chart showing a group's whole spread: the middle line is the typical value, the box is the middle half, the whiskers are most of the rest, and the dots are unusual values.

**`count()`** — how many values a column has.

**CSV** — "comma-separated values": a table saved as plain text with commas between the values. What `read_csv` reads.

**DataFrame** — pandas' table: rows, columns and a header. The central object of this entire lab.

**`describe()`** — a method printing count, mean, std, min, the three quartiles and max for every numeric column.

**`dropna()`** — removes every row that has a missing value in it. Use `subset=['col']` to only consider one column.

**`dtypes`** — an attribute listing what kind of data each column holds. `float64` and `int64` are Week-1's `float` and `int`; text shows as `str` on newer pandas and `object` on older ones — the same thing, relabelled.

**`fillna(value)`** — replaces missing values with something. Filling with the column's mean is common and often honest.

**filtering** — keeping only the rows that match a condition. See boolean indexing.

**`groupby()`** — splits rows into groups by the values in a column, so each group can be summarised. The grouping column becomes the index of the result.

**heatmap** — a chart that paints a grid of values as colours. On `df.isna()` it becomes a map of exactly where your data is missing.

**`iloc`** — select by **position** (i for *integer*). Follows Week 1's slicing rule: the end is **left out**.

**index** — the labels down the left-hand side of a DataFrame. Starts at 0 by default, and survives filtering and sorting rather than renumbering.

**`info()`** — a method printing the full inventory of a table: every column, its non-null count and its type.

**`isna()`** — turns a table into True/False, True wherever a value is missing. Add `.sum()` to count them per column.

**`loc`** — select by **label**. Unlike Week-1 slicing and unlike `iloc`, its end label is **included**.

**matplotlib** — the charting library. Imported as `plt`; handles figures, titles and axis labels.

**mean** — the average: everything added up, divided by how many. In pandas it **ignores** missing values rather than counting them as zero.

**median** — the middle value, shown as `50%` in `describe()`. When the mean is well above the median, a few large values are pulling the average up.

**`NaN`** — "Not a Number": how pandas writes a missing value.

**`normalize=True`** *(🚀 bonus)* — an argument to `value_counts()` that returns shares instead of counts, so `0.36` means 36%.

**NumPy** — the library for fast maths on many numbers at once. Imported as `np`. Installed automatically with pandas, and running quietly underneath everything you did today.

**`nunique()`** — how many **different** values a column contains.

**`os.makedirs("charts", exist_ok=True)`** — creates the folder if it is not already there. Chart scripts need it because matplotlib will not create a folder for you.

**pandas** — the library for working with tables. Imported as `pd`. The tool this lab exists to teach.

**p-value** — the answer a statistical test gives: *if the claim were true, how surprising would this data be?* Large means unsurprising (no reason to doubt the claim); small (under 0.05 by convention) means the data argues against it.

**`plt.savefig(path)`** — saves the current chart to a file. Always call it **before** `plt.show()`.

**`plt.show()`** — displays the chart in a window, and **pauses the script until you close it**. The window may open behind your editor.

**quartile** — the 25%, 50% and 75% rows of `describe()`: the values below which a quarter, half and three quarters of the data fall.

**`read_csv(path)`** — reads a CSV file and hands back a DataFrame. The path is relative to the folder your terminal is standing in.

**scikit-learn** — the machine-learning library. Mentioned today, used later in the course.

**SciPy** — scientific algorithms, including the statistics used in STEP 22.

**seaborn** — a charting library built on matplotlib that draws attractive statistical charts from a DataFrame in one line. Imported as `sns`.

**Series** — a single column of a DataFrame: values in order, each with an index label. Essentially Week 1's list, labelled.

**`shape`** — an attribute giving `(rows, columns)`. Ours is `(244, 7)`.

**`sort_values(by=...)`** — reorders rows by a column. `ascending=False` puts the biggest first. Hands back a new table.

**statsmodels** — a library for regressions and hypothesis tests in an R-like style. Mentioned in class; not used today.

**std (standard deviation)** — how spread out the values are. Small means they are all alike; large means they vary a lot.

**t-test** — a statistical test comparing your data against a claimed value. `ttest_1samp(column, popmean=20)` asks whether the data is consistent with an average of 20.

**third-party library** — code written by someone else that you install yourself, rather than something that comes with Python. All four of today's are third-party.

**`value_counts()`** — how many times each value appears in a column, sorted with the most common first.
