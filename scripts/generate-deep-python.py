#!/usr/bin/env python3
"""
Deep Python Curriculum Generator — JavaScript-quality content with:
- Unique per-lesson subtopics with code examples
- Inline markdown links to exact Python doc URLs
- Per-lesson practice questions
- LLM prompts and key takeaways
"""

import json
import os

BASE = os.path.join(os.path.dirname(__file__), '..', 'static-data', 'knowledge', 'languages', 'python')

LESSONS = [
    {
        "slug": "py-01-getting-started",
        "title": "Getting Started with Python",
        "description": "Install Python, set up a development environment, understand the interpreter and REPL, and write your first program.",
        "order": 1, "duration": "45 min", "difficulty": "beginner",
        "objectives": [
            "Install Python 3 and configure PATH/JAVA_HOME equivalents",
            "Understand the Python interpreter, REPL, and script execution",
            "Write and run your first Python program",
            "Use pip to install third-party packages",
        ],
        "prereqs": ["None — entry point"],
        "refs": [
            ("Python Tutorial — 1. Whetting Your Appetite", "https://docs.python.org/3/tutorial/appetite.html"),
            ("Python Tutorial — 2. Using the Interpreter", "https://docs.python.org/3/tutorial/interpreter.html"),
            ("Real Python — Python Development Setup", "https://realpython.com/installing-python/"),
            ("Python Crash Course — Ch. 1: Getting Started", "https://nostarch.com/python-crash-course-3rd-edition"),
        ],
        "content": """
## Introduction

Python is a high-level, dynamically-typed programming language that emphasizes readability and productivity. Before writing any code, you need to set up your environment properly.

## Installing Python

Visit [python.org/downloads](https://python.org/downloads/) and download the latest Python 3 release (3.12+). During installation on macOS/Windows, **check "Add Python to PATH"** — this lets you run `python3` from the terminal.

Verify the installation:

```python
# In your terminal:
# python3 --version
# Python 3.12.3

# pip3 --version
# pip 24.0 from ...
```

## The Python Interpreter and REPL

Python can run in two modes:

**1. Interactive REPL** — type `python3` in your terminal to start the [interactive interpreter](https://docs.python.org/3/tutorial/interpreter.html#interactive-mode). Each line is evaluated immediately:

```python
>>> print("Hello, World!")
Hello, World!
>>> 2 + 2
4
>>> import this  # The Zen of Python
```

**2. Script mode** — save code in a `.py` file and run it:

```python
# hello.py
print("Hello, World!")
name = input("What's your name? ")
print(f"Nice to meet you, {name}!")
```

Run with:
```bash
python3 hello.py
```

## Your First Program: The Pythonic Way

```python
#!/usr/bin/env python3
\"\"\"A friendly greeting program.\"\"\"

def greet(name: str) -> str:
    \"\"\"Return a personalized greeting.\"\"\"
    return f"Hello, {name}! Welcome to Python."

def main() -> None:
    name = input("Enter your name: ")
    print(greet(name))

if __name__ == "__main__":
    main()
```

This demonstrates:
- **Shebang** for Unix-like systems
- **Docstrings** (`\"\"\"...\"\"\"`) for documentation
- **Type hints** (`name: str`, `-> str`) for clarity
- **`if __name__ == "__main__"`** guard for reusable modules

## Managing Packages with pip

Python's package manager `pip` installs third-party libraries:

```bash
pip3 install requests numpy pytest
pip3 list           # Show installed packages
pip3 freeze > requirements.txt  # Export dependencies
```

## Key Takeaways

- Python 3 is the standard — avoid Python 2
- The REPL is excellent for experimentation
- Use `pip` for dependency management
- Python emphasizes readability and explicit code

## Practice Questions

1. What's the difference between running Python interactively and running a script?
2. Why is `if __name__ == "__main__"` important?
3. Install a package with pip and import it in a script.
"""
    },
    {
        "slug": "py-02-variables-types",
        "title": "Variables, Types, and Basic Operations",
        "description": "Python's dynamic type system, primitive types, variables, numbers, strings, operators, and type conversion.",
        "order": 2, "duration": "60 min", "difficulty": "beginner",
        "objectives": [
            "Master Python's dynamic type system and 7 primitive types",
            "Work with integers, floats, booleans, None, and strings",
            "Understand type conversion and operator precedence",
            "Use type hints for documentation and static analysis",
        ],
        "prereqs": ["PY-01"],
        "refs": [
            ("Python Tutorial — 3.1 Numbers", "https://docs.python.org/3/tutorial/introduction.html#numbers"),
            ("Python Tutorial — 3.2 Strings", "https://docs.python.org/3/tutorial/introduction.html#text"),
            ("Python Reference — Data Model", "https://docs.python.org/3/reference/datamodel.html#objects"),
            ("Real Python — Python Variables", "https://realpython.com/python-variables/"),
            ("Fluent Python — Ch. 1: The Python Data Model", "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/"),
        ],
        "content": """
## Introduction

Python is dynamically typed — variables can hold any type, and types are checked at runtime. But Python is also **strongly typed** — implicit type coercion is limited.

## Variables and Dynamic Typing

Variables are created by assignment. No declaration needed:

```python
x = 42           # x is int
x = "hello"      # now x is str
x = [1, 2, 3]    # now x is list
```

Use `type()` to inspect types:

```python
print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>
print(type(None))        # <class 'NoneType'>
```

## Numeric Types

Python has three numeric types — see the [Python Tutorial on Numbers](https://docs.python.org/3/tutorial/introduction.html#numbers):

```python
# Integers (unbounded)
a = 42
b = 2 ** 1000  # Huge integer — no overflow!

# Floats (IEEE 754 double)
c = 3.14159
d = 1.5e-10

# Complex numbers
z = 3 + 4j
print(z.real, z.imag)  # 3.0 4.0
```

**Operator precedence** follows PEMDAS:

```python
result = 2 + 3 * 4       # 14, not 20
result = (2 + 3) * 4     # 20
result = 10 / 3           # 3.333... (float)
result = 10 // 3          # 3 (integer division)
result = 10 % 3           # 1 (modulo)
result = 2 ** 4           # 16 (exponentiation)
```

## Strings

Python strings are immutable sequences of Unicode code points — [Tutorial on Strings](https://docs.python.org/3/tutorial/introduction.html#text):

```python
s1 = "double quotes"
s2 = 'single quotes'
s3 = \"\"\"multi-line
strings are useful\"\"\"

# String operations
print("Hello" + " " + "World")   # Concatenation
print("Hello" * 3)                # Repetition: HelloHelloHello
print("Hello"[0])                 # Indexing: H
print("Hello"[1:4])               # Slicing: ell
print(len("Hello"))               # Length: 5
```

## Booleans and None

```python
is_valid = True
is_done = False
result = None  # Absence of value

# Boolean operators
print(True and False)   # False
print(True or False)    # True
print(not True)         # False
```

## Type Conversion (Explicit)

```python
# int(), float(), str(), bool()
print(int("42"))           # 42
print(float("3.14"))       # 3.14
print(str(42))             # "42"
print(bool(1))             # True
print(bool(0))             # False
print(bool(""))            # False
print(bool("hello"))       # True
```

## Type Hints (Python 3.5+)

Type hints improve code readability and enable static analysis with `mypy`:

```python
def add(a: int, b: int) -> int:
    return a + b

name: str = "Alice"
count: int = 42
items: list[int] = [1, 2, 3]
```

## Key Takeaways

- Python is dynamically but strongly typed
- All values are objects — even integers and booleans
- Use explicit type conversion over implicit
- Type hints are optional but recommended for production code

## Practice Questions

1. Why does `print(10 / 3)` produce a float but `print(10 // 3)` produces an int?
2. What's the difference between `is` and `==` for string comparison?
3. Write a function that takes two floats and returns their sum with a type hint.
"""
    },
    {
        "slug": "py-03-control-flow",
        "title": "Control Flow: Conditionals and Loops",
        "description": "if/elif/else, for loops, while loops, match statements, and loop control with break/continue/else clauses.",
        "order": 3, "duration": "60 min", "difficulty": "beginner",
        "objectives": [
            "Write conditional logic with if/elif/else and truthiness rules",
            "Iterate with for loops over ranges, sequences, and iterables",
            "Use while loops for conditional iteration",
            "Master break, continue, pass, and the match statement",
        ],
        "prereqs": ["PY-02"],
        "refs": [
            ("Python Tutorial — 4. More Control Flow", "https://docs.python.org/3/tutorial/controlflow.html"),
            ("Python Tutorial — 4.7 match Statements", "https://docs.python.org/3/tutorial/controlflow.html#match-statements"),
            ("Real Python — Conditional Statements", "https://realpython.com/python-conditional-statements/"),
            ("Real Python — Python For Loops", "https://realpython.com/python-for-loop/"),
        ],
        "content": """
## Introduction

Control flow determines the order in which code executes. Python's control flow is clean and readable, using indentation rather than braces.

## Conditionals: if/elif/else

All conditionals evaluate **truthiness** — values are coerced to `bool`:

```python
x = 10
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is exactly 10")
else:
    print("x is less than 10")
```

**Falsy values** in Python:
```python
# All of these evaluate to False in a boolean context:
False, None, 0, 0.0, "" (empty string), [] (empty list),
{} (empty dict), set() (empty set), range(0)
```

**Ternary expression** (conditional expression):
```python
status = "adult" if age >= 18 else "minor"
```

## The for Loop

Python's `for` loop iterates over **iterables** — it's a foreach, not a C-style for. See the [Tutorial on `for` statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements):

```python
# Iterate over a range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# enumerate — get index and value
for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")

# zip — iterate multiple sequences in parallel
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

## The while Loop

Use `while` when the number of iterations isn't known in advance:

```python
count = 0
while count < 5:
    print(count)
    count += 1

# Infinite loop with break
while True:
    response = input("Type 'quit' to exit: ")
    if response == "quit":
        break
```

## Loop Control: break, continue, else

```python
# break — exit the loop entirely
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} = {x} * {n//x}")
            break
    else:
        # else clause runs when loop completes WITHOUT break
        print(f"{n} is prime")
```

The `else` clause on loops is unique to Python — it runs only if the loop wasn't terminated by `break`.

## The match Statement (Python 3.10+)

Structural pattern matching — like switch on steroids. See the [match statement docs](https://docs.python.org/3/tutorial/controlflow.html#match-statements):

```python
def handle_command(command: str) -> str:
    match command.split():
        case ["quit"]:
            return "Goodbye!"
        case ["hello", name]:
            return f"Hello, {name}!"
        case ["load", filename] if filename.endswith(".json"):
            return f"Loading JSON: {filename}"
        case ["load", filename]:
            return f"Loading file: {filename}"
        case _:
            return f"Unknown command: {command}"
```

## Practice Questions

1. Write a function that uses `for` and `range()` to sum all even numbers from 1 to 100.
2. How does the `else` clause on a `for` loop differ from an `else` on an `if`?
3. Use `match` to write a Fibonacci sequence pattern.
"""
    },
]

def generate_md(lesson: dict) -> str:
    """Generate a .md file from lesson data."""
    objectives = "\n".join(f'  - "{obj}"' for obj in lesson["objectives"])
    prereqs = "\n".join(f'  - "{p}"' for p in lesson["prereqs"])
    refs = "\n".join(
        f'    - title: "{title}"\n      url: "{url}"'
        for title, url in lesson["refs"]
    )

    return f"""---
title: "{lesson['title']}"
description: "{lesson['description']}"
type: lesson
order: {lesson['order']}
duration: "{lesson['duration']}"
difficulty: {lesson['difficulty']}
learning_objectives:
{objectives}
knowledge_refs:
  - python/{lesson['slug']}
prerequisites:
{prereqs}
references:
{refs}
---

# {lesson["slug"].upper()}: {lesson["title"]}

{lesson["content"]}
"""


def update_index_json(lessons: list[dict]) -> None:
    idx_path = os.path.join(BASE, 'index.json')
    with open(idx_path, 'r') as f:
        data = json.load(f)
    
    lesson_entries = []
    for lesson in lessons:
        lesson_entries.append({
            "slug": lesson["slug"],
            "title": lesson["title"],
            "description": lesson["description"],
            "type": "lesson",
            "order": lesson["order"],
            "duration": lesson["duration"],
            "difficulty": lesson["difficulty"],
            "knowledge_refs": [f"python/{lesson['slug']}"],
        })
    
    data["lessons"] = lesson_entries
    with open(idx_path, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f'✅ index.json updated ({len(lessons)} lessons)')


def main():
    # Delete existing .md lesson files
    for fname in os.listdir(BASE):
        if fname.endswith('.md') and fname != 'index.json':
            os.remove(os.path.join(BASE, fname))
    
    # Generate new lessons
    for lesson in LESSONS:
        md_content = generate_md(lesson)
        md_path = os.path.join(BASE, f"{lesson['slug']}.md")
        with open(md_path, 'w') as f:
            f.write(md_content)
        print(f'  ✅ {lesson["slug"]}.md')
    
    # Update index.json
    # (skipping until we have all 21)
    print(f'\n✅ Generated {len(LESSONS)} deep Python lessons')


if __name__ == '__main__':
    main()
