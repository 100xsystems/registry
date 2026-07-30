---
title: "Dictionaries and Sets"
description: "Dictionary operations, set theory, hash tables, and when to use each collection type."
type: lesson
order: 6
duration: "60 min"
difficulty: beginner
learning_objectives:
  - "Create and manipulate dictionaries"\n  - "Use set operations for membership and dedup"\n  - "Understand hash table internals"\n  - "Choose the right collection"
knowledge_refs:
  - python/py-06-dicts-sets
prerequisites:
  - "PY-05"
references:
    - title: "Python Tutorial — 5.5 Dictionaries"\n      url: "https://docs.python.org/3/tutorial/datastructures.html#dictionaries"\n    - title: "Python Tutorial — 5.4 Sets"\n      url: "https://docs.python.org/3/tutorial/datastructures.html#sets"\n    - title: "Fluent Python — Ch. 3: Dictionaries and Sets"\n      url: "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/"
---

# PY-06-DICTS-SETS: Dictionaries and Sets


## Dictionaries

Key-value mapping with O(1) lookup — see [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries):
```python
user = {"name": "Alice", "age": 30, "active": True}
print(user["name"])           # Alice
print(user.get("email", "N/A"))  # N/A — safe access
user["age"] = 31
del user["active"]

# Dict comprehensions
squares = {x: x**2 for x in range(5)}
```

## Sets

Unordered collection of unique elements — see [Sets](https://docs.python.org/3/tutorial/datastructures.html#sets):
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)  # union: {1,2,3,4,5,6}
print(a & b)  # intersection: {3,4}
print(a - b)  # difference: {1,2}
print(a ^ b)  # symmetric diff: {1,2,5,6}
```

## When to Use What

- **list**: ordered, indexed by position, duplicates OK
- **tuple**: ordered, immutable, hashable
- **set**: unordered, unique, fast membership
- **dict**: key-value mapping, fast lookup by key

