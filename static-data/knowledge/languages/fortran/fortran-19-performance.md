---
{
  "title": "Performance and Optimization",
  "description": "Vectorization, alignment, and profiling.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Enable compiler optimizations",
    "Write vectorizable loops",
    "Use contiguous arrays",
    "Profile and benchmark"
  ],
  "knowledge_refs": [
    "fortran/fortran-19-performance"
  ],
  "prerequisites": [
    "Fortran-18: MPI for Distributed Computing"
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

# FORTRAN-19-PERFORMANCE: Performance and Optimization

## Introduction

Vectorization, alignment, and profiling. By the end of this lesson you will be able to: Enable compiler optimizations; Write vectorizable loops; Use contiguous arrays; Profile and benchmark.

## Key Concepts

### 1. Enable compiler optimizations

Target: Enable compiler optimizations. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
! compile: gfortran -O3 -march=native app.f90
```
### 2. Write vectorizable loops

Target: Write vectorizable loops. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
real, dimension(:), contiguous :: v
! contiguous guarantees tight layout
```
### 3. Use contiguous arrays

Target: Use contiguous arrays. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
do i = 1, n
  a(i) = b(i) * c(i)   ! vectorizable
end do
```
### 4. Profile and benchmark

Target: Profile and benchmark. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
call system_clock(t1)
! ... work ...
call system_clock(t2)
print *, "time:", (t2 - t1) / 1000.0
```

## Practice Questions

1. What is the key idea behind "Performance and Optimization"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Performance and Optimization with analogies and real-world examples"
1. "Show me common mistakes beginners make with Performance and Optimization"
1. "Provide advanced patterns and performance considerations for Performance and Optimization"

## Key Takeaways

- Master the core ideas of Performance and Optimization through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
