---
{
  "title": "Bit Manipulation",
  "description": "popcnt, bsf, and efficient tricks.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Count set bits",
    "Find lowest set bit",
    "Use bts/btr",
    "Optimize with bit tricks"
  ],
  "knowledge_refs": [
    "assembly/assembly-16-bit-manipulation"
  ],
  "prerequisites": [
    "Assembly-15: File Operations"
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

# ASSEMBLY-16-BIT-MANIPULATION: Bit Manipulation

## Introduction

popcnt, bsf, and efficient tricks. By the end of this lesson you will be able to: Count set bits; Find lowest set bit; Use bts/btr; Optimize with bit tricks.

## Key Concepts

### 1. Count set bits

Target: Count set bits. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
popcnt rax, rax    ; count 1 bits
```
### 2. Find lowest set bit

Target: Find lowest set bit. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
bsf rax, rbx       ; lowest set bit index
jnz found
```
### 3. Use bts/btr

Target: Use bts/btr. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
bts rax, 3         ; set bit 3
btr rax, 3         ; reset bit 3
```
### 4. Optimize with bit tricks

Target: Optimize with bit tricks. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
xor eax, eax       ; fast zero (better than mov)
```

## Practice Questions

1. What is the key idea behind "Bit Manipulation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Bit Manipulation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Bit Manipulation"
1. "Provide advanced patterns and performance considerations for Bit Manipulation"

## Key Takeaways

- Master the core ideas of Bit Manipulation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
