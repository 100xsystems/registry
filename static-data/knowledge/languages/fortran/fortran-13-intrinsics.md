---
{
  "title": "Intrinsic Functions",
  "description": "Mathematical and array intrinsics.",
  "type": "lesson",
  "order": 13,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use math intrinsics",
    "Use array reduction intrinsics",
    "Use dot_product and matmul",
    "Find array locations"
  ],
  "knowledge_refs": [
    "fortran/fortran-13-intrinsics"
  ],
  "prerequisites": [
    "Fortran-12: File Input/Output"
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

# FORTRAN-13-INTRINSICS: Intrinsic Functions

## Introduction

Mathematical and array intrinsics. By the end of this lesson you will be able to: Use math intrinsics; Use array reduction intrinsics; Use dot_product and matmul; Find array locations.

## Key Concepts

### 1. Use math intrinsics

Target: Use math intrinsics. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
print *, exp(1.0), log(2.0), sin(0.5)
```
### 2. Use array reduction intrinsics

Target: Use array reduction intrinsics. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
print *, sum(a), product(a), maxval(a), minval(a)
```
### 3. Use dot_product and matmul

Target: Use dot_product and matmul. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
dot = dot_product(u, v)
mat = matmul(a, b)
```
### 4. Find array locations

Target: Find array locations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
idx = maxloc(a, 1)
print *, "max at", idx
```

## Practice Questions

1. What is the key idea behind "Intrinsic Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Intrinsic Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Intrinsic Functions"
1. "Provide advanced patterns and performance considerations for Intrinsic Functions"

## Key Takeaways

- Master the core ideas of Intrinsic Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
