---
{
  "title": "Arrays and Indexing",
  "description": "Index arithmetic and iteration.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Index arrays",
    "Iterate with pointers",
    "Compute element offsets",
    "Sum an array"
  ],
  "knowledge_refs": [
    "assembly/assembly-11-arrays"
  ],
  "prerequisites": [
    "Assembly-10: String Operations"
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

# ASSEMBLY-11-ARRAYS: Arrays and Indexing

## Introduction

Index arithmetic and iteration. By the end of this lesson you will be able to: Index arrays; Iterate with pointers; Compute element offsets; Sum an array.

## Key Concepts

### 1. Index arrays

Target: Index arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
section .data
    arr dq 10, 20, 30, 40

; load arr[2]
mov rbx, arr
mov rax, [rbx + 2*8]
```
### 2. Iterate with pointers

Target: Iterate with pointers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
xor rax, rax
xor rcx, rcx
.loop:
    add rax, [rbx + rcx*8]
    inc rcx
    cmp rcx, 4
    jl .loop
```
### 3. Compute element offsets

Target: Compute element offsets. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
lea rbx, [arr]
mov rax, [rbx]     ; first element
add rbx, 8          ; advance
```
### 4. Sum an array

Target: Sum an array. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
mov rdx, 8
imul rdx, rcx       ; offset = index * 8
mov rax, [rbx + rdx]
```

## Practice Questions

1. What is the key idea behind "Arrays and Indexing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays and Indexing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays and Indexing"
1. "Provide advanced patterns and performance considerations for Arrays and Indexing"

## Key Takeaways

- Master the core ideas of Arrays and Indexing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
