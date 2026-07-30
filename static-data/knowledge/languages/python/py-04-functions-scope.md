---
title: "Functions and Scope"
description: "Function definitions, parameters, return values, scope rules, lambda expressions, and annotations."
type: lesson
order: 4
duration: "75 min"
difficulty: intermediate
learning_objectives:
  - "Define functions with various parameter types"\n  - "Understand LEGB scope rules and closures"\n  - "Write lambda expressions"\n  - "Use function annotations and docstrings"
knowledge_refs:
  - python/py-04-functions-scope
prerequisites:
  - "PY-03"
references:
    - title: "Python Tutorial — 4.8 Defining Functions"\n      url: "https://docs.python.org/3/tutorial/controlflow.html#defining-functions"\n    - title: "Python Tutorial — 4.9 More on Functions"\n      url: "https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions"\n    - title: "Fluent Python — Ch. 7: First-Class Functions"\n      url: "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/"
---

# PY-04-FUNCTIONS-SCOPE: Functions and Scope


## Defining Functions

```python
def greet(name: str, greeting: str = "Hello") -> str:
    """Return a personalized greeting."""
    return f"{greeting}, {name}!"
```

## Parameters

```python
# *args collects extra positional args as a tuple
# **kwargs collects extra keyword args as a dict
def log(message, *args, level="INFO", **kwargs):
    print(f"[{level}] {message}", args, kwargs)

log("Server started", 8080, "v2", level="DEBUG", env="prod")
```

## Scope — LEGB Rule

Python resolves names in order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in:

```python
x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # local
    inner()
    print(x)  # enclosing
outer()
print(x)  # global
```

## Lambda Expressions

```python
square = lambda x: x ** 2
add = lambda a, b: a + b
print(square(5))  # 25
```

## Practice Questions
1. What does `nonlocal` do vs `global`?
2. Write a function that accepts any number of arguments and returns their sum.

