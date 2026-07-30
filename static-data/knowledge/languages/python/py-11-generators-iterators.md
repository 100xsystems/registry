---
{
  "title": "Generators and Iterators",
  "description": "Build iterators with __iter__/__next__",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Build iterators with __iter__/__next__",
    "Create generators with yield",
    "Use generator expressions",
    "Master itertools for iterator composition"
  ],
  "knowledge_refs": [
    "python/py-11-generators-iterators"
  ],
  "prerequisites": [
    "PY-05"
  ],
  "references": [
    {
      "title": "Python Tutorial — Iterators",
      "url": "https://docs.python.org/3/tutorial/classes.html#iterators"
    },
    {
      "title": "Python Tutorial — Generators",
      "url": "https://docs.python.org/3/tutorial/classes.html#generators"
    },
    {
      "title": "Python Library — itertools",
      "url": "https://docs.python.org/3/library/itertools.html"
    },
    {
      "title": "Real Python — Generators",
      "url": "https://realpython.com/introduction-to-python-generators/"
    }
  ]
}
---

# PY-11-GENERATORS-ITERATORS: Generators and Iterators

## Introduction

Iterators and generators are Python's lazy evaluation mechanisms. Generators (yield) produce values on demand, enabling memory-efficient processing of large datasets.

## Key Concepts

### 1. Iterator Protocol

An iterator implements __iter__ (returns self) and __next__ (raises StopIteration when done). for loops call __next__ internally until StopIteration.

```python
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # iterator returns itself

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for n in CountDown(5):
    print(n)  # 5, 4, 3, 2, 1
```

### 2. Generator Functions with yield

A function with yield is a generator. Calling returns a generator object. Each next() resumes execution until next yield. Generators are single-use iterators.

```python
def countdown(start):
    while start > 0:
        yield start
        start -= 1

for n in countdown(5):
    print(n)  # 5, 4, 3, 2, 1

# generator for reading large files
def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

for line in read_lines("huge.csv"):
    process(line)  # memory efficient
```

### 3. Generator Expressions

Generator expressions use (x for x in iterable) syntax. Similar to list comprehensions but produce values lazily, one at a time. Use for memory-efficient pipelines.

```python
# generator expression (lazy)
squares = (x**2 for x in range(1_000_000))
print(next(squares))  # 1
print(next(squares))  # 4

# no memory allocation
sum(x**2 for x in range(1000))  # no list created

# generator pipeline
logs = (line for line in open("app.log"))
errors = (line for line in logs if "ERROR" in line)
for err in errors:
    print(err)
```

### 4. yield from — Generator Delegation

yield from delegates yielding to another generator. Flattens nested generator calls. Essential for coroutines and recursive generator patterns.

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, [3, 4]], 5]
list(flatten(nested))  # [1, 2, 3, 4, 5]

# chain generators
def gen1(): yield from range(3)
def gen2(): yield from "abc"
list(gen1()) + list(gen2())  # [0, 1, 2, "a", "b", "c"]
```

### 5. itertools — Iterator Toolkit

itertools provides combinatoric iterator building blocks. chain, cycle, repeat, accumulate, takewhile, dropwhile, product, permutations, combinations, groupby.

```python
from itertools import chain, cycle, accumulate, islice

# chain multiple iterables
list(chain([1, 2], [3, 4]))  # [1, 2, 3, 4]

# accumulate (running sum)
list(accumulate([1, 2, 3, 4]))  # [1, 3, 6, 10]

# islice for slicing iterators
list(islice(range(100), 5))  # [0, 1, 2, 3, 4]

# combinations
from itertools import combinations
list(combinations([1, 2, 3], 2))  # [(1,2), (1,3), (2,3)]
```

## Practice Questions

1. What is the difference between an iterable and an iterator?
1. How does yield differ from return in a generator?
1. When would you use a generator expression vs a list comprehension?
1. What does yield from do? Give an example.

## LLM Prompts for Deeper Understanding

1. "Explain iterator protocol: __iter__, __next__, StopIteration"
1. "Show generator patterns for streaming data and pipelines"
1. "Teach itertools: chain, cycle, groupby, combinations, product"

## Key Takeaways

- Generators (yield) produce values lazily, one at a time
- Generator expressions use (x for x in iter) — memory efficient
- itertools provides combinatoric iterator building blocks