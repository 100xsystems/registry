---
{
  "title": "Globbing and Regular Expressions",
  "description": "Glob patterns, extended globs, grep, sed, and awk fundamentals.",
  "type": "lesson",
  "order": 9,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Match files with glob patterns",
    "Search with grep regexes",
    "Edit streams with sed",
    "Process columns with awk"
  ],
  "knowledge_refs": [
    "bash/bash-09-globbing-regex"
  ],
  "prerequisites": [
    "BASH-08"
  ],
  "references": [
    {
      "title": "Bash — Filename Expansion",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Filename-Expansion"
    },
    {
      "title": "grep manual",
      "url": "https://man7.org/linux/man-pages/man1/grep.1.html"
    },
    {
      "title": "sed — a stream editor",
      "url": "https://www.gnu.org/software/sed/manual/sed.html"
    }
  ]
}
---

# BASH-09-GLOBBING-REGEX: Globbing and Regular Expressions

## Introduction

Glob patterns, extended globs, grep, sed, and awk fundamentals. By the end of this lesson you will be able to: Match files with glob patterns; Search with grep regexes; Edit streams with sed; Process columns with awk.

## Key Concepts

### 1. Match files with glob patterns

Target: Match files with glob patterns. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# Glob patterns
echo *.txt                # all txt files
echo file?.txt            # single char wildcard
echo file[0-9].txt        # character class
echo file[!0-9].txt       # negation
# Enable extended globs:
shopt -s extglob
echo !(backup).txt        # all txt except backup
```
### 2. Search with grep regexes

Target: Search with grep regexes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# grep: regular expression search
echo "error 42 occurred" | grep -E "error [0-9]+"
grep -i "warning" *.log || true        # case-insensitive
grep -rn "TODO" src/ | head -5         # recursive with line numbers
# Capture the matched portion with -o:
echo "key=value" | grep -oE "=.*"
```
### 3. Edit streams with sed

Target: Edit streams with sed. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# sed: stream editor basics
echo "hello world" | sed 's/world/universe/'
echo "a b c" | sed 's/ /-/g'               # global replace
printf '1\n2\n3\n' | sed -n '2p'            # print line 2
printf 'x\ny\n' | sed '/x/d'                # delete matching
sed -i.bak 's/old/new/g' file.txt           # in-place edit
```
### 4. Process columns with awk

Target: Process columns with awk. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# awk: columnar text processing
printf 'Alice 30\nBob 25\n' | awk '{print $2, $1}'   # swap columns
printf 'Alice 30\nBob 25\n' | awk '$2 > 26 {print $1}'
# With field separator:
awk -F: '{print $1}' /etc/passwd | head -3
# Sum a column:
printf '1\n2\n3\n' | awk '{s+=$1} END {print s}'   # 6
```

## Practice Questions

1. What is the key idea behind "Globbing and Regular Expressions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Globbing and Regular Expressions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Globbing and Regular Expressions"
1. "Provide advanced patterns and performance considerations for Globbing and Regular Expressions"

## Key Takeaways

- Master the core ideas of Globbing and Regular Expressions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
