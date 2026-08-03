---
{
  "title": "Conditionals and test",
  "description": "if/elif/else, test brackets [ ], and compound conditions.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write if/elif/else branches",
    "Use [ ] and [[ ]] test expressions",
    "Test files, strings, and numbers",
    "Combine conditions with && || !"
  ],
  "knowledge_refs": [
    "shell/shell-04-conditionals"
  ],
  "prerequisites": [
    "Shell-03: Arithmetic and Exit Status"
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

# SHELL-04-CONDITIONALS: Conditionals and test

## Introduction

if/elif/else, test brackets [ ], and compound conditions. By the end of this lesson you will be able to: Write if/elif/else branches; Use [ ] and [[ ]] test expressions; Test files, strings, and numbers; Combine conditions with && || !.

## Key Concepts

### 1. Write if/elif/else branches

Target: Write if/elif/else branches. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
if [ "$1" = "start" ]; then
  echo "Starting..."
elif [ "$1" = "stop" ]; then
  echo "Stopping..."
else
  echo "Usage: $0 start|stop"
fi
```
### 2. Use [ ] and [[ ]] test expressions

Target: Use [ ] and [[ ]] test expressions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
if [ -f "config.yml" ]; then
  echo "Config exists"
fi
```
### 3. Test files, strings, and numbers

Target: Test files, strings, and numbers. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
if [[ "$name" == A* ]]; then
  echo "Matches A*"
fi
```
### 4. Combine conditions with && || !

Target: Combine conditions with && || !. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
if [ "$x" -gt 10 ] && [ "$x" -lt 20 ]; then
  echo "Between 10 and 20"
fi
```

## Practice Questions

1. What is the key idea behind "Conditionals and test"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Conditionals and test with analogies and real-world examples"
1. "Show me common mistakes beginners make with Conditionals and test"
1. "Provide advanced patterns and performance considerations for Conditionals and test"

## Key Takeaways

- Master the core ideas of Conditionals and test through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
