---
{
  "title": "NumPy: Arrays & Vectorization",
  "description": "Master the n-dimensional array, vectorized operations, and the broadcasting rules that make Python fast.",
  "type": "lesson",
  "order": 4,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create and inspect NumPy arrays with the key constructors",
    "Perform vectorized arithmetic and aggregations",
    "Explain broadcasting and index with boolean masks",
    "Understand why vectorization outperforms Python loops"
  ],
  "knowledge_refs": [
    "data-science/ds-03-python-for-data-science",
    "data-science/ds-05-pandas-dataframes",
    "data-science/ds-09-statistics-fundamentals"
  ],
  "prerequisites": [
    "DS-03: Python for Data Science"
  ],
  "references": [
    {
      "title": "NumPy: The Absolute Basics for Beginners",
      "url": "https://numpy.org/doc/stable/user/absolute_beginners.html",
      "description": "The official beginner's guide to arrays, indexing, and vectorized math."
    },
    {
      "title": "From Python to NumPy — Nicolas P. Rougier",
      "url": "https://github.com/rougier/from-python-to-numpy",
      "description": "Open-access book on vectorization, memory layout, and high-performance NumPy."
    },
    {
      "title": "NumPy User Guide",
      "url": "https://numpy.org/doc/stable/user/index.html",
      "description": "The authoritative reference for the array-computing foundation."
    },
    {
      "title": "Python Data Science Handbook — Chapter 2 (NumPy)",
      "url": "https://jakevdp.github.io/PythonDataScienceHandbook/",
      "description": "Hands-on NumPy coverage: arrays, broadcasting, masks, and aggregation."
    },
    {
      "title": "SciPy Lecture Notes — NumPy chapter",
      "url": "https://lectures.scientific-python.org/advanced/advanced_numpy/",
      "description": "Deeper dive into NumPy internals and advanced indexing."
    }
  ]
}
---

# DS-04-NUMPY-ARRAYS: NumPy: Arrays & Vectorization

## Introduction

If pandas is the spreadsheet, NumPy is the calculator underneath. NumPy provides the **n-dimensional array** (`ndarray`) — a homogeneous, fixed-size block of numbers — plus fast operations on whole arrays. Its superpower is **vectorization**: expressing operations on entire arrays at once so that the heavy lifting happens in optimized C code instead of a slow Python loop. Nearly every other scientific library (pandas, scikit-learn, Matplotlib, PyTorch) is built on NumPy arrays, so this foundation pays off everywhere.

## Key Concepts

### 1. Creating arrays

```python
import numpy as np

a = np.array([1, 2, 3])                 # from a list
zeros = np.zeros((3, 4))                # 3x4 of zeros
ones = np.ones((2, 3))                  # 2x3 of ones
rng = np.arange(0, 10, 2)               # [0, 2, 4, 6, 8]
lin = np.linspace(0, 1, 5)              # 5 evenly spaced points: [0., .25, .5, .75, 1.]
r = np.random.default_rng(42)           # reproducible generator
rand = r.normal(0, 1, (3, 3))           # 3x3 standard normal draws

print(a.ndim, a.shape, a.dtype)         # 1 (3,) int64
```

Note the modern style: `np.random.default_rng(seed)` instead of the legacy `np.random.seed` — it is faster and safer (each generator is isolated).

### 2. Vectorized arithmetic and aggregation

```python
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)          # [11 22 33 44]
print(a * 2)          # [2 4 6 8]  — scalar broadcast
print(a ** 2)         # elementwise power
print(a.mean(), a.sum(), a.std(), a.max())   # 2.5 10 1.118 4
```

Aggregations accept an `axis` argument — the dimension you collapse. For a 2-D array (rows=samples, columns=features):

```python
X = np.array([[1, 2], [3, 4], [5, 6]])
print(X.mean(axis=0))   # mean of each column: [3. 4.]
print(X.mean(axis=1))   # mean of each row:    [1.5 3.5 5.5]
```

Remembering `axis=0` = "down the rows" and `axis=1` = "across the columns" saves you endless confusion in data work.

### 3. Boolean masking: filtering without loops

Comparison operators return boolean arrays, which you can use directly as indexes:

```python
temps = np.array([18.2, 22.1, 15.9, 29.4, 21.0])
hot = temps > 25
print(hot)                  # [False False False  True False]
print(temps[hot])           # [29.4]
print(temps[(temps > 15) & (temps < 25)])   # combine masks with & |
```

This pattern — *compute a mask, then index* — is the NumPy equivalent of "WHERE" in SQL, and it is everywhere in data science.

### 4. Broadcasting: the rules

Broadcasting lets NumPy operate on arrays of *different shapes* without making copies, as long as the shapes are *compatible*. The rule: align shapes from the trailing dimension; dimensions must either match or be 1.

```python
col = np.array([[1], [2], [3]])     # (3,1)
row = np.array([10, 20])            # (2,)  -> treated as (1,2)
print(col + row)
# [[11 21]
#  [12 22]
#  [13 23]]
```

A very common real usage: subtract the column means from every column ("centering"), or divide by column standard deviations ("standardizing") — one line, no loops:

```python
X = np.random.default_rng(0).normal(5, 2, (100, 3))
Xc = X - X.mean(axis=0)          # center each column
Xs = Xc / X.std(axis=0)          # standardize each column
```

### 5. Why vectorization matters

Compare a Python loop with a vectorized operation on one million elements:

```python
n = 1_000_000
data = np.random.default_rng(1).normal(size=n)

# Slow: Python loop
total = 0.0
for x in data:
    total += x ** 2

# Fast: vectorized
total_fast = (data ** 2).sum()
```

The vectorized version is typically 50–100× faster, because the loop runs in compiled C, not interpreted Python. This speed gap is why the entire scientific stack is built on arrays. It also matters for correctness: vectorized code has fewer places for bugs to hide.

## Practice Questions

1. Create a 5×5 array of random integers between 0 and 100 using a seeded generator, then compute the mean of each row and each column.
2. Given `scores = np.array([88, 92, 47, 73, 95])`, use a boolean mask to get all scores above 80 and below 90.
3. What does `X.mean(axis=0)` compute for a matrix where rows are samples? Why is this the default mental model for tabular data?
4. Explain the broadcasting rule in one sentence, and give an example where shapes are incompatible.

## LLM Prompts for Deeper Understanding

1. "Explain NumPy broadcasting with five progressively harder examples."
2. "Show me how vectorization changes how I think about writing data-cleaning code."
3. "What are the differences between numpy arrays and pandas DataFrames, and when should I use each?"

## Key Takeaways

- NumPy arrays are homogeneous, fast, and the foundation of the whole scientific stack.
- Use vectorized arithmetic and aggregations with `axis` instead of Python loops.
- Boolean masks are your SQL-WHERE for arrays.
- Broadcasting allows shape-mismatched math when dimensions match or equal 1.
- Seeded `default_rng` keeps random experiments reproducible.

## Footnotes & Attribution

1. NumPy team, *NumPy: The Absolute Basics for Beginners*. Official tutorial. [https://numpy.org/doc/stable/user/absolute_beginners.html](https://numpy.org/doc/stable/user/absolute_beginners.html)
2. Nicolas P. Rougier, *From Python to NumPy*. Open-access vectorization book. [https://github.com/rougier/from-python-to-numpy](https://github.com/rougier/from-python-to-numpy)
3. NumPy team, *NumPy User Guide*. The authoritative reference. [https://numpy.org/doc/stable/user/index.html](https://numpy.org/doc/stable/user/index.html)
4. Jake VanderPlas, *Python Data Science Handbook*, Ch. 2. Free, open-access. [https://jakevdp.github.io/PythonDataScienceHandbook/](https://jakevdp.github.io/PythonDataScienceHandbook/)
5. Scipy Lecture Notes, *Advanced NumPy*. [https://lectures.scientific-python.org/advanced/advanced_numpy/](https://lectures.scientific-python.org/advanced/advanced_numpy/)
