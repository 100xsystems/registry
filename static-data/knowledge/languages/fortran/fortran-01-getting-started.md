---
{
  "title": "Getting Started with Fortran",
  "description": "Modern Fortran, compiler setup, hello world.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install a Fortran compiler",
    "Write free-form Fortran",
    "Compile and run programs",
    "Use print and read"
  ],
  "knowledge_refs": [
    "fortran/fortran-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
  ],
  "references": [
    {
      "title": "Fortran 90/95 Standard",
      "url": "https://wg5-fortran.org/",
      "description": "The official standards committee"
    },
    {
      "title": "Fortran Best Practices",
      "url": "https://fortran-lang.org/en/learn/",
      "description": "fortran-lang.org learning resources"
    },
    {
      "title": "Modern Fortran Explained",
      "url": "https://www.oxford.universitypressscholarship.com/",
      "description": "Metcalf, Reid & Cohen textbook"
    }
  ]
}
---

# FORTRAN-01-GETTING-STARTED: Getting Started with Fortran

## Introduction

Modern Fortran, compiler setup, hello world. By the end of this lesson you will be able to: Install a Fortran compiler; Write free-form Fortran; Compile and run programs; Use print and read.

## Key Concepts

### 1. Install a Fortran compiler

Target: Install a Fortran compiler. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
program hello
  print *, "Hello, World!"
end program hello
```
### 2. Write free-form Fortran

Target: Write free-form Fortran. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
gfortran hello.f90 -o hello
./hello
```
### 3. Compile and run programs

Target: Compile and run programs. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
program greet
  character(len=20) :: name
  print *, "Enter your name:"
  read *, name
  print *, "Hello, ", trim(name)
end program greet
```
### 4. Use print and read

Target: Use print and read. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
program math
  print *, 2 + 3, " is the answer"
end program math
```

## Practice Questions

1. What is the key idea behind "Getting Started with Fortran"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Fortran with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Fortran"
1. "Provide advanced patterns and performance considerations for Getting Started with Fortran"

## Key Takeaways

- Master the core ideas of Getting Started with Fortran through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
