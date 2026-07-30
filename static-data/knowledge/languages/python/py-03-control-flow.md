---
title: "Control Flow: Conditionals and Loops"
description: "if/elif/else, for loops, while loops, match statements, and loop control with break/continue/else clauses."
type: lesson
order: 3
duration: "60 min"
difficulty: beginner
learning_objectives:
  - "Write conditional logic with if/elif/else and truthiness"\n  - "Iterate with for loops over ranges and iterables"\n  - "Use while loops for conditional iteration"\n  - "Master break, continue, and the match statement"
knowledge_refs:
  - python/py-03-control-flow
prerequisites:
  - "PY-02"
references:
    - title: "Python Tutorial — 4. More Control Flow"\n      url: "https://docs.python.org/3/tutorial/controlflow.html"\n    - title: "Python Tutorial — 4.7 match Statements"\n      url: "https://docs.python.org/3/tutorial/controlflow.html#match-statements"\n    - title: "Real Python — Python For Loops"\n      url: "https://realpython.com/python-for-loop/"
---

# PY-03-CONTROL-FLOW: Control Flow: Conditionals and Loops


## Conditionals — if/elif/else

Python uses [if/elif/else](https://docs.python.org/3/tutorial/controlflow.html#if-statements), evaluating truthiness:
```python
x = 10
if x > 10: print("greater")
elif x == 10: print("exactly 10")
else: print("less than 10")
```
**Falsy values**: `False, None, 0, 0.0, "", [], {}, set(), range(0)`

## The for Loop

Python's `for` is a [foreach-style iterator](https://docs.python.org/3/tutorial/controlflow.html#for-statements):
```python
for i in range(5): print(i)             # 0 1 2 3 4
for idx, val in enumerate(["a","b"]):
    print(f"{idx}: {val}")               # 0: a, 1: b
for a, b in zip([1,2], ["x","y"]):
    print(a, b)                          # 1 x, 2 y
```

## Loop Control: break, continue, else

The unique `else` clause runs when the loop completes WITHOUT `break`:
```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} = {x}*{n//x}")
            break
    else:
        print(f"{n} is prime")
```

## match Statement (3.10+)

[Structural pattern matching](https://docs.python.org/3/tutorial/controlflow.html#match-statements):
```python
match command.split():
    case ["quit"]: return "Bye!"
    case ["hello", name]: return f"Hi {name}!"
    case _: return "Unknown"
```

