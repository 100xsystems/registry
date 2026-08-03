---
{
  "title": "Variables and Expansion",
  "description": "Assignment, quoting, parameter expansion, and special variables.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Assign and reference variables",
    "Quote with single, double, and backticks",
    "Use special parameters $0 $# $@",
    "Apply parameter expansion patterns"
  ],
  "knowledge_refs": [
    "shell/shell-02-variables"
  ],
  "prerequisites": [
    "Shell-01: Getting Started with Shell Scripting"
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

# SHELL-02-VARIABLES: Variables and Expansion

## Introduction

Assignment, quoting, parameter expansion, and special variables. By the end of this lesson you will be able to: Assign and reference variables; Quote with single, double, and backticks; Use special parameters $0 $# $@; Apply parameter expansion patterns.

## Key Concepts

### 1. Assign and reference variables

Target: Assign and reference variables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
name="Ada"
echo "Hello, $name"
```
### 2. Quote with single, double, and backticks

Target: Quote with single, double, and backticks. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
echo "Double quotes: $HOME"
echo 'Single quotes: $HOME'
```
### 3. Use special parameters $0 $# $@

Target: Use special parameters $0 $# $@. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
echo "Script: $0"
echo "Args: $#"
echo "All: $@"
```
### 4. Apply parameter expansion patterns

Target: Apply parameter expansion patterns. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
file="report.pdf"
echo "${file%.pdf}.txt"   # strip suffix
```

## Practice Questions

1. What is the key idea behind "Variables and Expansion"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Expansion with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Expansion"
1. "Provide advanced patterns and performance considerations for Variables and Expansion"

## Key Takeaways

- Master the core ideas of Variables and Expansion through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
