---
{
  "title": "Shellcode Basics",
  "description": "Position-independent code.",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write position-independent code",
    "Avoid null bytes",
    "Extract shellcode bytes",
    "Understand exploitation context"
  ],
  "knowledge_refs": [
    "assembly/assembly-20-shellcode"
  ],
  "prerequisites": [
    "Assembly-19: Interfacing with C"
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

# ASSEMBLY-20-SHELLCODE: Shellcode Basics

## Introduction

Position-independent code. By the end of this lesson you will be able to: Write position-independent code; Avoid null bytes; Extract shellcode bytes; Understand exploitation context.

## Key Concepts

### 1. Write position-independent code

Target: Write position-independent code. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
xor rax, rax
mov al, 60
xor rdi, rdi
syscall
```
### 2. Avoid null bytes

Target: Avoid null bytes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
; avoid absolute addresses — use RIP-relative
lea rsi, [rel msg]
```
### 3. Extract shellcode bytes

Target: Extract shellcode bytes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
; objcopy -O binary --only-section=.text in.o out.bin
```
### 4. Understand exploitation context

Target: Understand exploitation context. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
; use push to build values without null bytes
```

## Practice Questions

1. What is the key idea behind "Shellcode Basics"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Shellcode Basics with analogies and real-world examples"
1. "Show me common mistakes beginners make with Shellcode Basics"
1. "Provide advanced patterns and performance considerations for Shellcode Basics"

## Key Takeaways

- Master the core ideas of Shellcode Basics through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
