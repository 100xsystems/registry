---
{
  "title": "Python for Data Science",
  "description": "The Python fundamentals every data scientist leans on: collections, comprehensions, file I/O, and reproducible notebooks.",
  "type": "lesson",
  "order": 3,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use core Python collections and comprehensions fluently",
    "Read and write data files with the standard library",
    "Write clean, vectorization-friendly, reproducible Python",
    "Structure code in Jupyter notebooks for exploration"
  ],
  "knowledge_refs": [
    "data-science/ds-04-numpy-arrays",
    "data-science/ds-05-pandas-dataframes",
    "data-science/ds-01-what-is-data-science"
  ],
  "prerequisites": [
    "DS-02: The Data Science Pipeline"
  ],
  "references": [
    {
      "title": "Scientific Python Lectures — Scipy Lecture Notes",
      "url": "https://lectures.scientific-python.org/",
      "description": "The definitive free tutorial path from Python basics to NumPy/SciPy/Matplotlib."
    },
    {
      "title": "Python Data Science Handbook — Jake VanderPlas (Chapter 1)",
      "url": "https://jakevdp.github.io/PythonDataScienceHandbook/",
      "description": "Free book; Chapter 1 covers the Python data science idioms used throughout this course."
    },
    {
      "title": "Python for Data Analysis — Wes McKinney (Chapter 2)",
      "url": "https://wesmckinney.com/book/python-basics",
      "description": "Python language basics from the creator of pandas."
    },
    {
      "title": "Real Python — Python Tutorials",
      "url": "https://realpython.com/",
      "description": "Huge library of practical Python tutorials at every level."
    }
  ]
}
---

# DS-03-PYTHON-FOR-DATA-SCIENCE: Python for Data Science

## Introduction

Python became the language of data science for three reasons: it is *readable* (so analyses can be audited), it has a *massive scientific ecosystem* (NumPy, pandas, Matplotlib, scikit-learn), and it *glues* — you can call C/Fortran-speed libraries from a few lines of Python. This lesson covers the core language you need *before* touching those libraries: collections, comprehensions, functions, file I/O, and the discipline of writing reproducible code. If you already know Python, skim fast and focus on the "data science idioms" at the end.

## Key Concepts

### 1. The four collections you will actually use

- **Lists** `[...]` — ordered, mutable sequences. Your default for anything ordered.
- **Tuples** `(...)` — ordered, immutable. Great for fixed records like `(lat, lon)` or `(year, month)`.
- **Dicts** `{...}` — key→value maps. Used everywhere: configs, counts, lookups.
- **Sets** `{...}` — unique, unordered. Ideal for membership tests and deduplication.

```python
prices = [19.99, 29.99, 9.99]          # list
coords = (52.52, 13.41)                # tuple (Berlin)
lookup = {"free": 0.0, "pro": 19.99}   # dict
unique_tags = {"ai", "ml", "data"}     # set

print(prices[0], coords[0], lookup["pro"], "ml" in unique_tags)
```

The collection you *don't* see — **NumPy arrays** — is next lesson's subject; lists are too slow for serious numeric work.

### 2. Comprehensions: the data science idiom

Comprehensions build a new collection from an existing one in one readable line. In data science you will write these constantly — filtering rows, transforming features, collecting results.

```python
nums = [1, 2, 3, 4, 5, 6]
evens = [n for n in nums if n % 2 == 0]      # [2, 4, 6]
squares = {n: n**2 for n in nums}            # dict comprehension
odds = {n for n in nums if n % 2 == 1}       # set comprehension

print(evens, squares[3], odds)
```

Rule of thumb: if you find yourself writing a `for` loop that just builds a list, replace it with a comprehension — it is faster to read and marginally faster to run.

### 3. Functions, unpacking, and `*args`/`**kwargs`

Functions are how you keep analyses organized. Two idioms matter most: **tuple unpacking** (used constantly with pandas rows and `enumerate`) and **default arguments** (used to make functions flexible without clutter).

```python
def summarize(prices, currency="USD"):
    total = sum(prices)
    return len(prices), total

count, total = summarize(prices, currency="EUR")
print(count, total)

for idx, price in enumerate(prices):   # unpacking in loops
    print(idx, price)
```

### 4. File I/O: reading raw data

Before pandas there is the standard library. `csv` and `json` cover 90% of raw files you will meet:

```python
import csv, json

with open("data.csv", "r", newline="") as f:
    rows = list(csv.DictReader(f))   # each row is a dict keyed by header

with open("config.json") as f:
    cfg = json.load(f)

print(len(rows), cfg.get("seed"))
```

Use `with` blocks so files are always closed — even when an exception interrupts your notebook cell.

### 5. Reproducible notebooks: the discipline

A notebook is a living analysis, so keep it *auditable*:

- **Set a random seed** at the top (`import random; random.seed(42)`) so sampling is repeatable.
- **Keep cells small and ordered** — a notebook that must be run top-to-bottom is reproducible; one with hidden state is not.
- **Version your data**, not just your code: record where each dataset came from and when you fetched it.
- **Prefer functions over long scripts** — testable, reusable, reviewable.

This discipline is what separates analyses people trust from analyses people rerun suspiciously.

## Practice Questions

1. Write a list comprehension that filters words shorter than 4 characters from `words = ["cat", "data", "ml", "science"]`.
2. What is the difference between a list and a tuple? When would you choose a set?
3. Convert a dict of counts into a list of `(key, count)` tuples sorted by count descending, using a comprehension and `sorted`.
4. Why does this course stress setting a random seed at the top of a notebook?

## LLM Prompts for Deeper Understanding

1. "Explain when to use list, tuple, set, and dict in Python with data-science-flavored examples."
2. "Show me how to rewrite a nested for loop as a comprehension, and when I shouldn't."
3. "What are the most common Python bugs in data-cleaning code, and how do I avoid them?"

## Key Takeaways

- Lists, tuples, dicts, and sets cover almost all everyday data structures.
- Comprehensions are the idiomatic way to filter and transform collections.
- Use `with` blocks for files; `csv.DictReader` and `json` handle most raw data.
- Reproducibility = seed + ordered cells + versioned data + functions.

## Footnotes & Attribution

1. Scipy Lecture Notes, *Scientific Python Lectures*. The canonical free path from Python to the scientific stack. [https://lectures.scientific-python.org/](https://lectures.scientific-python.org/)
2. Jake VanderPlas, *Python Data Science Handbook* (Chapter 1). Free, open-access. [https://jakevdp.github.io/PythonDataScienceHandbook/](https://jakevdp.github.io/PythonDataScienceHandbook/)
3. Wes McKinney, *Python for Data Analysis* (Chapter 2). Python language basics. [https://wesmckinney.com/book/python-basics](https://wesmckinney.com/book/python-basics)
4. Real Python. Practical Python tutorials. [https://realpython.com/](https://realpython.com/)
