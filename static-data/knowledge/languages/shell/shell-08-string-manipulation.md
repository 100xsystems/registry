---
{
  "title": "String Manipulation",
  "description": "Substring, length, replacement, and case conversion.",
  "type": "lesson",
  "order": 8,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Get string length and substrings",
    "Strip and replace patterns",
    "Split strings into arrays",
    "Convert case and trim whitespace"
  ],
  "knowledge_refs": [
    "shell/shell-08-string-manipulation"
  ],
  "prerequisites": [
    "Shell-07: Globbing and Pattern Matching"
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

# SHELL-08-STRING-MANIPULATION: String Manipulation

## Introduction

Substring, length, replacement, and case conversion. By the end of this lesson you will be able to: Get string length and substrings; Strip and replace patterns; Split strings into arrays; Convert case and trim whitespace.

## Key Concepts

### 1. Get string length and substrings

Target: Get string length and substrings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
s="hello world"
echo "${#s}"           # 11
echo "${s:0:5}"        # hello
```
### 2. Strip and replace patterns

Target: Strip and replace patterns. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
path="/usr/local/bin"
echo "${path#/usr/}"   # local/bin
echo "${path%/*}"      # /usr/local
```
### 3. Split strings into arrays

Target: Split strings into arrays. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
s="a,b,c"
IFS=, read -ra parts <<< "$s"
echo "${parts[1]}"
```
### 4. Convert case and trim whitespace

Target: Convert case and trim whitespace. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
s="Hello"
echo "${s,,}"          # lowercase
echo "${s^^}"          # UPPERCASE
```

## Practice Questions

1. What is the key idea behind "String Manipulation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain String Manipulation with analogies and real-world examples"
1. "Show me common mistakes beginners make with String Manipulation"
1. "Provide advanced patterns and performance considerations for String Manipulation"

## Key Takeaways

- Master the core ideas of String Manipulation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
