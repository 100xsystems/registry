---
{
  "title": "Arithmetic and Exit Status",
  "description": "Integer math, command substitution, and exit codes.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Perform arithmetic with $(( ))",
    "Capture command output with $( )",
    "Check and use exit statuses",
    "Chain commands with && and ||"
  ],
  "knowledge_refs": [
    "shell/shell-03-arithmetic"
  ],
  "prerequisites": [
    "Shell-02: Variables and Expansion"
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

# SHELL-03-ARITHMETIC: Arithmetic and Exit Status

## Introduction

Integer math, command substitution, and exit codes. By the end of this lesson you will be able to: Perform arithmetic with $(( )); Capture command output with $( ); Check and use exit statuses; Chain commands with && and ||.

## Key Concepts

### 1. Perform arithmetic with $(( ))

Target: Perform arithmetic with $(( )). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
a=10
b=3
echo $((a + b)) $((a * b)) $((a / b))
```
### 2. Capture command output with $( )

Target: Capture command output with $( ). Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
files=$(ls | wc -l)
echo "Files: $files"
```
### 3. Check and use exit statuses

Target: Check and use exit statuses. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
grep "error" app.log && echo "Found" || echo "Clean"
```
### 4. Chain commands with && and ||

Target: Chain commands with && and ||. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
command_that_fails; echo "exit: $?"
```

## Practice Questions

1. What is the key idea behind "Arithmetic and Exit Status"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arithmetic and Exit Status with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arithmetic and Exit Status"
1. "Provide advanced patterns and performance considerations for Arithmetic and Exit Status"

## Key Takeaways

- Master the core ideas of Arithmetic and Exit Status through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
