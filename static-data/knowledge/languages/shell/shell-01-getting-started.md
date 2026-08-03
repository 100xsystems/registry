---
{
  "title": "Getting Started with Shell Scripting",
  "description": "Shebang, echo, permissions, and your first script.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write a script with a proper shebang",
    "Make a script executable with chmod",
    "Use echo and comments effectively",
    "Run a script from any directory"
  ],
  "knowledge_refs": [
    "shell/shell-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# SHELL-01-GETTING-STARTED: Getting Started with Shell Scripting

## Introduction

Shebang, echo, permissions, and your first script. By the end of this lesson you will be able to: Write a script with a proper shebang; Make a script executable with chmod; Use echo and comments effectively; Run a script from any directory.

## Key Concepts

### 1. Write a script with a proper shebang

Target: Write a script with a proper shebang. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# Hello from 100X Systems!
echo "Hello, World!"
```
### 2. Make a script executable with chmod

Target: Make a script executable with chmod. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# run with: bash hello.sh
echo "Hello, $USER!"
```
### 3. Use echo and comments effectively

Target: Use echo and comments effectively. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
chmod +x hello.sh
./hello.sh   # execute directly
```
### 4. Run a script from any directory

Target: Run a script from any directory. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
echo "Date: $(date)"
echo "Shell: $SHELL"
```

## Practice Questions

1. What is the key idea behind "Getting Started with Shell Scripting"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Shell Scripting with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Shell Scripting"
1. "Provide advanced patterns and performance considerations for Getting Started with Shell Scripting"

## Key Takeaways

- Master the core ideas of Getting Started with Shell Scripting through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
