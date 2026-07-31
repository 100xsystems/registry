---
{
  "title": "Concurrency and Parallelism",
  "description": "xargs -P, parallel, background fan-out, subshells, and coprocesses.",
  "type": "lesson",
  "order": 17,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Parallelize with xargs",
    "Fan out with background jobs",
    "Understand subshell semantics",
    "Use coprocesses"
  ],
  "knowledge_refs": [
    "bash/bash-17-concurrency"
  ],
  "prerequisites": [
    "BASH-16"
  ],
  "references": [
    {
      "title": "GNU parallel",
      "url": "https://www.gnu.org/software/parallel/"
    },
    {
      "title": "Bash — Command Execution",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Command-Execution-Environment"
    },
    {
      "title": "Bash — Coprocesses",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Coprocesses"
    }
  ]
}
---

# BASH-17-CONCURRENCY: Concurrency and Parallelism

## Introduction

xargs -P, parallel, background fan-out, subshells, and coprocesses. By the end of this lesson you will be able to: Parallelize with xargs; Fan out with background jobs; Understand subshell semantics; Use coprocesses.

## Key Concepts

### 1. Parallelize with xargs

Target: Parallelize with xargs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# xargs parallel execution
seq 1 8 | xargs -P8 -I{} sh -c 'echo "task {}"; sleep 0.5'
echo "parallel batch done"
# -n1 processes one at a time:
seq 1 3 | xargs -n1 echo "single"
```
### 2. Fan out with background jobs

Target: Fan out with background jobs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# GNU parallel (if installed): fan-out with output control
# seq 1 4 | parallel -j4 'sleep 0.5; echo job {}' 2>/dev/null
# Without parallel, emulate with background jobs:
run_task() { sleep 0.5; echo "task $1 done"; }
pids=()
for i in 1 2 3 4; do
  run_task "$i" & pids+=("$!")
done
for p in "${pids[@]}"; do wait "$p"; done
echo "all 4 tasks finished"
```
### 3. Understand subshell semantics

Target: Understand subshell semantics. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# Subshells vs current shell: (
(
  cd /tmp
  echo "subshell pwd: $PWD"
)
echo "parent pwd: $PWD"    # unchanged!
# Variables set in subshells don't persist:
x=1
( x=2 )
echo "x is still $x"
```
### 4. Use coprocesses

Target: Use coprocesses. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# Coprocesses (Bash 4+)
coproc MYPROC { cat; }
echo "hello coproc" >&"${MYPROC[1]}"
read -r reply <&"${MYPROC[0]}"
echo "coproc replied: $reply"
# Coprocesses let a script talk to a long-running program
# bidirectionally — rare but powerful.
```

## Practice Questions

1. What is the key idea behind "Concurrency and Parallelism"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Concurrency and Parallelism with analogies and real-world examples"
1. "Show me common mistakes beginners make with Concurrency and Parallelism"
1. "Provide advanced patterns and performance considerations for Concurrency and Parallelism"

## Key Takeaways

- Master the core ideas of Concurrency and Parallelism through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
