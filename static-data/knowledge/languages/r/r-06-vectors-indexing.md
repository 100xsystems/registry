---
{
  "title": "Vectors and Indexing",
  "description": "Atomic vectors, naming, logical subsetting, and sequences.",
  "type": "lesson",
  "order": 6,
  "duration": 30,
  "difficulty": "beginner",
  "learning_objectives": [
    "Create and index vectors (1-based indexing)",
    "Name vector elements",
    "Filter with logical subsetting"
  ],
  "knowledge_refs": [
    "r/r-06-vectors-indexing"
  ],
  "prerequisites": [
    "r-02-values-types"
  ],
  "references": [
    {
      "title": "An Introduction to R — Vectors",
      "url": "https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Vectors-and-assignment"
    },
    {
      "title": "R for Data Science — Subsetting",
      "url": "https://r4ds.hadley.nz/subset"
    }
  ]
}
---

# R-06-VECTORS-INDEXING: Vectors and Indexing

## Introduction

Atomic vectors, naming, logical subsetting, and sequences. By the end of this lesson you will be able to: Create and index vectors (1-based indexing); Name vector elements; Filter with logical subsetting.

## Key Concepts

### 1. Create and index vectors (1-based indexing)

Target: Create and index vectors (1-based indexing). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# Vectors: the fundamental data structure
v <- c(10, 20, 30, 40)
print(v[1])                 # 10 — indexing starts at 1!
print(v[2:3])               # 20 30
print(v[c(1, 4)])           # 10 40

```
### 2. Name vector elements

Target: Name vector elements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# Named vectors
scores <- c(ada = 95, grace = 88, linus = 91)
print(scores["ada"])        # ada: 95
print(names(scores))        # "ada" "grace" "linus"

```
### 3. Filter with logical subsetting

Target: Filter with logical subsetting. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# Logical subsetting — the idiomatic R pattern
ages <- c(25, 40, 33, 60)
print(ages[ages > 30])      # 40 33 60
print(which(ages > 30))     # 2 3 4

```
### 4. Create and index vectors (1-based indexing)

Target: Create and index vectors (1-based indexing). Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# seq(), rep(), and colon operator
print(1:5)                  # 1 2 3 4 5
print(seq(1, 10, by = 2))   # 1 3 5 7 9
print(rep("x", 3))          # "x" "x" "x"

```

## Practice Questions

1. What is the key idea behind "Vectors and Indexing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Vectors and Indexing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Vectors and Indexing"
1. "Provide advanced patterns and performance considerations for Vectors and Indexing"

## Key Takeaways

- Master the core ideas of Vectors and Indexing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
