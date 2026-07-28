# ☕ M1-W2-Lab02 — The Second Branch: The Bank Wants Numbers

### Pandas & the Data-Analysis Toolkit
**Apeiron AI Training Academy** · *"Boundless Possibilities, Infinite Potential"*

| | |
|---|---|
| **Module** | M1: AI/ML Fundamentals |
| **Week** | Week 2 |
| **Lab** | Lab02 — The Second Branch: The Bank Wants Numbers |
| **Duration** | **≈ 4 hours 15 minutes** of lab work (**plus ~30 minutes of one-time setup, not counted**) |
| **Difficulty** | ⭐⭐ Beginner, level 2 — you've got Week 1 behind you |

> 🛋️ **Split this across two or three sittings.** A natural break is after **Cluster E**, when you can load a table, look at it, filter it, sort it and group it — everything before the charts. That is already enough pandas to be useful at work.

### What you learned in class (and will now make your own)

The Python ML toolbox · `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy` · `read_csv` · `head()` / `tail()` · `info()`, `shape`, `columns`, `dtypes` · attributes vs methods · selecting columns · `nunique()`, `value_counts()`, `count()` · boolean filtering · combined conditions · `sort_values()` · `groupby()` and `agg()` · `describe()` · missing values, `isna()`, `fillna()`, `dropna()` · `loc` and `iloc` · scatter plots, boxplots and heatmaps · a one-sample t-test

---

## 1. ☕ The Story

The dream is real. There is an empty unit two streets over — bigger than The Cozy Bean, with a proper kitchen and room for twelve tables — and it would make a beautiful **sit-down café**. Table service. Lunch and dinner. Actual waiters.

You cannot fund that out of the till. So on Monday morning you are taking a loan application to the bank.

The loan officer is called Mrs Adeyemi, she is perfectly friendly, and she is completely unmoved by how nice your coffee is. She wants **evidence**. Specifically, she wants to know whether people will actually sit down and spend money in a Cozy Bean with tables in it — because that is a different business from selling flat whites to people on their way to work.

Luckily, you thought of this. Last season you ran a **trial table-service season**: Thursday to Sunday, lunch and dinner, proper table service, for a few months. And the till recorded every single bill. **244 of them** — what each table spent, what they tipped, how many people were sitting there, which day, and whether it was lunch or dinner.

That export is sitting in `data/tips.csv`, and it is the whole lab.

Marcus and Priya were at a fair few of those tables, incidentally. Priya still insists the Sunday lunch rush was her idea, and by the end of today the receipts will have settled it one way or the other.

Every idea in this lab is a physical thing in that meeting with Mrs Adeyemi:

- the **DataFrame** is the big ledger book the till printed
- `head()` and `tail()` are peeking at the first and last pages
- **filtering** is *"show me only the big bills"*
- **`groupby`** is sorting the receipts into piles by day
- **sorting** is restacking them biggest-first
- **charts** are what physically goes into the loan-application folder
- and the **t-test** at the end is Mrs Adeyemi looking over her glasses and saying: *"Your application says the average bill is about twenty dollars. Do these receipts back that up?"*

### Why this matters in real life (and in AI/ML)

This one needs no stretching at all.

- **Pandas is the daily tool of every data person alive.** Not an exaggeration. `read_csv` → `head` → `describe` → filter → `groupby` is literally the first hour of every real data job, every time, for everyone.
- **Every ML model is fed by a DataFrame you prepared exactly this way.** In later modules you will train models. The training data will arrive as a CSV, and getting it clean and shaped is this lab, repeated.
- **"Do the numbers back up the claim?"** is the entire job.** Today you answer it for a loan officer. Later you will answer it for a model, and the question will not have changed.

### ✅ Success Criteria — what you will be able to produce

- `python scripts/00_check_setup.py` — proof your four new libraries are installed
- `python scripts/02_opening_the_ledger.py` — 244 bills loaded and inspected
- `python scripts/03_one_column.py` — one column at a time, and one famous trap
- `python scripts/04_the_big_bills.py` — the 97 big bills, found and sorted
- `python scripts/05_receipt_piles.py` — receipts piled by day and summarised
- `python scripts/06_smudged_receipts.py` — missing values found, filled and dropped
- `python scripts/07_labels_vs_positions.py` — `loc` and `iloc`, side by side
- **three charts of your own** in `charts/`, made by scripts 08, 09 and 10
- `python scripts/11_the_claim.py` — a real statistical test, read in one sentence
- `python scripts/12_report_for_the_bank.py` — **the finished report**
- …and eight practice problems, including a capstone report in your own words.

---

## 2. 🎯 Learning Objectives

By the end of this lab you will be able to:

1. Name the six libraries in the Python data toolbox and say what each is for.
2. Install third-party libraries with `pip`, and check they worked.
3. Load a CSV into a **DataFrame** and inspect it with `head()`, `tail()`, `info()` and `shape`.
4. Tell an **attribute** from a **method**, and say why `df.size` is a trap.
5. Select columns, and explain the difference between a **Series** and a **DataFrame**.
6. Summarise one column with `nunique()`, `value_counts()` and `count()`.
7. **Filter** rows with a condition, combine two conditions correctly, and sort the result.
8. **Group** rows and aggregate each pile with `mean()`, `min()` and `agg()`.
9. Read `describe()` line by line, in plain English.
10. Find missing values and choose honestly between `fillna()` and `dropna()`.
11. Draw, label and **save** a chart with seaborn and matplotlib.
12. Run a one-sample t-test and read its p-value in one sentence.

---

## 3. 🔧 Before You Start — **this week the setup IS a lesson**

> ### ⏱️ Set aside about 30 minutes for this section, and do not rush it.
>
> This is the first time you install software that other people wrote. It is a genuine milestone, it is how every real project starts, and it goes wrong for almost everybody at least once. Every way it commonly goes wrong is in the table below.

### 3.1 What is about to change

Until now, everything you have used came with Python. Today you add four **third-party libraries** — code written by other people, downloaded from the internet, and installed once onto your computer. After today they are simply there, like `math` is.

### 3.2 Install them

> 📥 **Not cloned this lab yet?** The [README](README.md#1--get-this-repo-onto-your-computer) walks you through it: click the GitHub Classroom link from Google Classroom, copy your own repo address, and clone it into `AperionAI/Module1/Week2/Lab02`. Do that first.

**File → Open Folder…** on your **`Lab02`** folder, then **Terminal → New Terminal**, and type this:

```text
pip install pandas matplotlib seaborn scipy
```

On **Windows**, if that is not recognised, use this instead — and then keep using the `py -m` style for the rest of the lab:

```text
py -m pip install pandas matplotlib seaborn scipy
```

On **Mac**:

```text
python3 -m pip install pandas matplotlib seaborn scipy
```

It will print a lot of scrolling text for a minute or two. **What success looks like** is a final line starting:

```text
Successfully installed ...
```

> 💡 **You asked for four libraries. You will see more than four install.** That is correct and nothing is wrong — **NumPy arrives automatically** because pandas needs it, so pip fetches it for you. You never have to ask for NumPy by name. This is one of the nicest things about pip.

### 3.3 Prove it worked

```text
python scripts/00_check_setup.py
```

📺 **Expected output** (your version numbers will differ, and that is fine):

```text
=== THE COZY BEAN -- KITCHEN INSPECTION ===

  ✅  pandas       3.0.3
  ✅  numpy        2.4.6
  ✅  matplotlib   3.10.9
  ✅  seaborn      0.13.2
  ✅  scipy        1.17.1

All five ready. You can start the lab.
```

**Five ticks and you are done.** If any line has a ❌ next to it, the script tells you the exact command to fix that one. Run the script again afterwards — it is safe to run as many times as you like.

### 3.4 "If you see this, do this" — the setup table

| What you see | What it means | What to do |
|---|---|---|
| `'pip' is not recognized…` | Windows cannot find pip on its own | Use `py -m pip install pandas matplotlib seaborn scipy`. This asks *Python* to run pip, which always works. Then use `py` for everything else too. |
| `SSL: CERTIFICATE_VERIFY_FAILED`, `ProxyError`, or it hangs on "Collecting…" | You are on a company or campus network that inspects internet traffic | Try again on home wifi first — that fixes it 90% of the time. If you must use the work network, ask IT for the proxy settings. Or skip installing entirely and use the **Colab path** in §3.6. |
| It said `Successfully installed`, but you still get `ModuleNotFoundError: No module named 'pandas'` | **You have more than one Python**, and pip installed into the other one | Use the same one for both: `py -m pip install pandas` then `py scripts/00_check_setup.py`. Whichever prefix you pick, use it for *everything* in this lab. |
| `FileNotFoundError: [Errno 2] No such file or directory: 'data/tips.csv'` | 🔙 Week 1's classic — **you are running from the wrong folder** | Type `pwd`. It must end in `Lab02`. Type `ls` — you must be able to see `data`. If not: **File → Open Folder** on your `Lab02` folder, then a fresh terminal. |
| **The terminal froze after a chart appeared** | It has not frozen. The script is waiting for you to close the chart window — **and the window may be hiding behind VS Code** | Find it (check your taskbar), admire your chart, close it. The script finishes immediately. **Your PNG was already saved** before the window ever opened. |
| `charts/` has appeared and you never made it | Correct — the chart scripts build it themselves | Nothing to do. STEP 19 explains. |

### 3.5 Where the data lives

The `data/` folder ships with **both** files you need:

| File | What it holds |
|---|---|
| `data/tips.csv` | the till export — **244 bills** from the trial table-service season |
| `data/cozybean_takings.csv` | the shop's handwritten daily takings book, typed up — **with real gaps in it** |

**Nothing in this lab needs the internet once the install is done.** You can do the whole thing on a train.

> 📌 **You saw this in class:** your instructor loaded the data straight from a web address —
>
> ```python
> url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
> df = pd1.read_csv(url)
> ```
>
> That works, and it is worth knowing you *can* read a CSV straight off the web. We use the local copy instead so that a flaky connection can never stop your lab.

### 3.6 🌐 The Google Colab path (the alternative — no install at all)

The class session ran in **Google Colab**, and you can do this whole lab there instead. In Colab:

- **All four libraries are already installed.** There is nothing to `pip`. Skip §3.2 entirely.
- **Upload the data**: click the folder icon in the left sidebar, then the upload button, and upload `data/tips.csv` and `data/cozybean_takings.csv`. Then read them without the `data/` part: `pd.read_csv("tips.csv")`.
- **Or read the class URL directly**, exactly as the 📌 callout above shows.
- **Charts appear underneath the cell** instead of in a window, so `plt.show()` never pauses anything and the "frozen terminal" row above will never happen to you.

Everything else in this lab — every line of code, every expected output — is identical.

---

## 4. 📖 Guided Walkthrough

Twenty-three steps in ten groups. Same rhythm as always: read the STEP, run the script, compare to the 📺 block, do the 🎤 tweak.

> ### 📌 A note about your screen versus your instructor's
>
> pandas changes a little between versions. In class, text columns were described as `object`; on a newer pandas they are described as `str`. **It is the same column, differently labelled.** If your output says `object` where this lab says `str`, you have a slightly older pandas and absolutely everything else still matches. No numbers are affected — only the word used to describe text.

---

## ☕ Cluster A — What's in the Accountant's Bag

*Script for this cluster:* **`scripts/01_the_toolbox.py`**

---

### STEP 1 — Six tools, one line each

▶ *In your script:* Section 2 of `scripts/01_the_toolbox.py`

🎯 **Objective:** Know what each library in the toolbox is for.

☕ **Story moment:** Your accountant arrives for the loan meeting carrying a bag. Inside it are six tools. You do not need to know how any of them work today — you need to know which one to reach for.

🧠 **The idea in plain English:**

| Library | What it is for | Today? |
|---|---|---|
| **NumPy** | fast maths on a great many numbers at once | behind the scenes |
| **SciPy** | scientific algorithms — and the statistics we use at the end | STEP 22 |
| **Pandas** | **tables.** The one you will actually live in | ⭐ all of it |
| **scikit-learn** | the machine-learning algorithms | later in the course |
| **Matplotlib** | charts | STEPs 19–21 |
| **Seaborn** | prettier statistical charts, built on Matplotlib | STEPs 19–21 |

You also heard **statsmodels** mentioned — regressions and hypothesis tests in an R-like style. Like scikit-learn, it is a road sign for later, not a stop today.

Two things worth noticing. First, several of these are built **on top of** each other: seaborn is built on matplotlib, and pandas and scipy are both built on NumPy. You are not learning six unrelated things. Second, **pandas is the one that matters today**, and honestly it is the one that matters most for the next several years.

📺 **Expected output:**

```text
=== THE ACCOUNTANT'S BAG ===

numpy       2.4.6 - fast maths on a great many numbers
pandas      3.0.3 - tables. THE one you will live in
matplotlib  3.10.9 - charts
seaborn     0.13.2 - prettier statistical charts
scipy       1.17.1 - scientific algorithms + statistics

scikit-learn  - the machine-learning algorithms (later in the course)
statsmodels   - regressions and hypothesis tests, R-style (later)

Today is entirely pandas, with three charts at the end.
```

✅ **Verify:** Five version numbers. They will not match mine exactly, and that does not matter at all.

🎤 **Try it yourself (30 seconds):** Look at your five version numbers and compare them with a classmate's. Different numbers, identical lab. Version differences are normal life in this job.

---

### STEP 2 — The four import lines

▶ *In your script:* Section 1 of `scripts/01_the_toolbox.py`

🎯 **Objective:** Write the four imports every data script on earth begins with.

☕ **Story moment:** Every trade has its shorthand. Ask any barista for "a flat white" and nobody says "a drink of espresso with steamed microfoam". Data people have exactly the same habit with these four libraries.

🧠 **The idea in plain English:** 🔙 In Lab01 you learned `import x`. There is one more form: `import x as y`, which imports it **under a nickname**.

These four nicknames are a worldwide convention. Not a rule — a convention so strong that breaking it makes your code harder for everyone else to read:

💻 **The code:**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

That is why the rest of this lab says `pd.read_csv(...)` rather than `pandas.read_csv(...)`.

⚠️ **Common mistake:** Inventing your own nickname. It runs perfectly and it will confuse every person who ever reads your code — including you, in three months. **Use `pd`.**

✅ **Verify:** Nothing prints from these four lines. Silence is success; they only fetch the tools.

🎤 **Try it yourself (30 seconds):** Type `print(pd.__version__)` at the bottom. You just asked pandas its own version, using its nickname.

> 📌 **You saw this in class:** your instructor's notebook opened with these same four imports. One small difference worth knowing about: the class notebook nicknamed pandas `pd1` rather than `pd`, so its later cells read `pd1.read_csv(...)`. **`pd` is the universal convention** and it is what you will find in every book, every tutorial and every codebase, so that is what we use here.

---

## ☕ Cluster B — Opening the Ledger

*Script for this cluster:* **`scripts/02_opening_the_ledger.py`**

---

### STEP 3 — Open the ledger

▶ *In your script:* Section 1 of `scripts/02_opening_the_ledger.py`

🎯 **Objective:** Load a CSV file into a DataFrame.

☕ **Story moment:** The till export is a plain text file of 244 lines, each one a bill. You *could* open it with Week 1's `open()` and pick it apart with `.split(",")` by hand. You will not, because one line of pandas does the whole thing and hands you something far more useful.

🧠 **The idea in plain English:** A **CSV** file is a table saved as text, with commas between the values. `pd.read_csv(path)` reads one and hands back a **DataFrame** — pandas' name for a table.

A DataFrame is the ledger book: rows (each a bill), columns (each a kind of fact), and a header naming the columns.

💻 **The code:**

```python
import pandas as pd

df = pd.read_csv("data/tips.csv")
```

📺 **Expected output:** nothing at all. 🔙 A script only shows what you `print()`. The ledger is open on the counter; nobody has read from it yet.

⚠️ **Common mistake:** Running it from the wrong folder. The path `data/tips.csv` is relative to where your **terminal** is standing, exactly as in Week 1. If you get `FileNotFoundError: [Errno 2] No such file or directory: 'data/tips.csv'`, check `pwd` before anything else.

✅ **Verify:** No output and no error. That is exactly right.

🎤 **Try it yourself (30 seconds):** `df` is a normal variable, so 🔙 Week 1's `type()` works on it: add `print(type(df))`. You get `<class 'pandas.DataFrame'>` — a DataFrame is an **object**, exactly like the espresso machine you built yesterday.

---

### STEP 4 — Peeking at the first pages

▶ *In your script:* Section 2 of `scripts/02_opening_the_ledger.py`

🎯 **Objective:** Look at the top and bottom of a table without printing all 244 rows.

☕ **Story moment:** You do not read a ledger cover to cover. You flip it open, glance at the first page to see what shape it is in, then check the last page to see where it ends.

🧠 **The idea in plain English:** `head()` shows the first five rows; `head(n)` shows the first `n`. `tail()` does the same from the bottom. These two are the most-typed methods in all of pandas, and for good reason: **always look at your data before you do anything to it.**

💻 **The code:**

```python
print(df.head())
print(df.head(2))
print(df.tail(3))
```

📺 **Expected output:**

```text
First 5 records of the dataset:
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4

Just the first 2:
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3

The last 3 bills of the season:
     total_bill   tip     sex smoker   day    time  size
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2
```

**Now read what is actually in your ledger:**

| Column | What it is |
|---|---|
| `total_bill` | what the table spent, in dollars |
| `tip` | what they left on top |
| `sex`, `smoker` | two things the old till software recorded about whoever paid |
| `day` | Thur, Fri, Sat or Sun |
| `time` | Lunch or Dinner |
| `size` | **how many people were at the table** |

A straight word about `sex` and `smoker`: they are in the export because the till software of the day asked for them. They are not what Mrs Adeyemi is asking about, and we do not build anything on them in this lab. But you will see them in every `head()`, so you deserve to know what they are rather than wonder.

🔙 Also notice the numbers down the left: 0, 1, 2, 3, 4. That is the **index** — the row labels — and it starts at **0**, exactly like a Week-1 list.

⚠️ **Common mistake:** `print(df)` on a big table. pandas politely truncates the middle with `...`, but you still get a screenful. Use `head()`.

✅ **Verify:** Five rows, then two, then the last three. The last row is number 243 — because counting started at 0, so 244 bills end at 243.

🎤 **Try it yourself (30 seconds):** The class exercise: read the first 10, then 20, then 50 rows. Then work out for yourself how to see the last few. *(You already know: `tail()`.)*

> 📌 **You saw this in class:** `df.head()`, `df.head(2)` and `df.tail(10)` — the same three calls, on this same data. And the class's own hands-on exercise was exactly the 🎤 above: *"Try to read the first 10, 20, 50 records; can you guess how to view the last few?"*

---

### STEP 5 — How big is this book?

▶ *In your script:* Section 3 of `scripts/02_opening_the_ledger.py`

🎯 **Objective:** Get the size and full inventory of a table.

☕ **Story moment:** Before Mrs Adeyemi will look at a single number, she wants to know how much evidence there is. *"How many bills, exactly?"*

🧠 **The idea in plain English:** `df.shape` hands back `(rows, columns)`. `df.info()` prints a full inventory: every column, how many non-empty values it has, and what kind of data is in it.

💻 **The code:**

```python
print("Shape (rows, columns):", df.shape)
df.info()
```

📺 **Expected output:**

```text
Shape (rows, columns): (244, 7)

The full inventory:
<class 'pandas.DataFrame'>
RangeIndex: 244 entries, 0 to 243
Data columns (total 7 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   total_bill  244 non-null    float64
 1   tip         244 non-null    float64
 2   sex         244 non-null    str    
 3   smoker      244 non-null    str    
 4   day         244 non-null    str    
 5   time        244 non-null    str    
 6   size        244 non-null    int64  
dtypes: float64(2), int64(1), str(4)
memory usage: 17.3 KB
```

**244 rows, 7 columns.** That is your evidence pack, and it is a real number you can say out loud in a bank.

Look at the `Non-Null Count` column: every single one says `244 non-null`. **Nothing is missing anywhere in this file.** Hold that thought — STEP 16 comes back to it.

🔙 And `float64`, `int64` — those are Week 1's `float` and `int`, with the number of bits tacked on. Same types you already know.

⚠️ **Common mistake:** Writing `df.shape()` with brackets. `shape` is an **attribute**, not a method — brackets give you `TypeError: 'tuple' object is not callable`. The next STEP is entirely about this distinction.

✅ **Verify:** `(244, 7)`, and seven columns each with `244 non-null`.

🎤 **Try it yourself (30 seconds):** Print `df.shape[0]` — just the row count, 🔙 indexed out of the tuple exactly as in Week 1. That is how you get "244" into a sentence.

> 📌 **You saw this in class:** `df.info()` and `df.shape` → `(244, 7)`, both on this data. *(Your instructor's screen said `object` where yours says `str`, and `13.5+ KB` where yours says `17.3 KB` — that is the pandas version difference from the note at the top of this walkthrough. The seven columns and 244 rows are identical.)*

---

### STEP 6 — Names, types, and the brackets rule

▶ *In your script:* Section 4 of `scripts/02_opening_the_ledger.py`

🎯 **Objective:** Get column names and types, and nail the attribute-versus-method distinction.

☕ **Story moment:** This is the single most common thing that trips people up in their first week of pandas, and it takes thirty seconds to learn properly. So let us learn it properly.

🧠 **The idea in plain English:** 🔙 Yesterday's STEP 20, word for word:

| Kind | What it is | Brackets? | Example |
|---|---|---|---|
| **attribute** | a fact the table carries | **no** | `df.shape`, `df.columns`, `df.dtypes` |
| **method** | something the table does | **yes** | `df.head()`, `df.describe()` |

This point was made in class, and it is worth the thirty seconds because getting it wrong produces a confusing error rather than an obvious one.

💻 **The code:**

```python
print(df.columns)
print(df.dtypes)
```

📺 **Expected output:**

```text
Column names:
Index(['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size'], dtype='str')

What kind of thing is in each column:
total_bill    float64
tip           float64
sex               str
smoker            str
day               str
time              str
size            int64
dtype: object
```

⚠️ **Common mistake:** Guessing which is which. When you are not sure, 🔙 Lab01 STEP 9's `dir()` still works: `dir(df)` lists everything a DataFrame has. It is a long list, but it is there.

✅ **Verify:** Seven column names, then seven types. Two `float64`, one `int64`, four text columns.

🎤 **Try it yourself (30 seconds):** Deliberately type `df.columns()` with brackets and read the error. Then take them off. Meeting this error once on purpose is much better than meeting it by accident at 11 p.m.

---

### 🧠 Quick Quiz #1 — answer from memory, before peeking

*(Answers are in the **Answer Key** at the end. No scrolling ahead.)*

**Q1.** Which library is the table one — the one you will live in?

- A) NumPy
- B) Pandas
- C) Matplotlib
- D) SciPy

**Q2.** `df.shape` gave `(244, 7)`. What is the 7?

- A) The number of rows
- B) The number of trading days
- C) The number of missing values
- D) The number of columns

**Q3.** How do you see the LAST ten rows?

- A) `df.head(10)`
- B) `df.last(10)`
- C) `df.tail(10)`
- D) `df.bottom(10)`

---

## ☕ Cluster C — One Column at a Time

*Script for this cluster:* **`scripts/03_one_column.py`**

---

### STEP 7 — Pulling out one column

▶ *In your script:* Section 1 of `scripts/03_one_column.py`

🎯 **Objective:** Select a column, and meet the Series.

☕ **Story moment:** Mrs Adeyemi does not want the whole ledger. She wants one column of figures at a time — *"just show me the days"*.

🧠 **The idea in plain English:** Two ways to ask for a column:

```python
df['day']     # square brackets -- always works
df.day        # dot notation -- looks tidier, sometimes lies
```

And an important new word. One column on its own is not a DataFrame — it is a **Series**: a single column of values with an index attached.

🔙 **Remember from Week 1:** a Series is essentially a **labelled list**. Values in order, each with a label, all the same kind of thing.

Single brackets give you a Series. **Double** brackets give you back a (smaller) DataFrame:

```python
df['total_bill']              # a Series
df[['total_bill', 'tip']]     # a DataFrame with 2 columns
```

💻 **The code:**

```python
print(df['day'].head())
print(df.day.head())

print(type(df['total_bill']))
print(type(df[['total_bill', 'tip']]))
```

📺 **Expected output:**

```text
Square brackets:
0    Sun
1    Sun
2    Sun
3    Sun
4    Sun
Name: day, dtype: str

Dot notation -- same answer:
0    Sun
1    Sun
2    Sun
3    Sun
4    Sun
Name: day, dtype: str

One column -> a Series:
<class 'pandas.Series'>
Two columns -> a DataFrame:
<class 'pandas.DataFrame'>
```

Notice the Series prints differently from a DataFrame: no column headers across the top, just labels down the left and a `Name:` at the bottom telling you which column it was.

⚠️ **Common mistake:** Forgetting that column names are **text**, so they need quotes. `df[day]` (no quotes) gives `NameError: name 'day' is not defined` — Python thinks you are naming a variable.

✅ **Verify:** The same five `Sun` values twice, then the two type lines.

🎤 **Try it yourself (30 seconds):** Print `df[['day', 'time']].head()`. Two columns, so a DataFrame — and it prints with headers again.

> 📌 **You saw this in class:** `df['day'].head()` and `df.day.head()`, side by side, producing the same five rows.

---

### STEP 8 — When dot notation lies to you

▶ *In your script:* Section 2 of `scripts/03_one_column.py`

🎯 **Objective:** See a wrong answer arrive with no error at all.

☕ **Story moment:** This is the most dangerous thing in the whole lab, and it is dangerous precisely because **nothing goes wrong**. No red text. No traceback. Just a number in your loan application that is completely made up.

🧠 **The idea in plain English:** Dot notation works by asking the DataFrame for something by name. But a DataFrame already has lots of built-in attributes of its own — and **if a column name collides with one of them, the built-in wins.** Silently.

Our table has a column called `size` — the number of people at the table. Every DataFrame also has a built-in `.size` attribute, meaning "how many cells are in this table altogether".

Guess which one `df.size` gives you.

💻 **The code:**

```python
print(df['size'].head(3))     # the column we wanted
print(df.size)                # NOT the column
```

📺 **Expected output:**

```text
df['size'] -- the column we wanted:
0    2
1    3
2    3
Name: size, dtype: int64

df.size -- NOT the column. No error. Just wrong:
1708
```

**1708.** That is 244 rows × 7 columns. It is not a party size, it is not a bill, it is not anything you asked for — and pandas handed it over without a murmur.

Imagine putting *that* in front of a loan officer.

⚠️ **Common mistake:** Trusting dot notation because it is prettier. It also breaks on any column name with a space in it (`df.total bill` is not even valid Python). **Use square brackets. Always. It is never ambiguous, and it always means the column.**

✅ **Verify:** Three party sizes (2, 3, 3), then the nonsense `1708`.

🎤 **Try it yourself (30 seconds):** Try `df.count` (no brackets) — another collision, since `count` is a method. You get a description of the method rather than any data at all. Then try `df['count']` and read the `KeyError`: there genuinely is no column called `count`, and pandas says so honestly.

> 📌 **You saw this in class:** exactly this point was made with a different column name —
>
> > *"Note: There is an attribute `rank` for pandas data frames, so to select a column with a name "rank" we should use method 1."*
>
> "Method 1" is the square brackets. Our table has no `rank` column, so we have demonstrated the same trap live using the one it *does* have: `size`.

---

### STEP 9 — What one column can tell you

▶ *In your script:* Section 3 of `scripts/03_one_column.py`

🎯 **Objective:** Summarise a single column three ways.

☕ **Story moment:** *"How many days a week were you open? And were they evenly busy?"* Two questions, two one-line answers.

🧠 **The idea in plain English:**

| Method | Answers |
|---|---|
| `.nunique()` | how many **different** values are in this column? |
| `.value_counts()` | how many of **each**? |
| `.count()` | how many values are there in total? |

💻 **The code:**

```python
print("How many different days did we trade?", df['day'].nunique())
print(df['day'].value_counts())
print("How many bills in total?", df['total_bill'].count())
```

📺 **Expected output:**

```text
How many different days did we trade? 4

How many bills on each day?
day
Sat     87
Sun     76
Thur    62
Fri     19
Name: count, dtype: int64

How many bills in total? 244
```

**Your first real finding.** Saturday and Sunday together are 163 of the 244 bills — and Friday, at 19, is barely worth opening for. That is a fact about your business that you did not know an hour ago, and it came out of three lines of code.

⚠️ **Common mistake:** Expecting `value_counts()` in alphabetical order. It sorts by **count**, biggest first — which is almost always what you want when you are about to say "our busiest day is…".

✅ **Verify:** `4`, then the four days with Sat on top, then `244`.

🎤 **Try it yourself (30 seconds):** Run `df['time'].value_counts()`. Dinner or lunch — which is your real business?

> 📌 **You saw this in class:** `df['day'].nunique()` → `4`, and `df['day'].value_counts()` with exactly these four numbers. The hands-on exercise in class asked these same questions about a "salary" column in a different dataset — here they are, asked about your bills instead.

> ### 🚀 Bonus — beyond class: percentages instead of counts
>
> Banks think in percentages. Same method, one extra argument:
>
> ```python
> print(df['day'].value_counts(normalize=True))
> ```
>
> ```text
> day
> Sat     0.356557
> Sun     0.311475
> Thur    0.254098
> Fri     0.077869
> Name: proportion, dtype: float64
> ```
>
> `0.356557` means 35.7% of all bills fell on a Saturday. Multiply by 100 when you want to say it out loud. Practice problem 🚀 p09 turns these into a bar chart.

---

### 🧠 Quick Quiz #2 — answer from memory, before peeking

**Q1.** `size` is a real column in this table. So what does `df.size` hand back?

- A) The party-size column
- B) An error, because it is ambiguous
- C) `1708` — the DataFrame's own size attribute
- D) The number of rows

**Q2.** Which one has brackets — attributes or methods?

- A) Attributes
- B) Methods

**Q3.** 🔙 One column of a DataFrame is a Series. Which Week-1 container is it most like?

- A) A dictionary
- B) A tuple
- C) A set
- D) A labelled list

---

## ☕ Cluster D — Finding the Big Bills

*Script for this cluster:* **`scripts/04_the_big_bills.py`**

---

### STEP 10 — "Show me only the big bills"

▶ *In your script:* Section 1 of `scripts/04_the_big_bills.py`

🎯 **Objective:** Filter rows with a condition.

☕ **Story moment:** *"Small bills are your coffee business,"* says Mrs Adeyemi. *"I already believe in your coffee business. Show me the tables that actually sat down and ate."*

🧠 **The idea in plain English:** This is the single most-used move in pandas, and it looks odd the first time.

`df['total_bill'] > 20` does not give you rows. It gives you a **whole column of True/False** — one answer per bill, 244 of them. Then `df[ ... ]` uses that column as a mask: keep every row where it says True.

Say it as one sentence: ***"from df, take the rows where total_bill is over 20."***

💻 **The code:**

```python
filtered_df = df[df['total_bill'] > 20]
print(filtered_df.head())
print("Big bills:", filtered_df.shape)
```

📺 **Expected output:**

```text
Filtered rows where total_bill > 20:
   total_bill   tip     sex smoker  day    time  size
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
5       25.29  4.71    Male     No  Sun  Dinner     4
7       26.88  3.12    Male     No  Sun  Dinner     4

Big bills: (97, 7)
```

**97 of your 244 bills were over $20.** Nearly forty per cent. That is the number that funds a second branch, and you just found it.

Look at the index down the left: 2, 3, 4, 5, **7**. Row 6 is missing because that bill was under $20. **Filtering keeps the original row labels** — it does not renumber. That is deliberate and useful: those labels still point at the real rows in the real ledger.

⚠️ **Common mistake:** Forgetting the outer `df[...]`. Writing `filtered = df['total_bill'] > 20` hands you the column of True/False itself, not the rows. If your "filtered table" prints as a column of `True` and `False`, that is what happened.

✅ **Verify:** Five rows, and `(97, 7)`.

🎤 **Try it yourself (30 seconds):** Change `20` to `40` and rerun. How many really big tables did you serve? *(You should get 10.)*

> 📌 **You saw this in class:**
>
> ```python
> # Filter data where the total bill is greater than 20
> filtered_df = df[df['total_bill'] > 20]
> print(filtered_df.head())
> ```
>
> followed by `filtered_df.shape` → `(97, 7)`. Identical.

> ### 🚀 Bonus — beyond class: and what did those tables average?
>
> The filtered table is a DataFrame like any other, so every method still works on it:
>
> ```python
> print(filtered_df['total_bill'].mean())
> print(filtered_df['tip'].max())
> ```
>
> ```text
> 28.425257731958762
> 10.0
> ```
>
> The average big bill is about $28.43, and the biggest single tip of the season was $10.

---

### STEP 11 — 🔙 The Week-1 habit that breaks here

▶ *In your script:* Section 2 of `scripts/04_the_big_bills.py`

🎯 **Objective:** Combine two conditions — and understand why `and` does not work.

☕ **Story moment:** *"Now show me tables of three who tipped well."* Two conditions at once. You already know how to do this from Week 1 — and Week 1 is about to let you down in an interesting way.

🧠 **The idea in plain English:** 🔙 In Week 1 you wrote `is_member and big_order`. That works on **single** True/False answers.

Inside `df[...]` you are not dealing with single answers. You have **two whole columns of 244 True/Falses each**, and you want them combined row by row. Python's `and` cannot do that — it wants one answer per side, gets 244, and refuses.

So pandas gives you different tools:

| Week 1 (single answers) | pandas (whole columns) |
|---|---|
| `and` | `&` |
| `or` | `\|` |
| `not` | `~` |

**And every condition must be wrapped in its own brackets**, because `&` binds more tightly than `>` does. Leave them out and pandas tries to combine the wrong things.

💻 **First, the mistake, on purpose:**

```python
filtered_data = df[df['size'] == 3 and df['tip'] > 3]
```

📺 **Expected output** — a real error, captured by running exactly this:

```text
Traceback (most recent call last):
  File "your_file.py", line 4, in <module>
    filtered_data = df[df['size'] == 3 and df['tip'] > 3]
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().
```

**Translated:** *"You handed me a whole column of True/False and asked me to treat it as a single yes-or-no. Which of the 244 answers did you mean?"* That is what "ambiguous" is telling you — pandas is not confused about your data, it is confused about **which one answer you wanted**.

**And the fix:**

```python
filtered_data = df[(df['size'] == 3) & (df['tip'] > 3)]
print(filtered_data.head())
print("How many:", filtered_data.shape)
```

```text
Tables of 3 who tipped over $3:
    total_bill   tip     sex smoker  day    time  size
2        21.01  3.50    Male     No  Sun  Dinner     3
17       16.29  3.71    Male     No  Sun  Dinner     3
18       16.97  3.50  Female     No  Sun  Dinner     3
19       20.65  3.35    Male     No  Sat  Dinner     3
35       24.06  3.60    Male     No  Sat  Dinner     3
How many: (22, 7)
```

⚠️ **Common mistake:** Dropping the inner brackets — `df[df['size'] == 3 & df['tip'] > 3]`. That is a different error and a more confusing one. **Bracket every condition, every time.** It costs two characters and saves an afternoon.

✅ **Verify:** Five rows, all with `size` 3 and `tip` above 3, and `(22, 7)`.

🎤 **Try it yourself (30 seconds):** Swap the `&` for a `|` and rerun. Now you get tables of three **or** anyone who tipped over $3 — a much bigger group. Predict whether the number goes up or down before you run it.

> 📌 **You saw this in class:**
>
> ```python
> # Subset data where 'size' is 3 and 'tip' is greater than 3
> filtered_data = df[(df['size'] == 3) & (df['tip'] > 3)]
> ```
>
> Same line, brackets and all.

---

### STEP 12 — Restacking the receipts

▶ *In your script:* Section 3 of `scripts/04_the_big_bills.py`

🎯 **Objective:** Sort a table by one column, then by two.

☕ **Story moment:** *"What was your best table all season?"* You need the receipts restacked, biggest on top.

🧠 **The idea in plain English:** `sort_values(by='column')` sorts smallest-first by default. Add `ascending=False` for biggest-first.

You can sort by **several** columns: pandas sorts by the first, and uses the second only to break ties. Pass a list of directions to match.

💻 **The code:**

```python
sorted_df = df.sort_values(by='total_bill', ascending=False)
print(sorted_df.head())

sorted_df_multi = df.sort_values(by=['day', 'total_bill'],
                                 ascending=[True, False])
print(sorted_df_multi.head())
```

📺 **Expected output:**

```text
Data sorted by total_bill in descending order:
     total_bill    tip   sex smoker  day    time  size
170       50.81  10.00  Male    Yes  Sat  Dinner     3
212       48.33   9.00  Male     No  Sat  Dinner     4
59        48.27   6.73  Male     No  Sat  Dinner     4
156       48.17   5.00  Male     No  Sun  Dinner     6
182       45.35   3.50  Male    Yes  Sun  Dinner     3

Sorted by day, then biggest bill first:
    total_bill   tip     sex smoker  day    time  size
95       40.17  4.73    Male    Yes  Fri  Dinner     4
90       28.97  3.00    Male    Yes  Fri  Dinner     2
96       27.28  4.00    Male    Yes  Fri  Dinner     2
94       22.75  3.25  Female     No  Fri  Dinner     2
91       22.49  3.50    Male     No  Fri  Dinner     2
```

**Your best table of the season was $50.81, on a Saturday, with a $10 tip.** Four of the top five were Saturdays.

In the second sort, `Fri` comes first because days are sorted A–Z ascending, and within Friday the bills run biggest-first. Two rules, applied in order.

⚠️ **Common mistake:** Expecting `sort_values` to change `df` itself. It does **not** — it hands back a **new** sorted table and leaves the original alone. If your sort seems to have done nothing, check that you caught the result in a variable.

✅ **Verify:** `50.81` on top of the first block; `Fri` at the top of the second.

🎤 **Try it yourself (30 seconds):** Sort by `tip` descending instead. Is your biggest tipper also your biggest bill? *(They are — row 170. Not always true in real data, which is what makes the scatter plot in STEP 19 interesting.)*

> 📌 **You saw this in class:** both of these — `sort_values(by='total_bill', ascending=False)` and the two-column sort `by=['day', 'total_bill'], ascending=[True, False]`.

---

### 🧠 Quick Quiz #3 — answer from memory, before peeking

**Q1.** 🔙 Why did the filter written with `and` fail?

- A) Inside `df[...]` you combine whole columns at once, so you need `&`
- B) `size` is not really a column in this table
- C) pandas requires a `.filter()` method instead
- D) The numbers were still text and needed converting

**Q2.** What is `df[df['total_bill'] > 20].shape`?

- A) `(244, 7)`
- B) `(97, 7)`
- C) `(20, 7)`
- D) `(7, 97)`

**Q3.** `ascending=False` puts what first?

- A) The smallest values
- B) The values in alphabetical order
- C) The rows in random order
- D) The biggest values

---

## ☕ Cluster E — Piles of Receipts

*Script for this cluster:* **`scripts/05_receipt_piles.py`**

---

### STEP 13 — Sorting receipts into piles

▶ *In your script:* Section 1 of `scripts/05_receipt_piles.py`

🎯 **Objective:** Group rows and summarise each group.

☕ **Story moment:** Picture yourself doing this on the counter with actual paper. You take the 244 receipts and deal them into four piles — Thursday, Friday, Saturday, Sunday. Then you go pile by pile and work out what each one is worth.

That is `groupby`. That is genuinely all it is.

🧠 **The idea in plain English:** `df.groupby('day')` deals the rows into piles by day. On its own it does nothing visible — you then say **which columns** you care about and **what to work out** for each pile.

```python
df.groupby('day')[['total_bill', 'tip']].mean()
#          ^pile by  ^these columns      ^work this out per pile
```

💻 **The code:**

```python
grouped_df = df.groupby('day')[['total_bill', 'tip']].min()
print(grouped_df)

grouped_mean = df.groupby('day')[['total_bill', 'tip']].mean()
print(grouped_mean)
```

📺 **Expected output:**

```text
Smallest bill and tip on each day:
      total_bill   tip
day                   
Fri         5.75  1.00
Sat         3.07  1.00
Sun         7.25  1.01
Thur        7.51  1.25

Average bill and tip on each day:
      total_bill       tip
day                       
Fri    17.151579  2.734737
Sat    20.441379  2.993103
Sun    21.410000  3.255132
Thur   17.682742  2.771452
```

Notice `day` has moved: it is no longer a column, it is now the **index** — the label down the left. That is what grouping does; each pile gets one row, labelled with what made it a pile.

**And the finding Mrs Adeyemi actually wants:** Sunday averages $21.41 a table, Friday $17.15. Sunday tables are worth about 25% more.

⚠️ **Common mistake:** Expecting `.min()` and `.mean()` to give similar-looking answers. The smallest Saturday bill was $3.07; the *average* Saturday bill was $20.44. Both are true and they answer completely different questions. **Always know which one you asked for.**

✅ **Verify:** Two four-row tables, days down the left.

🎤 **Try it yourself (30 seconds):** Try `.max()` and `.sum()` on the same grouping. `.sum()` tells you which day earned the most money in total — which is a different question from which day had the biggest average, and arguably the more important one.

> 📌 **You saw this in class:**
>
> ```python
> # Group by 'day' and calculate the mean of total_bill and tip
> grouped_df = df.groupby('day')[['total_bill', 'tip']].min()
> print(grouped_df)
> ```
>
> ```text
>       total_bill   tip
> day
> Fri         5.75  1.00
> Sat         3.07  1.00
> Sun         7.25  1.01
> Thur        7.51  1.25
> ```
>
> **Worth knowing:** the comment on that cell says *mean*, but the code calls `.min()` — so what it actually printed was the **smallest** bill in each pile, exactly as shown. That is why this STEP runs both: `.min()` as your instructor ran it, then `.mean()` for the number the bank asked about. Reading what code *does* rather than what its comment *says* is a genuinely valuable habit.

---

### STEP 14 — Several numbers at once

▶ *In your script:* Section 2 of `scripts/05_receipt_piles.py`

🎯 **Objective:** Use `agg()` for more than one calculation per column.

☕ **Story moment:** Mrs Adeyemi is warming up. *"For each day: the average bill, the total takings, and the biggest single table. And the average and total tips while you are at it."* Five numbers per day. You are not running five separate commands.

🧠 **The idea in plain English:** `agg()` takes a **dictionary** — 🔙 Week 1's dictionary, in its natural habitat. Each key is a column; each value is a list of what you want worked out for it.

💻 **The code:**

```python
grouped_agg = df.groupby('day').agg({
    'total_bill': ['mean', 'sum', 'max'],
    'tip': ['mean', 'sum']
})
print(grouped_agg)
```

📺 **Expected output:**

```text
Grouped data by 'day' with multiple aggregations:
     total_bill                       tip        
           mean      sum    max      mean     sum
day                                              
Fri   17.151579   325.88  40.17  2.734737   51.96
Sat   20.441379  1778.40  50.81  2.993103  260.40
Sun   21.410000  1627.16  48.17  3.255132  247.39
Thur  17.682742  1096.33  43.11  2.771452  171.83
```

Look at the header: it has **two rows**. `total_bill` spans three sub-columns, `tip` spans two. That is pandas showing you a grouped header, and it is exactly the shape of a real management report.

**The finding that matters most for your loan:** look at `sum`. Saturday brought in **$1,778.40** across the season, Friday only **$325.88**. Sunday has the best *average* table, but Saturday earns the most *money*. Both facts go in the folder.

**And one more thing** — the single vs double bracket rule from class:

```python
df.groupby('day')['tip'].mean()      # single -> a Series
df.groupby('day')[['tip']].mean()    # double -> a DataFrame
```

```text
Single brackets gives a Series
Double brackets gives a DataFrame
```

⚠️ **Common mistake:** Writing the aggregation names without quotes — `'total_bill': [mean, sum, max]`. They are **text labels**, so they need quotes. Without them Python looks for variables called `mean` and `sum` and gives you a `NameError`.

✅ **Verify:** A four-row table with a two-level header, then the two bracket lines.

🎤 **Try it yourself (30 seconds):** Add `'size': ['mean']` to the dictionary. What is your average party size on each day? *(Sunday's is biggest — bigger tables, bigger bills. The numbers are starting to tell a story.)*

> 📌 **You saw this in class:** the exact `agg({...})` call above, with those same five aggregations.

---

### STEP 15 — The summary page

▶ *In your script:* Section 3 of `scripts/05_receipt_piles.py`

🎯 **Objective:** Read `describe()` line by line.

☕ **Story moment:** There is one command that produces the page Mrs Adeyemi will actually read first. This is it.

🧠 **The idea in plain English:** `describe()` gives eight summary numbers for every numeric column at once.

💻 **The code:**

```python
print(df.describe())
```

📺 **Expected output:**

```text
Descriptive statistics for numeric columns:
       total_bill         tip        size
count  244.000000  244.000000  244.000000
mean    19.785943    2.998279    2.569672
std      8.902412    1.383638    0.951100
min      3.070000    1.000000    1.000000
25%     13.347500    2.000000    2.000000
50%     17.795000    2.900000    2.000000
75%     24.127500    3.562500    3.000000
max     50.810000   10.000000    6.000000
```

**Now read it, line by line, in plain English** — using the `total_bill` column:

| Row | Means | Here |
|---|---|---|
| `count` | how many values there are | 244 bills, none missing |
| `mean` | the average | **the average bill is about $19.79** |
| `std` | how spread out they are — small means bills are alike, big means they vary a lot | $8.90, so bills vary quite a bit |
| `min` | the smallest | $3.07 — somebody had a coffee and left |
| `25%` | a quarter of bills are below this | $13.35 |
| `50%` | **the middle bill** (half above, half below) | $17.80 |
| `75%` | three quarters are below this | $24.13 |
| `max` | the biggest | $50.81 — the Saturday table from STEP 12 |

One thing worth noticing: the **mean is $19.79 but the middle bill is $17.80.** The average is higher than the middle because a handful of very large tables drag it up. That gap is a real and useful signal, and you can now see it in ten seconds.

⚠️ **Common mistake:** Reading `describe()` for the `size` column as money. It is people at a table — an average party of 2.57. The command does not know what your columns mean; **you** supply that.

✅ **Verify:** Three columns, eight rows, and `mean` for `total_bill` reading `19.785943`.

🎤 **Try it yourself (30 seconds):** Run `df['tip'].describe()` on its own. Same eight numbers, one column. And the class's own exercise: `df.head(50).describe()` — the summary of just the first fifty bills.

> 📌 **You saw this in class:** `df.describe()`, producing exactly this table.

---

### 🧠 Quick Quiz #4 — answer from memory, before peeking

**Q1.** What shape does `df.groupby('day')[['total_bill','tip']].mean()` hand back?

- A) One row per day, one column per measure
- B) One single number
- C) The whole table, unchanged
- D) A finished chart

**Q2.** Single brackets versus double brackets after `groupby` — what is the difference?

- A) Both hand back a DataFrame
- B) Single gives a DataFrame, double gives a Series
- C) Single gives a Series, double gives a DataFrame
- D) Both hand back a Series

**Q3.** According to `describe()`, roughly what is the average bill?

- A) About `$19.79`
- B) About `$2.99`
- C) About `$50.81`
- D) About `$244.00`

---

## ☕ Cluster F — Smudged Entries

*Script for this cluster:* **`scripts/06_smudged_receipts.py`**

---

### STEP 16 — Checking for gaps (and finding none)

▶ *In your script:* Section 1 of `scripts/06_smudged_receipts.py`

🎯 **Objective:** Check a table for missing values.

☕ **Story moment:** Before any number goes in front of a bank, you check the evidence is complete. A report built on a book with holes in it is worse than no report.

🧠 **The idea in plain English:** Missing values in pandas show up as **`NaN`** — "Not a Number", pandas' way of writing "there was nothing here".

`df.isna()` turns the whole table into True/False: True wherever a value is missing. Adding `.sum()` counts the Trues per column. 🔙 It works because Python counts `True` as 1 — the same `bool` you met in Week 1.

💻 **The code:**

```python
print(df.isna().sum())
```

📺 **Expected output:**

```text
Check for missing values:
total_bill    0
tip           0
sex           0
smoker        0
day           0
time          0
size          0
dtype: int64
```

**Every single number is zero.** The till export is perfect — no gaps anywhere. Which is excellent news for your loan application, and completely useless for learning how to *fix* gaps.

So let us be honest about that rather than pretend: in class, `fillna()` and `dropna()` were run on this same spotless file, which means they ran and changed absolutely nothing. Perfectly correct code, invisible effect.

**We happen to have a messier book.**

⚠️ **Common mistake:** `isna()` without `.sum()` on a big table. You get 244 rows of True/False, which tells you nothing at a glance. Always add `.sum()`.

✅ **Verify:** Seven zeros.

🎤 **Try it yourself (30 seconds):** Try `df.isna().sum().sum()` — the double sum totals every column into one number. `0`. One number that says "this file is complete".

> 📌 **You saw this in class:** `df.isna().sum()`, producing exactly these seven zeros.

---

### STEP 17 — The takings book, which has real holes in it

▶ *In your script:* Section 2 of `scripts/06_smudged_receipts.py`

🎯 **Objective:** Find real gaps, and choose between filling and dropping them.

☕ **Story moment:** The other book on the counter is the coffee-shop side's **daily takings book** — cups sold, muffins sold, money taken, written by hand at closing by whoever was on. Two weeks of it got typed up, and it has genuine holes:

- **Wednesday the 9th** — nobody counted what was left on the muffin tray.
- **Friday the 11th** — Ben knocked a flat white over the takings page.
- **Tuesday the 15th** — Aisha's first solo close; the muffin count got missed.
- **Friday the 18th** — the till tablet died at 4 p.m. and took *both* numbers with it.

🧠 **The idea in plain English:** Two honest options, and the choice is a judgement call, not a rule:

| Option | What it does | When it is honest |
|---|---|---|
| `fillna(value)` | puts a stand-in value in the gap | one number missing from an otherwise good row, and an average is a fair guess |
| `dropna()` | removes any row with a gap in it | the row is too damaged to trust |

💻 **The code:**

```python
takings = pd.read_csv("data/cozybean_takings.csv")
print(takings.isna().sum())

muffin_average = takings['muffins_sold'].mean()
filled = takings.copy()
filled['muffins_sold'] = filled['muffins_sold'].fillna(muffin_average)

dropped = takings.dropna()
```

📺 **Expected output:**

```text
=== THE TAKINGS BOOK ===
          date  day barista  cups_sold  muffins_sold  takings
0   2026-09-07  Mon    Sara        118          24.0   451.50
1   2026-09-08  Tue     Ben        104          21.0   398.75
2   2026-09-09  Wed   Aisha        131           NaN   489.25
3   2026-09-10  Thu    Sara        127          26.0   486.00
4   2026-09-11  Fri     Ben        156          33.0      NaN
5   2026-09-12  Sat   Aisha        188          41.0   712.25
6   2026-09-13  Sun    Sara        142          30.0   548.00
7   2026-09-14  Mon     Ben        109          22.0   415.75
8   2026-09-15  Tue   Aisha         97           NaN   371.50
9   2026-09-16  Wed    Sara        124          25.0   472.00
10  2026-09-17  Thu     Ben        133          27.0   507.25
11  2026-09-18  Fri   Aisha        161           NaN      NaN
12  2026-09-19  Sat    Sara        195          41.0   738.50
13  2026-09-20  Sun     Ben        138          29.0   529.25

Where are the gaps?
date            0
day             0
barista         0
cups_sold       0
muffins_sold    3
takings         2
dtype: int64

Rows with at least one gap: 4

Average muffins on counted days: 29.0
After filling, gaps left in muffins_sold: 0

Rows before dropping: 14
Rows after dropping:  10
```

**There they are** — you can actually see the `NaN`s in the printed table, and row 11 (Friday the 18th) has two of them.

Now the numbers **change** when you act on them: three gaps in `muffins_sold` become zero after filling; fourteen rows become ten after dropping.

One quiet detail worth catching: the average muffin count is **29.0**, worked out from the eleven days that *were* counted. `.mean()` **ignores** the gaps rather than treating them as zero — which is exactly right. If it counted them as zero the average would be dragged down and your fill would be a lie.

⚠️ **Common mistake:** `dropna()` as a reflex. Here it throws away four days — nearly a third of your fortnight — including Friday the 11th, where the only problem was one spilled drink and the cup and muffin counts were fine. Dropping is not "the safe option"; it is a decision, and you should be able to defend it.

✅ **Verify:** Three gaps in `muffins_sold`, two in `takings`, four damaged rows, average `29.0`, and 14 → 10 rows after dropping.

🎤 **Try it yourself (30 seconds):** Try `takings.dropna(subset=['takings'])` — drop only rows missing the *takings* figure, keeping the ones where just the muffin count is absent. Twelve rows survive. That is often the honest middle path.

---

## ☕ Cluster G — Labels versus Positions

*Script for this cluster:* **`scripts/07_labels_vs_positions.py`**

---

### STEP 18 — `loc`, `iloc`, and the rule that changes

▶ *In your script:* the whole of `scripts/07_labels_vs_positions.py`

🎯 **Objective:** Select rows by label and by position, and spot the one difference.

☕ **Story moment:** Two ways to find a receipt. *"Give me the tenth receipt in the stack"* — that is counting. *"Give me the receipt labelled 9"* — that is looking up. Usually the same receipt. Not always.

🧠 **The idea in plain English:**

| Tool | Selects by | Think |
|---|---|---|
| `.iloc[...]` | **position** — where it sits | **i** for *integer position* |
| `.loc[...]` | **label** — what the index says | **l** for *label* |

And here is the bit that catches everyone, which is why it gets its own 🔙:

> ### 🔙 Week-1 contrast — this is worth ten seconds of your attention
>
> In Week 1, `queue[1:3]` gave you **two** names. The end was **left out**.
>
> - **`iloc` follows that same Week-1 rule.** `df.iloc[0:10]` → the end is **left out**.
> - **`loc` does NOT.** `df.loc[0:9]` → the end label is **included**.
>
> `iloc[0:10]` and `loc[0:9]` both give you **ten rows** — for two completely different reasons. Knowledge that *almost* transfers is exactly what trips people up, so hold on to this one.

💻 **The code:**

```python
subset_iloc = df.iloc[:10, df.columns.get_loc('total_bill')]
print(subset_iloc)

subset_loc = df.loc[0:9, 'total_bill']
print(subset_loc)
```

📺 **Expected output** (both blocks are identical — here is the `loc` one):

```text
First 10 rows of 'total_bill' column using .loc[]:
0    16.99
1    10.34
2    21.01
3    23.68
4    24.59
5    25.29
6     8.77
7    26.88
8    15.04
9    14.78
Name: total_bill, dtype: float64
```

**And the proof, from the same script:**

```text
Week-1 list slice [1:3] -> ['Ben', 'Aisha'] (2 names, 3 left out)
iloc[0:10] gives 10 rows (10 left out)
loc[0:9]  gives 10 rows (9 included)

Both gave 10 rows -- for two completely different reasons.
```

⚠️ **Common mistake:** Assuming labels and positions are always the same number. They are here — because this table's index happens to be 0, 1, 2, 3… But **after you sort or filter, they are not.** Look back at STEP 10: the filtered table's labels went 2, 3, 4, 5, 7. There, `iloc[0]` is the *first row shown* while `loc[2]` is *the row labelled 2* — and they are the same row for entirely different reasons. When in doubt, `head()` and look.

✅ **Verify:** Two identical ten-value blocks, then the three comparison lines.

🎤 **Try it yourself (30 seconds):** Run `df.loc[0:9]` with no column named — all seven columns, ten rows. Then `df.iloc[0:3, 0:2]` — the first three rows and first two columns, both counted by position.

> 📌 **You saw this in class:** both lines exactly as written above — the `iloc` slice using `df.columns.get_loc('total_bill')`, and `df.loc[0:9, 'total_bill']`.

---

### 🧠 Quick Quiz #5 — answer from memory, before peeking

**Q1.** `isna().sum()` on the till export was all zeros. What does that mean?

- A) The file failed to load properly
- B) Nothing is missing from it
- C) Everything is missing from it
- D) The command was written wrongly

**Q2.** What does `dropna()` do to the takings book?

- A) Fills the gaps with the column average
- B) Marks the gaps in red for review
- C) Removes every row that has a gap in it
- D) Nothing at all on this data

**Q3.** 🔙 How many rows does `df.loc[0:9]` hand back?

- A) `9`
- B) `11`
- C) `0`
- D) `10`

---

## ☕ Cluster H — The Loan-Application Folder

*Scripts for this cluster:* **`scripts/08_chart_scatter.py`**, **`scripts/09_chart_boxplot.py`**, **`scripts/10_chart_missing.py`**

Numbers convince analysts. Pictures convince everybody else.

---

### STEP 19 — Your first chart (and what `show()` feels like)

▶ *In your script:* the whole of `scripts/08_chart_scatter.py`

🎯 **Objective:** Draw, label, save and display a chart.

☕ **Story moment:** The obvious question about a table-service business: **do bigger bills actually tip more?** If they do, table service scales beautifully. One picture answers it.

> ### ⚠️ Read this BEFORE you run the script
>
> When the chart appears, **your terminal will stop and appear to freeze.** It has not frozen. The script is waiting for you to **close the chart window**, and only then will it finish.
>
> **The window may open BEHIND VS Code.** This catches almost everybody. Check your taskbar, find it, admire your work, close it — and the script completes instantly.
>
> **And your PNG is already saved either way**, because `savefig` runs *before* `show`. Even if you never find the window, the file is on disk.

🧠 **The idea in plain English:** Three libraries cooperate:

- **seaborn** (`sns`) draws the chart from your DataFrame in one line
- **matplotlib** (`plt`) handles the figure, title and labels
- and **you** save it before showing it

The first two lines are about the **folder**. `os.makedirs("charts", exist_ok=True)` builds the display folder before we pin anything to it — because **matplotlib will not create the folder for you**, and `savefig` into a folder that does not exist crashes with `FileNotFoundError`. `exist_ok=True` means "and don't complain if it's already there", so it is safe every run.

💻 **The code:**

```python
import os
os.makedirs("charts", exist_ok=True)

plt.figure(figsize=(9, 6))
sns.scatterplot(x='total_bill', y='tip', data=df)
plt.title('The Cozy Bean -- Bill vs Tip (244 bills)')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')

plt.savefig("charts/bills_vs_tips.png")     # SAVE first...
plt.show()                                   # ...THEN show
```

📺 **Expected output:**

```text
Saved charts/bills_vs_tips.png
Window closed. Script finished.
```

…and a window with 244 dots in it, one per bill.

**Read your chart:** it drifts up and to the right — bigger bills really do tip more. The dots also spread out as they go right, meaning big tables are less predictable tippers. Both facts are worth a sentence in your application.

⚠️ **Common mistake:** Calling `plt.show()` *before* `plt.savefig()`. On many setups showing the figure clears it, so `savefig` then writes a **blank PNG**. **Save first, show second.** Every time.

✅ **Verify:** **Check the folder, not the window.** Open `charts/` in the VS Code Explorer — `bills_vs_tips.png` should be sitting there. Click it. That file is your success signal, and it exists whether or not you ever found the window.

🎤 **Try it yourself (30 seconds):** Add `hue='time'` inside `sns.scatterplot(...)` to colour the dots by lunch versus dinner. Save, rerun, look again. Do dinner tables behave differently?

> 📌 **You saw this in class:**
>
> ```python
> # Scatter plot for total_bill vs tip
> plt.figure(figsize=(18, 6))
> sns.scatterplot(x='total_bill', y='tip', data=df)
> plt.title('Scatter Plot: Total Bill vs Tip')
> plt.xlabel('Total Bill')
> plt.ylabel('Tip')
> plt.show()
> ```
>
> Identical, with two changes: a slightly narrower figure so it fits a laptop screen, and `savefig` added — because in a notebook the chart stays on screen, but a script's window closes and takes the picture with it.

---

### STEP 20 — Which day tips best?

▶ *In your script:* the whole of `scripts/09_chart_boxplot.py`

🎯 **Objective:** Compare groups with a boxplot.

☕ **Story moment:** You know Saturday is busiest. But is it the most *generous*? A boxplot compares four days at a glance.

🧠 **The idea in plain English:** A **boxplot** shows the whole spread of a group, not just its average:

- the **line in the middle of the box** — the typical (middle) tip
- the **box** — the middle half of all tips that day
- the **whiskers** — most of the rest
- the **dots beyond** — unusually generous tables

💻 **The code:**

```python
plt.figure(figsize=(8, 6))
sns.boxplot(x='day', y='tip', data=df)
plt.title('The Cozy Bean -- Tips by Day')
plt.savefig("charts/tips_by_day.png")
plt.show()
```

📺 **Expected output:**

```text
Saved charts/tips_by_day.png
Window closed. Script finished.
```

✅ **Verify:** `charts/tips_by_day.png` exists. Four boxes, one per day.

🎤 **Try it yourself (30 seconds):** Change `y='tip'` to `y='total_bill'`. Same four days, different question — and a rather different-looking chart.

> 📌 **You saw this in class:**
>
> ```python
> # Boxplot for tips by day
> plt.figure(figsize=(8, 6))
> sns.boxplot(x='day', y='tip', data=df)
> plt.title('Boxplot: Tips by Day')
> plt.show()
> ```

---

### STEP 21 — A picture of the gaps

▶ *In your script:* the whole of `scripts/10_chart_missing.py`

🎯 **Objective:** See missing data as a map.

☕ **Story moment:** You could count the holes in the takings book by reading it. On a book with two thousand rows, you could not. A heatmap of the damage scales to any size.

🧠 **The idea in plain English:** 🔙 STEP 17's `isna()` turns the table into True/False. A **heatmap** paints that: one colour for present, another for missing. The gaps light up.

💻 **The code:**

```python
takings = pd.read_csv("data/cozybean_takings.csv")

plt.figure(figsize=(8, 6))
sns.heatmap(takings.isna(), cbar=False, cmap='viridis')
plt.title('The Cozy Bean -- Where the Takings Book is Smudged')
plt.savefig("charts/takings_gaps.png")
plt.show()
```

📺 **Expected output:**

```text
Saved charts/takings_gaps.png
Window closed. Script finished.
```

**Read it:** bright marks are missing values. You should see three in the `muffins_sold` column, two in `takings` — and one row where both light up together. That is Friday the 18th, the day the tablet died.

Notice we ran this on the **takings book**, not the till export. Running it on `tips.csv` gives you a completely blank rectangle — technically correct, and no use to anybody.

⚠️ **Common mistake:** Leaving out `cbar=False`. You get a colour-scale bar down the side labelled 0 to 1, which is meaningless for True/False and just clutters the picture.

✅ **Verify:** `charts/takings_gaps.png` exists, with visible bright marks in exactly two columns.

🎤 **Try it yourself (30 seconds):** Run the same heatmap on `df` (the till export). A single flat colour — the picture of a perfect file.

> 📌 **You saw this in class:**
>
> ```python
> # Visualizing missing values using a heatmap
> plt.figure(figsize=(8, 6))
> sns.heatmap(df.isna(), cbar=False, cmap='viridis')
> plt.title('Missing Values Heatmap')
> plt.show()
> ```
>
> Same call — pointed at the book that actually has gaps in it, so you can see it work.

---

### 🧠 Quick Quiz #6 — answer from memory, before peeking

**Q1.** Your terminal seems frozen after a chart appeared. What is happening?

- A) The chart window is open and waiting for you to close it
- B) The script crashed and stopped responding
- C) The PNG failed to save
- D) Python is downloading something

**Q2.** Why does every chart script call `os.makedirs("charts", exist_ok=True)` first?

- A) It makes the chart look better
- B) It clears out yesterday's charts
- C) matplotlib will not create the folder itself
- D) It imports seaborn behind the scenes

---

## ☕ Cluster I — Does the Claim Hold Up?

*Script for this cluster:* **`scripts/11_the_claim.py`**

---

### STEP 22 — Mrs Adeyemi looks over her glasses

▶ *In your script:* the whole of `scripts/11_the_claim.py`

🎯 **Objective:** Run a one-sample t-test and read its answer in one sentence.

☕ **Story moment:** Page two of your application says: *"average bill approximately $20."* Mrs Adeyemi taps it with her pen. **"Do these 244 receipts back that up?"**

🧠 **The idea in plain English:** Your 244 bills are a **sample** — one season, not every meal you will ever serve. So the question is not "is the average exactly $20" (it never is, exactly). It is: **"are these receipts consistent with a true average of about $20, or do they argue against it?"**

A **t-test** answers exactly that, and hands back a **p-value**:

> **The p-value answers one question: if the true average really were $20, how surprising would these particular 244 receipts be?**

- **Big p-value** → not surprising at all → the receipts give you no reason to doubt the claim.
- **Small p-value** (under 0.05 is the usual line) → these receipts would be hard to explain if the average really were $20 → the claim looks wrong.

That is all you need today. No theory, no formulas.

💻 **The code:**

```python
from scipy import stats

t_stat, p_value = stats.ttest_1samp(df['total_bill'], popmean=20)
print(f"T-test for total_bill: t-stat = {t_stat}, p-value = {p_value}")
```

📺 **Expected output:**

```text
T-test for total_bill: t-stat = -0.37559294451919506, p-value = 0.7075471935626721

What the actual average is: 19.78594262295082

p-value is large, so the receipts do not contradict
the $20 claim. The application stands.
```

**Read it in one sentence:** the p-value is about **0.71** — very large, nowhere near 0.05 — so these receipts are entirely unsurprising if the true average is $20. **Your application stands.**

The actual average is $19.79, which is a whisker under $20. The test's job was to tell you whether that whisker means anything. It does not.

*(The `t-stat` of −0.376 is the raw distance from the claim, in statistical units. Negative because $19.79 is slightly below $20. You will meet it properly later; the p-value is the part you read today.)*

⚠️ **Common mistake:** Reading a big p-value as "proof the average IS exactly $20". It is not. It means *"nothing here argues against it"* — which is a weaker and more honest statement. Absence of evidence against a claim is not proof of the claim.

✅ **Verify:** A p-value beginning `0.7075`.

🎤 **Try it yourself (30 seconds):** Change `popmean=20` to `popmean=25` and rerun. The p-value collapses to a tiny number — because these receipts would be *very* surprising if the true average were $25. That is what a small p-value looks like, and now you have seen both.

> 📌 **You saw this in class:**
>
> ```python
> # Example: Hypothesis test for total_bill mean using t-test
> from scipy import stats
> t_stat, p_value = stats.ttest_1samp(df['total_bill'], popmean=20)
> print(f"T-test for total_bill: t-stat = {t_stat}, p-value = {p_value}")
> ```
>
> Identical. *(The very last digit of the p-value may differ between computers — that is ordinary floating-point rounding, not a different answer.)*

---

## ☕ Cluster J — The Report for the Bank

*Script for this cluster:* **`scripts/12_report_for_the_bank.py`**

---

### STEP 23 — Everything, doing one job

▶ *In your script:* the whole of `scripts/12_report_for_the_bank.py`

🎯 **Objective:** Chain the whole lab into one useful program.

☕ **Story moment:** Monday morning. This is the page that goes in the folder.

🧠 **The idea in plain English:** Six moves, each one a STEP you already did:

1. **open the ledger** — `read_csv` (STEP 3)
2. **keep the big bills** — filter (STEP 10)
3. **pile them by day** — `groupby` (STEP 13)
4. **restack, best first** — `sort_values` (STEP 12)
5. **write the findings** — 🔙 Week-1 f-strings
6. **save one chart** — `savefig` (STEP 19)

💻 **The code** (the heart of it):

```python
big = df[df['total_bill'] > 20]
by_day = big.groupby('day')[['total_bill', 'tip']].mean()
by_day = by_day.sort_values(by='total_bill', ascending=False)

best_day = by_day.index[0]
best_avg = by_day['total_bill'].iloc[0]
```

📺 **Expected output:**

```text
====================================================
   THE COZY BEAN -- SECOND BRANCH LOAN APPLICATION
====================================================

Evidence: 244 bills from the trial table-service season.
Average bill across the whole season: $19.79
Average tip across the whole season:  $3.00

Bills over $20: 97 of 244 (39.8% of all bills)

Big-bill days, best first:
      total_bill       tip
day                       
Sun    28.582162  3.980000
Sat    28.476579  3.842368
Thur   28.433125  4.150625
Fri    27.111667  3.580000

FINDING: Sun is our strongest day for big tables,
averaging $28.58 per bill over $20.

====================================================
Saved charts/report_bills_by_day.png
Report complete. Take it to the bank.
```

**That is a real report.** Every number in it is true, every number came from evidence, and you can defend all of them.

Notice `:.2f` in the f-strings, making `19.785943` print as `$19.79` — 🔙 the money formatting from Week 1's bonus box, earning its keep at last.

And notice `by_day.index[0]` — after grouping, the day names became the **index** (STEP 13), so the winner's name is the first index entry.

⚠️ **Common mistake:** Doing the moves in the wrong order. Grouping *before* filtering answers a completely different question — "the average of all bills by day" rather than "the average big bill by day". **Filter, then group.** The order is the question.

✅ **Verify:** The report prints, and `charts/report_bills_by_day.png` exists.

🎤 **Try it yourself (30 seconds):** Change the `> 20` threshold to `> 30` and rerun. Does your best day change? *(It does. Which is worth knowing before you tell a bank which day is your best.)*

---

### 🧠 Quick Quiz #7 — answer from memory, before peeking

**Q1.** The t-test p-value was about 0.71. In one sentence, what does that mean?

- A) The receipts strongly contradict the $20 claim
- B) The receipts give no reason to doubt the $20 claim
- C) The average is exactly $20
- D) The test did not run properly

**Q2.** 🔙 Which Week-1 tool builds the report's sentences?

- A) f-strings
- B) `while` loops
- C) `.split()`
- D) Sets

---

## 5. 🏋️ Practice Problems

Reading pandas feels easy. Writing it is where it sticks.

**How practice works here:** one problem per file in `practice/`; run just the one you want with `python practice/p01_open_the_ledger.py`. Every file's header repeats the task **and the exact expected output**. Every file runs as-is before you touch it — it just prints the wrong things. Answers are in `solutions/` — **open them only after a genuine attempt.**

| # | File | Story task | You will practise |
|---|---|---|---|
| p01 | `p01_open_the_ledger.py` | Mrs Adeyemi's three warm-up questions: how many bills, what columns, show me five. | `read_csv`, `shape`, `columns`, `head()` |
| p02 | `p02_one_column.py` | How many days did we trade? How many bills each? Lunch or dinner? | `nunique`, `value_counts` |
| p03 | `p03_the_big_bills.py` | The bank calls anything over $30 a "big table". How many, and what did they tip? | filtering, `.mean()` on a subset |
| **p04** | `p04_filter_group_sort.py` | **"On your big tables, which day earns most?"** Filter, group and sort — all three, in order. | ⭐ the full chain |
| p05 | `p05_smudged_takings.py` | Clean the takings book: count the gaps, fill the muffin counts, drop the damaged rows. | `isna`, `fillna`, `dropna` |
| **p06** | `p06_a_function_that_filters.py` | The officer keeps moving the goalposts. Write the filter **once**, as a function. | ⭐ 🔙 Week-1 `def` returning a DataFrame |
| p07 | `p07_your_own_chart.py` | One more page for the folder: bill size by service, saved as a PNG. | seaborn + `savefig` |
| **p08** | `p08_capstone_report_for_the_bank.py` | **CAPSTONE — your own evidence page.** Five findings in your own f-strings, plus the chart. | the whole lab |
| 🚀 p09 | `p09_bonus_shares_and_bars.py` | **Bonus:** turn counts into percentages and draw them as bars. | bonus material only |

> 🚀 **p09 is a bonus** and uses `value_counts(normalize=True)`, which was not in your class session. Nothing depends on it.

### 🏔️ About the capstone

**p08 — Your Report for the Bank** is the one to be proud of. It is not hard in the sense of needing a new idea — every piece is something you did in p01 to p07. It is hard in the sense that **nobody tells you which piece to use where**. That is exactly what real data work feels like, and finishing it means you can genuinely do this.

Your own report will not be identical to `scripts/12`, and it should not be. That one looked at big bills; yours looks at all of them.

---

## 6. 📚 Cheat Sheet & Glossary

- **[CHEATSHEET.md](CHEATSHEET.md)** — the pandas one-pager: load, look, select, filter, group, sort, clean, chart, save. This is the one you will actually keep.
- **[GLOSSARY.md](GLOSSARY.md)** — every new word this week in one plain sentence: DataFrame, Series, aggregation, p-value and the rest.

*(Week 2 Lab01's [cheat sheet](../M1-W2-Lab01/CHEATSHEET.md) still applies — a DataFrame is an object, `pd` is a module, and `df.shape` vs `df.head()` is yesterday's attribute-versus-method rule.)*

---

## 7. 🤔 Reflection (2 minutes — please actually do this)

1. **What surprised you in the data?** You found at least one thing today you did not know about your own shop. Which was it?
2. **What is still fuzzy?** Name the one thing you would ask an instructor sitting beside you. Write it down — it is your first question next session.
3. **Find your own 244 rows.** What is one spreadsheet or export in your own life — bank statements, a fitness app, a hobby log — that you could load with `read_csv` this week? You now genuinely have the skills to look at it properly.

---

## 8. ✅ Answer Key

*No peeking until you have answered. Nineteen questions in total.*

### Quiz #1

| Q | Answer | Why |
|---|---|---|
| 1 | **B** — Pandas | Tables are pandas' whole job. NumPy is arrays, matplotlib is charts, SciPy is algorithms. |
| 2 | **D** — the number of columns | `shape` is always `(rows, columns)`, so 244 bills and 7 columns. |
| 3 | **C** — `df.tail(10)` | `head` is the top, `tail` is the bottom. The other two are not pandas methods at all. |

### Quiz #2

| Q | Answer | Why |
|---|---|---|
| 1 | **C** — `1708`, the DataFrame's own size attribute | The built-in attribute wins over the column name, silently, with no error at all. Use `df['size']`. |
| 2 | **B** — methods | Methods do something, so they need brackets. Attributes are facts, so they never take them. |
| 3 | **D** — a labelled list | Values in order, all the same kind, each with a label. |

### Quiz #3

| Q | Answer | Why |
|---|---|---|
| 1 | **A** — you combine whole columns at once, so you need `&` | Python's `and` wants one True/False per side and was handed 244, hence "ambiguous". |
| 2 | **B** — `(97, 7)` | 97 of the 244 bills were over $20; filtering never changes the number of columns. |
| 3 | **D** — the biggest values | `ascending=False` reverses the default smallest-first order. |

### Quiz #4

| Q | Answer | Why |
|---|---|---|
| 1 | **A** — one row per day, one column per measure | Each pile collapses to a single row, labelled by what made it a pile. |
| 2 | **C** — single gives a Series, double gives a DataFrame | The same rule as selecting columns from a DataFrame. |
| 3 | **A** — about `$19.79` | The `mean` row of the `total_bill` column. `$2.99` is the average tip; `$50.81` is the largest bill. |

### Quiz #5

| Q | Answer | Why |
|---|---|---|
| 1 | **B** — nothing is missing | `isna()` counts gaps, so all zeros means a complete file. |
| 2 | **C** — removes every row that has a gap | Which took the takings book from 14 rows to 10. |
| 3 | **D** — `10` | `loc` **includes** its end label, so 0 to 9 is ten rows. `iloc[0:10]` gives ten as well, by leaving the end out. |

### Quiz #6

| Q | Answer | Why |
|---|---|---|
| 1 | **A** — the chart window is open, waiting to be closed | It is often hiding behind VS Code. Close it and the script finishes; the PNG was saved before it opened. |
| 2 | **C** — matplotlib will not create the folder itself | Without it, `savefig` into a missing folder raises `FileNotFoundError`. |

### Quiz #7

| Q | Answer | Why |
|---|---|---|
| 1 | **B** — the receipts give no reason to doubt the claim | A large p-value means these receipts would be unsurprising if the claim were true. It does not *prove* the claim. |
| 2 | **A** — f-strings | `f"Average bill: ${df['total_bill'].mean():.2f}"` — Week 1's f-string with Week 1's money formatting. |

---

## 9. ➡️ What's Next

Take a moment. Two weeks ago you had never written a line of Python. Today you loaded 244 real records, filtered them, grouped them, cleaned a second file that had holes in it, drew three charts, ran a statistical test, and produced a report you could genuinely hand to a bank.

**You are a data person now.** That is not encouragement; it is a description of what you just did.

**Next session** the toolbox tour pays off. You met scikit-learn and statsmodels as one-line mentions in STEP 1 — those are where the road goes next, into machine learning proper. And every model you meet from here starts exactly where today started: `pd.read_csv(...)`, then `head()`, then a long careful look at what you actually have.

The DataFrame you learned today is the thing you will hand to those models. Everything you did in Cluster F — finding gaps, deciding whether to fill or drop — is the work that decides whether a model learns anything real. It is not the boring part before the clever part. It **is** the job.

The Cozy Bean's second branch opens in the spring. ☕

---

*Apeiron AI Training Academy · Module 1: AI/ML Fundamentals · Week 2 · Lab02*
*"Boundless Possibilities, Infinite Potential"*
