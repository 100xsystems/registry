---
{
  "title": "Syscalls and Interrupts",
  "description": "Linux syscall interface.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Understand syscall numbers",
    "Use rax for syscall number",
    "Use syscall instruction",
    "Map common syscalls"
  ],
  "knowledge_refs": [
    "assembly/assembly-14-interrupts"
  ],
  "prerequisites": [
    "Assembly-13: Floating Point"
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

# ASSEMBLY-14-INTERRUPTS: Syscalls and Interrupts

## Introduction

Linux syscall interface. By the end of this lesson you will be able to: Understand syscall numbers; Use rax for syscall number; Use syscall instruction; Map common syscalls.

## Key Concepts

### 1. Understand syscall numbers

Target: Understand syscall numbers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
; exit
mov rax, 60
mov rdi, 0
syscall
```
### 2. Use rax for syscall number

Target: Use rax for syscall number. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
; write
mov rax, 1
mov rdi, 1
mov rsi, msg
mov rdx, len
syscall
```
### 3. Use syscall instruction

Target: Use syscall instruction. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
; read
mov rax, 0
mov rdi, 0
mov rsi, buf
mov rdx, 100
syscall
```
### 4. Map common syscalls

Target: Map common syscalls. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
; open
mov rax, 2
mov rdi, path
mov rsi, 0
syscall
```

## Practice Questions

1. What is the key idea behind "Syscalls and Interrupts"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Syscalls and Interrupts with analogies and real-world examples"
1. "Show me common mistakes beginners make with Syscalls and Interrupts"
1. "Provide advanced patterns and performance considerations for Syscalls and Interrupts"

## Key Takeaways

- Master the core ideas of Syscalls and Interrupts through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
