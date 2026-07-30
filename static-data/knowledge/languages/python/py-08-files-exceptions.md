---
{
  "title": "Files, Exceptions, and Context Managers",
  "description": "Read/write files with open() and pathlib",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read/write files with open() and pathlib",
    "Use context managers (with statement)",
    "Handle exceptions with try/except/else/finally",
    "Define custom exception classes"
  ],
  "knowledge_refs": [
    "python/py-08-files-exceptions"
  ],
  "prerequisites": [
    "PY-03",
    "PY-05"
  ],
  "references": [
    {
      "title": "Python Tutorial — Reading/Writing Files",
      "url": "https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files"
    },
    {
      "title": "Python Tutorial — Errors and Exceptions",
      "url": "https://docs.python.org/3/tutorial/errors.html"
    },
    {
      "title": "Python Library — pathlib",
      "url": "https://docs.python.org/3/library/pathlib.html"
    },
    {
      "title": "Real Python — Exceptions",
      "url": "https://realpython.com/python-exceptions/"
    }
  ]
}
---

# PY-08-FILES-EXCEPTIONS: Files, Exceptions, and Context Managers

## Introduction

File I/O and exception handling are fundamental to robust Python programs. Context managers (with) ensure proper resource cleanup. Modern pathlib provides OOP file system access.

## Key Concepts

### 1. Reading and Writing Files

open() returns a file object. Modes: r (read), w (write), a (append), r+ (read/write), x (exclusive create). Use with for automatic closing. Iterate directly over file lines.

```python
with open("data.txt", "r") as f:
    content = f.read()       # entire file
    lines = f.readlines()    # list of lines
    for line in f:           # iterate (memory efficient)
        print(line.strip())

with open("out.txt", "w") as f:
    f.write("Hello World\n")
    f.writelines(["line1\n", "line2\n"])
```

### 2. Pathlib — Modern File Paths

pathlib (3.4+) provides object-oriented path handling. Path / operator joins paths. Methods: read_text, write_text, exists, is_file, is_dir, glob, rglob, mkdir.

```python
from pathlib import Path
p = Path("data") / "subdir" / "file.txt"
p.parent       # Path("data/subdir")
p.suffix       # ".txt"
p.stem         # "file"
p.exists()     # True/False

# read/write with pathlib
content = Path("file.txt").read_text()
Path("out.txt").write_text("Hello")

# glob patterns
list(Path(".").glob("*.py"))
list(Path(".").rglob("*test*"))
```

### 3. Exception Handling: try/except/else/finally

try block runs risky code; except catches specific exceptions; else runs if no exception; finally always runs (cleanup). Catch specific types, never bare except:.

```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError as e:
        print(f"Type error: {e}")
        return None
    else:
        print("Division succeeded")
        return result
    finally:
        print("Cleanup runs always")
```

### 4. Custom Exceptions and Exception Hierarchy

Define custom exceptions by inheriting from Exception. Use exception chaining (raise ... from). All built-in exceptions derive from BaseException: Exception, SystemExit, KeyboardInterrupt.

```python
class ValidationError(Exception):
    """Raised when input validation fails."""
    def __init__(self, field: str, message: str):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")

# chaining
try:
    int("abc")
except ValueError as e:
    raise ValidationError("age", "Not a number") from e

# custom with error code
class ApiError(Exception):
    def __init__(self, status: int, body: str):
        self.status = status
        self.body = body
        super().__init__(f"API {status}: {body[:50]}")
```

### 5. Context Managers and contextlib

Use @contextmanager decorator to turn a generator into a context manager. The with statement calls __enter__ and __exit__. Custom context managers for resources.

```python
from contextlib import contextmanager

@contextmanager
def temporary_change(filename):
    backup = open(filename).read() if Path(filename).exists() else None
    try:
        yield  # context body runs here
    finally:
        if backup is not None:
            Path(filename).write_text(backup)

# usage
with temporary_change("config.json"):
    modify_config()
    # file auto-restores after with block

# closing resources
from contextlib import closing
from urllib.request import urlopen
with closing(urlopen("https://python.org")) as page:
    for line in page:
        print(line)
```

## Practice Questions

1. What does the with statement do? Why use it for files?
1. What is the difference between read(), readline(), readlines()?
1. Why catch specific exception types instead of bare except:?
1. When does the else clause on try execute? When does finally?

## LLM Prompts for Deeper Understanding

1. "Explain pathlib vs os.path with modern file handling patterns"
1. "Show exception handling: try/except/else/finally with real examples"
1. "Teach context managers: __enter__/__exit__ and @contextmanager decorator"

## Key Takeaways

- Use with statements for automatic resource cleanup
- Catch specific exception types, never bare except:
- Pathlib provides OOP file path handling (3.4+)