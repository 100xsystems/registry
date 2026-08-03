---
{
  "title": "Values and Types",
  "description": "Numeric, integer, character, logical — and special values.",
  "type": "lesson",
  "order": 2,
  "duration": "25 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Identify core R types with class() and typeof()",
    "Explain NA, NULL, NaN, and Inf",
    "Describe automatic type coercion in vectors"
  ],
  "knowledge_refs": [
    "r/r-02-values-types"
  ],
  "prerequisites": [
    "r-01-getting-started"
  ],
  "references": [
    {
      "title": "R Language Definition — Objects",
      "url": "https://cran.r-project.org/doc/manuals/r-release/R-lang.html#Objects"
    },
    {
      "title": "R for Data Science — Data Types",
      "url": "https://r4ds.hadley.nz/vectors"
    }
  ]
}
---

# R-02-VALUES-TYPES: Values and Types

## Introduction

Numeric, integer, character, logical — and special values. By the end of this lesson you will be able to: Identify core R types with class() and typeof(); Explain NA, NULL, NaN, and Inf; Describe automatic type coercion in vectors.

## Key Concepts

### 1. Identify core R types with class() and typeof()

Target: Identify core R types with class() and typeof(). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# Core types: numeric, integer, character, logical
print(class(3.14))         # "numeric"
print(class(42L))          # "integer" (L suffix)
print(class("hello"))      # "character"
print(class(TRUE))         # "logical"

```
### 2. Explain NA, NULL, NaN, and Inf

Target: Explain NA, NULL, NaN, and Inf. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# typeof() gives the lower-level type
print(typeof(3.14))        # "double"
print(typeof("hi"))        # "character"
print(typeof(TRUE))        # "logical"

```
### 3. Describe automatic type coercion in vectors

Target: Describe automatic type coercion in vectors. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# NA, NULL, NaN, and Inf — R's special values
x <- NA                     # missing value
print(is.na(x))             # TRUE
print(is.null(NULL))        # TRUE
print(0 / 0)                # NaN
print(1 / 0)                # Inf

```
### 4. Identify core R types with class() and typeof()

Target: Identify core R types with class() and typeof(). Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# Vectors hold one type; coercion happens automatically
mixed <- c(1, "two", 3)
print(mixed)                # "1" "two" "3" — everything became character
print(typeof(mixed))        # "character"

```

## Practice Questions

1. What is the key idea behind "Values and Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Values and Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Values and Types"
1. "Provide advanced patterns and performance considerations for Values and Types"

## Key Takeaways

- Master the core ideas of Values and Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
