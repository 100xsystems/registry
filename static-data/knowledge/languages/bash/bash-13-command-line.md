---
{
  "title": "Command-Line Argument Parsing",
  "description": "Positional params, getopts, shift, and flag loops.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use positional parameters",
    "Parse options with getopts",
    "Shift through arguments",
    "Handle flags with case loops"
  ],
  "knowledge_refs": [
    "bash/bash-13-command-line"
  ],
  "prerequisites": [
    "BASH-12"
  ],
  "references": [
    {
      "title": "Bash — Positional Parameters",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Positional-Parameters"
    },
    {
      "title": "getopts builtin",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#index-getopts"
    },
    {
      "title": "BashGuide — Parameters",
      "url": "https://mywiki.wooledge.org/BashGuide/Parameters"
    }
  ]
}
---

# BASH-13-COMMAND-LINE: Command-Line Argument Parsing

## Introduction

Positional params, getopts, shift, and flag loops. By the end of this lesson you will be able to: Use positional parameters; Parse options with getopts; Shift through arguments; Handle flags with case loops.

## Key Concepts

### 1. Use positional parameters

Target: Use positional parameters. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# Positional parameters and defaults
script() {
  local name="${1:-world}"
  local count="${2:-1}"
  for (( i = 0; i < count; i++ )); do
    echo "hello $name"
  done
}
script
script "Bash" 2
```
### 2. Parse options with getopts

Target: Parse options with getopts. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# getopts: standard option parsing
usage() { echo "Usage: $0 -n NAME [-v]" >&2; exit 1; }
name=""
verbose=0
while getopts "n:v" opt; do
  case "$opt" in
    n) name="$OPTARG" ;;
    v) verbose=1 ;;
    *) usage ;;
  esac
done
shift $((OPTIND - 1))
echo "name=$name verbose=$verbose rest=$*"
```
### 3. Shift through arguments

Target: Shift through arguments. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# shift: walking positional arguments
process() {
  while [ $# -gt 0 ]; do
    echo "arg: $1"
    shift
  done
}
process a b c
# Extract a range:
echo "arg2..3: ${@:2:2}"
```
### 4. Handle flags with case loops

Target: Handle flags with case loops. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# Parsing flags with a case-based loop
verbose=false
debug=false
for arg in "$@"; do
  case "$arg" in
    -v|--verbose) verbose=true ;;
    -d|--debug)   debug=true ;;
    *)            echo "unknown: $arg" ;;
  esac
done
$verbose && echo "verbose mode"
$debug && echo "debug mode"
```

## Practice Questions

1. What is the key idea behind "Command-Line Argument Parsing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Command-Line Argument Parsing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Command-Line Argument Parsing"
1. "Provide advanced patterns and performance considerations for Command-Line Argument Parsing"

## Key Takeaways

- Master the core ideas of Command-Line Argument Parsing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
