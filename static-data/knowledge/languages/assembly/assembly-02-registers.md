---
{
  "title": "Registers and Data Sizes",
  "description": "General-purpose, sizes, and moves.",
  "type": "lesson",
  "order": 2,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Name the general-purpose registers",
    "Use 8/16/32/64-bit registers",
    "Use mov variants",
    "Understand zero/sign extension"
  ],
  "knowledge_refs": [
    "assembly/assembly-02-registers"
  ],
  "prerequisites": [
    "Assembly-01: Getting Started with Assembly"
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

# ASSEMBLY-02-REGISTERS: Registers and Data Sizes

## Introduction

General-purpose, sizes, and moves. By the end of this lesson you will be able to: Name the general-purpose registers; Use 8/16/32/64-bit registers; Use mov variants; Understand zero/sign extension.

## Key Concepts

### 1. Name the general-purpose registers

Target: Name the general-purpose registers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
mov rax, 10      ; 64-bit
mov eax, 10      ; 32-bit (zero-extends)
mov ax, 10       ; 16-bit
mov al, 10       ; 8-bit
```
### 2. Use 8/16/32/64-bit registers

Target: Use 8/16/32/64-bit registers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
mov rax, rbx    ; register to register
```
### 3. Use mov variants

Target: Use mov variants. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
mov rbx, 0      ; clear
mov rcx, -1     ; all ones
```
### 4. Understand zero/sign extension

Target: Understand zero/sign extension. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
movzx eax, al   ; zero extend
movsx rax, eax  ; sign extend
```

## Practice Questions

1. What is the key idea behind "Registers and Data Sizes"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Registers and Data Sizes with analogies and real-world examples"
1. "Show me common mistakes beginners make with Registers and Data Sizes"
1. "Provide advanced patterns and performance considerations for Registers and Data Sizes"

## Key Takeaways

- Master the core ideas of Registers and Data Sizes through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
