---
{
  "title": "NumPy: Arrays & Vectorization",
  "description": "Master ndarrays, broadcasting and vectorized math — the engine under every serious data workflow.",
  "type": "lesson",
  "order": 4,
  "duration": "55 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create and reshape NumPy arrays",
    "Use vectorized math instead of Python loops",
    "Apply broadcasting rules correctly",
    "Index, slice and mask arrays efficiently"
  ],
  "knowledge_refs": [
    "data-science/ds-04-numpy-arrays"
  ],
  "prerequisites": [
    "DS-03: Python for Data Science"
  ],
  "references": [
    {
      "title": "Python for Data Analysis — Wes McKinney",
      "url": "https://wesmckinney.com/book/",
      "description": "The definitive guide to pandas, NumPy and the PyData stack."
    },
    {
      "title": "Pandas User Guide",
      "url": "https://pandas.pydata.org/docs/user_guide/index.html",
      "description": "Official documentation for the pandas data-analysis library."
    },
    {
      "title": "The Elements of Statistical Learning",
      "url": "https://hastie.su.domains/ElemStatLearn/",
      "description": "The classic statistical-learning reference (free PDF)."
    },
    {
      "title": "Kaggle Learn — Data Science",
      "url": "https://www.kaggle.com/learn",
      "description": "Hands-on micro-courses covering pandas, EDA and modeling."
    },
    {
      "title": "scikit-learn User Guide",
      "url": "https://scikit-learn.org/stable/user_guide.html",
      "description": "Authoritative guide to the Python machine-learning toolbox."
    }
  ]
}
---

# DS-04-NUMPY-ARRAYS: NumPy: Arrays & Vectorization

## Introduction

Master ndarrays, broadcasting and vectorized math — the engine under every serious data workflow. By the end of this lesson you will be able to: Create and reshape NumPy arrays; Use vectorized math instead of Python loops; Apply broadcasting rules correctly; Index, slice and mask arrays efficiently.

## Key Concepts

### 1. Create and reshape NumPy arrays

Target: Create and reshape NumPy arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```python
import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)
print("shape:", a.shape, "dtype:", a.dtype)
```
### 2. Use vectorized math instead of Python loops

Target: Use vectorized math instead of Python loops. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```python
import numpy as np

vals = np.random.default_rng(42).normal(size=1_000_000)
# Vectorized: one pass over the buffer, no Python loop
mean = vals.mean()
std = vals.std()
print(f"mean={mean:.3f} std={std:.3f}")
```
### 3. Apply broadcasting rules correctly

Target: Apply broadcasting rules correctly. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```python
import numpy as np

col = np.array([[1], [2], [3]])   # (3, 1)
row = np.array([10, 20, 30])     # (3,)
result = col + row                # broadcasts to (3, 3)
print(result)
```
### 4. Index, slice and mask arrays efficiently

Target: Index, slice and mask arrays efficiently. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```python
import numpy as np

x = np.linspace(0, 1, 100)
mask = (x > 0.25) & (x < 0.75)
print("kept:", x[mask].size, "of", x.size)
print("first 5 kept:", x[mask][:5])
```

## Practice Questions

1. What is the key idea behind "NumPy: Arrays & Vectorization"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain NumPy: Arrays & Vectorization with analogies and real-world examples"
1. "Show me common mistakes beginners make with NumPy: Arrays & Vectorization"
1. "Provide advanced patterns and performance considerations for NumPy: Arrays & Vectorization"

## Key Takeaways

- Master the core ideas of NumPy: Arrays & Vectorization through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
