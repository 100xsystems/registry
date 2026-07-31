---
{
  "title": "Process Management",
  "description": "Background jobs, wait, kill, pgrep, and job control.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Run jobs in the background",
    "Manage jobs with fg/bg/kill",
    "Use nohup and disown",
    "Probe processes with pgrep"
  ],
  "knowledge_refs": [
    "bash/bash-12-process-management"
  ],
  "prerequisites": [
    "BASH-11"
  ],
  "references": [
    {
      "title": "Bash — Job Control",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Job-Control"
    },
    {
      "title": "pgrep manual",
      "url": "https://man7.org/linux/man-pages/man1/pgrep.1.html"
    },
    {
      "title": "kill manual",
      "url": "https://man7.org/linux/man-pages/man1/kill.1.html"
    }
  ]
}
---

# BASH-12-PROCESS-MANAGEMENT: Process Management

## Introduction

Background jobs, wait, kill, pgrep, and job control. By the end of this lesson you will be able to: Run jobs in the background; Manage jobs with fg/bg/kill; Use nohup and disown; Probe processes with pgrep.

## Key Concepts

### 1. Run jobs in the background

Target: Run jobs in the background. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# Background jobs
sleep 3 &
job1=$!
echo "started job $job1"
wait $job1
echo "job finished"
# Multiple jobs and wait:
sleep 1 & sleep 2 & wait
echo "all done"
```
### 2. Manage jobs with fg/bg/kill

Target: Manage jobs with fg/bg/kill. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# Job control: jobs, fg, bg, kill
sleep 100 &
sleep 200 &
jobs -l
kill %1                  # kill by job number
kill 12345 2>/dev/null || true   # kill by PID
wait
echo "jobs terminated"
```
### 3. Use nohup and disown

Target: Use nohup and disown. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# Disowning and nohup
nohup sleep 60 >/dev/null 2>&1 &
# nohup survives terminal close; & backgrounds it
# disown removes a job from the shell's job table:
sleep 30 &
disown
echo "disowned"
```
### 4. Probe processes with pgrep

Target: Probe processes with pgrep. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# Checking if a process is running
if pgrep -x "nginx" >/dev/null; then
  echo "nginx is running"
else
  echo "nginx is NOT running"
fi
# Kill by pattern with pkill:
pkill -f "my-app" || true
# Monitor a command:
until pgrep -x "nginx" >/dev/null; do sleep 1; done
echo "nginx came up"
```

## Practice Questions

1. What is the key idea behind "Process Management"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Process Management with analogies and real-world examples"
1. "Show me common mistakes beginners make with Process Management"
1. "Provide advanced patterns and performance considerations for Process Management"

## Key Takeaways

- Master the core ideas of Process Management through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
