---
{
  "title": "Control Flow",
  "description": "if, select case, and structured flow.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write if/else if/else blocks",
    "Use select case",
    "Use named constructs",
    "Guard with logical conditions"
  ],
  "knowledge_refs": [
    "fortran/fortran-04-control"
  ],
  "prerequisites": [
    "Fortran-03: Operators and Expressions"
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

# FORTRAN-04-CONTROL: Control Flow

## Introduction

if, select case, and structured flow. By the end of this lesson you will be able to: Write if/else if/else blocks; Use select case; Use named constructs; Guard with logical conditions.

## Key Concepts

### 1. Write if/else if/else blocks

Target: Write if/else if/else blocks. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```fortran
program grade
  implicit none
  integer :: score
  score = 85
  if (score >= 90) then
    print *, "A"
  else if (score >= 80) then
    print *, "B"
  else
    print *, "C"
  end if
end program grade
```
### 2. Use select case

Target: Use select case. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```fortran
program select
  implicit none
  integer :: n
  n = 2
  select case (n)
  case (1)
    print *, "one"
  case (2)
    print *, "two"
  case default
    print *, "other"
  end select
end program select
```
### 3. Use named constructs

Target: Use named constructs. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```fortran
if (x > 0 .and. y > 0) then
  print *, "both positive"
end if
```
### 4. Guard with logical conditions

Target: Guard with logical conditions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```fortran
named: if (flag) then
  print *, "flagged"
end if named
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
