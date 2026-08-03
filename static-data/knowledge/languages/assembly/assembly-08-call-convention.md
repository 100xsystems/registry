---
{
  "title": "SysV Calling Convention",
  "description": "Function arguments and System V ABI.",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Pass args in rdi/rsi/rdx",
    "Return in rax",
    "Align the stack",
    "Call C functions"
  ],
  "knowledge_refs": [
    "assembly/assembly-08-call-convention"
  ],
  "prerequisites": [
    "Assembly-07: The Stack"
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

# ASSEMBLY-08-CALL-CONVENTION: SysV Calling Convention

## Introduction

Function arguments and System V ABI. By the end of this lesson you will be able to: Pass args in rdi/rsi/rdx; Return in rax; Align the stack; Call C functions.

## Key Concepts

### 1. Pass args in rdi/rsi/rdx

Target: Pass args in rdi/rsi/rdx. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
; int add(int a, int b)
add:
    mov rax, rdi
    add rax, rsi
    ret
```
### 2. Return in rax

Target: Return in rax. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
global add
add:
    lea rax, [rdi + rsi]
    ret
```
### 3. Align the stack

Target: Align the stack. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
; call printf
mov rdi, fmt
mov rsi, 42
xor eax, eax
call printf
```
### 4. Call C functions

Target: Call C functions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
extern printf

section .data
    fmt db "val: %d", 0xa, 0
```

## Practice Questions

1. What is the key idea behind "SysV Calling Convention"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain SysV Calling Convention with analogies and real-world examples"
1. "Show me common mistakes beginners make with SysV Calling Convention"
1. "Provide advanced patterns and performance considerations for SysV Calling Convention"

## Key Takeaways

- Master the core ideas of SysV Calling Convention through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
