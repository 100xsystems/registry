---
{
  "title": "Pandas: DataFrames & Series",
  "description": "Load, inspect, filter, group and merge tabular data with the most important library in data science.",
  "type": "lesson",
  "order": 5,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Load tabular data into a DataFrame",
    "Inspect, filter and sort rows and columns",
    "Group by and aggregate with split-apply-combine",
    "Join datasets on keys"
  ],
  "knowledge_refs": [
    "data-science/ds-04-numpy-arrays",
    "data-science/ds-06-data-cleaning",
    "data-science/ds-07-exploratory-data-analysis"
  ],
  "prerequisites": [
    "DS-04: NumPy: Arrays & Vectorization"
  ],
  "references": [
    {
      "title": "pandas — Getting Started Tutorials",
      "url": "https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html",
      "description": "Official hands-on tutorials using real datasets."
    },
    {
      "title": "10 minutes to pandas",
      "url": "https://pandas.pydata.org/docs/user_guide/10min.html",
      "description": "The quintessential quick introduction to Series, DataFrames, indexing and grouping."
    },
    {
      "title": "Python for Data Analysis — Wes McKinney (Chapter 5)",
      "url": "https://wesmckinney.com/book/pandas-basics",
      "description": "The definitive guide to pandas by its creator."
    },
    {
      "title": "pandas User Guide — Indexing and Selecting Data",
      "url": "https://pandas.pydata.org/docs/user_guide/indexing.html",
      "description": "The authoritative reference for loc/iloc and boolean selection."
    },
    {
      "title": "pandas User Guide — Group By: split-apply-combine",
      "url": "https://pandas.pydata.org/docs/user_guide/groupby.html",
      "description": "The official reference for groupby aggregation."
    }
  ]
}
---

# DS-05-PANDAS-DATAFRAMES: Pandas: DataFrames & Series

## Introduction

pandas is the spreadsheet engine of Python data science. Its two core structures are the **Series** (a labeled 1-D array) and the **DataFrame** (a labeled 2-D table of Series sharing an index). What makes pandas special is *label-based* work: you address data by names — columns, index labels — instead of by position, which keeps analyses readable and robust. This lesson covers the five operations you will use daily: load, inspect, filter, group, and join.

## Key Concepts

### 1. Loading data

```python
import pandas as pd

df = pd.read_csv("sales.csv")          # 90% of the time
df_excel = pd.read_excel("sales.xlsx", sheet_name="2024")
df_json = pd.read_json("events.json")
```

For URLs, pass the link directly — pandas will fetch it. `read_csv` accepts `sep`, `encoding`, `parse_dates`, and `index_col`; you will use these constantly as data gets messier (next lesson).

### 2. Inspecting a DataFrame

```python
print(df.head())          # first 5 rows
print(df.info())          # dtypes + non-null counts (essential!)
print(df.describe())      # numeric summary stats
print(df.shape)           # (rows, columns)
print(df.columns)         # column names
print(df["revenue"].value_counts(dropna=False).head())
```

`df.info()` is the first call in any analysis: it reveals missing values and wrong dtypes before they bite you.

### 3. Selecting and filtering

Two accessors, one rule: **`.loc` is labels, `.iloc` is positions.**

```python
df["revenue"]                          # one column (Series)
df[["name", "revenue"]]                # several columns
df.loc[df["revenue"] > 1000]           # boolean filter (THE workhorse)
df.loc[df["plan"].isin(["pro", "team"])]
df.iloc[10:20]                         # rows 10-19 by position
df.sort_values("revenue", ascending=False)
```

Remember: `df["col"] > x` produces a boolean Series; passing it to `.loc` (or `df[]`) selects the rows where it is `True`. This is pandas' answer to SQL `WHERE`.

### 4. Group by: split-apply-combine

The most powerful pandas idiom: **split** the data into groups, **apply** a function to each, **combine** the results.

```python
df.groupby("region")["revenue"].mean()
# region
# east     2350.5
# west     1980.2

df.groupby(["region", "plan"])["revenue"].agg(["sum", "count", "mean"])
```

You can group by any column(s), then aggregate with `mean`, `sum`, `count`, `median`, `std`, `nunique`, or a custom function via `.agg`. `groupby` is the tool that turns "compare segments" questions into two lines of code.

### 5. Joining datasets

Real analyses stitch multiple tables together:

```python
customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")

merged = orders.merge(customers, on="customer_id", how="left")
# how="left" keeps every order, filling customer info where known
```

`how` mirrors SQL joins: `inner`, `left`, `right`, `outer`. Always check the row count before and after — a doubling of rows usually means duplicate keys, which you'll fix in the cleaning lesson.

### 6. Two habits that prevent bugs

1. **Check for duplicates**: `df.duplicated().sum()` before and after merges.
2. **Check dtypes early**: `df.info()`; a numeric column read as `object` will break math silently (you'll see "strings that look like numbers" in the next lesson).

## Practice Questions

1. Load any CSV you have (or `df = pd.DataFrame({"a": [1,2,3], "b": [4,5,6]})`) and print `info()`, `describe()`, and the first 3 rows.
2. Filter a DataFrame to rows where a column is in a list of values, then sort by another column descending.
3. Compute, per category, the mean and count of a numeric column using `groupby`.
4. What is the difference between `loc` and `iloc`? Give one example of each.

## LLM Prompts for Deeper Understanding

1. "Explain the pandas split-apply-combine pattern with three real business examples."
2. "When would I use merge with how='left' vs how='inner', and what bugs arise from each?"
3. "Show me pandas code that answers 'which segment has the highest median revenue per month'."

## Key Takeaways

- DataFrame = labeled 2-D table; Series = labeled 1-D column.
- `.loc` for labels, `.iloc` for positions; boolean masks are SQL `WHERE`.
- `groupby().agg()` = split-apply-combine, the core analysis idiom.
- `merge(..., how=...)` joins tables like SQL; verify row counts.
- Always run `info()` first — it exposes missing values and wrong dtypes.

## Footnotes & Attribution

1. pandas documentation, *Getting Started Tutorials*. [https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
2. pandas documentation, *10 minutes to pandas*. [https://pandas.pydata.org/docs/user_guide/10min.html](https://pandas.pydata.org/docs/user_guide/10min.html)
3. Wes McKinney, *Python for Data Analysis* (Ch. 5). [https://wesmckinney.com/book/pandas-basics](https://wesmckinney.com/book/pandas-basics)
4. pandas documentation, *Indexing and Selecting Data*. [https://pandas.pydata.org/docs/user_guide/indexing.html](https://pandas.pydata.org/docs/user_guide/indexing.html)
5. pandas documentation, *Group By: split-apply-combine*. [https://pandas.pydata.org/docs/user_guide/groupby.html](https://pandas.pydata.org/docs/user_guide/groupby.html)
