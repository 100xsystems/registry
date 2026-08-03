---
{
  "title": "Getting Started with Assembly",
  "description": "Registers, syscalls, and hello world in NASM.",
  "type": "lesson",
  "order": 1,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Understand CPU registers",
    "Write a hello world syscall",
    "Assemble with nasm",
    "Link with ld"
  ],
  "knowledge_refs": [
    "assembly/assembly-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# ASSEMBLY-01-GETTING-STARTED: Getting Started with Assembly

## Introduction

Registers, syscalls, and hello world in NASM. By the end of this lesson you will be able to: Understand CPU registers; Write a hello world syscall; Assemble with nasm; Link with ld.

## Key Concepts

### 1. Understand CPU registers

Target: Understand CPU registers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
section .data
    msg db "Hello, World!", 0xa
    len equ $ - msg

section .text
    global _start

_start:
    mov rax, 1          ; write syscall
    mov rdi, 1          ; stdout
    mov rsi, msg
    mov rdx, len
    syscall

    mov rax, 60         ; exit syscall
    xor rdi, rdi
    syscall
```
### 2. Write a hello world syscall

Target: Write a hello world syscall. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
nasm -f elf64 hello.asm
ld -o hello hello.o
./hello
```
### 3. Assemble with nasm

Target: Assemble with nasm. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
section .data
    msg db "Assembly!", 0xa
    len equ $ - msg
```
### 4. Link with ld

Target: Link with ld. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
section .text
    global _start
_start:
    mov rax, 60
    mov rdi, 0
    syscall
```

## Practice Questions

1. What is the key idea behind "Getting Started with Assembly"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Assembly with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Assembly"
1. "Provide advanced patterns and performance considerations for Getting Started with Assembly"

## Key Takeaways

- Master the core ideas of Getting Started with Assembly through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
