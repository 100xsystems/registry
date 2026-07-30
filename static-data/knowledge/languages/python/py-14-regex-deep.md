---
{
  "title": "Regular Expressions Deep Dive",
  "description": "Write regex patterns with anchors, quantifiers, groups",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write regex patterns with anchors, quantifiers, groups",
    "Use named groups and non-capturing groups",
    "Apply re.sub with backreferences and callbacks",
    "Optimize regex with compilation and flags"
  ],
  "knowledge_refs": [
    "python/py-14-regex-deep"
  ],
  "prerequisites": [
    "PY-07"
  ],
  "references": [
    {
      "title": "Python Library — re",
      "url": "https://docs.python.org/3/library/re.html"
    },
    {
      "title": "HOWTO — Regex",
      "url": "https://docs.python.org/3/howto/regex.html"
    },
    {
      "title": "Real Python — Regex",
      "url": "https://realpython.com/regex-python/"
    }
  ]
}
---

# PY-14-REGEX-DEEP: Regular Expressions Deep Dive

## Introduction

Regular expressions are patterns for matching text. Python's re module provides search, match, fullmatch, findall, finditer, sub, and split. Compiled patterns (re.compile) are faster for reuse.

## Key Concepts

### 1. Pattern Syntax: Anchors, Quantifiers, Classes

. matches any char; * + ? {} for quantifiers; ^ $ for anchors; \d \w \s for classes; [abc] for character sets; | for alternation. Raw strings r"pattern" avoid escaping.

```python
import re

# anchors
re.search(r"^hello", "hello world")  # match at start
re.search(r"world$", "hello world")  # match at end

# quantifiers
re.search(r"go+d", "gooood")  # g + one or more o + d
re.search(r"colou?r", "color")  # optional u

# character classes
re.findall(r"\d+", "abc123def456")  # ["123", "456"]
re.findall(r"[aeiou]", "hello")      # ["e", "o"]
```

### 2. Groups and Capturing

Parentheses (...) create capturing groups. re.search().group(0) is full match; group(1), group(2) are captured groups. Named groups (?P<name>...) for readability.

```python
text = "Alice: alice@example.com"

# capturing groups
m = re.search(r"(\w+): (\w+@[\w.]+)", text)
print(m.group(0))  # Alice: alice@example.com
print(m.group(1))  # Alice
print(m.group(2))  # alice@example.com

# named groups
m = re.search(r"(?P<name>\w+): (?P<email>\w+@[\w.]+)", text)
print(m.group("name"))   # Alice
print(m.groupdict())     # {"name": "Alice", "email": "alice@example.com"}

# non-capturing group (?:)
re.findall(r"(?:https?://)?(\w+\.\w+)", "http://example.com")
```

### 3. re.sub — Substitution and Backreferences

re.sub replaces matches. Use \1, \2 for backreferences to captured groups. Replacement can be a string with backreferences or a callback function.

```python
import re

# basic substitution
result = re.sub(r"\d+", "NUM", "Page 42 of 100")
print(result)  # Page NUM of NUM

# backreferences in replacement
result = re.sub(r"(\w+)@(\w+)", r"\1 at \2", "alice@example.com")
print(result)  # alice at example

# callback function
def uppercase(match):
    return match.group(0).upper()

result = re.sub(r"\w+", uppercase, "hello world")
print(result)  # HELLO WORLD
```

### 4. Flags: re.IGNORECASE, re.MULTILINE, re.DOTALL

Flags modify regex behavior. re.I for case-insensitive. re.M makes ^/$ match line boundaries. re.S makes . match newlines. Combine with | (pipe).

```python
text = "Hello\nWorld"

# case insensitive
re.search(r"hello", text, re.I)  # matches Hello

# multiline — ^ and $ match each line
re.findall(r"^\w+", text, re.M)  # ["Hello", "World"]

# DOTALL — . matches newline
re.search(r"Hello.World", text, re.S)  # matches

# VERBOSE — readable patterns with comments
pattern = re.compile(r"""
    ^\d{3}       # area code
    [-.]?        # optional separator
    \d{3}       # prefix
    [-]?         # optional separator
    \d{4}       # line number
""", re.VERBOSE)
```

### 5. Compiled Patterns and Performance

re.compile() pre-compiles a pattern into a regex object. Reusing compiled patterns is faster than calling re.search() with the same raw string. compile also stores flags.

```python
# without compile (slow in loops)
for item in thousands_of_items:
    re.search(r"complex.pattern", item)  # recompiles each iteration

# with compile (fast)
pattern = re.compile(r"complex.pattern")
for item in thousands_of_items:
    pattern.search(item)  # pre-compiled

# compiled pattern methods
pat = re.compile(r"\d+")
pat.search("abc123")       # first match
pat.findall("abc123def456")  # all matches
pat.match("123abc")        # match at start
pat.fullmatch("123")       # entire string matches
```

## Practice Questions

1. What do ^ and $ match? How does re.M change this?
1. What is the difference between group(0), group(1), and group("name")?
1. How do you use a callback function with re.sub?
1. Why use re.compile()? When does it matter?

## LLM Prompts for Deeper Understanding

1. "Explain regex groups, backreferences, named groups with examples"
1. "Show advanced regex: lookahead, lookbehind, atomic groups in Python"
1. "Teach re.compile() performance benefits with loop benchmarks"

## Key Takeaways

- Use r"raw strings" for regex patterns to avoid escaping
- Named groups (?P<name>...) improve readability
- re.compile() pre-compiles patterns for faster reuse