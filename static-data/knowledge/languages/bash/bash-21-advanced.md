---
{
  "title": "Advanced Bash: Regex, Substitution, and Completion",
  "description": "BASH_REMATCH, process substitution tricks, completions, and checklists.",
  "type": "lesson",
  "order": 21,
  "duration": "75 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Capture with BASH_REMATCH",
    "Use /dev/fd and substitution tricks",
    "Register completion functions",
    "Apply the production checklist"
  ],
  "knowledge_refs": [
    "bash/bash-21-advanced"
  ],
  "prerequisites": [
    "BASH-20"
  ],
  "references": [
    {
      "title": "Bash — The Shopt Builtin",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#The-Shopt-Builtin"
    },
    {
      "title": "BashFAQ",
      "url": "https://mywiki.wooledge.org/BashFAQ"
    },
    {
      "title": "Programmable Completion",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Programmable-Completion"
    }
  ]
}
---

# BASH-21-ADVANCED: Advanced Bash: Regex, Substitution, and Completion

## Introduction

BASH_REMATCH, process substitution tricks, completions, and checklists. By the end of this lesson you will be able to: Capture with BASH_REMATCH; Use /dev/fd and substitution tricks; Register completion functions; Apply the production checklist.

## Key Concepts

### 1. Capture with BASH_REMATCH

Target: Capture with BASH_REMATCH. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# BASH_REMATCH: regex captures
if [[ "order-12345" =~ ^order-([0-9]+)$ ]]; then
  echo "order id: ${BASH_REMATCH[1]}"
fi
# Named capture via array indexing:
[[ "key=value" =~ ^([^=]+)=(.*)$ ]]
echo "key=${BASH_REMATCH[1]} value=${BASH_REMATCH[2]}"
```
### 2. Use /dev/fd and substitution tricks

Target: Use /dev/fd and substitution tricks. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# Process substitution tricks and /dev/fd
diff <(sort a.txt) <(sort b.txt) && echo "same content" || true
# Feed a function's output as a file argument:
echo_data() { printf 'x\ny\nz\n'; }
while read -r l; do echo "> $l"; done < <(echo_data)
```
### 3. Register completion functions

Target: Register completion functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# Bash completion hooks (for interactive shells)
# _example() { COMPREPLY=( $(compgen -W "start stop restart" -- "${COMP_WORDS[1]}") ); }
# complete -F _example myapp
# This snippet documents the pattern; completion needs an
# interactive shell to demo.
echo "completion functions registered via complete -F"
```
### 4. Apply the production checklist

Target: Apply the production checklist. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# Performance & portability checklist
set -euo pipefail
# Prefer [[ ]] over [ ], (( )) over expr, ${var//} over sed.
# Batch with awk/sed/tr once instead of per-line.
# Quote everything, never eval, shellcheck before commit.
# Profile with `time` and bash -x when debugging.
bash -n "$0" && echo "syntax check passed"
echo "advanced Bash: done"
```

## Practice Questions

1. What is the key idea behind "Advanced Bash: Regex, Substitution, and Completion"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Advanced Bash: Regex, Substitution, and Completion with analogies and real-world examples"
1. "Show me common mistakes beginners make with Advanced Bash: Regex, Substitution, and Completion"
1. "Provide advanced patterns and performance considerations for Advanced Bash: Regex, Substitution, and Completion"

## Key Takeaways

- Master the core ideas of Advanced Bash: Regex, Substitution, and Completion through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
