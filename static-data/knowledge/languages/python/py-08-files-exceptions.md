---
title: "File I/O and Exception Handling"
description: "Reading/writing files, context managers, try/except/finally, custom exceptions, and data persistence."
type: lesson
order: 8
duration: "60 min"
difficulty: intermediate
learning_objectives:
  - "Read and write files with context managers"\n  - "Handle exceptions with try/except/else/finally"\n  - "Create custom exception classes"\n  - "Serialize data with JSON and CSV"
knowledge_refs:
  - python/py-08-files-exceptions
prerequisites:
  - "PY-03"
references:
    - title: "Python Tutorial — 7.2 Reading Files"\n      url: "https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files"\n    - title: "Python Tutorial — 8. Errors and Exceptions"\n      url: "https://docs.python.org/3/tutorial/errors.html"\n    - title: "Real Python — Python File I/O"\n      url: "https://realpython.com/read-write-files-python/"
---

# PY-08-FILES-EXCEPTIONS: File I/O and Exception Handling


## File I/O with Context Managers

Always use `with` for proper resource cleanup — see [Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files):
```python
# Writing
with open("data.txt", "w") as f:
    f.write("Hello, World!\n")
    f.writelines(["line1\n", "line2\n"])

# Reading
with open("data.txt", "r") as f:
    content = f.read()       # entire file as string
    lines = f.readlines()    # list of lines
```

## Exception Handling

See [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html):
```python
try:
    result = risky_operation()
except ValueError as e:
    print(f"Value error: {e}")
except (TypeError, RuntimeError):
    print("Type or runtime error")
else:
    print(f"Success: {result}")
finally:
    cleanup()  # Always runs
```

## Custom Exceptions

```python
class ValidationError(Exception):
    """Custom exception for data validation."""
    def __init__(self, field: str, message: str):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")
```

## JSON Persistence

```python
import json
data = {"name": "Alice", "scores": [85, 92, 78]}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
with open("data.json", "r") as f:
    loaded = json.load(f)
```

