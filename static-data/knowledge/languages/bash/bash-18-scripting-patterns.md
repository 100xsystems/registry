---
{
  "title": "Production Scripting Patterns",
  "description": "Library scripts, dry-run, logging, and idempotency.",
  "type": "lesson",
  "order": 18,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Structure maintainable scripts",
    "Implement dry-run mode",
    "Log with levels",
    "Make scripts idempotent"
  ],
  "knowledge_refs": [
    "bash/bash-18-scripting-patterns"
  ],
  "prerequisites": [
    "BASH-17"
  ],
  "references": [
    {
      "title": "BashGuide — Practices",
      "url": "https://mywiki.wooledge.org/BashGuide/Practices"
    },
    {
      "title": "12-factor CLI apps",
      "url": "https://clig.dev/"
    },
    {
      "title": "The Bash Hackers Wiki",
      "url": "https://wiki.bash-hackers.org/"
    }
  ]
}
---

# BASH-18-SCRIPTING-PATTERNS: Production Scripting Patterns

## Introduction

Library scripts, dry-run, logging, and idempotency. By the end of this lesson you will be able to: Structure maintainable scripts; Implement dry-run mode; Log with levels; Make scripts idempotent.

## Key Concepts

### 1. Structure maintainable scripts

Target: Structure maintainable scripts. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# The canonical "library" script pattern
#!/usr/bin/env bash
set -euo pipefail

VERSION="1.0.0"

log()  { printf '[%s] %s\n' "$(date +%H:%M:%S)" "$*"; }
info() { log "INFO  $*"; }
warn() { log "WARN  $*" >&2; }
die()  { log "FATAL $*" >&2; exit 1; }

main() {
  info "starting $0 v$VERSION"
  command -v git >/dev/null || die "git not found"
  git status >/dev/null 2>&1 || warn "not a git repo"
  info "done"
}
main "$@"
```
### 2. Implement dry-run mode

Target: Implement dry-run mode. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# Dry-run pattern: preview what would run
DRY_RUN="${DRY_RUN:-0}"
run() {
  echo "+ $*"
  if [ "$DRY_RUN" -eq 0 ]; then "$@"; fi
}
run mkdir -p /tmp/x
run echo "real work"
DRY_RUN=1
run echo "preview only"
```
### 3. Log with levels

Target: Log with levels. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# Logging with levels and a log file
LOG_FILE="${LOG_FILE:-/tmp/script.log}"
debug() { [ "${DEBUG:-0}" = "1" ] && echo "DEBUG: $*" | tee -a "$LOG_FILE"; }
info()  { echo "INFO:  $*" | tee -a "$LOG_FILE"; }
error() { echo "ERROR: $*" | tee -a "$LOG_FILE" >&2; }
DEBUG=1 debug "verbose detail"
info "step 1 complete"
error "something bad"
```
### 4. Make scripts idempotent

Target: Make scripts idempotent. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# Idempotency: safe re-runs
mkdir -p /opt/myapp                    # -p: no error if exists
[ -f /etc/myapp.conf ] || cp default.conf /etc/myapp.conf
if ! grep -q "MYAPP_ENABLED" .env 2>/dev/null; then
  echo "MYAPP_ENABLED=1" >> .env
fi
echo "re-run safe"
```

## Practice Questions

1. What is the key idea behind "Production Scripting Patterns"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Production Scripting Patterns with analogies and real-world examples"
1. "Show me common mistakes beginners make with Production Scripting Patterns"
1. "Provide advanced patterns and performance considerations for Production Scripting Patterns"

## Key Takeaways

- Master the core ideas of Production Scripting Patterns through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
