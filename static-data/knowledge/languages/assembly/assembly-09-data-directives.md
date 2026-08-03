---
{
  "title": "Data Directives",
  "description": "db, dw, dd, dq, resb, equ.",
  "type": "lesson",
  "order": 9,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Declare data with directives",
    "Use resb for BSS",
    "Use equ constants",
    "Build arrays"
  ],
  "knowledge_refs": [
    "assembly/assembly-09-data-directives"
  ],
  "prerequisites": [
    "Assembly-08: SysV Calling Convention"
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

# ASSEMBLY-09-DATA-DIRECTIVES: Data Directives

## Introduction

db, dw, dd, dq, resb, equ. By the end of this lesson you will be able to: Declare data with directives; Use resb for BSS; Use equ constants; Build arrays.

## Key Concepts

### 1. Declare data with directives

Target: Declare data with directives. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
section .data
    b db 1       ; byte
    w dw 2       ; word
    d dd 3       ; dword
    q dq 4       ; qword
```
### 2. Use resb for BSS

Target: Use resb for BSS. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
section .bss
    buffer resb 256
    array resq 10
```
### 3. Use equ constants

Target: Use equ constants. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
section .data
    SIZE equ 100
    buf times SIZE db 0
```
### 4. Build arrays

Target: Build arrays. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
section .data
    arr dd 1, 2, 3, 4, 5
    arr_len equ ($ - arr) / 4
```

## Practice Questions

1. What is the key idea behind "Data Directives"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Data Directives with analogies and real-world examples"
1. "Show me common mistakes beginners make with Data Directives"
1. "Provide advanced patterns and performance considerations for Data Directives"

## Key Takeaways

- Master the core ideas of Data Directives through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
