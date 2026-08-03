---
{
  "title": "The Stack",
  "description": "push, pop, and calling conventions.",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Push and pop",
    "Understand stack growth",
    "Save and restore registers",
    "Use the frame pointer"
  ],
  "knowledge_refs": [
    "assembly/assembly-07-stack"
  ],
  "prerequisites": [
    "Assembly-06: Control Flow"
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

# ASSEMBLY-07-STACK: The Stack

## Introduction

push, pop, and calling conventions. By the end of this lesson you will be able to: Push and pop; Understand stack growth; Save and restore registers; Use the frame pointer.

## Key Concepts

### 1. Push and pop

Target: Push and pop. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```nasm
push rax
; ... work ...
pop rax
```
### 2. Understand stack growth

Target: Understand stack growth. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```nasm
push rbx
push rcx
; ...
pop rcx
pop rbx
```
### 3. Save and restore registers

Target: Save and restore registers. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```nasm
call func
; returns here

func:
    push rbp
    mov rbp, rsp
    ; ...
    pop rbp
    ret
```
### 4. Use the frame pointer

Target: Use the frame pointer. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```nasm
sub rsp, 32   ; reserve 32 bytes
; ...
add rsp, 32
```

## Practice Questions

1. What is the key idea behind "The Stack"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain The Stack with analogies and real-world examples"
1. "Show me common mistakes beginners make with The Stack"
1. "Provide advanced patterns and performance considerations for The Stack"

## Key Takeaways

- Master the core ideas of The Stack through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
