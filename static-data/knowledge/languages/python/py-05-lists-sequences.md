---
{
  "title": "Lists, Sequences, and Indexing",
  "description": "Create and manipulate lists with methods and slicing",
  "type": "lesson",
  "order": 5,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create and manipulate lists with methods and slicing",
    "Master slice syntax [start:stop:step]",
    "Use list methods: append, extend, insert, pop, sort",
    "Understand shallow vs deep copy"
  ],
  "knowledge_refs": [
    "python/py-05-lists-sequences"
  ],
  "prerequisites": [
    "PY-02"
  ],
  "references": [
    {
      "title": "Python Tutorial — Lists",
      "url": "https://docs.python.org/3/tutorial/introduction.html#lists"
    },
    {
      "title": "Python Tutorial — More on Lists",
      "url": "https://docs.python.org/3/tutorial/datastructures.html#more-on-lists"
    },
    {
      "title": "Real Python — Lists and Tuples",
      "url": "https://realpython.com/python-lists-tuples/"
    }
  ]
}
---

# PY-05-LISTS-SEQUENCES: Lists, Sequences, and Indexing

## Introduction

Lists are Python's most versatile sequence: mutable, ordered, heterogeneous. Slicing, negative indexing, and rich methods make them incredibly expressive for data manipulation.

## Key Concepts

### 1. List Creation and Indexing

Lists are zero-indexed. Positive indices from 0, negative from -1 (last). Brackets access elements. in for membership. len() for size. Lists can hold mixed types.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])    # apple
print(fruits[-1])   # cherry
print(fruits[-2])   # banana
print(len(fruits))  # 3
print("banana" in fruits)  # True
```

### 2. Slicing — [start:stop:step]

Slices create new lists from subsequences. start:stop:step, all optional. Never IndexError. [::-1] reverses. Works on any sequence (str, tuple, list).

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums[2:5]     # [2, 3, 4]
nums[:4]      # [0, 1, 2, 3]
nums[-3:]     # [7, 8, 9]
nums[::2]     # [0, 2, 4, 6, 8]
nums[::-1]    # reverse

# slice assignment
nums[3:6] = [30, 40, 50]
```

### 3. List Methods

append adds one item; extend adds iterable; insert at index; pop removes and returns; remove by value; index finds position; count tallies; sort in-place; reverse in-place.

```python
stack = []
stack.append(1)
stack.extend([2, 3, 4])
stack.insert(0, 0)
last = stack.pop()
first = stack.pop(0)
stack.remove(2)

# sorting
items = [3, 1, 4, 1, 5]
items.sort()
items.sort(reverse=True)
sorted(items)  # new list
```

### 4. Shallow vs Deep Copy

b = a does NOT copy — creates a new reference to same object. Use copy(), list(), [:] for shallow. Use copy.deepcopy() for nested structures.

```python
a = [1, 2, [3, 4]]
b = a            # not a copy!
b.append(5)
print(a)  # [1, 2, [3, 4], 5]

s = a.copy()     # shallow
s[2].append(99)  # affects a too!

from copy import deepcopy
d = deepcopy(a)  # fully independent
```

## Practice Questions

1. What does nums[1:-1:2] produce for range(10)?
1. Difference between append, extend, and +=?
1. Why does b = a not copy? How is copy() different?
1. Sort [(1, "x"), (3, "z"), (2, "y")] by second element.

## LLM Prompts for Deeper Understanding

1. "Explain slicing with negative indices, step, and slice assignment"
1. "Show shallow vs deep copying for lists and custom objects"
1. "Teach list method complexities (Big-O) for each operation"

## Key Takeaways

- Slicing [start:stop:step] creates new lists — never IndexError
- Use .sort() in-place, sorted() for new sorted list
- Assignment does not copy — use .copy() or deepcopy()