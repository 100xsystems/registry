---
{
  "title": "Logical and Bit Operations",
  "description": "and, or, xor, shifts.",
  "type": "lesson",
  "order": 5,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use and/or/xor",
    "Shift left and right",
    "Test bits",
    "Use not"
  ],
  "knowledge_refs": [
    "assembly/assembly-05-logical"
  ],
  "prerequisites": [
    "Assembly-04: Arithmetic Instructions"
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

# ASSEMBLY-05-LOGICAL: Logical and Bit Operations

## Introduction

and, or, xor, shifts. By the end of this lesson you will be able to: Use and/or/xor; Shift left and right; Test bits; Use not.

## Key Concepts

### 1. Use and/or/xor

Target: Use and/or/xor. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
and rax, rbx
or rax, rbx
xor rax, rbx
```
### 2. Shift left and right

Target: Shift left and right. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
shl rax, 2      ; multiply by 4
shr rax, 1      ; divide by 2
```
### 3. Test bits

Target: Test bits. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
test rax, 1
jz even        ; jump if zero
```
### 4. Use not

Target: Use not. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
mov rax, 0b1010
and rax, 0b1100  ; rax = 0b1000
```

## Practice Questions

1. What is the key idea behind "Logical and Bit Operations"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Logical and Bit Operations with analogies and real-world examples"
1. "Show me common mistakes beginners make with Logical and Bit Operations"
1. "Provide advanced patterns and performance considerations for Logical and Bit Operations"

## Key Takeaways

- Master the core ideas of Logical and Bit Operations through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
