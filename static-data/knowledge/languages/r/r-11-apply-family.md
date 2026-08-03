---
{
  "title": "The Apply Family",
  "description": "apply, lapply, sapply, tapply, and friends.",
  "type": "lesson",
  "order": 11,
  "duration": "35 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Apply functions over rows and columns",
    "Simplify lists with sapply",
    "Compute group-wise summaries with tapply"
  ],
  "knowledge_refs": [
    "r/r-11-apply-family"
  ],
  "prerequisites": [
    "r-05-functions"
  ],
  "references": [
    {
      "title": "R for Data Science — The map functions",
      "url": "https://r4ds.hadley.nz/iteration"
    },
    {
      "title": "An Introduction to R — apply family",
      "url": "https://cran.r-project.org/doc/manuals/r-release/R-intro.html#The-function-apply"
    }
  ]
}
---

# R-11-APPLY-FAMILY: The Apply Family

## Introduction

apply, lapply, sapply, tapply, and friends. By the end of this lesson you will be able to: Apply functions over rows and columns; Simplify lists with sapply; Compute group-wise summaries with tapply.

## Key Concepts

### 1. Apply functions over rows and columns

Target: Apply functions over rows and columns. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# apply family: apply, lapply, sapply, tapply
m <- matrix(1:6, nrow = 2)
print(apply(m, 1, sum))     # row sums: 9 12
print(apply(m, 2, sum))     # col sums: 3 7 11

```
### 2. Simplify lists with sapply

Target: Simplify lists with sapply. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# lapply returns a list; sapply simplifies
print(lapply(c(1, 2, 3), function(x) x^2))  # list
print(sapply(c(1, 2, 3), function(x) x^2))  # 1 4 9 (vector)

```
### 3. Compute group-wise summaries with tapply

Target: Compute group-wise summaries with tapply. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# tapply: group-wise operations
groups <- c("a", "a", "b", "b")
values <- c(1, 2, 10, 20)
print(tapply(values, groups, mean))  # a: 1.5, b: 15

```
### 4. Apply functions over rows and columns

Target: Apply functions over rows and columns. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# Reduce, Filter, and Map
nums <- c(1, 2, 3, 4, 5)
print(Filter(function(x) x %% 2 == 0, nums))   # 2 4
print(Reduce(`+`, nums))                       # 15
print(Map(function(x) x * 10, nums))           # list of 10 20 ...

```

## Practice Questions

1. What is the key idea behind "The Apply Family"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain The Apply Family with analogies and real-world examples"
1. "Show me common mistakes beginners make with The Apply Family"
1. "Provide advanced patterns and performance considerations for The Apply Family"

## Key Takeaways

- Master the core ideas of The Apply Family through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
