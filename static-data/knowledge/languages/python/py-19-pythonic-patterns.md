---
title: "Pythonic Patterns and Idioms"
description: "EAFP vs LBYL, duck typing, property decorators, descriptors, context manager patterns, and SOLID in Python."
type: lesson
order: 19
duration: "60 min"
difficulty: advanced
learning_objectives:
  - "Apply EAFP and duck typing"\n  - "Use properties and descriptors"\n  - "Implement SOLID principles"\n  - "Write Pythonic idiomatic code"
knowledge_refs:
  - python/py-19-pythonic-patterns
prerequisites:
  - "PY-10"\n  - "PY-12"
references:
    - title: "Fluent Python — Ch. 11: Pythonic Object"\n      url: "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/"\n    - title: "Fluent Python — Ch. 22: Descriptors"\n      url: "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/"
---

# PY-19-PYTHONIC-PATTERNS: Pythonic Patterns and Idioms


## EAFP vs LBYL

```python
# LBYL (Look Before You Leap) — not Pythonic
if os.path.exists("file.txt") and os.access("file.txt", os.R_OK):
    with open("file.txt") as f: data = f.read()

# EAFP (Easier to Ask for Forgiveness) — Pythonic
try:
    with open("file.txt") as f: data = f.read()
except FileNotFoundError:
    data = ""
```

## Property Decorator

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9
```

