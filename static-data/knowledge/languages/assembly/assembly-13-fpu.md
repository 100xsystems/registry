---
{
  "title": "Floating Point",
  "description": "SSE and scalar float ops.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use xmm registers",
    "Add and multiply floats",
    "Convert int to float",
    "Use divss"
  ],
  "knowledge_refs": [
    "assembly/assembly-13-fpu"
  ],
  "prerequisites": [
    "Assembly-12: Input/Output"
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

# ASSEMBLY-13-FPU: Floating Point

## Introduction

SSE and scalar float ops. By the end of this lesson you will be able to: Use xmm registers; Add and multiply floats; Convert int to float; Use divss.

## Key Concepts

### 1. Use xmm registers

Target: Use xmm registers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
movss xmm0, [val]
movss xmm1, [val2]
addss xmm0, xmm1
```
### 2. Add and multiply floats

Target: Add and multiply floats. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
mulss xmm0, xmm0    ; square
```
### 3. Convert int to float

Target: Convert int to float. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
cvtsi2ss xmm0, eax  ; int -> float
```
### 4. Use divss

Target: Use divss. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
divss xmm0, xmm1    ; float divide
```

## Practice Questions

1. What is the key idea behind "Floating Point"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Floating Point with analogies and real-world examples"
1. "Show me common mistakes beginners make with Floating Point"
1. "Provide advanced patterns and performance considerations for Floating Point"

## Key Takeaways

- Master the core ideas of Floating Point through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
