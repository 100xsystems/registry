---
{
  "title": "Input/Output Redirection",
  "description": "Redirect stdin/stdout/stderr, pipes, and heredocs.",
  "type": "lesson",
  "order": 10,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Redirect output with > and >>",
    "Feed input with < and heredocs",
    "Separate stderr with 2>",
    "Build pipelines with |"
  ],
  "knowledge_refs": [
    "shell/shell-10-io-redirection"
  ],
  "prerequisites": [
    "Shell-09: Arrays"
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

# SHELL-10-IO-REDIRECTION: Input/Output Redirection

## Introduction

Redirect stdin/stdout/stderr, pipes, and heredocs. By the end of this lesson you will be able to: Redirect output with > and >>; Feed input with < and heredocs; Separate stderr with 2>; Build pipelines with |.

## Key Concepts

### 1. Redirect output with > and >>

Target: Redirect output with > and >>. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
echo "log line" >> app.log
```
### 2. Feed input with < and heredocs

Target: Feed input with < and heredocs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
sort < names.txt > sorted.txt
```
### 3. Separate stderr with 2>

Target: Separate stderr with 2>. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
command 2> error.log 1> output.log
```
### 4. Build pipelines with |

Target: Build pipelines with |. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
cat <<EOF > config.ini
host=localhost
port=8080
EOF
```

## Practice Questions

1. What is the key idea behind "Input/Output Redirection"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Input/Output Redirection with analogies and real-world examples"
1. "Show me common mistakes beginners make with Input/Output Redirection"
1. "Provide advanced patterns and performance considerations for Input/Output Redirection"

## Key Takeaways

- Master the core ideas of Input/Output Redirection through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
