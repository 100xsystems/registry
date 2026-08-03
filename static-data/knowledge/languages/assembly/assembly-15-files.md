---
{
  "title": "File Operations",
  "description": "Open, read, write, close files.",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Open files with syscalls",
    "Read file contents",
    "Write to files",
    "Close descriptors"
  ],
  "knowledge_refs": [
    "assembly/assembly-15-files"
  ],
  "prerequisites": [
    "Assembly-14: Syscalls and Interrupts"
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

# ASSEMBLY-15-FILES: File Operations

## Introduction

Open, read, write, close files. By the end of this lesson you will be able to: Open files with syscalls; Read file contents; Write to files; Close descriptors.

## Key Concepts

### 1. Open files with syscalls

Target: Open files with syscalls. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
; open("data.txt", O_RDONLY)
mov rax, 2
lea rdi, [path]
mov rsi, 0
syscall
mov r12, rax    ; fd
```
### 2. Read file contents

Target: Read file contents. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
; read(fd, buf, 100)
mov rax, 0
mov rdi, r12
lea rsi, [buf]
mov rdx, 100
syscall
```
### 3. Write to files

Target: Write to files. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
; write(fd, msg, len)
mov rax, 1
mov rdi, r12
lea rsi, [msg]
mov rdx, len
syscall
```
### 4. Close descriptors

Target: Close descriptors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
; close(fd)
mov rax, 3
mov rdi, r12
syscall
```

## Practice Questions

1. What is the key idea behind "File Operations"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain File Operations with analogies and real-world examples"
1. "Show me common mistakes beginners make with File Operations"
1. "Provide advanced patterns and performance considerations for File Operations"

## Key Takeaways

- Master the core ideas of File Operations through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
