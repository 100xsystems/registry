---
{
  "title": "Operators and Expressions",
  "description": "Arithmetic, relational, and logical operators.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use arithmetic operators",
    "Compare values relationally",
    "Combine logical expressions",
    "Handle integer division"
  ],
  "knowledge_refs": [
    "fortran/fortran-03-operators"
  ],
  "prerequisites": [
    "Fortran-02: Variables and Declarations"
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

# FORTRAN-03-OPERATORS: Operators and Expressions

## Introduction

Arithmetic, relational, and logical operators. By the end of this lesson you will be able to: Use arithmetic operators; Compare values relationally; Combine logical expressions; Handle integer division.

## Key Concepts

### 1. Use arithmetic operators

Target: Use arithmetic operators. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
program arith
  implicit none
  integer :: a, b
  a = 7; b = 2
  print *, a + b, a - b, a * b, a / b, mod(a, b)
end program arith
```
### 2. Compare values relationally

Target: Compare values relationally. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
program realdiv
  implicit none
  print *, 7.0 / 2.0
end program realdiv
```
### 3. Combine logical expressions

Target: Combine logical expressions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
program compare
  implicit none
  integer :: x = 5
  print *, x > 3, x <= 5
end program compare
```
### 4. Handle integer division

Target: Handle integer division. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
program logic
  implicit none
  logical :: flag = .true.
  print *, flag .and. .not. flag
end program logic
```

## Practice Questions

1. What is the key idea behind "Operators and Expressions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Operators and Expressions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Operators and Expressions"
1. "Provide advanced patterns and performance considerations for Operators and Expressions"

## Key Takeaways

- Master the core ideas of Operators and Expressions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
