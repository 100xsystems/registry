---
{
  "title": "Parallel Programming with OpenMP",
  "description": "OpenMP directives for shared-memory parallelism.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use omp parallel regions",
    "Parallelize loops",
    "Use reduction clauses",
    "Manage shared/private vars"
  ],
  "knowledge_refs": [
    "fortran/fortran-17-parallel"
  ],
  "prerequisites": [
    "Fortran-16: Object-Oriented Fortran"
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

# FORTRAN-17-PARALLEL: Parallel Programming with OpenMP

## Introduction

OpenMP directives for shared-memory parallelism. By the end of this lesson you will be able to: Use omp parallel regions; Parallelize loops; Use reduction clauses; Manage shared/private vars.

## Key Concepts

### 1. Use omp parallel regions

Target: Use omp parallel regions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
program par
  use omp_lib
  implicit none
  !$omp parallel
  print *, "hello from thread", omp_get_thread_num()
  !$omp end parallel
end program par
```
### 2. Parallelize loops

Target: Parallelize loops. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
!$omp parallel do
  do i = 1, 1000
    a(i) = i * i
  end do
!$omp end parallel do
```
### 3. Use reduction clauses

Target: Use reduction clauses. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
!$omp parallel do reduction(+:total)
  do i = 1, 100
    total = total + a(i)
  end do
!$omp end parallel do
```
### 4. Manage shared/private vars

Target: Manage shared/private vars. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
!$omp critical
  counter = counter + 1
!$omp end critical
```

## Practice Questions

1. What is the key idea behind "Parallel Programming with OpenMP"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Parallel Programming with OpenMP with analogies and real-world examples"
1. "Show me common mistakes beginners make with Parallel Programming with OpenMP"
1. "Provide advanced patterns and performance considerations for Parallel Programming with OpenMP"

## Key Takeaways

- Master the core ideas of Parallel Programming with OpenMP through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
