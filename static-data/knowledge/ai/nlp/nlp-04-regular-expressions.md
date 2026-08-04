---
slug: nlp-04-regular-expressions
title: "Regular Expressions for Text"
description: "Pattern matching for text processing — from simple matches to complex extraction pipelines."
order: 4
tags:
  - nlp
  - regex
  - pattern-matching
  - text-extraction
prerequisites:
  - nlp-03-text-preprocessing
  - nlp-01-what-is-nlp
references:
  - title: "Python re Documentation"
    url: "https://docs.python.org/3/library/re.html"
    description: "Official Python regex documentation"
  - title: "Regular Expression HOWTO (Python)"
    url: "https://docs.python.org/3/howto/regex.html"
    description: "Official Python regex tutorial"
  - title: "Regex in Python (Real Python)"
    url: "https://realpython.com/regex-python/"
    description: "Comprehensive regex guide with examples"
  - title: "Regex Cheat Sheet (GeeksforGeeks)"
    url: "https://www.geeksforgeeks.org/python/python-regex-cheat-sheet/"
    description: "Quick reference for regex patterns"
  - title: "Regex101"
    url: "https://regex101.com/"
    description: "Interactive regex tester and debugger"
knowledge_refs:
  - nlp-03-text-preprocessing
  - nlp-02-text-representation
  - cv-17-ocr-and-document-ai
---

# Regular Expressions for Text

Regular expressions (regex) are a powerful pattern-matching language for text processing. They're essential for cleaning, extracting, and validating text in NLP pipelines.

## Basic Patterns

| Pattern | Matches | Example |
|---|---|---|
| `.` | Any character | "a.c" matches "abc", "a1c" |
| `\d` | Digit [0-9] | "\d+" matches "123" |
| `\w` | Word character [a-zA-Z0-9_] | "\w+" matches "hello" |
| `\s` | Whitespace | "\s+" matches spaces, tabs |
| `^` | Start of string | "^Hello" matches "Hello world" |
| `$` | End of string | "world$" matches "Hello world" |

## Quantifiers

| Quantifier | Meaning | Example |
|---|---|---|
| `*` | 0 or more | "ab*" matches "a", "ab", "abb" |
| `+` | 1 or more | "ab+" matches "ab", "abb" (not "a") |
| `?` | 0 or 1 | "ab?" matches "a", "ab" |
| `{n}` | Exactly n | "a{3}" matches "aaa" |
| `{n,m}` | Between n and m | "a{2,4}" matches "aa", "aaa", "aaaa" |

## Character Classes

```python
import re

text = "Email: user@example.com, Phone: (555) 123-4567"

# Match email
emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+', text)
# ['user@example.com']

# Match phone numbers
phones = re.findall(r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}', text)
# ['(555) 123-4567']
```

## Groups and Capturing

```python
# Named groups
pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
match = re.search(pattern, "Today is 2024-01-15")
print(match.group('year'))  # 2024
print(match.group('month')) # 01

# Non-capturing groups
pattern = r'(?:https?://)?[\w.-]+\.[\w]+'
urls = re.findall(pattern, "Visit https://example.com or example.org")
```

## Lookahead and Lookbehind

Match positions without consuming characters:
```python
# Positive lookahead: what follows matches
re.findall(r'\d+(?= dollars)', "100 dollars, 200 dollars")
# ['100', '200']

# Negative lookahead: what follows doesn't match
re.findall(r'\d+(?! dollars)', "100 dollars, 200 euros")
# ['200']

# Positive lookbehind: what precedes matches
re.findall(r'(?<=\$)\d+', "$100 and €200")
# ['100']
```

## Practical NLP Patterns

### Email Extraction
```python
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
```

### URL Extraction
```python
urls = re.findall(r'https?://\S+|www\.\S+', text)
```

### HTML Tag Removal
```python
clean = re.sub(r'<[^>]+>', '', html_text)
```

### Whitespace Normalization
```python
clean = re.sub(r'\s+', ' ', text).strip()
```

### Number Extraction
```python
numbers = re.findall(r'\d+(?:,\d{3})*(?:\.\d+)?', text)
```

## re Module Functions

```python
import re

# Search: Find first match
match = re.search(r'\d+', 'abc123def')  # <Match '123'>

# Match: Match at start
match = re.match(r'\d+', '123abc')  # <Match '123'>

# Findall: Find all matches
matches = re.findall(r'\d+', 'a1b2c3')  # ['1', '2', '3']

# Sub: Replace matches
clean = re.sub(r'\s+', ' ', 'too   many   spaces')  # 'too many spaces'

# Split: Split by pattern
parts = re.split(r'[,;]', 'one,two;three')  # ['one', 'two', 'three']

# Compile: Pre-compile for reuse
email_pattern = re.compile(r'[\w.+-]+@[\w-]+\.[\w.]+')
emails = email_pattern.findall(text)
```

## Tips for NLP

1. **Compile patterns** you use repeatedly
2. **Use raw strings** (r'...') for regex in Python
3. **Be specific**: `\d+` is better than `[0-9]+`
4. **Test with regex101.com** before using in code
5. **For complex NLP**: Use spaCy's EntityRuler instead of regex

## Further Reading

- Python's re documentation is the official reference
- Real Python's guide is the best tutorial
- regex101.com is essential for debugging patterns
- For production NLP: combine regex with spaCy's pipeline
