---
{
  "title": "Text Processing with awk",
  "description": "Column extraction, conditions, and summary reports.",
  "type": "lesson",
  "order": 13,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Print selected columns",
    "Filter rows with conditions",
    "Use BEGIN/END blocks",
    "Accumulate sums and counts"
  ],
  "knowledge_refs": [
    "shell/shell-13-awk"
  ],
  "prerequisites": [
    "Shell-12: Text Processing with sed"
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

# SHELL-13-AWK: Text Processing with awk

## Introduction

Column extraction, conditions, and summary reports. By the end of this lesson you will be able to: Print selected columns; Filter rows with conditions; Use BEGIN/END blocks; Accumulate sums and counts.

## Key Concepts

### 1. Print selected columns

Target: Print selected columns. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
echo "alice 90" | awk '{print $1}'
```
### 2. Filter rows with conditions

Target: Filter rows with conditions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
awk '$2 > 80 {print $1}' grades.txt
```
### 3. Use BEGIN/END blocks

Target: Use BEGIN/END blocks. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
awk 'BEGIN {print "Report"} {print} END {print "Done"}' file.txt
```
### 4. Accumulate sums and counts

Target: Accumulate sums and counts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
awk '{sum += $2; n++} END {print "avg:", sum/n}' data.txt
```

## Practice Questions

1. What is the key idea behind "Text Processing with awk"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Text Processing with awk with analogies and real-world examples"
1. "Show me common mistakes beginners make with Text Processing with awk"
1. "Provide advanced patterns and performance considerations for Text Processing with awk"

## Key Takeaways

- Master the core ideas of Text Processing with awk through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
