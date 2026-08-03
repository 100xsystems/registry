---
{
  "title": "find and xargs",
  "description": "Find files, execute commands, and parallel processing.",
  "type": "lesson",
  "order": 18,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Search files with find criteria",
    "Execute commands with -exec",
    "Chain with xargs safely",
    "Handle spaces and special chars"
  ],
  "knowledge_refs": [
    "shell/shell-18-commands-find-xargs"
  ],
  "prerequisites": [
    "Shell-17: Environment and Configuration"
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

# SHELL-18-COMMANDS-FIND-XARGS: find and xargs

## Introduction

Find files, execute commands, and parallel processing. By the end of this lesson you will be able to: Search files with find criteria; Execute commands with -exec; Chain with xargs safely; Handle spaces and special chars.

## Key Concepts

### 1. Search files with find criteria

Target: Search files with find criteria. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
find . -name "*.py" -type f
```
### 2. Execute commands with -exec

Target: Execute commands with -exec. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
find . -name "*.log" -mtime +7 -delete
```
### 3. Chain with xargs safely

Target: Chain with xargs safely. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
find . -name "*.txt" -print0 | xargs -0 wc -l
```
### 4. Handle spaces and special chars

Target: Handle spaces and special chars. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
find . -name "*.js" -exec grep -l "console.log" {} \\;
```

## Practice Questions

1. What is the key idea behind "find and xargs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain find and xargs with analogies and real-world examples"
1. "Show me common mistakes beginners make with find and xargs"
1. "Provide advanced patterns and performance considerations for find and xargs"

## Key Takeaways

- Master the core ideas of find and xargs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
