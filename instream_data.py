# ===============================================================
# Program: instream_examples.py
# Purpose: Demonstrate instream data in Python (equivalent to SAS DATALINES)
# ===============================================================

import pandas as pd
from io import StringIO

# ***********************************
# | EXAMPLE #1
# ***********************************

# -------------------------------
# SECTION 1: Define Instream Movie Data
# -------------------------------
movie_data = """
ID|Title|Year
01|The Big Lebowski|1998
02|Happy Gilmore|1996
03|Kindergarten Cop|1990
04|Good Will Hunting|1997
05|Pretty Woman|1990
06|Groundhog Day|1993
07|Twister|1996
08|Sphere|1998
09|Home Alone|1990
"""

df_movies = pd.read_csv(StringIO(movie_data.strip()), sep='|', dtype={'ID': str})

# -------------------------------
# SECTION 2: Display Output
# -------------------------------
print("------------------------------------------------------------")
print("Instream Movie Data with Leading Zeros in ID (Python)")
print("------------------------------------------------------------")
print("\n[DATAFRAME STRUCTURE] (similar to PROC CONTENTS):")
df_movies.info()
print("\n[DATA PREVIEW] (similar to PROC PRINT):")
print(df_movies.to_string(index=False))

# ***********************************
# | EXAMPLE #2
# ***********************************

# -------------------------------
# SECTION 1: Define Instream Race/Ethnicity Data
# -------------------------------
ethnicity_data = """
ID SPED H I A P B W
0001 1 1 0 0 0 0 0
0002 1 0 1 0 0 0 0
0003 1 0 0 1 0 0 0
0004 1 0 0 0 1 0 0
0005 1 0 0 0 0 1 0
0006 1 0 0 0 0 0 1
0007 1 1 1 0 0 0 0
0008 1 0 1 1 0 0 0
0009 1 1 0 1 0 0 0
0010 1 0 0 1 1 0 0
0011 1 0 1 0 1 0 0
0012 1 1 0 0 1 0 0
0013 1 0 0 0 1 1 0
0014 1 0 0 1 0 1 0
0015 1 0 1 0 0 1 0
0016 1 1 0 0 0 1 0
0017 1 0 0 0 0 1 1
0018 1 0 0 0 1 0 1
0019 1 0 0 1 0 0 1
0020 1 . . . . . .
"""

df_eth_race = pd.read_csv(
    StringIO(ethnicity_data.strip()), 
    delim_whitespace=True, 
    dtype={'ID': str},
    na_values='.'
)

# -------------------------------
# SECTION 2: Display Output
# -------------------------------
print("\n\n------------------------------------------------------------")
print("Instream Race/Ethnicity Data with Leading Zeros in ID (Python)")
print("------------------------------------------------------------")
print("\n[DATAFRAME STRUCTURE] (similar to PROC CONTENTS):")
df_eth_race.info()
print("\n[DATA PREVIEW] (similar to PROC PRINT):")
print(df_eth_race.to_string(index=False))

# Optional: Labels (SAS-style, for reference)
column_labels = {
    'ID': 'Student ID',
    'SPED': 'Special Education',
    'H': 'Hispanic',
    'I': 'American Indian or Alaska Native',
    'A': 'Asian',
    'P': 'Pacific Islander',
    'B': 'Black or African American',
    'W': 'White'
}

# ===============================================================
# Python Script End
# ===============================================================
