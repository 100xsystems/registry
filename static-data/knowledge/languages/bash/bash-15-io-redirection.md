---
{
  "title": "Advanced I/O and Redirection",
  "description": "File descriptors, /dev/null, safe file reads, and named pipes.",
  "type": "lesson",
  "order": 15,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Manipulate file descriptors",
    "Use /dev/null and /dev/zero",
    "Read files safely with while-read",
    "Build FIFOs and named pipes"
  ],
  "knowledge_refs": [
    "bash/bash-15-io-redirection"
  ],
  "prerequisites": [
    "BASH-14"
  ],
  "references": [
    {
      "title": "Bash — Redirections",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Redirections"
    },
    {
      "title": "File descriptor overview",
      "url": "https://en.wikipedia.org/wiki/File_descriptor"
    },
    {
      "title": "mkfifo manual",
      "url": "https://man7.org/linux/man-pages/man1/mkfifo.1.html"
    }
  ]
}
---

# BASH-15-IO-REDIRECTION: Advanced I/O and Redirection

## Introduction

File descriptors, /dev/null, safe file reads, and named pipes. By the end of this lesson you will be able to: Manipulate file descriptors; Use /dev/null and /dev/zero; Read files safely with while-read; Build FIFOs and named pipes.

## Key Concepts

### 1. Manipulate file descriptors

Target: Manipulate file descriptors. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# File descriptor gymnastics
exec 3<> /tmp/fd3.txt        # open read/write
echo "written via fd3" >&3
exec 3>&-                    # close fd3
cat /tmp/fd3.txt
# Duplicate descriptors:
exec 4>&1                    # save stdout
exec 1> /tmp/capture.txt     # redirect stdout
echo "this is captured"
exec 1>&4                    # restore stdout
echo "this is visible again"
```
### 2. Use /dev/null and /dev/zero

Target: Use /dev/null and /dev/zero. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# /dev/null and /dev/zero
# Discard output:
command -v nonexistent >/dev/null 2>&1 || echo "not found"
# Provide infinite zeros:
head -c 10 /dev/zero | wc -c
# /dev/null as a sink:
curl -s https://example.com >/dev/null 2>&1 || true
echo "done"
```
### 3. Read files safely with while-read

Target: Read files safely with while-read. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# Reading files with while-read (safe pattern)
while IFS= read -r line; do
  echo "line: $line"
done < file.txt
# Avoid the classic pipe-subshell bug:
# BAD:  cat file.txt | while read ...  (runs in subshell)
# GOOD: while read ... < file.txt      (same shell)
```
### 4. Build FIFOs and named pipes

Target: Build FIFOs and named pipes. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# FIFOs and named pipes
mkfifo /tmp/mypipe
# writer in background
(echo "through the pipe" > /tmp/mypipe) &
# reader blocks until a writer connects
read -r msg < /tmp/mypipe
echo "received: $msg"
rm -f /tmp/mypipe
```

## Practice Questions

1. What is the key idea behind "Advanced I/O and Redirection"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Advanced I/O and Redirection with analogies and real-world examples"
1. "Show me common mistakes beginners make with Advanced I/O and Redirection"
1. "Provide advanced patterns and performance considerations for Advanced I/O and Redirection"

## Key Takeaways

- Master the core ideas of Advanced I/O and Redirection through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
