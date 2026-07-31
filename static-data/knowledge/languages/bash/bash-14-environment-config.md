---
{
  "title": "Environment and Configuration",
  "description": "Env vars, exports, dotfiles, sourcing, and shell modes.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read and set environment variables",
    "Export to child processes",
    "Manage dotfiles and sourcing",
    "Detect shell interaction modes"
  ],
  "knowledge_refs": [
    "bash/bash-14-environment-config"
  ],
  "prerequisites": [
    "BASH-13"
  ],
  "references": [
    {
      "title": "Bash — Bash Startup Files",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Bash-Startup-Files"
    },
    {
      "title": "Environment Variables",
      "url": "https://man7.org/linux/man-pages/man7/environ.7.html"
    },
    {
      "title": "Dotfiles guide",
      "url": "https://dotfiles.github.io/"
    }
  ]
}
---

# BASH-14-ENVIRONMENT-CONFIG: Environment and Configuration

## Introduction

Env vars, exports, dotfiles, sourcing, and shell modes. By the end of this lesson you will be able to: Read and set environment variables; Export to child processes; Manage dotfiles and sourcing; Detect shell interaction modes.

## Key Concepts

### 1. Read and set environment variables

Target: Read and set environment variables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# Environment variables: reading and defaults
echo "HOME=$HOME"
echo "USER=$USER"
echo "PWD=$PWD"
: "${EDITOR:=vi}"        # set default if unset
echo "editor: $EDITOR"
# List all exported env vars:
env | head -5
```
### 2. Export to child processes

Target: Export to child processes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# Exporting for child processes
export DEBUG=1
export PATH="$PATH:$HOME/bin"
run_child() {
  # child sees the inherited environment
  echo "child sees DEBUG=$DEBUG and PATH=$PATH"
}
run_child
# Scope: exports in a subshell do NOT leak out
(
  export TEMP_ONLY=1
  echo "inside subshell: $TEMP_ONLY"
)
echo "outside: ${TEMP_ONLY:-unset}"
```
### 3. Manage dotfiles and sourcing

Target: Manage dotfiles and sourcing. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# Dotfiles and sourcing
# ~/.bashrc, ~/.bash_profile load environment at startup.
# Source a config file (runs it in THIS shell):
# shellcheck disable=SC1090
source "$HOME/.myenv" 2>/dev/null || echo "no .myenv"
# Difference: source vs executing
#   source ./x.sh   -> runs in current shell (vars persist)
#   ./x.sh          -> runs in subshell (vars lost)
```
### 4. Detect shell interaction modes

Target: Detect shell interaction modes. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# Interactive vs non-interactive shell detection
if [[ $- == *i* ]]; then
  echo "interactive shell"
else
  echo "non-interactive (script) shell"
fi
# Bash startup files differ by mode:
#   login interactive: .bash_profile
#   non-login interactive: .bashrc
#   non-interactive: $BASH_ENV
```

## Practice Questions

1. What is the key idea behind "Environment and Configuration"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Environment and Configuration with analogies and real-world examples"
1. "Show me common mistakes beginners make with Environment and Configuration"
1. "Provide advanced patterns and performance considerations for Environment and Configuration"

## Key Takeaways

- Master the core ideas of Environment and Configuration through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
