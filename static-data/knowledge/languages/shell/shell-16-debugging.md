---
{
  "title": "Debugging and Error Handling",
  "description": "set -euxo, tracing, and defensive scripting.",
  "type": "lesson",
  "order": 16,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Trace execution with set -x",
    "Exit on errors with set -e",
    "Use set -u and pipefail",
    "Write fail-fast scripts"
  ],
  "knowledge_refs": [
    "shell/shell-16-debugging"
  ],
  "prerequisites": [
    "Shell-15: Advanced Parameter Expansion"
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

# SHELL-16-DEBUGGING: Debugging and Error Handling

## Introduction

set -euxo, tracing, and defensive scripting. By the end of this lesson you will be able to: Trace execution with set -x; Exit on errors with set -e; Use set -u and pipefail; Write fail-fast scripts.

## Key Concepts

### 1. Trace execution with set -x

Target: Trace execution with set -x. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
set -euo pipefail
echo "Safe script starts"
```
### 2. Exit on errors with set -e

Target: Exit on errors with set -e. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
bash -x script.sh    # trace every command
```
### 3. Use set -u and pipefail

Target: Use set -u and pipefail. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
set -e
false
echo "never reached"
```
### 4. Write fail-fast scripts

Target: Write fail-fast scripts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
trap 'echo "Failed at $LINENO"' ERR
```

## Practice Questions

1. What is the key idea behind "Debugging and Error Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Debugging and Error Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Debugging and Error Handling"
1. "Provide advanced patterns and performance considerations for Debugging and Error Handling"

## Key Takeaways

- Master the core ideas of Debugging and Error Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
