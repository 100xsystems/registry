---
{
  "title": "Testing and Debugging",
  "description": "Write unit tests with pytest and unittest",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write unit tests with pytest and unittest",
    "Use assert statements effectively",
    "Debug with pdb, breakpoint(), and logging",
    "Write test fixtures, parametrization, and mocks"
  ],
  "knowledge_refs": [
    "python/py-15-testing-debugging"
  ],
  "prerequisites": [
    "PY-08"
  ],
  "references": [
    {
      "title": "Python Library — unittest",
      "url": "https://docs.python.org/3/library/unittest.html"
    },
    {
      "title": "Pytest Documentation",
      "url": "https://docs.pytest.org/"
    },
    {
      "title": "Python Library — pdb",
      "url": "https://docs.python.org/3/library/pdb.html"
    },
    {
      "title": "Real Python — Testing",
      "url": "https://realpython.com/python-testing/"
    }
  ]
}
---

# PY-15-TESTING-DEBUGGING: Testing and Debugging

## Introduction

Testing is essential for reliable Python code. pytest is the modern standard (unittest is built-in). pdb and breakpoint() (3.7+) provide interactive debugging. logging captures runtime information.

## Key Concepts

### 1. pytest Basics

pytest discovers test functions matching test_*. Assert with plain assert (no self.assertEqual). Run with pytest command. -v for verbose; -k to filter tests by name.

```python
# test_math.py
def test_add():
    assert add(2, 3) == 5  # plain assert

def test_strings():
    assert "hello".upper() == "HELLO"

def test_list_contains():
    assert 3 in [1, 2, 3]

# Run: pytest -v test_math.py
# Filter: pytest -k "string" test_math.py
```

### 2. Fixtures and Parametrization

pytest fixtures provide reusable test setup/teardown. parametrize tests multiple inputs. conftest.py shares fixtures across test files.

```python
import pytest

@pytest.fixture
def user():
    return {"name": "Alice", "age": 30}

def test_user_name(user):
    assert user["name"] == "Alice"

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

### 3. unittest Module

unittest uses class-based tests with assert* methods. setUp/tearDown for fixtures. Test discovery with python -m unittest discover. Compatible with pytest runner.

```python
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

if __name__ == "__main__":
    unittest.main()
```

### 4. Debugging with pdb and breakpoint()

breakpoint() (3.7+) drops into pdb interactively. pdb commands: n (next), s (step), c (continue), p (print), l (list), q (quit). PYTHONBREAKPOINT env var customizes debugger.

```python
def buggy_function(x):
    result = x * 2
    breakpoint()  # drops into debugger
    return result + 1

# pdb commands:
# (Pdb) p x       -- print x
# (Pdb) n         -- next line
# (Pdb) s         -- step into function
# (Pdb) l         -- list source
# (Pdb) c         -- continue
# (Pdb) q         -- quit

# post-mortem debugging
import pdb
try:
    1 / 0
except ZeroDivisionError:
    pdb.post_mortem()  # inspect at crash site
```

### 5. Logging Best Practices

logging module provides configurable output levels: DEBUG, INFO, WARNING, ERROR, CRITICAL. Use loggers per module. Configure handlers (file, console). Never use print() for production.

```python
import logging

# configure once at app startup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

logger = logging.getLogger(__name__)

def process(data):
    logger.info("Processing %d items", len(data))
    try:
        result = do_something(data)
        logger.debug("Result: %s", result)
        return result
    except Exception as e:
        logger.error("Failed: %s", e, exc_info=True)
        raise
```

## Practice Questions

1. What is the difference between pytest and unittest? When use each?
1. What does breakpoint() do? How is it better than import pdb; pdb.set_trace()?
1. What are the five logging levels? What does basicConfig configure?
1. Write a pytest fixture that creates a temporary file that gets cleaned up.

## LLM Prompts for Deeper Understanding

1. "Explain pytest fixtures, parametrization, conftest.py with examples"
1. "Show pdb debugging: breakpoints, post-mortem, and PYTHONBREAKPOINT"
1. "Teach logging best practices: loggers, handlers, formatters, levels"

## Key Takeaways

- pytest is the modern standard — plain assert, fixtures, parametrize
- breakpoint() (3.7+) drops into pdb with zero imports
- Use logging, not print(), for production applications