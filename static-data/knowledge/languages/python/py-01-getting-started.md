---
{
  "title": "Getting Started with Python",
  "description": "Install Python and set up development",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install Python and set up development",
    "Run code via REPL, scripts, and notebooks",
    "Understand PEP 20 (Zen of Python)",
    "Write your first Python program"
  ],
  "knowledge_refs": [
    "python/py-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "Python Tutorial",
      "url": "https://docs.python.org/3/tutorial/appetite.html"
    },
    {
      "title": "Interpreter",
      "url": "https://docs.python.org/3/tutorial/interpreter.html"
    },
    {
      "title": "PEP 20",
      "url": "https://peps.python.org/pep-0020/"
    }
  ]
}
---

# PY-01-GETTING-STARTED: Getting Started with Python

## Introduction

Python is a high-level, interpreted language known for readability and versatility. It powers web apps, data science, AI/ML, automation, and DevOps.

## Key Concepts

### 1. Installing and the REPL

Python 3.x is the current major version. The REPL (Read-Eval-Print Loop) is an interactive shell for experimentation. It is the fastest way to test ideas.

```python
# Verify installation
$ python3 --version
# Python 3.13.1

# Start the REPL
$ python3
>>> print("Hello, World!")
Hello, World!
>>> 2 + 3
5
```

### 2. Scripts and __name__

Python .py files are scripts. The __name__ variable equals "__main__" when run directly and the module name when imported. This dual-purpose pattern lets files be both runnable and importable.

```python
# hello.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
```

### 3. The Zen of Python

PEP 20 captures 19 guiding principles. "Beautiful is better than ugly," "Simple is better than complex," "Readability counts." Run `import this` in the REPL.

```python
>>> import this
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Readability counts.
```

### 4. Virtual Environments with venv

Virtual environments isolate dependencies per project. Python 3.3+ includes venv natively. pip installs from PyPI. Always use a virtual environment.

```python
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install requests flask
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
```

### 5. Python in Different Contexts

Python runs as scripts, Jupyter notebooks for data science, web frameworks, and embedded systems. Same language, different runtimes.

```python
$ python3 my_script.py
$ python3 -m http.server 8000
$ python3 -c "print(sum(range(100)))"
```

## Practice Questions

1. What is the difference between REPL, script, and module mode?
1. Why does `if __name__ == "__main__"` matter?
1. Why should every project use a virtual environment?
1. Run `import this` and explain your favorite principle.

## LLM Prompts for Deeper Understanding

1. "Explain Python virtual environments: venv vs pipenv vs poetry"
1. "Show the __name__ variable pattern with examples"
1. "Teach PEP 20 and how each principle applies to code design"

## Key Takeaways

- Use __name__ == "__main__" for dual-purpose script/module files
- Virtual environments with venv + pip isolate project dependencies
- Python prioritizes readability, simplicity, and explicitness