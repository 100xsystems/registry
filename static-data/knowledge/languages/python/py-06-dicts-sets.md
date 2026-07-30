---
{
  "title": "Dictionaries and Sets",
  "description": "Create and manipulate dicts with methods/comprehensions",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create and manipulate dicts with methods/comprehensions",
    "Use dict views, | merging, defaultdict, Counter",
    "Perform set operations: union, intersection, difference",
    "Understand hashability for keys/members"
  ],
  "knowledge_refs": [
    "python/py-06-dicts-sets"
  ],
  "prerequisites": [
    "PY-02"
  ],
  "references": [
    {
      "title": "Python Tutorial — Dictionaries",
      "url": "https://docs.python.org/3/tutorial/datastructures.html#dictionaries"
    },
    {
      "title": "Python Tutorial — Sets",
      "url": "https://docs.python.org/3/tutorial/datastructures.html#sets"
    },
    {
      "title": "Python Library — collections",
      "url": "https://docs.python.org/3/library/collections.html"
    },
    {
      "title": "Real Python — Dicts",
      "url": "https://realpython.com/python-dicts/"
    }
  ]
}
---

# PY-06-DICTS-SETS: Dictionaries and Sets

## Introduction

Dictionaries (key-value mappings) and sets (unique elements) use hash tables for O(1) average operations. Python 3.7+ preserves dict insertion order; 3.9+ supports | merging.

## Key Concepts

### 1. Dict Creation and Access

Map hashable keys to values. Use {} or dict(). d[k] raises KeyError; d.get(k, default) is safe. setdefault sets if missing. Membership check with in.

```python
config = {"host": "localhost", "port": 8080}
config.get("host")           # localhost
config.get("timeout", 30)    # default
config.setdefault("timeout", 60)
"host" in config  # True
```

### 2. Views and Merging (3.9+)

.keys(), .values(), .items() return dynamic views. Python 3.9+ uses | for merging. updates merge another dict or iterable of pairs.

```python
user = {"name": "Alice", "age": 30}
list(user.keys())    # ["name", "age"]
list(user.values())  # ["Alice", 30]
list(user.items())   # [("name", "Alice"), ("age", 30)]

# merging (3.9+)
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1 | d2  # {"a": 1, "b": 3, "c": 4}
```

### 3. defaultdict and Counter

collections module provides specialized dicts. defaultdict(factory) auto-creates missing entries. Counter tallies iterable elements. OrderedDict with move_to_end.

```python
from collections import defaultdict, Counter

groups = defaultdict(list)
for w in ["apple", "apricot", "banana"]:
    groups[w[0]].append(w)
print(dict(groups))

cnt = Counter(["r","b","r","g","r","b"])
cnt.most_common(2)  # [("r", 3), ("b", 2)]
```

### 4. Set Operations

Sets: unordered, unique, hashable. | union, & intersection, - difference, ^ symmetric diff. Set comprehensions use {x for x in ...}.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a | b  # {1, 2, 3, 4, 5, 6}
a & b  # {3, 4}
a - b  # {1, 2}
a ^ b  # {1, 2, 5, 6}
{1, 2} < {1, 2, 3}  # True, proper subset
```

### 5. Hashability Requirements

Only hashable objects can be dict keys/set members. Hashable means implements __hash__ and __eq__. Immutable types (int, str, tuple) are hashable; mutable (list, dict, set) are not.

```python
# Hashable keys
d = {42: "int", ("a", 1): "tuple"}

# Not hashable
try:
    {[1, 2]: "bad"}
except TypeError as e:
    print(e)  # unhashable type: list

# Custom hashable class
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __hash__(self):
        return hash((self.x, self.y))
    def __eq__(self, o):
        return (self.x, self.y) == (o.x, o.y)
```

## Practice Questions

1. What happens with d["x"] vs d.get("x")? When use each?
1. How does defaultdict(list) differ from setdefault?
1. Time complexity of set membership? Why O(1)?
1. Why cant a list be a dict key? What about tuple(list)?

## LLM Prompts for Deeper Understanding

1. "Explain dict views, | merging, defaultdict, Counter, ChainMap"
1. "Show set operations with Venn diagram examples"
1. "Teach hashability: __hash__ and __eq__ contracts"

## Key Takeaways

- Dicts/sets use hash tables — O(1) avg lookup/insert/delete
- defaultdict and Counter simplify common dict patterns
- Only hashable (immutable) objects can be keys/set members