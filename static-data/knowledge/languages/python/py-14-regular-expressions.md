---
title: "Regular Expressions"
description: "Regex syntax, pattern compilation, groups, lookahead/lookbehind, and text processing with the re module."
type: lesson
order: 14
duration: "60 min"
difficulty: intermediate
learning_objectives:
  - "Write regex patterns for text matching"\n  - "Use groups, named groups, backreferences"\n  - "Apply lookahead and lookbehind"\n  - "Use findall, search, match, sub"
knowledge_refs:
  - python/py-14-regular-expressions
prerequisites:
  - "PY-07"
references:
    - title: "Python Docs — re module"\n      url: "https://docs.python.org/3/library/re.html"\n    - title: "Automate the Boring Stuff — Ch. 7: Regex"\n      url: "https://automatetheboringstuff.com/2e/chapter7/"
---

# PY-14-REGULAR-EXPRESSIONS: Regular Expressions


## Basic Patterns

```python
import re
text = "Contact: alice@example.com or bob@test.org"

# Find all emails
emails = re.findall(r'\w+@\w+\.\w+', text)
print(emails)  # ['alice@example.com', 'bob@test.org']

# Search for first match
match = re.search(r'(\w+)@(\w+\.\w+)', text)
if match:
    print(match.group(0))  # alice@example.com
    print(match.group(1))  # alice (username)
    print(match.group(2))  # example.com (domain)
```

## Substitution

```python
# Mask emails
masked = re.sub(r'\w+@', '***@', text)
print(masked)  # Contact: ***@example.com or ***@test.org
```

## Practice Questions
1. Write a regex to validate a phone number format.
2. Extract all hashtags from a string using regex.

