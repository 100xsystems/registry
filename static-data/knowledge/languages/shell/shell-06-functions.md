---
{
  "title": "Functions",
  "description": "Define, call, and scope functions with arguments.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define and call functions",
    "Pass arguments with $1 $2",
    "Return values and use local vars",
    "Structure scripts with helpers"
  ],
  "knowledge_refs": [
    "shell/shell-06-functions"
  ],
  "prerequisites": [
    "Shell-05: Loops: for, while, until"
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

# SHELL-06-FUNCTIONS: Functions

## Introduction

Define, call, and scope functions with arguments. By the end of this lesson you will be able to: Define and call functions; Pass arguments with $1 $2; Return values and use local vars; Structure scripts with helpers.

## Key Concepts

### 1. Define and call functions

Target: Define and call functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
greet() {
  echo "Hello, $1!"
}
greet "World"
```
### 2. Pass arguments with $1 $2

Target: Pass arguments with $1 $2. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
add() {
  local sum=$(( $1 + $2 ))
  echo "$sum"
}
result=$(add 4 5)
echo "Sum: $result"
```
### 3. Return values and use local vars

Target: Return values and use local vars. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
is_file() {
  [ -f "$1" ]
}
if is_file "notes.md"; then
  echo "It exists"
fi
```
### 4. Structure scripts with helpers

Target: Structure scripts with helpers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
main() {
  local who="${1:-stranger}"
  echo "Hi, $who"
}
main "Ada"
```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
