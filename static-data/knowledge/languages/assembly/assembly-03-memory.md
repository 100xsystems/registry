---
{
  "title": "Memory Addressing",
  "description": "Effective addresses and addressing modes.",
  "type": "lesson",
  "order": 3,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Load from memory",
    "Store to memory",
    "Use base+index addressing",
    "Use displacement"
  ],
  "knowledge_refs": [
    "assembly/assembly-03-memory"
  ],
  "prerequisites": [
    "Assembly-02: Registers and Data Sizes"
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

# ASSEMBLY-03-MEMORY: Memory Addressing

## Introduction

Effective addresses and addressing modes. By the end of this lesson you will be able to: Load from memory; Store to memory; Use base+index addressing; Use displacement.

## Key Concepts

### 1. Load from memory

Target: Load from memory. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
section .data
    value dq 42

section .text
    mov rax, [value]   ; load
```
### 2. Store to memory

Target: Store to memory. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
section .bss
    buffer resb 64

section .text
    mov byte [buffer], 65
```
### 3. Use base+index addressing

Target: Use base+index addressing. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
mov rax, [rbx + 8]       ; base + displacement
mov rax, [rbx + rcx*4]    ; base + index*scale
```
### 4. Use displacement

Target: Use displacement. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
mov [rsp + 16], rax      ; stack access
```

## Practice Questions

1. What is the key idea behind "Memory Addressing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Memory Addressing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Memory Addressing"
1. "Provide advanced patterns and performance considerations for Memory Addressing"

## Key Takeaways

- Master the core ideas of Memory Addressing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
