---
{
  "title": "Functions and Scope",
  "description": "Define functions with positional, keyword, and default params",
  "type": "lesson",
  "order": 4,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define functions with positional, keyword, and default params",
    "Use *args and **kwargs for variable-length arguments",
    "Understand LEGB scope rules and the nonlocal keyword",
    "Write lambda expressions and closure factories"
  ],
  "knowledge_refs": [
    "python/py-04-functions-scope"
  ],
  "prerequisites": [
    "PY-02"
  ],
  "references": [
    {
      "title": "Python Tutorial — Defining Functions",
      "url": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions"
    },
    {
      "title": "Python Tutorial — More on Functions",
      "url": "https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions"
    },
    {
      "title": "Python Reference — Function Definitions",
      "url": "https://docs.python.org/3/reference/compound_stmts.html#function-definitions"
    },
    {
      "title": "Real Python — Scope LEGB",
      "url": "https://realpython.com/python-scope-legb-rule/"
    }
  ]
}
---

# PY-04-FUNCTIONS-SCOPE: Functions and Scope

## Introduction

Functions are first-class citizens in Python: they can be passed as arguments, returned from other functions, and assigned to variables. The parameter system covers positional, keyword, default, *args, and **kwargs.

## Key Concepts

### 1. Parameter Types: Positional, Keyword, Default

Python functions support positional args (by order), keyword args (by name), and default values. Positional-only parameters (before /) and keyword-only (after *).

```python
def connect(host, port=8080, *, timeout=30):
    return f"Connecting to {host}:{port}"

# positional-only, keyword-only
def divide(a, b, /):  # a,b positional-only
    return a / b

connect("localhost", 3000, timeout=60)
```

### 2. *args and **kwargs

*args captures extra positional args as tuple; **kwargs captures keyword args as dict. Essential for wrapper/decorator/function-forwarding patterns.

```python
def log(level, *messages):
    for msg in messages:
        print(f"[{level}] {msg}")
log("INFO", "Start", "Processing", "Done")

def create_user(name, **attrs):
    user = {"name": name}
    user.update(attrs)
    return user
create_user("Alice", age=30, role="admin")
```

### 3. LEGB Scope and nonlocal

Python resolves names in LEGB order: Local, Enclosing, Global, Built-in. Use global for module-level writes; nonlocal for enclosing scope writes (not global). Closures capture enclosing variables.

```python
x = "global"
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner"
        print(x)
    inner()
    print(x)  # "inner" (modified by nonlocal)
outer()
print(x)  # "global" (unchanged)
```

### 4. Lambda and Closures

Lambdas are anonymous single-expression functions. Use for short callbacks. Closures let functions remember enclosing scope variables even after scope exits.

```python
# Lambda
sorted(students, key=lambda s: s["grade"])
list(filter(lambda x: x > 0, [-1, 2, -3, 4]))

# Closure factory
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter()
print(c())  # 1
print(c())  # 2
```

## Practice Questions

1. Order of params in Python function signature?
1. What does *args capture? What does **kwargs capture?
1. What is LEGB? When would you use nonlocal vs global?
1. Write a closure-based make_timer that returns elapsed seconds.

## LLM Prompts for Deeper Understanding

1. "Explain function parameter types: positional, keyword, default, *args, **kwargs"
1. "Show closures with practical caching and configuration examples"
1. "Teach LEGB scope and when to use global vs nonlocal"

## Key Takeaways

- Use / for positional-only, * for keyword-only params
- *args captures positional extras; **kwargs captures keyword extras
- Closures remember their enclosing scope — foundation of decorators