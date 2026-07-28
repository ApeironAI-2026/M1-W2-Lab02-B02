# ============================================================
#  The Cozy Bean -- Script 01: What's in the Accountant's Bag
#  Lab STEPs 1-2.
#  Shows: the six libraries, and the four import lines that
#         start almost every data script ever written.
#  Run:   python scripts/01_the_toolbox.py  (from M1-W2-Lab02/)
# ============================================================

# ---- Section 1  (STEP 2): the four famous nicknames --------
# These four lines, with these four nicknames, are a
# convention the whole world follows. Write them this way and
# any data person on earth can read your code.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=== THE ACCOUNTANT'S BAG ===")
print()

# ---- Section 2  (STEP 1): what each one is for ------------
print("numpy      ", np.__version__, "- fast maths on a great many numbers")
print("pandas     ", pd.__version__, "- tables. THE one you will live in")
print("matplotlib ", plt.matplotlib.__version__, "- charts")
print("seaborn    ", sns.__version__, "- prettier statistical charts")

from scipy import stats
import scipy

print("scipy      ", scipy.__version__, "- scientific algorithms + statistics")
print()
print("scikit-learn  - the machine-learning algorithms (later in the course)")
print("statsmodels   - regressions and hypothesis tests, R-style (later)")
print()
print("Today is entirely pandas, with three charts at the end.")
