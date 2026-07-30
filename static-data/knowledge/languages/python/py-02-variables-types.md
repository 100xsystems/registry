---
title: "Variables, Types, and Basic Operations"
description: "Python's dynamic type system, primitive types, variables, numbers, strings, operators, and type conversion."
type: lesson
order: 2
duration: "60 min"
difficulty: beginner
learning_objectives:
  - "Master Python's dynamic type system and primitive types"\n  - "Work with integers, floats, booleans, None, and strings"\n  - "Understand type conversion and operator precedence"\n  - "Use type hints for documentation"
knowledge_refs:
  - python/py-02-variables-types
prerequisites:
  - "PY-01"
references:
    - title: "Python Tutorial — 3.1 Numbers"\n      url: "https://docs.python.org/3/tutorial/introduction.html#numbers"\n    - title: "Python Tutorial — 3.2 Strings"\n      url: "https://docs.python.org/3/tutorial/introduction.html#text"\n    - title: "Python Reference — Data Model"\n      url: "https://docs.python.org/3/reference/datamodel.html#objects"\n    - title: "Fluent Python — Ch. 1: Data Model"\n      url: "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/"
---

# PY-02-VARIABLES-TYPES: Variables, Types, and Basic Operations


## Introduction

Python is dynamically but **strongly** typed — variables can hold any type, but implicit coercion is limited.

## Variables

No declaration needed — [variables](https://realpython.com/python-variables/) are created by assignment:
```python
x = 42; x = "hello"; x = [1,2,3]  # x changes type
print(type(42))   # <class 'int'>
print(type(3.14)) # <class 'float'>
```

## Numbers

See the [Tutorial on Numbers](https://docs.python.org/3/tutorial/introduction.html#numbers):
```python
a = 2 ** 1000        # big ints — no overflow!
b = 10 / 3           # 3.333... (float)
c = 10 // 3          # 3 (floor division)
d = 10 % 3           # 1 (modulo)
```

## Strings

Immutable Unicode — see [Tutorial on Strings](https://docs.python.org/3/tutorial/introduction.html#text):
```python
s = "Hello" + " " + "World"  # Concatenation
print(s[0], s[1:4])          # H ell
print(len(s))                 # 11
```

## Type Hints

```python
def add(a: int, b: int) -> int:
    return a + b
```

