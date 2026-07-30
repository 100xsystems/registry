---
{
  "title": "Pythonic Patterns and Best Practices",
  "description": "Apply EAFP vs LBYL idioms",
  "type": "lesson",
  "order": 19,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Apply EAFP vs LBYL idioms",
    "Use contextlib utilities",
    "Write idiomatic Python with zip, enumerate, reversed",
    "Understand PEP 8 style conventions"
  ],
  "knowledge_refs": [
    "python/py-19-pythonic-patterns"
  ],
  "prerequisites": [
    "PY-04",
    "PY-10"
  ],
  "references": [
    {
      "title": "PEP 8 — Style Guide",
      "url": "https://peps.python.org/pep-0008/"
    },
    {
      "title": "PEP 20 — Zen of Python",
      "url": "https://peps.python.org/pep-0020/"
    },
    {
      "title": "Python Library — contextlib",
      "url": "https://docs.python.org/3/library/contextlib.html"
    },
    {
      "title": "Real Python — Pythonic",
      "url": "https://realpython.com/learning-paths/writing-pythonic-code/"
    }
  ]
}
---

# PY-19-PYTHONIC-PATTERNS: Pythonic Patterns and Best Practices

## Introduction

Pythonic code follows the idioms and conventions of the Python community: EAFP (Easier to Ask for Forgiveness than Permission), context managers, clean iteration patterns, and PEP 8 naming conventions.

## Key Concepts

### 1. EAFP vs LBYL

EAFP: "Easier to Ask for Forgiveness than Permission" — try/except around risky operations. LBYL: "Look Before You Leap" — check conditions first. Python favors EAFP.

```python
# LBYL style (less Pythonic)
if key in data and isinstance(data[key], list):
    items = data[key]
else:
    items = []

# EAFP style (Pythonic)
try:
    items = data[key]
except (KeyError, TypeError):
    items = []
```

### 2. contextlib Utilities

contextlib provides utilities for working with context managers: closing(), suppress(), redirect_stdout(), contextmanager decorator, ExitStack for dynamic cleanup.

```python
from contextlib import suppress, ExitStack

# suppress — ignore specific exceptions
with suppress(FileNotFoundError):
    os.remove("temp.txt")  # no error if file missing

# ExitStack — dynamic cleanup
with ExitStack() as stack:
    for filename in files:
        f = open(filename)
        stack.enter_context(f)  # all closed on exit
        process(f)
```

### 3. Clean Iteration Patterns

use enumerate for index, zip for parallel iteration, reversed for reverse, sorted with key for custom ordering, itertools.groupby for grouping.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# enumerate — index + value
for i, name in enumerate(names, 1):
    print(f"{i}. {name}")

# zip — parallel iteration
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# sorted with key
sorted(names, key=len)  # shortest to longest

# reversed
for item in reversed(names):
    print(item)
```

### 4. PEP 8 Conventions

PEP 8 defines Python style: 4-space indentation, snake_case for functions/variables, CamelCase for classes, UPPER_CASE for constants. Max line 79 chars. Two blank lines around top-level definitions.

```python
# PEP 8 examples
MAX_RETRIES = 3  # constants: UPPER_CASE

class UserService:  # classes: CamelCase
    """Service for user operations."""

    def get_user(self, user_id):  # functions: snake_case
        """Fetch a user by ID."""
        return database.query_user(user_id)

# blank lines: 2 between classes, 1 between methods
```

### 5. Naming Conventions and Dunder Patterns

Single underscore _ for throwaway vars. Single trailing underscore to avoid name collisions (class_). Double underscore __ for name mangling in classes. Dunder __methods__ for protocol implementation.

```python
# conventions
for _ in range(10):  # throwaway variable
    do_something()

def function(class_):  # trailing _ to avoid keyword clash
    pass

class MyClass:
    def __init__(self):
        self.__private = True  # name mangling
        self._protected = True  # convention: internal use
    def __str__(self):
        return "MyClass"
```

## Practice Questions

1. What is EAFP? How is it different from LBYL?
1. What does contextlib.suppress do?
1. What is the difference between _var, var_, and __var?
1. What does PEP 8 say about indentation and line length?

## LLM Prompts for Deeper Understanding

1. "Explain Pythonic idioms: EAFP, context managers, iteration patterns"
1. "Show PEP 8 conventions with naming rules and formatting guidelines"
1. "Teach contextlib: suppress, ExitStack, redirect_stdout, closing"

## Key Takeaways

- Python favors EAFP (try/except) over LBYL (if/else)
- contextlib.suppress ignores specified exceptions silently
- PEP 8: 4-space indent, snake_case, CamelCase, UPPER_CASE