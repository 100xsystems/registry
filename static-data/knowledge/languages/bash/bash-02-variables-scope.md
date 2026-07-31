---
{
  "title": "Variables and Scoping",
  "description": "local vs global scope, quoting, export, and special parameters.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Understand local vs global scope",
    "Quote variables correctly",
    "Export variables to children",
    "Use readonly and special params"
  ],
  "knowledge_refs": [
    "bash/bash-02-variables-scope"
  ],
  "prerequisites": [
    "BASH-01"
  ],
  "references": [
    {
      "title": "Bash — Shell Parameters",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Shell-Parameters"
    },
    {
      "title": "Bash — Quoting",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Quoting"
    },
    {
      "title": "ShellCheck SC2155",
      "url": "https://www.shellcheck.net/wiki/SC2155"
    }
  ]
}
---

# BASH-02-VARIABLES-SCOPE: Variables and Scoping

## Introduction

local vs global scope, quoting, export, and special parameters. By the end of this lesson you will be able to: Understand local vs global scope; Quote variables correctly; Export variables to children; Use readonly and special params.

## Key Concepts

### 1. Understand local vs global scope

Target: Understand local vs global scope. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# Variable scoping: script-level vs function-local
greeting="Hello"                 # global
greet() {
  local name="$1"                # local to the function
  echo "$greeting, $name"
}
greet "World"
echo "greeting is still: $greeting"
# local keeps globals unclobbered — critical in big scripts
```
### 2. Quote variables correctly

Target: Quote variables correctly. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# Quoting: single vs double quotes vs no quotes
word="hello world"
echo $word        # unquoted: splits into two words
echo "$word"      # double-quoted: one word
echo '$word'      # single-quoted: literal $word
echo "path: $HOME/file with space.txt"
# Rule: always quote expansions unless you WANT splitting
```
### 3. Export variables to children

Target: Export variables to children. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# Exporting variables to child processes
export APP_ENV="production"
export API_URL="https://api.example.com"
./child.sh           # child inherits the exported vars
# Without export, child processes never see the variable:
NORMAL_VAR="hidden"
env | grep -E 'APP_ENV|NORMAL_VAR' || true
```
### 4. Use readonly and special params

Target: Use readonly and special params. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# Readonly and special shell parameters
readonly CONFIG="/etc/myapp.conf"
echo "config: $CONFIG"
echo "script name: $0"
echo "first arg: $1, arg count: $#"
echo "all args: $*"
echo "last exit: $?"
```

## Practice Questions

1. What is the key idea behind "Variables and Scoping"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variables and Scoping with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variables and Scoping"
1. "Provide advanced patterns and performance considerations for Variables and Scoping"

## Key Takeaways

- Master the core ideas of Variables and Scoping through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
