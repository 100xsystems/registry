---
title: "Strings, Formatting, and Text Processing"
description: "String methods, f-strings, formatting, Unicode encoding, and text processing patterns."
type: lesson
order: 7
duration: "60 min"
difficulty: beginner
learning_objectives:
  - "Use all major string methods"\n  - "Format strings with f-strings and format()"\n  - "Handle Unicode and encoding correctly"\n  - "Apply common text processing patterns"
knowledge_refs:
  - python/py-07-strings-text
prerequisites:
  - "PY-02"
references:
    - title: "Python Tutorial — 7.1 Fancier Output"\n      url: "https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting"\n    - title: "Fluent Python — Ch. 4: Unicode Text vs Bytes"\n      url: "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/"
---

# PY-07-STRINGS-TEXT: Strings, Formatting, and Text Processing


## String Methods

```python
text = "  Hello, Python World!  "
print(text.strip())            # "Hello, Python World!"
print(text.lower().startswith("  hello"))  # True
print("python" in text.lower())  # True
print(text.split(","))         # ['  Hello', ' Python World!  ']
print(" - ".join(["a","b","c"]))  # "a - b - c"
```

## f-Strings (Python 3.6+)

The modern way to [format strings](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting):
```python
name, age = "Alice", 30
print(f"{name} is {age} years old")
print(f"Pi ≈ {3.14159:.2f}")     # Pi ≈ 3.14
print(f"{1000000:,}")             # 1,000,000
```

## Unicode

```python
s = "Python 🐍"
print(len(s))           # 8 (emoji is one code point)
print(s.encode("utf-8"))  # b'Python \xf0\x9f\x90\x8d'
```

