---
{
  "title": "Job Control and Processes",
  "description": "Background jobs, signals, and process management.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Run jobs in the background",
    "List and kill processes",
    "Handle signals with trap",
    "Wait for background jobs"
  ],
  "knowledge_refs": [
    "shell/shell-11-job-control"
  ],
  "prerequisites": [
    "Shell-10: Input/Output Redirection"
  ],
  "references": [
    {
      "title": "GNU Bash Reference Manual",
      "url": "https://www.gnu.org/software/bash/manual/bash.html",
      "description": "The authoritative Bash reference"
    },
    {
      "title": "ShellCheck",
      "url": "https://www.shellcheck.net/",
      "description": "Static analysis for shell scripts"
    },
    {
      "title": "BashGuide (Bash Hackers Wiki)",
      "url": "https://wiki.bash-hackers.org/",
      "description": "Practical Bash wiki"
    },
    {
      "title": "Explain Shell",
      "url": "https://explainshell.com/",
      "description": "Break down any command line"
    }
  ]
}
---

# SHELL-11-JOB-CONTROL: Job Control and Processes

## Introduction

Background jobs, signals, and process management. By the end of this lesson you will be able to: Run jobs in the background; List and kill processes; Handle signals with trap; Wait for background jobs.

## Key Concepts

### 1. Run jobs in the background

Target: Run jobs in the background. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
sleep 10 &
echo "PID: $!"
wait $!
```
### 2. List and kill processes

Target: List and kill processes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
kill -TERM 1234     # send signal
kill -9 1234        # force kill
```
### 3. Handle signals with trap

Target: Handle signals with trap. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
trap "echo Cleaning up; exit" INT
while true; do sleep 1; done
```
### 4. Wait for background jobs

Target: Wait for background jobs. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
jobs -l
fg %1     # bring job 1 to foreground
```

## Practice Questions

1. What is the key idea behind "Job Control and Processes"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Job Control and Processes with analogies and real-world examples"
1. "Show me common mistakes beginners make with Job Control and Processes"
1. "Provide advanced patterns and performance considerations for Job Control and Processes"

## Key Takeaways

- Master the core ideas of Job Control and Processes through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
