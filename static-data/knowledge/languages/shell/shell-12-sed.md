---
{
  "title": "Text Processing with sed",
  "description": "Stream editing: substitution, deletion, and ranges.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Substitute text with s///",
    "Delete and print lines",
    "Apply sed to line ranges",
    "Edit files in place"
  ],
  "knowledge_refs": [
    "shell/shell-12-sed"
  ],
  "prerequisites": [
    "Shell-11: Job Control and Processes"
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

# SHELL-12-SED: Text Processing with sed

## Introduction

Stream editing: substitution, deletion, and ranges. By the end of this lesson you will be able to: Substitute text with s///; Delete and print lines; Apply sed to line ranges; Edit files in place.

## Key Concepts

### 1. Substitute text with s///

Target: Substitute text with s///. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
echo "hello" | sed 's/hello/hi/'
```
### 2. Delete and print lines

Target: Delete and print lines. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
sed -n '2,5p' file.txt     # print lines 2-5
```
### 3. Apply sed to line ranges

Target: Apply sed to line ranges. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
sed '/^#/d' config.ini    # drop comments
```
### 4. Edit files in place

Target: Edit files in place. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
sed -i 's/old/new/g' file.txt
```

## Practice Questions

1. What is the key idea behind "Text Processing with sed"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Text Processing with sed with analogies and real-world examples"
1. "Show me common mistakes beginners make with Text Processing with sed"
1. "Provide advanced patterns and performance considerations for Text Processing with sed"

## Key Takeaways

- Master the core ideas of Text Processing with sed through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
