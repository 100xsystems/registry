---
title: "Advanced Functions: Lambdas and Functional Tools"
description: "Lambda functions, map/filter/reduce, functools, itertools, and functional programming patterns."
type: lesson
order: 13
duration: "60 min"
difficulty: intermediate
learning_objectives:
  - "Write effective lambda expressions"\n  - "Use map, filter, reduce for data processing"\n  - "Apply functools: partial, lru_cache, wraps"\n  - "Use itertools for iteration patterns"
knowledge_refs:
  - python/py-13-advanced-functions
prerequisites:
  - "PY-04"
references:
    - title: "Python Tutorial — Lambda Expressions"\n      url: "https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions"\n    - title: "Python Docs — functools"\n      url: "https://docs.python.org/3/library/functools.html"\n    - title: "Python Docs — itertools"\n      url: "https://docs.python.org/3/library/itertools.html"
---

# PY-13-ADVANCED-FUNCTIONS: Advanced Functions: Lambdas and Functional Tools


## Lambdas and map/filter/reduce

```python
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))     # [1, 4, 9, 16, 25]
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]

from functools import reduce
total = reduce(lambda a, b: a + b, nums)  # 15
```

## functools.partial

Fix arguments of a function to create a simpler version:
```python
from functools import partial

def power(base, exp): return base ** exp
square = partial(power, exp=2)
cube = partial(power, exp=3)
print(square(5))  # 25
print(cube(3))    # 27
```

## functools.lru_cache

Memoization with a single decorator:
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print(fib(100))  # 354224848179261915075 — instant!
```

