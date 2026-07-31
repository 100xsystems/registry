---
{
  "title": "Getting Started with Bash",
  "description": "Shebang, echo, variables, comments, and your first script.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write a shebang and run a script",
    "Use variables and command substitution",
    "Read user input",
    "Check command exit status"
  ],
  "knowledge_refs": [
    "bash/bash-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "GNU Bash Reference Manual",
      "url": "https://www.gnu.org/software/bash/manual/bash.html"
    },
    {
      "title": "Bash Guide (TLDP)",
      "url": "https://tldp.org/LDP/abs/html/"
    },
    {
      "title": "ShellCheck",
      "url": "https://www.shellcheck.net/"
    }
  ]
}
---

# BASH-01-GETTING-STARTED: Getting Started with Bash

## Introduction

Shebang, echo, variables, comments, and your first script. By the end of this lesson you will be able to: Write a shebang and run a script; Use variables and command substitution; Read user input; Check command exit status.

## Key Concepts

### 1. Write a shebang and run a script

Target: Write a shebang and run a script. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# Your first Bash script: shebang, echo, and comments
echo "Hello, 100X Systems!"
echo "Running with bash $BASH_VERSION"
# This line is a comment — the shell ignores it
echo "Done."
# run: bash hello.sh  (or chmod +x hello.sh && ./hello.sh)
```
### 2. Use variables and command substitution

Target: Use variables and command substitution. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# Variables: assignment, expansion, and word splitting
name="Alice"
echo "Hello, $name"          # quoted expansion: safe
echo "Hello, ${name}!"       # braces disambiguate
echo "count: $(wc -l < /etc/hostname)"   # command substitution
echo 'Literal $name'          # single quotes: no expansion
```
### 3. Read user input

Target: Read user input. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# Reading user input
read -rp "What is your name? " name
read -rp "How old are you? " age
echo "Nice to meet you, $name ($age years)."
if (( age >= 18 )); then
  echo "You are an adult."
else
  echo "You are a minor."
fi
```
### 4. Check command exit status

Target: Check command exit status. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# Checking a command succeeded with $?
mkdir -p /tmp/demo
cd /tmp/demo || { echo "cd failed"; exit 1; }
echo "hello" > file.txt
if [ -f file.txt ]; then
  echo "file.txt exists with $(wc -c < file.txt) bytes"
fi
cd - >/dev/null
```

## Practice Questions

1. What is the key idea behind "Getting Started with Bash"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Bash with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Bash"
1. "Provide advanced patterns and performance considerations for Getting Started with Bash"

## Key Takeaways

- Master the core ideas of Getting Started with Bash through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
