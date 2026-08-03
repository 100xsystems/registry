---
{
  "title": "Regular Expressions with grep",
  "description": "grep patterns, extended regex, and ripgrep alternatives.",
  "type": "lesson",
  "order": 14,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Search with grep and egrep",
    "Use character classes and anchors",
    "Extract matches with -o",
    "Count and invert matches"
  ],
  "knowledge_refs": [
    "shell/shell-14-regex"
  ],
  "prerequisites": [
    "Shell-13: Text Processing with awk"
  ],
  "references": [
    {
      "title": "GNU Bash Reference Manual",
      "url": "https://www.gnu.org/software/bash/manual/bash.html",
      "description": "The authoritative Bash reference"
    },
    {
      "title": "ShellCheck",
      "url": "https://www.shellcheck.net/",
      "description": "Static analysis for shell scripts"
    },
    {
      "title": "BashGuide (Bash Hackers Wiki)",
      "url": "https://wiki.bash-hackers.org/",
      "description": "Practical Bash wiki"
    },
    {
      "title": "Explain Shell",
      "url": "https://explainshell.com/",
      "description": "Break down any command line"
    }
  ]
}
---

# SHELL-14-REGEX: Regular Expressions with grep

## Introduction

grep patterns, extended regex, and ripgrep alternatives. By the end of this lesson you will be able to: Search with grep and egrep; Use character classes and anchors; Extract matches with -o; Count and invert matches.

## Key Concepts

### 1. Search with grep and egrep

Target: Search with grep and egrep. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
grep "error" app.log
```
### 2. Use character classes and anchors

Target: Use character classes and anchors. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
grep -E "^[0-9]{3}-" phones.txt
```
### 3. Extract matches with -o

Target: Extract matches with -o. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
grep -oE "[a-z]+@[a-z]+\\.com" emails.txt
```
### 4. Count and invert matches

Target: Count and invert matches. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
grep -c "TODO" *.py && grep -L "TODO" *.py
```

## Practice Questions

1. What is the key idea behind "Regular Expressions with grep"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Regular Expressions with grep with analogies and real-world examples"
1. "Show me common mistakes beginners make with Regular Expressions with grep"
1. "Provide advanced patterns and performance considerations for Regular Expressions with grep"

## Key Takeaways

- Master the core ideas of Regular Expressions with grep through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
