---
{
  "title": "Performance and Best Practices",
  "description": "Avoid subshells, optimize loops, and follow style guides.",
  "type": "lesson",
  "order": 20,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Avoid unnecessary subshells",
    "Use printf over echo for safety",
    "Apply Bash best practices",
    "Profile slow scripts"
  ],
  "knowledge_refs": [
    "shell/shell-20-performance"
  ],
  "prerequisites": [
    "Shell-19: Shell Scripts in Practice"
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

# SHELL-20-PERFORMANCE: Performance and Best Practices

## Introduction

Avoid subshells, optimize loops, and follow style guides. By the end of this lesson you will be able to: Avoid unnecessary subshells; Use printf over echo for safety; Apply Bash best practices; Profile slow scripts.

## Key Concepts

### 1. Avoid unnecessary subshells

Target: Avoid unnecessary subshells. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
if grep -q error file; then :; fi   # no subshell
```
### 2. Use printf over echo for safety

Target: Use printf over echo for safety. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
printf "%s\\n" "safe output"
```
### 3. Apply Bash best practices

Target: Apply Bash best practices. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
result=$(( ${result:-0} + 1 ))  # fast integer math
```
### 4. Profile slow scripts

Target: Profile slow scripts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
time bash big_script.sh       # profile
```

## Practice Questions

1. What is the key idea behind "Performance and Best Practices"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Performance and Best Practices with analogies and real-world examples"
1. "Show me common mistakes beginners make with Performance and Best Practices"
1. "Provide advanced patterns and performance considerations for Performance and Best Practices"

## Key Takeaways

- Master the core ideas of Performance and Best Practices through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
