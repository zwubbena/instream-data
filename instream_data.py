# ===============================================================
# Program: instream_data.py
# Purpose: Demonstrate instream data using Python StringIO
# ===============================================================

# -------------------------------
# SECTION 1: Import Dependencies
# -------------------------------
import pandas as pd
from io import StringIO

# -------------------------------
# SECTION 2: Define Instream Data
# -------------------------------
data = """ID,Title,Year
01,The Big Lebowski,1998
02,Happy Gilmore,1996
03,Kindergarten Cop,1990
04,Good Will Hunting,1997
05,Pretty Woman,1990
06,Groundhog Day,1993
07,Twister,1996
08,Sphere,1998
09,Home Alone,1990"""

# -------------------------------
# SECTION 3: Load Data to DataFrame
# -------------------------------
# Read ID as string to preserve leading zeros
df = pd.read_csv(StringIO(data), dtype={'ID': str})

# -------------------------------
# SECTION 4: Display Output
# -------------------------------
print("Instream Movie Data with Leading Zeros in ID:")
print(df.to_string(index=False))

# ===============================================================
# Python Script End
# ===============================================================
