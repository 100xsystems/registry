---
{
  "title": "Advanced Functions: map, filter, and functools",
  "description": "Use map, filter, and reduce functionally",
  "type": "lesson",
  "order": 13,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use map, filter, and reduce functionally",
    "Apply partial application and singledispatch",
    "Use operator module for functional patterns",
    "Understand functools higher-order functions"
  ],
  "knowledge_refs": [
    "python/py-13-advanced-functions"
  ],
  "prerequisites": [
    "PY-04",
    "PY-11"
  ],
  "references": [
    {
      "title": "Python Tutorial — map/filter",
      "url": "https://docs.python.org/3/library/functions.html#map"
    },
    {
      "title": "Python Library — functools",
      "url": "https://docs.python.org/3/library/functools.html"
    },
    {
      "title": "Python Library — operator",
      "url": "https://docs.python.org/3/library/operator.html"
    },
    {
      "title": "Real Python — map/filter",
      "url": "https://realpython.com/python-map-function/"
    }
  ]
}
---

# PY-13-ADVANCED-FUNCTIONS: Advanced Functions: map, filter, and functools

## Introduction

Python supports functional programming patterns: map, filter, reduce for data pipelines; partial for function specialization; singledispatch for type-based dispatch. The operator module provides function versions of operators.

## Key Concepts

### 1. map, filter, and reduce

map(func, iterable) transforms each element. filter(pred, iterable) keeps matching elements. reduce(func, iterable) cumulatively combines. Use list() to realize lazy results.

```python
nums = [1, 2, 3, 4, 5]

# map — transform
doubled = list(map(lambda x: x * 2, nums))
print(doubled)  # [2, 4, 6, 8, 10]

# filter — select
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]

# reduce — accumulate
from functools import reduce
total = reduce(lambda a, b: a + b, nums)
print(total)  # 15

# map with multiple iterables
list(map(pow, [2, 3, 4], [5, 4, 3]))  # [32, 81, 64]
```

### 2. functools.partial — Fix Arguments

partial freezes some function arguments, creating a new function with fewer parameters. Useful for callbacks and configuration. Like currying, but simpler.

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(3))     # 27

# real-world: configure logger
import logging
log_error = partial(logging.error, exc_info=True)
log_error("Something failed")
```

### 3. functools.singledispatch

singledispatch creates type-based function dispatch. Register implementations for different types with @register. Falls back to the base function for unregistered types.

```python
from functools import singledispatch

@singledispatch
def process(value):
    return f"Unknown type: {type(value).__name__}"

@process.register(int)
def _(value):
    return f"Integer: {value} (double: {value*2})"

@process.register(str)
def _(value):
    return f"String: {value.upper()}"

@process.register(list)
def _(value):
    return f"List with {len(value)} items"

print(process(42))    # Integer: 42
print(process("hi"))  # String: HI
print(process([1]))   # List with 1 items
```

### 4. operator Module

operator module provides function equivalents of Python operators: add, sub, mul, truediv, itemgetter, attrgetter, methodcaller. Faster and cleaner than lambdas for simple ops.

```python
from operator import add, mul, itemgetter, attrgetter

# operator functions
reduce(add, [1, 2, 3])       # 6
list(map(mul, [2, 3], [4, 5]))  # [8, 15]

# itemgetter — works like lambda x: x[1]
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted(students, key=itemgetter(1), reverse=True)

# attrgetter — works like lambda x: x.name
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
pts = [Point(3, 4), Point(1, 2), Point(5, 1)]
sorted(pts, key=attrgetter("x"))
```

## Practice Questions

1. What is the difference between map() and a list comprehension?
1. What does functools.partial do? When would you use it?
1. When would you use singledispatch vs isinstance checks?
1. Why use operator.add instead of lambda a, b: a + b?

## LLM Prompts for Deeper Understanding

1. "Explain map, filter, reduce with functional programming patterns"
1. "Show partial application and singledispatch with real examples"
1. "Teach the operator module: itemgetter, attrgetter, methodcaller"

## Key Takeaways

- map transforms, filter selects, reduce combines elements
- partial freezes arguments — great for configuration
- operator functions are faster/cleaner than lambdas for simple operations