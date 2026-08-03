---
{
  "title": "Data Cleaning & Wrangling",
  "description": "Fix missing values, wrong types, duplicates and inconsistent text — the 60–80% of real data work.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Diagnose missing values and wrong dtypes",
    "Handle missing data with drop, fill and imputation",
    "Deduplicate and standardize messy text",
    "Write a repeatable cleaning pipeline as functions"
  ],
  "knowledge_refs": [
    "data-science/ds-05-pandas-dataframes",
    "data-science/ds-07-exploratory-data-analysis",
    "data-science/ds-13-feature-engineering"
  ],
  "prerequisites": [
    "DS-05: Pandas: DataFrames & Series"
  ],
  "references": [
    {
      "title": "Pythonic Data Cleaning With pandas and NumPy — Real Python",
      "url": "https://realpython.com/python-data-cleaning-numpy-pandas/",
      "description": "Step-by-step guide to real-world wrangling: missing data, text cleanup, vectorized operations."
    },
    {
      "title": "pandas — Working with Missing Data",
      "url": "https://pandas.pydata.org/docs/user_guide/missing_data.html",
      "description": "Official reference for NaN handling, dropna and fillna."
    },
    {
      "title": "pandas — Cleaning Data (Getting Started)",
      "url": "https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html",
      "description": "Official getting-started tutorial covering missing-value workflows."
    },
    {
      "title": "Python for Data Analysis — Wes McKinney (Chapter 7)",
      "url": "https://wesmckinney.com/book/data-cleaning",
      "description": "Data cleaning and preparation from the creator of pandas."
    }
  ]
}
---

# DS-06-DATA-CLEANING: Data Cleaning & Wrangling

## Introduction

In real life, the "tidy" datasets of tutorials do not exist. Real data has missing values, inconsistent spelling, mixed types, duplicated rows, and "numbers" stored as text. Cleaning and wrangling reliably eats **60–80% of project time** — and it is not busywork: a clean dataset is what makes every later stage trustworthy. This lesson teaches the four core cleaning skills with a repeatable, function-based workflow.

## Key Concepts

### 1. Diagnose before you touch anything

```python
import pandas as pd

df = pd.read_csv("customers.csv")
print(df.info())                 # dtypes + non-null counts
print(df.isna().sum())           # missing values per column
print(df.duplicated().sum())     # duplicate rows
print(df["price"].unique()[:10]) # look at raw values — spot "12.5 USD"
```

`info()` and `isna().sum()` answer *what* is broken; looking at raw unique values answers *how* it is broken ("12.5 USD" instead of `12.5`).

### 2. Fixing dtypes

A numeric column stored as strings will break `mean()`, `sort_values`, and joins. Fix it with `pd.to_numeric`:

```python
df["price"] = pd.to_numeric(df["price"], errors="coerce")
# "12.5 USD" -> NaN; "12.5" -> 12.5
```

Dates are the other classic: `pd.to_datetime(df["date"], errors="coerce")`. `errors="coerce"` converts unparseable values to `NaN` instead of crashing, so you can see *how many* rows are broken in one go.

### 3. Handling missing values

There is no universal rule — the right choice depends on *why* the data is missing:

```python
df.dropna(subset=["email"])           # 1) drop rows missing a critical column
df.dropna(thresh=int(0.8 * len(df)))  # 2) drop rows missing >20% of columns
df["age"].fillna(df["age"].median())  # 3) fill with a statistic (mean/median)
df["age"] = df["age"].interpolate()   # 4) interpolate for ordered/time series
```

Key insight: **missingness often carries information.** A blank "churn_reason" might mean "did not churn." Consider adding an `is_missing` indicator column before you fill, and be wary of dropping rows that would bias your sample.

### 4. Deduplication and text standardization

```python
df = df.drop_duplicates(subset=["customer_id"], keep="first")

df["city"] = df["city"].str.strip().str.lower()   # "  NY " -> "ny"
df["city"] = df["city"].replace({"ny": "new york", "NYC": "new york"})
```

`Series.str` unlocks string methods: `strip`, `lower`, `replace`, `contains`, `extract` with regex. Standardizing categories is essential because "NY", "N.Y.", and "New York" will otherwise split into three groups in every `groupby`.

### 5. Outliers: investigate, don't just delete

Outliers can be typos (a salary of `9,999,999`) or real signal (a power user). Use EDA to look, then decide:

```python
print(df["revenue"].describe())          # where is the long tail?
q99 = df["revenue"].quantile(0.99)
df_trimmed = df[df["revenue"] <= q99]    # cap at 99th percentile (winsorize)
```

Never silently drop "weird" rows; document the rule (e.g., "capped revenue at the 99th percentile") so your analysis is reproducible.

### 6. Make cleaning a repeatable pipeline

The biggest mistake is cleaning in ad-hoc notebook cells that can't be re-run. Instead, wrap each fix in a named function, and chain them:

```python
def clean(df):
    df = df.copy()
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["price"])
    df["city"] = df["city"].str.strip().str.lower()
    df = df.drop_duplicates()
    return df

df_clean = clean(pd.read_csv("customers.csv"))
```

Now when a colleague asks "how did you clean this?", the answer is a versioned function — not a memory.

## Practice Questions

1. `df.isna().sum()` shows `price: 87`. List three different ways to handle those rows, and when each is appropriate.
2. A `date` column contains "2024-13-01" (invalid month). What does `pd.to_datetime(..., errors="coerce")` produce, and why is that better than crashing?
3. Why is "NY", "N.Y.", "ny" in one column a problem for `groupby`? Write the code to fix it.
4. Write a `clean()` function for a CSV of your choice and run it twice to prove it's idempotent.

## LLM Prompts for Deeper Understanding

1. "Explain the difference between MCAR, MAR, and MNAR missing data, and what each implies for imputation."
2. "Show me a pandas pipeline that cleans dates, currencies, and city names from a messy CSV."
3. "What are the most common ways people accidentally introduce bias while cleaning data?"

## Key Takeaways

- Diagnose with `info()`, `isna().sum()`, `duplicated()`, and raw `unique()` values first.
- Fix dtypes with `to_numeric`/`to_datetime(..., errors="coerce")`.
- Missing values: drop (with care), fill with statistics, or interpolate — know why you chose which.
- Standardize text (`strip().lower().replace()`) so categories group correctly.
- Wrap cleaning in functions so it is versionable and reproducible.

## Footnotes & Attribution

1. Real Python, *Pythonic Data Cleaning With pandas and NumPy*. [https://realpython.com/python-data-cleaning-numpy-pandas/](https://realpython.com/python-data-cleaning-numpy-pandas/)
2. pandas documentation, *Working with Missing Data*. [https://pandas.pydata.org/docs/user_guide/missing_data.html](https://pandas.pydata.org/docs/user_guide/missing_data.html)
3. pandas documentation, *Getting Started — Calculate Statistics* (missing data workflows). [https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html)
4. Wes McKinney, *Python for Data Analysis* (Ch. 7). [https://wesmckinney.com/book/data-cleaning](https://wesmckinney.com/book/data-cleaning)
