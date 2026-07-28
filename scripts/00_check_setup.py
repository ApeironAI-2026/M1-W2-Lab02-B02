# ============================================================
#  The Cozy Bean -- Script 00: Check Your Setup
#  Run this FIRST, before anything else in this lab.
#
#  It tries to import each of the four libraries you installed
#  and reports on each one. Nothing here can break anything --
#  run it as many times as you like.
#
#  Run:   python scripts/00_check_setup.py  (from M1-W2-Lab02/)
# ============================================================

import sys

# Make sure the tick and cross below can always be printed, on
# every computer and every terminal. (Without this, a Windows
# console can refuse to show them and stop the script -- which
# would be a rotten way to start a lab.)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

print("=== THE COZY BEAN -- KITCHEN INSPECTION ===")
print()

# (name to import, name to type at pip)
libraries = [
    ("pandas", "pandas"),
    ("numpy", "numpy"),
    ("matplotlib", "matplotlib"),
    ("seaborn", "seaborn"),
    ("scipy", "scipy"),
]

all_good = True

for import_name, pip_name in libraries:
    try:
        module = __import__(import_name)
        version = getattr(module, "__version__", "installed")
        print(f"  ✅  {import_name:12} {version}")
    except ImportError:
        all_good = False
        print(f"  ❌  {import_name:12} NOT INSTALLED")
        print(f"        try:  py -m pip install {pip_name}")

print()

if all_good:
    print("All five ready. You can start the lab.")
else:
    print("Something is missing -- see the line marked XX above.")
    print("Install it, then run this script again.")
