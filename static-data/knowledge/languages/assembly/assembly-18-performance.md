---
{
  "title": "Performance Optimization",
  "description": "Pipeline, alignment, and SIMD.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Avoid stalls",
    "Align hot loops",
    "Use SIMD instructions",
    "Reduce dependencies"
  ],
  "knowledge_refs": [
    "assembly/assembly-18-performance"
  ],
  "prerequisites": [
    "Assembly-17: Debugging Assembly"
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

# ASSEMBLY-18-PERFORMANCE: Performance Optimization

## Introduction

Pipeline, alignment, and SIMD. By the end of this lesson you will be able to: Avoid stalls; Align hot loops; Use SIMD instructions; Reduce dependencies.

## Key Concepts

### 1. Avoid stalls

Target: Avoid stalls. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
align 16
.loop:
    ; hot loop body
```
### 2. Align hot loops

Target: Align hot loops. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
movdqu xmm0, [rax]
movdqu xmm1, [rbx]
paddd xmm0, xmm1
movdqu [rcx], xmm0
```
### 3. Use SIMD instructions

Target: Use SIMD instructions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
pxor xmm0, xmm0   ; zero without dependency
```
### 4. Reduce dependencies

Target: Reduce dependencies. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
; unroll loops to reduce branch overhead
```

## Practice Questions

1. What is the key idea behind "Performance Optimization"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Performance Optimization with analogies and real-world examples"
1. "Show me common mistakes beginners make with Performance Optimization"
1. "Provide advanced patterns and performance considerations for Performance Optimization"

## Key Takeaways

- Master the core ideas of Performance Optimization through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
