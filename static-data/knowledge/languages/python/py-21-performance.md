---
{
  "title": "Performance: Profiling, Optimization, C Extensions",
  "description": "Profile code with timeit, cProfile, py-spy",
  "type": "lesson",
  "order": 21,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Profile code with timeit, cProfile, py-spy",
    "Optimize with __slots__, generators, built-in functions",
    "Use NumPy for array operations",
    "Understand C extensions with Cython and cffi"
  ],
  "knowledge_refs": [
    "python/py-21-performance"
  ],
  "prerequisites": [
    "PY-11",
    "PY-17"
  ],
  "references": [
    {
      "title": "Python Library — timeit",
      "url": "https://docs.python.org/3/library/timeit.html"
    },
    {
      "title": "Python Library — profile",
      "url": "https://docs.python.org/3/library/profile.html"
    },
    {
      "title": "Cython Docs",
      "url": "https://cython.readthedocs.io/"
    },
    {
      "title": "Real Python — Performance",
      "url": "https://realpython.com/python-performance/"
    }
  ]
}
---

# PY-21-PERFORMANCE: Performance: Profiling, Optimization, C Extensions

## Introduction

Python can be fast when you use the right tools: built-in functions (C-implemented), generators for memory efficiency, __slots__ for attribute optimization, and C extensions for CPU-heavy work.

## Key Concepts

### 1. Profiling with timeit and cProfile

timeit measures small code snippets. cProfile profiles entire programs. Use SnakeViz or py-spy for visualization. Focus optimization on the 10% of code that runs 90% of the time.

```python
import timeit

# timeit for microbenchmarks
timeit.timeit("[x**2 for x in range(100)]", number=1000)

# cProfile for full program
import cProfile
cProfile.run("my_program()", sort="cumtime")

# command line
$ python3 -m cProfile -s cumulative my_script.py
```

### 2. __slots__ for Memory Optimization

__slots__ declares fixed attributes, eliminating the per-instance __dict__. Saves memory (~50%) and speeds attribute access. Use only when creating millions of instances.

```python
class Point:
    __slots__ = ("x", "y")  # no __dict__

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(p.x)  # 3
# hasattr(p, "__dict__")  # False — memory saved

# compare memory
import sys
regular = sys.getsizeof(object.__dict__)
print(f"Regular class overhead: ~{regular} bytes per instance")
```

### 3. Using Built-in Functions and Libraries

Built-in functions (map, filter, sum, any, all) are C-implemented and faster than Python loops. collections.deque for fast appends from both ends. heapq for priority queues.

```python
# built-in sum vs manual loop
# SLOW: total = 0; for x in range(1000000): total += x
# FAST: sum(range(1000000))  # C implementation

# any() and all() for short-circuit evaluation
if any(x > 100 for x in large_list):
    print("Found a large value")

# deque for O(1) appends on both ends
from collections import deque
dq = deque(maxlen=1000)  # fixed size buffer
dq.append(1)
dq.appendleft(2)

# heapq for priority queue
import heapq
heap = [5, 3, 7, 1]
heapq.heapify(heap)
heapq.heappop(heap)  # 1
```

### 4. NumPy for Numerical Performance

NumPy arrays are C-contiguous, enabling vectorized operations. Avoid Python loops. Use broadcasting for element-wise operations. NumPy is the foundation of the Python data science stack.

```python
import numpy as np

# vectorized operations (no Python loops)
arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)  # [2, 4, 6, 8, 10]
print(arr ** 2)  # [1, 4, 9, 16, 25]

# broadcasting
matrix = np.ones((3, 3))
row = np.array([1, 2, 3])
result = matrix + row  # broadcasts across rows

# avoid Python loops at all costs
# SLOW: [x**2 for x in range(1000000)]
# FAST: np.arange(1000000) ** 2
```

### 5. C Extensions: Cython and Beyond

Cython compiles Python to C. Use type declarations for speed. cffi and ctypes call C libraries directly. For extreme performance, write C modules via Python/C API.

```python
# Cython example (.pyx file)
# def fib(int n):
#     cdef int a = 0, b = 1, i
#     for i in range(n):
#         a, b = b, a + b
#     return a

# ctypes for C library
from ctypes import CDLL, c_int
lib = CDLL("./mylib.so")
lib.my_function.restype = c_int
result = lib.my_function(42)
```

## Practice Questions

1. What is the difference between timeit and cProfile? When use each?
1. What do __slots__ do? When should you use them?
1. Why is sum(range(n)) faster than a manual for loop?
1. What is broadcasting in NumPy?

## LLM Prompts for Deeper Understanding

1. "Explain profiling: timeit, cProfile, py-spy, and optimization strategies"
1. "Show __slots__, generators, and deque for memory optimization"
1. "Teach NumPy vectorization vs Python loops with benchmarks"

## Key Takeaways

- timeit for microbenchmarks; cProfile for full program profiling
- __slots__ eliminates __dict__, saving ~50% memory per instance
- Built-in functions are C-implemented — faster than Python loops