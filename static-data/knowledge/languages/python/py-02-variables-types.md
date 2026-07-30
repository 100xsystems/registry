---
{
  "title": "Variables, Types, and Type System",
  "description": "Understand dynamic typing and type()",
  "type": "lesson",
  "order": 2,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Understand dynamic typing and type()",
    "Use int, float, complex, bool, None",
    "Master type conversion functions",
    "Write type annotations (3.5+)"
  ],
  "knowledge_refs": [
    "python/py-02-variables-types"
  ],
  "prerequisites": [
    "PY-01"
  ],
  "references": [
    {
      "title": "Python Tutorial",
      "url": "https://docs.python.org/3/tutorial/introduction.html#numbers"
    },
    {
      "title": "Reference — Data Model",
      "url": "https://docs.python.org/3/reference/datamodel.html#objects"
    },
    {
      "title": "Real Python — Data Types",
      "url": "https://realpython.com/python-data-types/"
    }
  ]
}
---

# PY-02-VARIABLES-TYPES: Variables, Types, and Type System

## Introduction

Python is dynamically typed — variable type is inferred at runtime. Python 3.5+ supports gradual typing with type annotations for static analysis.

## Key Concepts

### 1. Dynamic Typing and Assignment

Names refer to objects; assignment creates a reference. The same name can refer to different types. Use type() to inspect any value.

```python
x = 42
print(type(x))  # <class 'int'>

x = "hello"
print(type(x))  # <class 'str'>

x = [1, 2, 3]
print(type(x))  # <class 'list'>
```

### 2. Numeric Types: int, float, complex, bool

Arbitrary-precision int, IEEE-754 float, complex, and bool (subclass of int). // for floor division, % for modulo, underscore for readability.

```python
big = 2 ** 1000  # arbitrary precision
million = 1_000_000
hex_color = 0xFF_00_FF
print(7 / 3)    # 2.333...
print(7 // 3)   # 2 (floor division)
print(7 % 3)    # 1 (modulo)
```

### 3. None and Type Conversion

None is Python null — a singleton of NoneType. Compare with is (identity), not ==. int(), float(), str(), bool() for explicit conversion.

```python
result = None
print(result is None)  # True

print(int(3.9))       # 3 (truncates)
print(float("3.14"))  # 3.14
print(str(42))        # '42'
print(bool([]))       # False
```

### 4. Type Annotations (Gradual Typing)

Python 3.5+ supports optional type annotations. Runtime ignores them; mypy/pyright use them. typing module for complex types.

```python
name: str = "Alice"
age: int = 30

def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

from typing import Optional, List, Dict
def process(items: list[int]) -> Dict[str, int]:
    return {str(i): i for i in items}
```

## Practice Questions

1. What does 3 / 2 produce? What about 3 // 2?
1. Why prefer x is None over x == None?
1. What does bool("False") evaluate to?
1. Add annotations: def process(data, limit) -> list: ...

## LLM Prompts for Deeper Understanding

1. "Explain dynamic vs gradual typing in Python with mypy"
1. "Show Python numeric types: int, float, decimal, Fraction"
1. "Teach Python truthiness — what values evaluate to False"

## Key Takeaways

- Python is dynamically typed — names point to objects
- Type annotations enable static analysis with mypy/pyright
- Compare None with is, not ==