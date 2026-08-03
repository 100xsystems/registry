---
{
  "title": "Advanced Parameter Expansion",
  "description": "Defaults, indirection, and case modification.",
  "type": "lesson",
  "order": 15,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Provide default values ${var:-x}",
    "Use indirection ${!name}",
    "Handle unset variables strictly",
    "Transform with ${var^} and friends"
  ],
  "knowledge_refs": [
    "shell/shell-15-parameter-expansion"
  ],
  "prerequisites": [
    "Shell-14: Regular Expressions with grep"
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

# SHELL-15-PARAMETER-EXPANSION: Advanced Parameter Expansion

## Introduction

Defaults, indirection, and case modification. By the end of this lesson you will be able to: Provide default values ${var:-x}; Use indirection ${!name}; Handle unset variables strictly; Transform with ${var^} and friends.

## Key Concepts

### 1. Provide default values ${var:-x}

Target: Provide default values ${var:-x}. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
echo "${PORT:-8080}"     # default when unset
```
### 2. Use indirection ${!name}

Target: Use indirection ${!name}. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
name="PORT"
echo "${!name}"   # indirection
```
### 3. Handle unset variables strictly

Target: Handle unset variables strictly. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
set -u
echo "$UNDEFINED"   # errors on unset
```
### 4. Transform with ${var^} and friends

Target: Transform with ${var^} and friends. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
word="hello"
echo "${word^}"   # Hello
echo "${word^^}"  # HELLO
```

## Practice Questions

1. What is the key idea behind "Advanced Parameter Expansion"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Advanced Parameter Expansion with analogies and real-world examples"
1. "Show me common mistakes beginners make with Advanced Parameter Expansion"
1. "Provide advanced patterns and performance considerations for Advanced Parameter Expansion"

## Key Takeaways

- Master the core ideas of Advanced Parameter Expansion through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
