---
{
  "title": "Arithmetic Instructions",
  "description": "add, sub, imul, and idiv.",
  "type": "lesson",
  "order": 4,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Add and subtract",
    "Multiply with imul",
    "Divide with idiv",
    "Use inc and dec"
  ],
  "knowledge_refs": [
    "assembly/assembly-04-arithmetic"
  ],
  "prerequisites": [
    "Assembly-03: Memory Addressing"
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

# ASSEMBLY-04-ARITHMETIC: Arithmetic Instructions

## Introduction

add, sub, imul, and idiv. By the end of this lesson you will be able to: Add and subtract; Multiply with imul; Divide with idiv; Use inc and dec.

## Key Concepts

### 1. Add and subtract

Target: Add and subtract. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
add rax, 5
sub rax, 3
```
### 2. Multiply with imul

Target: Multiply with imul. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
mov rax, 6
mov rbx, 7
imul rax, rbx      ; rax = 42
```
### 3. Divide with idiv

Target: Divide with idiv. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
mov rax, 42
mov rbx, 6
xor rdx, rdx
idiv rbx          ; rax = 7, rdx = 0
```
### 4. Use inc and dec

Target: Use inc and dec. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
inc rax
dec rbx
```

## Practice Questions

1. What is the key idea behind "Arithmetic Instructions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arithmetic Instructions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arithmetic Instructions"
1. "Provide advanced patterns and performance considerations for Arithmetic Instructions"

## Key Takeaways

- Master the core ideas of Arithmetic Instructions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
