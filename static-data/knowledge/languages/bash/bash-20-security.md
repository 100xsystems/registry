---
{
  "title": "Security",
  "description": "Quoting against injection, shellcheck, secrets, and privilege checks.",
  "type": "lesson",
  "order": 20,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Prevent injection with quoting",
    "Apply shellcheck rules",
    "Handle secrets safely",
    "Check privileges and temp files"
  ],
  "knowledge_refs": [
    "bash/bash-20-security"
  ],
  "prerequisites": [
    "BASH-19"
  ],
  "references": [
    {
      "title": "ShellCheck wiki",
      "url": "https://www.shellcheck.net/wiki/"
    },
    {
      "title": "OWASP Shell Injection",
      "url": "https://owasp.org/www-community/attacks/Command_Injection"
    },
    {
      "title": "mktemp manual",
      "url": "https://man7.org/linux/man-pages/man1/mktemp.1.html"
    }
  ]
}
---

# BASH-20-SECURITY: Security

## Introduction

Quoting against injection, shellcheck, secrets, and privilege checks. By the end of this lesson you will be able to: Prevent injection with quoting; Apply shellcheck rules; Handle secrets safely; Check privileges and temp files.

## Key Concepts

### 1. Prevent injection with quoting

Target: Prevent injection with quoting. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# Quoting is security: the injection lesson
filename="user input; rm -rf /"
# BAD:  eval "ls $filename"       # executes the rm!
# GOOD: never eval user input
# Quoting prevents word-splitting/globbing surprises:
safe="a b*c"
echo "$safe"                # literal
printf '%s\n' "$safe"
echo "quoted properly"
```
### 2. Apply shellcheck rules

Target: Apply shellcheck rules. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# shellcheck: static analysis (install separately)
# shellcheck disable=SC2086   # when you intentionally split
# SC2086 is "double quote to prevent globbing/word splitting"
name="Alice"
echo "$name"                 # fixed: quoted
# Check scripts with: shellcheck myscript.sh
echo "run shellcheck on your scripts!"
```
### 3. Handle secrets safely

Target: Handle secrets safely. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# Reading secrets without leaking them
# NEVER: pass secrets via argv (visible in `ps`)
# Use stdin or env:
read -r -s -p "Password: " secret
echo
echo "received ${#secret} chars (not shown)"
# Prefer secret managers; avoid echo-ing secrets:
printf '%s\n' "${secret//?/*}"   # mask: *****
```
### 4. Check privileges and temp files

Target: Check privileges and temp files. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# Privilege checks and safe temp files
if [ "$(id -u)" -ne 0 ]; then
  echo "not root" >&2
fi
# Safe temp files:
tmp=$(mktemp /tmp/app.XXXXXX)
trap 'rm -f "$tmp"' EXIT
echo "temp file: $tmp"
# mktemp -d for directories; never guess names in /tmp
```

## Practice Questions

1. What is the key idea behind "Security"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Security with analogies and real-world examples"
1. "Show me common mistakes beginners make with Security"
1. "Provide advanced patterns and performance considerations for Security"

## Key Takeaways

- Master the core ideas of Security through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
