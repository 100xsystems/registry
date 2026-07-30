---
{
  "title": "Control Flow: Conditionals, Loops, Comprehensions",
  "description": "Write conditionals with if/elif/else",
  "type": "lesson",
  "order": 3,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write conditionals with if/elif/else",
    "Use for loops with range, enumerate, zip",
    "Master while loops and break/continue/else",
    "Write list/dict/set comprehensions",
    "Use match/case (Python 3.10+)"
  ],
  "knowledge_refs": [
    "python/py-03-control-flow"
  ],
  "prerequisites": [
    "PY-02"
  ],
  "references": [
    {
      "title": "Tutorial — if",
      "url": "https://docs.python.org/3/tutorial/controlflow.html#if-statements"
    },
    {
      "title": "Tutorial — for",
      "url": "https://docs.python.org/3/tutorial/controlflow.html#for-statements"
    },
    {
      "title": "Tutorial — list comps",
      "url": "https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions"
    },
    {
      "title": "PEP 636 — Pattern Matching",
      "url": "https://peps.python.org/pep-0636/"
    }
  ]
}
---

# PY-03-CONTROL-FLOW: Control Flow: Conditionals, Loops, Comprehensions

## Introduction

Control flow determines execution order. Python provides clean, indentation-based syntax for conditionals, iteration, and structural pattern matching (3.10+).

## Key Concepts

### 1. Conditionals: if/elif/else

No parentheses or braces — indentation defines blocks. Use in, is, comparison operators for expressive conditions. Walrus operator := assigns within conditions (3.8+).

```python
x = 42
if x > 100:
    print("Large")
elif x > 10:
    print("Medium")
else:
    print("Small")

if (n := len("hello")) > 3:
    print(f"Length: {n}")
```

### 2. for Loops: enumerate, zip, range

Python for loops iterate over iterables. enumerate for index+value, zip for parallel iteration, range for numeric sequences, reversed for reverse.

```python
names = ["Alice", "Bob", "Charlie"]
for idx, name in enumerate(names, 1):
    print(f"{idx}. {name}")

scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

### 3. while Loops and break/continue/else

while runs until condition is false. break exits early; continue skips to next iteration. else runs only if loop completed without break.

```python
import random
while True:
    v = random.randint(1, 10)
    if v == 7:
        print("Found 7!")
        break

for n in range(2, 10):
    for d in range(2, n):
        if n % d == 0:
            break
    else:
        print(f"{n} is prime")  # no break occurred
```

### 4. List, Dict, and Set Comprehensions

Comprehensions build collections concisely. Often faster and more readable than manual loops. Dict and set comprehensions use {}.

```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
flat = [item for row in [[1,2],[3,4]] for item in row]
square_dict = {x: x**2 for x in range(5)}
unique_lens = {len(w) for w in ["hi", "hello", "hey"]}
```

### 5. match/case (Python 3.10+)

Structural pattern matching supports literal, sequence, mapping, class, and guard patterns. Clean dispatch based on shape, not just value.

```python
def describe(value):
    match value:
        case 0:
            return "Zero"
        case 1 | 2 | 3:
            return "Small"
        case int():
            return f"Integer: {value}"
        case str():
            return f"String: {value}"
        case _:
            return "Something else"
```

## Practice Questions

1. What does range(10), range(5,10), range(0,10,2) produce?
1. When to use list comprehension vs for loop?
1. What does the else clause on a for loop do?
1. Write a match statement for a 2D coordinate (x, y) returning quadrant.

## LLM Prompts for Deeper Understanding

1. "Explain comprehensions: list, dict, set with performance"
1. "Show match/case patterns with seq, mapping, class, guards"
1. "Teach for-else and while-else — what problem do they solve?"

## Key Takeaways

- Use enumerate for index, zip for parallel, comprehensions for conciseness
- else on loops runs only if no break occurred
- match/case enables powerful structural pattern matching