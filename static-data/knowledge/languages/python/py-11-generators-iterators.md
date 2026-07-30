---
title: "Generators, Iterators, and Context Managers"
description: "Iterator protocol, generators with yield, generator expressions, itertools, and context managers."
type: lesson
order: 11
duration: "60 min"
difficulty: intermediate
learning_objectives:
  - "Implement the iterator protocol"\n  - "Create generators with yield"\n  - "Use generator expressions for lazy evaluation"\n  - "Build context managers"
knowledge_refs:
  - python/py-11-generators-iterators
prerequisites:
  - "PY-10"
references:
    - title: "Python Tutorial — 9.8 Iterators"\n      url: "https://docs.python.org/3/tutorial/classes.html#iterators"\n    - title: "Python Tutorial — 9.9 Generators"\n      url: "https://docs.python.org/3/tutorial/classes.html#generators"\n    - title: "Fluent Python — Ch. 17: Iterators, Generators"\n      url: "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/"
---

# PY-11-GENERATORS-ITERATORS: Generators, Iterators, and Context Managers


## Iterator Protocol

See [Iterators](https://docs.python.org/3/tutorial/classes.html#iterators):
```python
class CountDown:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= 0: raise StopIteration
        self.current -= 1
        return self.current + 1

for n in CountDown(3): print(n)  # 3, 2, 1
```

## Generators

[Generator functions](https://docs.python.org/3/tutorial/classes.html#generators) use `yield` — they're the easiest way to create iterators:
```python
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for n in fibonacci(100): print(n)  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
```

## Generator Expressions

```python
nums = (x**2 for x in range(10))  # Lazy — no list created
print(sum(nums))  # 285
```

## Context Managers

```python
from contextlib import contextmanager

@contextmanager
def timed(name):
    import time
    start = time.time()
    yield
    elapsed = time.time() - start
    print(f"{name}: {elapsed:.2f}s")

with timed("process"):
    sum(range(10_000_000))
```

