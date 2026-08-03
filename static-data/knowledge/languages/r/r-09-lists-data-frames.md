---
{
  "title": "Lists, Matrices, and Data Frames",
  "description": "Heterogeneous containers and tabular data.",
  "type": "lesson",
  "order": 9,
  "duration": "35 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create and access lists with $ and [[]]",
    "Work with matrices",
    "Build and subset data frames"
  ],
  "knowledge_refs": [
    "r/r-09-lists-data-frames"
  ],
  "prerequisites": [
    "r-06-vectors-indexing"
  ],
  "references": [
    {
      "title": "An Introduction to R — Lists",
      "url": "https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Lists"
    },
    {
      "title": "An Introduction to R — Data Frames",
      "url": "https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Data-frames"
    },
    {
      "title": "R for Data Science — Data Frames",
      "url": "https://r4ds.hadley.nz/data-frame"
    }
  ]
}
---

# R-09-LISTS-DATA-FRAMES: Lists, Matrices, and Data Frames

## Introduction

Heterogeneous containers and tabular data. By the end of this lesson you will be able to: Create and access lists with $ and [[]]; Work with matrices; Build and subset data frames.

## Key Concepts

### 1. Create and access lists with $ and [[]]

Target: Create and access lists with $ and [[]]. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# Lists: containers that can hold any type
lst <- list(name = "Ada", age = 36, scores = c(90, 95))
print(lst$name)             # "Ada"
print(lst[[3]])             # 90 95 — double bracket extracts

```
### 2. Work with matrices

Target: Work with matrices. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# Accessing lists: $, [[]], and []
lst <- list(a = 1, b = 2)
print(lst[["a"]])           # 1 — the element itself
print(lst["a"])             # list of length 1

```
### 3. Build and subset data frames

Target: Build and subset data frames. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# Matrices: two-dimensional arrays
m <- matrix(1:6, nrow = 2, ncol = 3)
print(m)
#      [,1] [,2] [,3]
# [1,]    1    3    5
# [2,]    2    4    6
print(m[1, 2])              # 3

```
### 4. Create and access lists with $ and [[]]

Target: Create and access lists with $ and [[]]. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# Data frames: the heart of data analysis
df <- data.frame(
    name = c("Ada", "Grace"),
    age = c(36, 85)
)
print(df$name)              # "Ada" "Grace"
print(df[1, ])              # first row
print(df[df$age > 40, ])    # filter rows

```

## Practice Questions

1. What is the key idea behind "Lists, Matrices, and Data Frames"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lists, Matrices, and Data Frames with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lists, Matrices, and Data Frames"
1. "Provide advanced patterns and performance considerations for Lists, Matrices, and Data Frames"

## Key Takeaways

- Master the core ideas of Lists, Matrices, and Data Frames through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
