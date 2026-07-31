---
{
  "title": "Error Handling",
  "description": "set -euo pipefail, trap, robust patterns, and exit codes.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Exit on errors with set -e",
    "Clean up with trap",
    "Apply robust error patterns",
    "Handle exit codes explicitly"
  ],
  "knowledge_refs": [
    "bash/bash-11-error-handling"
  ],
  "prerequisites": [
    "BASH-10"
  ],
  "references": [
    {
      "title": "Bash — The Set Builtin",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#The-Set-Builtin"
    },
    {
      "title": "BashGuide — Error Handling",
      "url": "https://mywiki.wooledge.org/BashGuide/Practices"
    },
    {
      "title": "ShellCheck — useful patterns",
      "url": "https://www.shellcheck.net/wiki/"
    }
  ]
}
---

# BASH-11-ERROR-HANDLING: Error Handling

## Introduction

set -euo pipefail, trap, robust patterns, and exit codes. By the end of this lesson you will be able to: Exit on errors with set -e; Clean up with trap; Apply robust error patterns; Handle exit codes explicitly.

## Key Concepts

### 1. Exit on errors with set -e

Target: Exit on errors with set -e. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# set -e: exit on first error
set -e
echo "before error"
false
echo "this never runs"   # set -e stops here
```
### 2. Clean up with trap

Target: Clean up with trap. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# trap: cleanup on exit and signals
cleanup() {
  rm -f /tmp/lockfile
  echo "cleaned up"
}
trap cleanup EXIT
trap 'echo "interrupted"; exit 1' INT TERM
echo "work in progress..."
sleep 2
# Ctrl-C or normal exit both run cleanup
```
### 3. Apply robust error patterns

Target: Apply robust error patterns. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# Robust error handling patterns
set -euo pipefail       # -e exit, -u unset vars, pipefail
die() { echo "FATAL: $*" >&2; exit 1; }
[ -n "${REQUIRED_VAR:-}" ] || die "REQUIRED_VAR not set"
command -v curl || die "curl is required"
curl -fsSL https://example.com/data.json -o data.json \
  || die "download failed"
echo "download OK"
```
### 4. Handle exit codes explicitly

Target: Handle exit codes explicitly. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# Exit codes and $? handling
run_or_fallback() {
  if "$@"; then
    return 0
  else
    echo "WARN: $* failed (exit $?)" >&2
    return 1
  fi
}
run_or_fallback true
run_or_fallback false || echo "caught the failure"
# 0 = success; non-zero = failure — always check!
```

## Practice Questions

1. What is the key idea behind "Error Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Error Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Error Handling"
1. "Provide advanced patterns and performance considerations for Error Handling"

## Key Takeaways

- Master the core ideas of Error Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
