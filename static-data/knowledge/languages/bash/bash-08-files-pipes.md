---
{
  "title": "Files, Pipes, and Redirection",
  "description": "Pipelines, stdout/stderr redirection, here-docs, and process substitution.",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Build pipelines with pipefail",
    "Redirect stdout and stderr",
    "Use here-documents and here-strings",
    "Leverage process substitution"
  ],
  "knowledge_refs": [
    "bash/bash-08-files-pipes"
  ],
  "prerequisites": [
    "BASH-07"
  ],
  "references": [
    {
      "title": "Bash — Pipelines",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Pipelines"
    },
    {
      "title": "Bash — Redirections",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Redirections"
    },
    {
      "title": "Here Documents",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Here-Documents"
    }
  ]
}
---

# BASH-08-FILES-PIPES: Files, Pipes, and Redirection

## Introduction

Pipelines, stdout/stderr redirection, here-docs, and process substitution. By the end of this lesson you will be able to: Build pipelines with pipefail; Redirect stdout and stderr; Use here-documents and here-strings; Leverage process substitution.

## Key Concepts

### 1. Build pipelines with pipefail

Target: Build pipelines with pipefail. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# Pipes: connect commands
cat /etc/passwd | grep "/bin/bash" | awk -F: '{print $1}'
# pipefail catches failures mid-pipeline:
set -o pipefail
false | true
echo "pipeline failed: $?"  # 1 with pipefail, 0 without
```
### 2. Redirect stdout and stderr

Target: Redirect stdout and stderr. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# Redirection: stdin, stdout, stderr
echo "stdout" > out.txt          # overwrite
echo "append" >> out.txt         # append
ls /nonexistent 2> err.txt       # stderr only
cmd > all.txt 2>&1               # both to one file
cmd &> combined.txt              # shorthand for the above
```
### 3. Use here-documents and here-strings

Target: Use here-documents and here-strings. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# Here-documents and here-strings
cat <<EOF
This is a here-doc.
Variables: $HOME expands here.
EOF
cat <<'EOF'
Literally no expansion: $HOME stays literal.
EOF
# Here-string:
grep -o "world" <<< "hello world"
```
### 4. Leverage process substitution

Target: Leverage process substitution. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# Process substitution
diff <(ls /usr/local/bin) <(ls /usr/bin) || true
# Commands run in parallel, outputs treated as files.
# Also useful to avoid subshell pitfalls:
while read -r line; do
  echo "got: $line"
done < <(printf 'a\nb\nc\n')
```

## Practice Questions

1. What is the key idea behind "Files, Pipes, and Redirection"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Files, Pipes, and Redirection with analogies and real-world examples"
1. "Show me common mistakes beginners make with Files, Pipes, and Redirection"
1. "Provide advanced patterns and performance considerations for Files, Pipes, and Redirection"

## Key Takeaways

- Master the core ideas of Files, Pipes, and Redirection through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
