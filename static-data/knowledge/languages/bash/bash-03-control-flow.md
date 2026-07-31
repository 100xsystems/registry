---
{
  "title": "Control Flow",
  "description": "if/elif/else, case, and the test commands [ ], [[ ]], ( ( ) ).",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write if/elif/else branches",
    "Use case for pattern matching",
    "Distinguish [ ], [[ ]] and (( ))",
    "Chain conditions with && and ||"
  ],
  "knowledge_refs": [
    "bash/bash-03-control-flow"
  ],
  "prerequisites": [
    "BASH-02"
  ],
  "references": [
    {
      "title": "Bash — Conditional Constructs",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs"
    },
    {
      "title": "Test — man page",
      "url": "https://man7.org/linux/man-pages/man1/test.1.html"
    },
    {
      "title": "BashGuide — Tests",
      "url": "https://mywiki.wooledge.org/BashGuide/TestsAndConditionals"
    }
  ]
}
---

# BASH-03-CONTROL-FLOW: Control Flow

## Introduction

if/elif/else, case, and the test commands [ ], [[ ]], ( ( ) ). By the end of this lesson you will be able to: Write if/elif/else branches; Use case for pattern matching; Distinguish [ ], [[ ]] and (( )); Chain conditions with && and ||.

## Key Concepts

### 1. Write if/elif/else branches

Target: Write if/elif/else branches. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# if / elif / else with test brackets
score=85
if (( score >= 90 )); then
  echo "Grade: A"
elif (( score >= 75 )); then
  echo "Grade: B"
else
  echo "Grade: C or lower"
fi
```
### 2. Use case for pattern matching

Target: Use case for pattern matching. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# case statement: pattern matching
fruit="banana"
case "$fruit" in
  apple|pear) echo "tree fruit" ;;
  banana)     echo "tropical fruit" ;;
  *)          echo "unknown fruit" ;;
esac
# Note the double semicolons — required per clause
```
### 3. Distinguish [ ], [[ ]] and (( ))

Target: Distinguish [ ], [[ ]] and (( )). Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# [ ] vs [[ ]] vs (( ))
if [[ "$name" == a* ]]; then        # [[ ]] glob & regex support
  echo "starts with a"
fi
if [ -f file.txt ]; then             # [ ] POSIX: file tests
  echo "file exists"
fi
if (( 3 > 2 )); then                 # (( )) arithmetic
  echo "3 is greater than 2"
fi
```
### 4. Chain conditions with && and ||

Target: Chain conditions with && and ||. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# Logical operators: && || !
if command -v jq >/dev/null 2>&1 && command -v curl >/dev/null 2>&1; then
  echo "jq and curl are installed"
fi
error=0
if [ $error -ne 0 ]; then
  echo "error state"
else
  echo "ok"
fi
# -a / -o are deprecated; always chain with && || inside [[ ]]
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
