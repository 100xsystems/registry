---
{
  "title": "Shell Scripts in Practice",
  "description": "Real CLI tools: argument parsing and help text.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Parse flags with getopts",
    "Write help and usage text",
    "Validate inputs robustly",
    "Structure a production script"
  ],
  "knowledge_refs": [
    "shell/shell-19-scripts-in-practice"
  ],
  "prerequisites": [
    "Shell-18: find and xargs"
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

# SHELL-19-SCRIPTS-IN-PRACTICE: Shell Scripts in Practice

## Introduction

Real CLI tools: argument parsing and help text. By the end of this lesson you will be able to: Parse flags with getopts; Write help and usage text; Validate inputs robustly; Structure a production script.

## Key Concepts

### 1. Parse flags with getopts

Target: Parse flags with getopts. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
while getopts "hv" opt; do
  case $opt in
    h) echo "Help!" ;;
    v) echo "v1.0.0" ;;
  esac
done
```
### 2. Write help and usage text

Target: Write help and usage text. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
usage() {
  echo "Usage: $0 [-v] file"
  exit 1
}
[ $# -lt 1 ] && usage
```
### 3. Validate inputs robustly

Target: Validate inputs robustly. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
[[ "$1" =~ ^- ]] && { echo "Bad flag: $1"; exit 1; }
```
### 4. Structure a production script

Target: Structure a production script. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
log() { echo "[$(date +%T)] $*"; }
log "started deploy"
```

## Practice Questions

1. What is the key idea behind "Shell Scripts in Practice"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Shell Scripts in Practice with analogies and real-world examples"
1. "Show me common mistakes beginners make with Shell Scripts in Practice"
1. "Provide advanced patterns and performance considerations for Shell Scripts in Practice"

## Key Takeaways

- Master the core ideas of Shell Scripts in Practice through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
