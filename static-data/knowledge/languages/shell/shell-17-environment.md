---
{
  "title": "Environment and Configuration",
  "description": "ENV vars, exports, and config file patterns.",
  "type": "lesson",
  "order": 17,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Export environment variables",
    "Load .env files safely",
    "Use positional default patterns",
    "Pass secrets via environment"
  ],
  "knowledge_refs": [
    "shell/shell-17-environment"
  ],
  "prerequisites": [
    "Shell-16: Debugging and Error Handling"
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

# SHELL-17-ENVIRONMENT: Environment and Configuration

## Introduction

ENV vars, exports, and config file patterns. By the end of this lesson you will be able to: Export environment variables; Load .env files safely; Use positional default patterns; Pass secrets via environment.

## Key Concepts

### 1. Export environment variables

Target: Export environment variables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
export DB_HOST="localhost"
./app
```
### 2. Load .env files safely

Target: Load .env files safely. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
set -a
source .env
set +a
```
### 3. Use positional default patterns

Target: Use positional default patterns. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
env | grep -i "PORT"
```
### 4. Pass secrets via environment

Target: Pass secrets via environment. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
run() {
  local api_key="${API_KEY:?missing}"
  curl -H "Authorization: Bearer $api_key" https://api.example.com
}
```

## Practice Questions

1. What is the key idea behind "Environment and Configuration"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Environment and Configuration with analogies and real-world examples"
1. "Show me common mistakes beginners make with Environment and Configuration"
1. "Provide advanced patterns and performance considerations for Environment and Configuration"

## Key Takeaways

- Master the core ideas of Environment and Configuration through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
