---
{
  "title": "Scientific Computing Patterns",
  "description": "Linear algebra, numerics, and LAPACK.",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use LAPACK routines",
    "Solve linear systems",
    "Compute eigenvalues",
    "Handle precision issues"
  ],
  "knowledge_refs": [
    "fortran/fortran-20-scientific"
  ],
  "prerequisites": [
    "Fortran-19: Performance and Optimization"
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

# FORTRAN-20-SCIENTIFIC: Scientific Computing Patterns

## Introduction

Linear algebra, numerics, and LAPACK. By the end of this lesson you will be able to: Use LAPACK routines; Solve linear systems; Compute eigenvalues; Handle precision issues.

## Key Concepts

### 1. Use LAPACK routines

Target: Use LAPACK routines. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
call dgesv(n, nrhs, a, lda, ipiv, b, ldb, info)
```
### 2. Solve linear systems

Target: Solve linear systems. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
call dgemm('N', 'N', m, n, k, alpha, a, lda, b, ldb, beta, c, ldc)
```
### 3. Compute eigenvalues

Target: Compute eigenvalues. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
call dsyev('V', 'U', n, a, lda, w, work, lwork, info)
```
### 4. Handle precision issues

Target: Handle precision issues. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
real(kind=dp), parameter :: eps = 1.0e-15_dp
if (abs(x) < eps) print *, "near zero"
```

## Practice Questions

1. What is the key idea behind "Scientific Computing Patterns"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Scientific Computing Patterns with analogies and real-world examples"
1. "Show me common mistakes beginners make with Scientific Computing Patterns"
1. "Provide advanced patterns and performance considerations for Scientific Computing Patterns"

## Key Takeaways

- Master the core ideas of Scientific Computing Patterns through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
