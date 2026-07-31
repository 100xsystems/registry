---
{
  "title": "Text Processing Toolkit",
  "description": "sort, uniq, cut, wc, head, tail, xargs, join, paste, tr.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Sort and deduplicate with uniq",
    "Slice columns and lines",
    "Run commands from stdin with xargs",
    "Combine files with join and paste"
  ],
  "knowledge_refs": [
    "bash/bash-10-text-processing"
  ],
  "prerequisites": [
    "BASH-09"
  ],
  "references": [
    {
      "title": "coreutils manual",
      "url": "https://www.gnu.org/software/coreutils/manual/"
    },
    {
      "title": "xargs manual",
      "url": "https://man7.org/linux/man-pages/man1/xargs.1.html"
    },
    {
      "title": "Command Line Text Processing",
      "url": "https://learnbyexample.github.io/"
    }
  ]
}
---

# BASH-10-TEXT-PROCESSING: Text Processing Toolkit

## Introduction

sort, uniq, cut, wc, head, tail, xargs, join, paste, tr. By the end of this lesson you will be able to: Sort and deduplicate with uniq; Slice columns and lines; Run commands from stdin with xargs; Combine files with join and paste.

## Key Concepts

### 1. Sort and deduplicate with uniq

Target: Sort and deduplicate with uniq. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# sort, uniq, cut, wc
printf 'b\na\nb\n' | sort | uniq -c
printf '1,2,3\n4,5,6\n' | cut -d, -f2
printf 'hello world\n' | wc -w        # word count
# Classic pipeline: most common word
tr -s ' ' '\n' < text.txt | sort | uniq -c | sort -rn | head -5
```
### 2. Slice columns and lines

Target: Slice columns and lines. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# head, tail, and line ranges
seq 1 100 | head -3
seq 1 100 | tail -3
seq 1 100 | sed -n '10,15p'
# tail -f for live logs:
tail -f /var/log/system.log 2>/dev/null | head -2 || true
```
### 3. Run commands from stdin with xargs

Target: Run commands from stdin with xargs. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# xargs: build and run commands from stdin
printf 'a.txt\nb.txt\n' | xargs -n1 echo "processing"
find . -name "*.tmp" -print0 | xargs -0 rm -f    # null-safe
# Parallel execution with -P:
seq 1 4 | xargs -P4 -I{} sh -c 'echo running {}; sleep 1'
echo "all done"
```
### 4. Combine files with join and paste

Target: Combine files with join and paste. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# join and paste
paste -d, <(printf 'a\nb\n') <(printf '1\n2\n')
# join requires sorted inputs:
sort a.txt > a.sorted
sort b.txt > b.sorted
join a.sorted b.sorted || true
# tr: translate characters
echo "hello" | tr 'a-z' 'A-Z'
echo "a,b,c" | tr ',' '\n' 
```

## Practice Questions

1. What is the key idea behind "Text Processing Toolkit"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Text Processing Toolkit with analogies and real-world examples"
1. "Show me common mistakes beginners make with Text Processing Toolkit"
1. "Provide advanced patterns and performance considerations for Text Processing Toolkit"

## Key Takeaways

- Master the core ideas of Text Processing Toolkit through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
