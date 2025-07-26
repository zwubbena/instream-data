# Instream Data in SAS and Python

## Overview

Instream data refers to data embedded directly within a script or program file, rather than being read from an external data file. 
This method is useful when:

- Teaching/educational examples and tutorials
- Testing and debugging scripts
- Test/demonstrating logic with small datasets
- Saring reproducible examples without external file dependencies

This repository shows how to use instream data in both **SAS** and **Python**.

---

## Dataset

The following dataset is used to show instream data loading:

| ID | Title               | Year |
|----|---------------------|------|
| 01  | The Big Lebowski    | 1998 |
| 02  | Happy Gilmore       | 1996 |
| 03  | Kindergarten Cop    | 1990 |
| 04  | Good Will Hunting   | 1997 |
| 05  | Pretty Woman        | 1990 |
| 06  | Groundhog Day       | 1993 |
| 07  | Twister             | 1996 |
| 08  | Sphere              | 1998 |
| 09  | Home Alone          | 1990 |

## Using Instream Data: SAS and Python

Instream data is useful when you want to **embed data directly inside your script** without referencing an external file. While the mechanics differ slightly between SAS and Python, the intent is the same: make small, readable datasets easily accessible in a self-contained program.

---

### 🟣 Python Example (`StringIO`)

In Python, the `io.StringIO` class simulates file input, making it ideal for loading instream text data. The following example shows tabular data defined inline as a multiline string.

```python
from io import StringIO
import pandas as pd

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

# Read ID as string to preserve leading zeros
df = pd.read_csv(StringIO(data), dtype={'ID': str})

print("Instream Movie Data with Leading Zeros in ID:")
print(df.to_string(index=False))
```

> [!NOTE]
> Python does not have true native inline data support like SAS. Instead, we simulate a file using `io.StringIO`.

---

### 🔵 SAS Example (`datalines`)

In SAS, `datalines` is a built-in feature that allows you to define instream data directly within a program, typically following an 'input' statement that defines the variable structure. The following example shows how to use instream data to simulate a small tabular dataset.

```sas
data movies;
    infile datalines dlm='|' dsd;
    length ID $2 Title $50 Year 4;
    input ID $ Title : $50. Year;
    datalines;
01|The Big Lebowski|1998
02|Happy Gilmore|1996
03|Kindergarten Cop|1990
04|Good Will Hunting|1997
05|Pretty Woman|1990
06|Groundhog Day|1993
07|Twister|1996
08|Sphere|1998
09|Home Alone|1990
;
run;

title "Instream Movie Data with Leading Zeros in ID (SAS)";
proc print data=movies noobs label;
    label 
        ID = "Movie ID"
        Title = "Title"
        Year = "Release Year";
run;
```
---

## ✅ When to Use Instream Data

These use cases apply to both SAS and Python:

- Small, self-contained examples for tutorials or documentation  
- Prototyping or testing logic before scaling up  
- Educational exercises and reproducible demonstrations  
- Debugging workflows where external file dependencies are a burden  

---

## ❌ When NOT to Use Instream Data

Avoid instream data for:

- Large or dynamic datasets that change over time  
- Production systems where external sources are standard  
- Scenarios requiring version control or team-managed data  
- Extract, Transform, Load (ETL) pipelines needing automation and scalability

---

## Output Files

Each example script prints or outputs a formatted table showing the instream data successfully loaded and parsed correctly.

- `instream_data.py` – Python script using `StringIO`
- `instream_data.sas` – SAS program using `DATALINES`
