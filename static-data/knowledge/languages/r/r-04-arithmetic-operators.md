---
{
  "title": "Arithmetic and Operators",
  "description": "Numeric, comparison, logical, and vectorized operators.",
  "type": "lesson",
  "order": 4,
  "duration": 25,
  "difficulty": "beginner",
  "learning_objectives": [
    "Use arithmetic and comparison operators",
    "Distinguish vectorized & / | from short-circuit && / ||",
    "Leverage vectorized arithmetic"
  ],
  "knowledge_refs": [
    "r/r-04-arithmetic-operators"
  ],
  "prerequisites": [
    "r-02-values-types"
  ],
  "references": [
    {
      "title": "An Introduction to R — Elementary Operations",
      "url": "https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Simple-manipulations-numbers-and-vectors"
    }
  ]
}
---

# R-04-ARITHMETIC-OPERATORS: Arithmetic and Operators

## Introduction

Numeric, comparison, logical, and vectorized operators. By the end of this lesson you will be able to: Use arithmetic and comparison operators; Distinguish vectorized & / | from short-circuit && / ||; Leverage vectorized arithmetic.

## Key Concepts

### 1. Use arithmetic and comparison operators

Target: Use arithmetic and comparison operators. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# Arithmetic operators
print(7 %% 4)               # 3 — modulo
print(7 %/% 2)              # 3 — integer division
print(2^10)                 # 1024 — exponentiation

```
### 2. Distinguish vectorized & / | from short-circuit && / ||

Target: Distinguish vectorized & / | from short-circuit && / ||. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# Comparison operators
print(1 == 1)               # TRUE
print(1 != 2)               # TRUE
print("a" < "b")            # TRUE — lexicographic

```
### 3. Leverage vectorized arithmetic

Target: Leverage vectorized arithmetic. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# Logical operators: & and | are vectorized; && and || short-circuit
print(c(TRUE, FALSE) & c(TRUE, TRUE))    # TRUE FALSE
if (TRUE && 1 < 2) print("both true")

```
### 4. Use arithmetic and comparison operators

Target: Use arithmetic and comparison operators. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# Vectorized arithmetic is the R superpower
x <- c(1, 2, 3)
y <- c(10, 20, 30)
print(x + y)                # 11 22 33
print(x^2)                  # 1 4 9

```

## Practice Questions

1. What is the key idea behind "Arithmetic and Operators"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arithmetic and Operators with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arithmetic and Operators"
1. "Provide advanced patterns and performance considerations for Arithmetic and Operators"

## Key Takeaways

- Master the core ideas of Arithmetic and Operators through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
