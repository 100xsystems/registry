---
title: "Getting Started with Python"
description: "Install Python, set up a dev environment, understand the interpreter and REPL, and write your first program."
type: lesson
order: 1
duration: "45 min"
difficulty: beginner
learning_objectives:
  - "Install Python 3 and configure your environment"\n  - "Understand the interpreter, REPL, and script execution"\n  - "Write and run Python programs"\n  - "Use pip for package management"
knowledge_refs:
  - python/py-01-getting-started
prerequisites:
  - "None — entry point"
references:
    - title: "Python Tutorial — 2. Using the Interpreter"\n      url: "https://docs.python.org/3/tutorial/interpreter.html"\n    - title: "Python Tutorial — 1. Whetting Your Appetite"\n      url: "https://docs.python.org/3/tutorial/appetite.html"\n    - title: "Real Python — Python Setup"\n      url: "https://realpython.com/installing-python/"
---

# PY-01-GETTING-STARTED: Getting Started with Python


## Introduction

Python is a high-level, dynamically-typed language emphasizing readability. Let's get your environment ready.

## Installing Python

Download Python 3.12+ from [python.org](https://python.org/downloads/). Verify:
```bash
python3 --version  # Python 3.12.3
pip3 --version     # pip 24.0
```

## The REPL

The [interactive interpreter](https://docs.python.org/3/tutorial/interpreter.html#interactive-mode) evaluates code line-by-line:
```python
>>> print("Hello, World!")
Hello, World!
>>> 2 + 2
4
>>> import this  # The Zen of Python
```

## Scripts

Save code in a `.py` file and run with `python3 filename.py`:
```python
# hello.py
name = input("What's your name? ")
print(f"Hello, {name}!")
```

## Practice Questions
1. What's the difference between REPL and script mode?
2. Why use `if __name__ == "__main__"`?

