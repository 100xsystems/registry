---
title: "Testing and Debugging"
description: "Unit testing with unittest and pytest, debugging with pdb, and logging best practices."
type: lesson
order: 15
duration: "75 min"
difficulty: intermediate
learning_objectives:
  - "Write unit tests with unittest and pytest"\n  - "Use fixtures and mocking"\n  - "Debug with pdb"\n  - "Log effectively"
knowledge_refs:
  - python/py-15-testing-debugging
prerequisites:
  - "PY-08"
references:
    - title: "Python Docs — unittest"\n      url: "https://docs.python.org/3/library/unittest.html"\n    - title: "Python Docs — pdb"\n      url: "https://docs.python.org/3/library/pdb.html"\n    - title: "pytest Documentation"\n      url: "https://docs.pytest.org/"
---

# PY-15-TESTING-DEBUGGING: Testing and Debugging


## pytest

```python
# test_math.py
def test_addition():
    assert 2 + 2 == 4

def test_string():
    assert "hello".upper() == "HELLO"
```

Run with: `pytest test_math.py -v`

## PDB Debugging

```python
def buggy_function(x, y):
    import pdb; pdb.set_trace()  # Set breakpoint
    result = x / y
    return result * 2
```

## Logging

```python
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Processing started")
logger.warning("Disk space low")
logger.error("Connection failed")
```

