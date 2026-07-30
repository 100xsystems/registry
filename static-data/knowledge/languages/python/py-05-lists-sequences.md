---
title: "Lists, Tuples, and Sequences"
description: "List operations, comprehensions, tuples, slicing, and the sequence protocol."
type: lesson
order: 5
duration: "60 min"
difficulty: beginner
learning_objectives:
  - "Manipulate lists with methods and slicing"\n  - "Create efficient list comprehensions"\n  - "Use tuples for immutable sequences"\n  - "Understand the sequence protocol"
knowledge_refs:
  - python/py-05-lists-sequences
prerequisites:
  - "PY-02"
references:
    - title: "Python Tutorial — 5.1 More on Lists"\n      url: "https://docs.python.org/3/tutorial/datastructures.html#more-on-lists"\n    - title: "Python Tutorial — 5.3 Tuples"\n      url: "https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences"\n    - title: "Fluent Python — Ch. 2: Array of Sequences"\n      url: "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/"
---

# PY-05-LISTS-SEQUENCES: Lists, Tuples, and Sequences


## List Operations

Lists are mutable sequences — see [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists):
```python
nums = [3, 1, 4, 1, 5]
nums.append(9)           # [3, 1, 4, 1, 5, 9]
nums.sort()              # [1, 1, 3, 4, 5, 9]
nums.pop()               # 9 — removes last
nums.insert(0, 0)        # [0, 1, 1, 3, 4, 5]
```

## Slicing

```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])    # [1, 2, 3]
print(nums[::-1])   # [5, 4, 3, 2, 1, 0] — reverse copy
print(nums[::2])    # [0, 2, 4] — every other
```

## List Comprehensions

Elegant, Pythonic way to build lists:
```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
matrix = [[i+j for j in range(3)] for i in range(3)]
```

## Tuples

Immutable sequences:
```python
point = (3, 4)
x, y = point          # tuple unpacking
print(x, y)           # 3 4
```

