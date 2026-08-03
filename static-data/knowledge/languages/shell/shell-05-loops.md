---
{
  "title": "Loops: for, while, until",
  "description": "Iteration over lists, reading files, and loop control.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Iterate with for loops",
    "Use while and until loops",
    "Read files line by line",
    "Control loops with break and continue"
  ],
  "knowledge_refs": [
    "shell/shell-05-loops"
  ],
  "prerequisites": [
    "Shell-04: Conditionals and test"
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

# SHELL-05-LOOPS: Loops: for, while, until

## Introduction

Iteration over lists, reading files, and loop control. By the end of this lesson you will be able to: Iterate with for loops; Use while and until loops; Read files line by line; Control loops with break and continue.

## Key Concepts

### 1. Iterate with for loops

Target: Iterate with for loops. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
for file in *.txt; do
  echo "Processing $file"
done
```
### 2. Use while and until loops

Target: Use while and until loops. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
for i in {1..5}; do
  echo "Iteration $i"
done
```
### 3. Read files line by line

Target: Read files line by line. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
while read -r line; do
  echo "$line"
done < data.txt
```
### 4. Control loops with break and continue

Target: Control loops with break and continue. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
for i in {1..10}; do
  [ $((i % 2)) -eq 0 ] && continue
  echo "$i"
done
```

## Practice Questions

1. What is the key idea behind "Loops: for, while, until"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Loops: for, while, until with analogies and real-world examples"
1. "Show me common mistakes beginners make with Loops: for, while, until"
1. "Provide advanced patterns and performance considerations for Loops: for, while, until"

## Key Takeaways

- Master the core ideas of Loops: for, while, until through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
