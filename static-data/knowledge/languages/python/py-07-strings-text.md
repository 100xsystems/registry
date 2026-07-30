---
{
  "title": "Strings and Text Processing",
  "description": "Format strings with f-strings, format(), and %",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Format strings with f-strings, format(), and %",
    "Master string methods: split, join, strip, replace",
    "Work with Unicode and bytes encoding",
    "Use regular expressions with the re module"
  ],
  "knowledge_refs": [
    "python/py-07-strings-text"
  ],
  "prerequisites": [
    "PY-02"
  ],
  "references": [
    {
      "title": "Python Tutorial — Strings",
      "url": "https://docs.python.org/3/tutorial/introduction.html#strings"
    },
    {
      "title": "Python Library — string",
      "url": "https://docs.python.org/3/library/string.html"
    },
    {
      "title": "Python Library — re",
      "url": "https://docs.python.org/3/library/re.html"
    },
    {
      "title": "Real Python — Strings",
      "url": "https://realpython.com/python-strings/"
    }
  ]
}
---

# PY-07-STRINGS-TEXT: Strings and Text Processing

## Introduction

Python strings are immutable Unicode sequences with 40+ built-in methods. F-strings (3.6+) are the modern standard for formatting. The re module provides full regular expression support.

## Key Concepts

### 1. String Formatting: f-strings

F-strings use {expression} for interpolation. Support format specifiers: {value:.2f}, {value:>10}. Call expressions and method calls inline. Use = for debug output (3.8+).

```python
name = "Alice"; age = 30
f"My name is {name} and I am {age}"
f"Pi to 2 decimals: {3.14159:.2f}"
f"Right aligned: {name:>10}"
f"Debug: {name=} {age=}"  # 3.8+

# str.format() for templates
"Hello, {}! You are {}.".format(name, age)
```

### 2. String Methods

split/join for delimiting. strip/lstrip/rstrip for whitespace. replace/sub. upper/lower/swapcase. startswith/endswith. find/index/count. isalpha/isdecimal/isspace.

```python
text = "  hello, world  "
text.strip()        # "hello, world"
text.upper()        # "  HELLO, WORLD  "
text.replace("o", "0")

csv = "a,b,c"
csv.split(",")      # ["a", "b", "c"]
"|".join(["a", "b", "c"])  # "a|b|c"

"hello".startswith("he")  # True
"hello".index("l")        # 2
```

### 3. Unicode and Encoding

Python 3 strings are Unicode. str holds code points; bytes holds encoded bytes. encode() converts str to bytes; decode() converts bytes back. Common codecs: utf-8, ascii, latin-1.

```python
s = "Hello"
b = s.encode("utf-8")   # b'Hello'
s2 = b.decode("utf-8")  # "Hello"

emoji = "Python "
len(emoji)  # 8
list(emoji)  # list of code points

# encoding errors
s.encode("ascii", errors="replace")
```

### 4. Regular Expressions with re

re module: search() finds first match; findall() finds all; sub() replaces; split() splits. Use raw strings r"pattern" to avoid escaping backslashes.

```python
import re
text = "Contact: alice@example.com"

m = re.search(r"[\w.]+@[\w.]+", text)
if m: print(m.group())  # alice@example.com

emails = re.findall(r"[\w.]+@[\w.]+", text)

masked = re.sub(r"(\w)@", "***@", text)

# named groups
m = re.search(r"(?P<name>\w+)@(?P<dom>[\w.]+)", text)
m.group("name")  # alice
```

### 5. Advanced: textwrap and difflib

string module has constants (ascii_letters, digits). textwrap handles paragraph formatting. difflib compares sequences and produces diffs.

```python
import string
string.ascii_letters  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM...
string.digits         # 0123456789

from textwrap import dedent, wrap, fill
dedent("    indented text")
fill("long line", width=40)

import difflib
diff = difflib.unified_diff(a, b, lineterm="")
```

## Practice Questions

1. What is the difference between f"{x}", "{}".format(x), and "%s" % x?
1. How do you join a list of strings? How to split by comma?
1. What does encode() do? What does decode() do?
1. Write a regex for US phone: (123) 456-7890.

## LLM Prompts for Deeper Understanding

1. "Explain f-strings, format(), % with benchmarks and use cases"
1. "Show regex patterns: named groups, lookahead, backreferences"
1. "Teach Unicode and encoding: str vs bytes vs bytearray"

## Key Takeaways

- F-strings are the modern standard for string formatting (3.6+)
- Python 3 uses Unicode strings; encode/decode for bytes
- The re module provides search, findall, sub, and split