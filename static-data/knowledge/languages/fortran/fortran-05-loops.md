---
{
  "title": "Loops",
  "description": "do loops, while forms, and iteration control.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write do loops with ranges",
    "Use implied loops",
    "Control with exit and cycle",
    "Loop over arrays"
  ],
  "knowledge_refs": [
    "fortran/fortran-05-loops"
  ],
  "prerequisites": [
    "Fortran-04: Control Flow"
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

# FORTRAN-05-LOOPS: Loops

## Introduction

do loops, while forms, and iteration control. By the end of this lesson you will be able to: Write do loops with ranges; Use implied loops; Control with exit and cycle; Loop over arrays.

## Key Concepts

### 1. Write do loops with ranges

Target: Write do loops with ranges. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
program sum
  implicit none
  integer :: i, total
  total = 0
  do i = 1, 10
    total = total + i
  end do
  print *, total
end program sum
```
### 2. Use implied loops

Target: Use implied loops. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
do i = 10, 1, -1
  print *, i
end do
```
### 3. Control with exit and cycle

Target: Control with exit and cycle. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
do
  if (done) exit
end do
```
### 4. Loop over arrays

Target: Loop over arrays. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
do i = 1, 10
  if (mod(i, 2) == 0) cycle
  print *, i
end do
```

## Practice Questions

1. What is the key idea behind "Loops"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Loops with analogies and real-world examples"
1. "Show me common mistakes beginners make with Loops"
1. "Provide advanced patterns and performance considerations for Loops"

## Key Takeaways

- Master the core ideas of Loops through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
