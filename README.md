# Instream Data in SAS and Python

## Overview

Instream data refers to data that is included directly within a script or program file, rather than being read from an external file. This approach is especially useful for:

- Educational examples and tutorials
- Testing and debugging scripts
- Demonstrating logic on a small dataset

This repository provides examples in both **SAS** and **Python** for how to use instream data, with a consistent dataset used across both languages.

---

## Dataset Used

The following simple dataset is used to demonstrate instream data loading:

| ID | Name     | Age |
|----|----------|-----|
| 1  | Alice    | 34  |
| 2  | Bob      | 45  |
| 3  | Charlie  | 29  |
| 4  | Denise   | 42  |
| 5  | Edward   | 23  |

---

## Python: Using `io.StringIO`

Python does not have built-in support for inline data like SAS. Instead, we use the `io.StringIO` module to simulate reading from a file.

### Pros
- Great for testing and examples
- Portable and avoids temporary file creation

### Cons
- Not practical for large data
- Not a substitute for persistent storage

---

## SAS: Using `DATALINES`

SAS supports instream data via the `DATALINES` or `CARDS` keyword, allowing you to define datasets inline.

### Pros
- Simple and readable
- Very common for demos and testing

### Cons
- Not intended for large-scale production data
- Manual editing required for changes

---

## When *Not* to Use Instream Data

- Large datasets better suited for CSV, Excel, or databases
- When data is maintained and updated separately
- When working in production environments where version control of data is critical

---

## Example Output

Both scripts print or display the loaded data so you can visually confirm that the instream data is loaded and parsed correctly.

---

## Files

- `instream_data.sas` — SAS program using `DATALINES`
- `instream_data.py` — Python script using `StringIO`
