---
{
  "title": "Decorators and Metaprogramming",
  "description": "Write decorators with @ syntax",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write decorators with @ syntax",
    "Use functools.wraps to preserve metadata",
    "Build decorators with arguments",
    "Understand class-based decorators"
  ],
  "knowledge_refs": [
    "python/py-12-decorators"
  ],
  "prerequisites": [
    "PY-04",
    "PY-11"
  ],
  "references": [
    {
      "title": "Python Tutorial — Decorators",
      "url": "https://docs.python.org/3/reference/compound_stmts.html#function-definitions"
    },
    {
      "title": "Python Library — functools",
      "url": "https://docs.python.org/3/library/functools.html"
    },
    {
      "title": "PEP 318 — Decorators",
      "url": "https://peps.python.org/pep-0318/"
    },
    {
      "title": "Real Python — Decorators",
      "url": "https://realpython.com/primer-on-python-decorators/"
    }
  ]
}
---

# PY-12-DECORATORS: Decorators and Metaprogramming

## Introduction

Decorators are functions that modify other functions or methods. The @ syntax is syntactic sugar for function composition. They enable cross-cutting concerns: logging, timing, caching, access control.

## Key Concepts

### 1. Basic Decorator Pattern

A decorator takes a function, wraps it with added behavior, and returns the wrapper. @decorator is equivalent to func = decorator(func). The wrapper accepts *args, **kwargs.

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Returned: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(2, 3)
# Calling add
# Returned: 5
```

### 2. functools.wraps — Preserving Metadata

Decorators replace the original function with a wrapper, losing __name__, __doc__, __module__. @functools.wraps copies these from the original to the wrapper.

```python
from functools import wraps

def logger(func):
    @wraps(func)  # preserves func.__name__, func.__doc__
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__)  # "add" (not "wrapper")
print(add.__doc__)   # "Add two numbers."
```

### 3. Decorators with Arguments

A decorator that takes arguments needs three levels: decorator(args) -> deco(func) -> wrapper(*args, **kwargs). Use functools.partial or a class for complex cases.

```python
from functools import wraps

def retry(max_attempts=3, delay=0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    import time; time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(max_attempts=5, delay=1)
def unreliable_api_call():
    # might fail...
    pass
```

### 4. Caching with functools.lru_cache and cache

lru_cache and cache (3.9+) memoize function results based on arguments. Use for expensive pure functions. maxsize limits cache entries. lru_cache has cache_info() and cache_clear().

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(50)  # fast! cached intermediate results
print(fibonacci.cache_info())  # CacheInfo(hits=48, misses=51)

# Python 3.9+
from functools import cache
@cache  # unlimited cache
def expensive_computation(x):
    return x ** x
```

### 5. Class-Based Decorators and __call__

A class with __call__ can serve as a decorator, maintaining state. Useful for parameterized decorators and decorators that need initialization.

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(name):
    return f"Hello, {name}"

say_hello("Alice")  # Called 1 times
say_hello("Bob")    # Called 2 times
```

## Practice Questions

1. What does the @ symbol do in Python?
1. Why use @functools.wraps in a decorator?
1. How do you create a decorator that takes arguments?
1. What does @lru_cache do? When would you use it?

## LLM Prompts for Deeper Understanding

1. "Explain decorator pattern: __call__, wraps, nested decorators"
1. "Show lru_cache and cache for memoization with real examples"
1. "Teach decorators with arguments: three-level nesting pattern"

## Key Takeaways

- @decorator is syntactic sugar for func = decorator(func)
- @wraps preserves __name__, __doc__, __module__ from original
- lru_cache memoizes function results — essential for DP algorithms