---
{
  "title": "Control Flow",
  "description": "cmp, jumps, and loops.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Compare values with cmp",
    "Use conditional jumps",
    "Build if/else",
    "Write loops"
  ],
  "knowledge_refs": [
    "assembly/assembly-06-control-flow"
  ],
  "prerequisites": [
    "Assembly-05: Logical and Bit Operations"
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

# ASSEMBLY-06-CONTROL-FLOW: Control Flow

## Introduction

cmp, jumps, and loops. By the end of this lesson you will be able to: Compare values with cmp; Use conditional jumps; Build if/else; Write loops.

## Key Concepts

### 1. Compare values with cmp

Target: Compare values with cmp. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
cmp rax, rbx
je equal
jg greater
jl less
```
### 2. Use conditional jumps

Target: Use conditional jumps. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
mov rax, 10
cmp rax, 5
jge at_least_five
    ; else path
at_least_five:
```
### 3. Build if/else

Target: Build if/else. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
mov rcx, 5
loop_start:
    ; body
    dec rcx
    jnz loop_start
```
### 4. Write loops

Target: Write loops. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
cmp rax, 0
jne not_zero
    ; zero path
not_zero:
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
