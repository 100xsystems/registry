---
{
  "title": "Loops",
  "description": "for, while, until, break, continue, and brace expansion.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Iterate with for over lists",
    "Loop over command output",
    "Use while and until",
    "Control loops with break/continue"
  ],
  "knowledge_refs": [
    "bash/bash-04-loops"
  ],
  "prerequisites": [
    "BASH-03"
  ],
  "references": [
    {
      "title": "Bash — Looping Constructs",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs"
    },
    {
      "title": "BashGuide — Loops",
      "url": "https://mywiki.wooledge.org/BashGuide/Loops"
    },
    {
      "title": "Brace Expansion",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Brace-Expansion"
    }
  ]
}
---

# BASH-04-LOOPS: Loops

## Introduction

for, while, until, break, continue, and brace expansion. By the end of this lesson you will be able to: Iterate with for over lists; Loop over command output; Use while and until; Control loops with break/continue.

## Key Concepts

### 1. Iterate with for over lists

Target: Iterate with for over lists. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# for loop over a list
for color in red green blue; do
  echo "color: $color"
done
# brace expansion produces the list:
for n in {1..5}; do
  echo "number $n"
done
```
### 2. Loop over command output

Target: Loop over command output. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# for loop with command output and C-style arithmetic
for file in *.txt; do
  echo "processing $file"
done
for (( i = 0; i < 3; i++ )); do
  echo "iteration $i"
done
```
### 3. Use while and until

Target: Use while and until. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# while and until loops
count=0
while (( count < 3 )); do
  echo "count: $count"
  (( count++ ))
done
until [ -f /tmp/ready ]; do
  echo "waiting for /tmp/ready..."
  sleep 1
done
echo "ready file appeared!"
```
### 4. Control loops with break/continue

Target: Control loops with break/continue. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# break and continue
for n in {1..10}; do
  (( n % 2 == 0 )) && continue    # skip evens
  [ "$n" -ge 7 ] && break          # stop at 7
  echo "odd under 7: $n"
done
# Output: 1 3 5
```

## Practice Questions

1. What is the key idea behind "Loops"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Loops with analogies and real-world examples"
1. "Show me common mistakes beginners make with Loops"
1. "Provide advanced patterns and performance considerations for Loops"

## Key Takeaways

- Master the core ideas of Loops through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
