---
{
  "title": "Interfacing with C",
  "description": "Call C from assembly and vice versa.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Export functions to C",
    "Call libc from asm",
    "Use C structs",
    "Link with gcc"
  ],
  "knowledge_refs": [
    "assembly/assembly-19-c-interop"
  ],
  "prerequisites": [
    "Assembly-18: Performance Optimization"
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

# ASSEMBLY-19-C-INTEROP: Interfacing with C

## Introduction

Call C from assembly and vice versa. By the end of this lesson you will be able to: Export functions to C; Call libc from asm; Use C structs; Link with gcc.

## Key Concepts

### 1. Export functions to C

Target: Export functions to C. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
global my_add
my_add:
    mov rax, rdi
    add rax, rsi
    ret

; C: extern int my_add(int, int);
```
### 2. Call libc from asm

Target: Call libc from asm. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
; assemble with gcc
gcc -c my_add.asm -o my_add.o
gcc main.c my_add.o -o app
```
### 3. Use C structs

Target: Use C structs. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
extern strlen
mov rdi, msg
call strlen
```
### 4. Link with gcc

Target: Link with gcc. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
; struct access: first field at [rdi], second at [rdi+8]
```

## Practice Questions

1. What is the key idea behind "Interfacing with C"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Interfacing with C with analogies and real-world examples"
1. "Show me common mistakes beginners make with Interfacing with C"
1. "Provide advanced patterns and performance considerations for Interfacing with C"

## Key Takeaways

- Master the core ideas of Interfacing with C through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
