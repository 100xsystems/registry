---
{
  "title": "Input/Output",
  "description": "Read and write with syscalls.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write to stdout",
    "Read from stdin",
    "Handle buffer sizes",
    "Convert integers to text"
  ],
  "knowledge_refs": [
    "assembly/assembly-12-io"
  ],
  "prerequisites": [
    "Assembly-11: Arrays and Indexing"
  ],
  "references": [
    {
      "title": "NASM Documentation",
      "url": "https://www.nasm.us/doc/",
      "description": "Official NASM manual"
    },
    {
      "title": "x86-64 Assembly Reference",
      "url": "https://www.felixcloutier.com/x86/",
      "description": "Complete instruction set reference"
    },
    {
      "title": "Programming from the Ground Up",
      "url": "https://download-mirror.savannah.gnu.org/releases/pgubook/",
      "description": "Classic introduction"
    }
  ]
}
---

# ASSEMBLY-12-IO: Input/Output

## Introduction

Read and write with syscalls. By the end of this lesson you will be able to: Write to stdout; Read from stdin; Handle buffer sizes; Convert integers to text.

## Key Concepts

### 1. Write to stdout

Target: Write to stdout. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
mov rax, 1      ; write
mov rdi, 1      ; stdout
mov rsi, msg
mov rdx, len
syscall
```
### 2. Read from stdin

Target: Read from stdin. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
mov rax, 0      ; read
mov rdi, 0      ; stdin
mov rsi, buffer
mov rdx, 255
syscall
```
### 3. Handle buffer sizes

Target: Handle buffer sizes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
section .bss
    buffer resb 256
```
### 4. Convert integers to text

Target: Convert integers to text. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
; print integer in rax
; (manual conversion to decimal string)
```

## Practice Questions

1. What is the key idea behind "Input/Output"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Input/Output with analogies and real-world examples"
1. "Show me common mistakes beginners make with Input/Output"
1. "Provide advanced patterns and performance considerations for Input/Output"

## Key Takeaways

- Master the core ideas of Input/Output through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
