---
{
  "title": "Functions",
  "description": "Defining functions, arguments, return values, and reusable helpers.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define and call functions",
    "Return exit status and data",
    "Use local variables and defaults",
    "Build reusable helper functions"
  ],
  "knowledge_refs": [
    "bash/bash-05-functions"
  ],
  "prerequisites": [
    "BASH-04"
  ],
  "references": [
    {
      "title": "Bash — Shell Functions",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Shell-Functions"
    },
    {
      "title": "BashGuide — Functions",
      "url": "https://mywiki.wooledge.org/BashGuide/Functions"
    },
    {
      "title": "Advanced Bash-Scripting — Functions",
      "url": "https://tldp.org/LDP/abs/html/functions.html"
    }
  ]
}
---

# BASH-05-FUNCTIONS: Functions

## Introduction

Defining functions, arguments, return values, and reusable helpers. By the end of this lesson you will be able to: Define and call functions; Return exit status and data; Use local variables and defaults; Build reusable helper functions.

## Key Concepts

### 1. Define and call functions

Target: Define and call functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# Defining and calling functions
say_hello() {
  echo "Hello, $1!"       # $1 is the first argument
}
say_hello "World"
# Function names must be called WITHOUT parentheses
```
### 2. Return exit status and data

Target: Return exit status and data. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# Return values: exit status, not data
is_even() {
  local n="$1"
  (( n % 2 == 0 ))          # exit status is the last command
}
if is_even 4; then
  echo "4 is even"
fi
# Functions returning data use echo/printf capture:
get_user() { echo "$USER"; }
user="$(get_user)"
echo "current user: $user"
```
### 3. Use local variables and defaults

Target: Use local variables and defaults. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# local variables and argument shifting
describe() {
  local name="$1"
  local role="${2:-unknown}"    # default value
  echo "$name is a $role"
}
describe "Bash" "shell"
describe "Python"
```
### 4. Build reusable helper functions

Target: Build reusable helper functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# A reusable helper pattern with error checking
die() {
  echo "ERROR: $*" >&2
  exit 1
}
require() {
  command -v "$1" >/dev/null 2>&1 || die "missing command: $1"
}
require jq
echo "jq is available"
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
