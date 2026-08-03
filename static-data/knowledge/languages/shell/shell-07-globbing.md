---
{
  "title": "Globbing and Pattern Matching",
  "description": "Filename expansion, wildcards, and extglob patterns.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use *, ?, and [] wildcards",
    "Prevent expansion with quoting",
    "Use extglob patterns",
    "Work with nullglob and dotglob"
  ],
  "knowledge_refs": [
    "shell/shell-07-globbing"
  ],
  "prerequisites": [
    "Shell-06: Functions"
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

# SHELL-07-GLOBBING: Globbing and Pattern Matching

## Introduction

Filename expansion, wildcards, and extglob patterns. By the end of this lesson you will be able to: Use *, ?, and [] wildcards; Prevent expansion with quoting; Use extglob patterns; Work with nullglob and dotglob.

## Key Concepts

### 1. Use *, ?, and [] wildcards

Target: Use *, ?, and [] wildcards. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
echo *.log            # all .log files
ls -d dir*            # dirs starting with dir
```
### 2. Prevent expansion with quoting

Target: Prevent expansion with quoting. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
echo "*.log"          # literal asterisk
```
### 3. Use extglob patterns

Target: Use extglob patterns. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
shopt -s extglob
rm !(*.txt)        # everything except .txt
```
### 4. Work with nullglob and dotglob

Target: Work with nullglob and dotglob. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
shopt -s nullglob
files=(*.nomatch)
echo "Count: ${#files[@]}"
```

## Practice Questions

1. What is the key idea behind "Globbing and Pattern Matching"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Globbing and Pattern Matching with analogies and real-world examples"
1. "Show me common mistakes beginners make with Globbing and Pattern Matching"
1. "Provide advanced patterns and performance considerations for Globbing and Pattern Matching"

## Key Takeaways

- Master the core ideas of Globbing and Pattern Matching through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
