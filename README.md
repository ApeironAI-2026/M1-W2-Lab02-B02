# ☕ M1-W2-Lab02 — The Second Branch: The Bank Wants Numbers

**Apeiron AI Training Academy** · *"Boundless Possibilities, Infinite Potential"*

| | |
|---|---|
| **Module** | M1: AI/ML Fundamentals |
| **Week** | Week 2 |
| **Lab** | Lab02 — The Second Branch: The Bank Wants Numbers |
| **Topic** | The Python data toolbox · pandas · filtering, grouping, missing values · charts with seaborn and matplotlib · a t-test |
| **Duration** | **≈ 1 hour** of lab work, **plus about 30 minutes of one-time setup** |
| **Difficulty** | ⭐⭐ Beginner, level 2 |

There is an empty unit two streets over that would make a beautiful sit-down café, and you cannot fund it out of the till. On Monday you take a loan application to the bank — and the loan officer wants **evidence**, not enthusiasm. You have some: **244 real bills** from the trial table-service season. This lab turns them into a report with charts in it.

**Start here → [`M1-W2-Lab02.md`](M1-W2-Lab02.md)** — 23 steps in 10 clusters, with quizzes and an answer key.

> ⚠️ **This lab installs software.** Unlike every lab so far, you need four third-party libraries. Section 2 below is a genuine milestone and it goes wrong for almost everybody at least once — every common failure is in the table. **Set aside 30 minutes and do not rush it.**

---

## 1. 📥 Get this repo onto your computer

You reached this repo by clicking the **GitHub Classroom link posted in Google Classroom**. That link made **your own private copy** of the lab — the URL has your GitHub username in it. This is the copy you clone.

### 1.1 Where to put it

This is a **separate repo** from Week 2 Lab01, so it gets its own folder right next to it:

```text
AperionAI/
└── Module1/
    ├── Week1/
    │   ├── Lab01/
    │   └── Lab02/
    ├── Week2/
    │   ├── Lab01/      ← already cloned
    │   └── Lab02/      ← this repo goes here
    └── Week3/
        ├── Lab01/
        └── Lab02/
```

**Do not put `AperionAI` inside OneDrive, iCloud Drive, Google Drive or Dropbox.** That matters more in this lab than any before it: your scripts write PNG files into `charts/`, and a syncing folder can lock a file mid-write and produce an error that looks like a bug in your code but is not.

### 1.2 Copy your repo's address

1. On this repo's page on GitHub, click the green **`< > Code`** button.
2. Make sure the **HTTPS** tab is selected.
3. Click the 📋 copy icon.

You now have something like `https://github.com/ApeironAI-2026/M1-W2-Lab02-B02-<your-username>.git` on your clipboard. **Use your own address**, not a classmate's.

### 1.3 Clone it into `Week2/Lab02`

**Windows (PowerShell):**

```text
cd ~\AperionAI\Module1\Week2
git clone PASTE-YOUR-REPO-URL-HERE Lab02
cd Lab02
```

**Mac / Linux:**

```text
cd ~/AperionAI/Module1/Week2
git clone PASTE-YOUR-REPO-URL-HERE Lab02
cd Lab02
```

That last word — `Lab02` — is what names the folder. Leave it off and git names it after the repo instead (`M1-W2-Lab02-B02-your-username`), which breaks the layout above.

> **Folder `Week2` does not exist yet?** You have not cloned Week 2 Lab01. Create it with `mkdir -Force ~\AperionAI\Module1\Week2` (Windows) or `mkdir -p ~/AperionAI/Module1/Week2` (Mac), then clone.
>
> **No git?** Install from [git-scm.com/downloads](https://git-scm.com/downloads) and reopen your terminal. Or **`< > Code` → Download ZIP**, unzip, rename the folder to `Lab02`.

Then check you landed right:

```text
pwd
ls
```

`pwd` must end in **`Week2/Lab02`**. `ls` must show `README.md`, `M1-W2-Lab02.md`, `CHEATSHEET.md`, `GLOSSARY.md`, `data`, `charts`, `scripts`, `practice` and `solutions`.

---

## 2. 🔧 Install the toolbox — **this week the setup IS a lesson**

Until now, everything you used came with Python. Today you add four **third-party libraries** — code other people wrote, downloaded from the internet, installed once. After today they are simply there, like `math` is.

**Open the folder in VS Code** (**File → Open Folder…** on your `Lab02` folder), open **Terminal → New Terminal**, and run:

```text
pip install pandas matplotlib seaborn scipy
```

On **Windows**, if `pip` is not recognised, use this instead — and then keep using the `py -m` style for the rest of the lab:

```text
py -m pip install pandas matplotlib seaborn scipy
```

On **Mac**:

```text
python3 -m pip install pandas matplotlib seaborn scipy
```

It prints a lot of scrolling text for a minute or two. **Success looks like** a final line starting `Successfully installed …`.

> 💡 **You asked for four libraries and more than four install.** That is correct. **NumPy arrives automatically** because pandas needs it, so pip fetches it for you. You never ask for NumPy by name.

### Prove it worked

```text
python scripts/00_check_setup.py
```

Five ✅ ticks and you are done. Any ❌ and the script tells you the exact command to fix that one. It is safe to run as many times as you like.

### When install goes wrong

| What you see | What it means | What to do |
|---|---|---|
| `'pip' is not recognized…` | Windows cannot find pip on its own | Use `py -m pip install pandas matplotlib seaborn scipy` — this asks *Python* to run pip, which always works. Then use `py` for everything else too. |
| `SSL: CERTIFICATE_VERIFY_FAILED`, `ProxyError`, or it hangs on "Collecting…" | You are on a company or campus network that inspects internet traffic | **Try home wifi first — that fixes it 90% of the time.** If you must use the work network, ask IT for the proxy settings. Or skip installing entirely and use the **Colab path** in §3.6 of the lab. |
| `Successfully installed` but still `ModuleNotFoundError: No module named 'pandas'` | **You have more than one Python**, and pip installed into the other one | Use the same one for both: `py -m pip install pandas`, then `py scripts/00_check_setup.py`. Whichever prefix you pick, use it for *everything* in this lab. |
| Version numbers differ from the lab's | Completely fine | Newer pandas describes text columns as `str` where older ones said `object`. Same column, different label. No numbers are affected. |

> 🌐 **Cannot install at all?** The lab's §3.6 covers doing the whole thing in **Google Colab**, where all four libraries are pre-installed. Every line of code and every expected output is identical.

---

## 3. 📂 What is in this repo

| Path | What it is |
|---|---|
| [`M1-W2-Lab02.md`](M1-W2-Lab02.md) | **The lab.** 23 steps, 10 clusters, quizzes, answer key. |
| [`CHEATSHEET.md`](CHEATSHEET.md) | Every pandas call from this lab on one page. Print it. |
| [`GLOSSARY.md`](GLOSSARY.md) | Plain-English definitions of the new words. |
| `data/` | Both CSV files the lab reads — see below. |
| `charts/` | **Starts almost empty on purpose.** Your PNG charts land here when you run scripts 08, 09, 10 and 12. |
| `scripts/` | `00_check_setup.py` plus twelve numbered scripts. |
| `practice/` | Nine practice problems, including a capstone report. **Your code goes here.** |
| `solutions/` | Worked solutions. Have a real go first. |

### The data

| File | What it holds |
|---|---|
| `data/tips.csv` | the till export — **244 bills** from the trial table-service season |
| `data/cozybean_takings.csv` | the shop's handwritten daily takings book, typed up — **with real gaps in it** |

Both ship with the repo. **Nothing in this lab needs the internet once the install is done** — you can do the whole thing on a train.

> 🛋️ **Aim for one sitting of about an hour**, with the setup done beforehand. If you do need to pause, the natural break is after Cluster F, with the data work done and the charts still ahead.

---

## 4. 💾 Saving your work back to GitHub

From inside `Lab02`, when you finish, or any time you pause:

```text
git add .
git commit -m "Made the scatter chart"
git push
```

Your PNG charts in `charts/` get committed too — that is deliberate. They are evidence of your own work, made on your own machine.

---

## 5. 🆘 If something goes wrong

| What you see | What it means | What to do |
|---|---|---|
| `FileNotFoundError: … 'data/tips.csv'` | You are running from the wrong folder. | `pwd` must end in `Lab02`. `ls` must show `data`. If not: **File → Open Folder** on your `Lab02` folder, then a fresh terminal. |
| **The terminal froze after a chart appeared** | It has not frozen. The script is waiting for you to close the chart window — **and the window may be hiding behind VS Code.** | Find it in your taskbar, admire your chart, close it. The script finishes immediately. **Your PNG was already saved** before the window ever opened. |
| `ModuleNotFoundError` for pandas / seaborn / scipy | The install did not land in the Python you are running. | See the install-troubleshooting table in section 2. |
| **Output did not change after an edit** | **The file was never saved.** | Look for the ● dot on the file tab. **Ctrl+S** / **Cmd+S**. Rerun. |

Still stuck after a genuine try? Post in the course channel with **what you ran**, **what you expected**, and **the last line of the error**.

---

*Apeiron AI Training Academy · Module 1, Week 2, Lab 02 · Previous: [Lab01 — The Cozy Bean Gets Organised](https://github.com/ApeironAI-2026/M1-W2-Lab01-B02)*
