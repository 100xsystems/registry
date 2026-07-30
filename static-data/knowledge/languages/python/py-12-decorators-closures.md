---
title: "Decorators and Closures"
description: "Closures, function decorators, decorator factories, class decorators, and practical decorator patterns."
type: lesson
order: 12
duration: "60 min"
difficulty: intermediate
learning_objectives:
  - "Understand closure mechanics"\n  - "Write function decorators and factories"\n  - "Apply decorators for caching, logging, timing"\n  - "Use functools.wraps"
knowledge_refs:
  - python/py-12-decorators-closures
prerequisites:
  - "PY-04"
references:
    - title: "Fluent Python — Ch. 9: Decorators and Closures"\n      url: "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/"\n    - title: "Real Python — Python Decorators"\n      url: "https://realpython.com/primer-on-python-decorators/"
---

# PY-12-DECORATORS-CLOSURES: Decorators and Closures


## Closures

A closure remembers variables from the enclosing scope even after the outer function returns:
```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))  # 10
print(triple(5))  # 15
```

## Basic Decorator

```python
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time.time()-start:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n): return sum(range(n))
```

## Decorator with Arguments

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi(): print("Hi!")
```

