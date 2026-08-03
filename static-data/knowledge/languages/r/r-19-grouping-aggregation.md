---
{
  "title": "Grouping and Aggregation",
  "description": "table, aggregate, split, and group_by + summarize.",
  "type": "lesson",
  "order": 19,
  "duration": "30 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Count categories with table()",
    "Compute group-wise means with aggregate()",
    "Use dplyr group_by + summarize"
  ],
  "knowledge_refs": [
    "r/r-19-grouping-aggregation"
  ],
  "prerequisites": [
    "r-11-apply-family"
  ],
  "references": [
    {
      "title": "R for Data Science — Groups",
      "url": "https://r4ds.hadley.nz/data-transform"
    },
    {
      "title": "An Introduction to R — tabulating",
      "url": "https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Grouping-loops-and-conditional-execution"
    }
  ]
}
---

# R-19-GROUPING-AGGREGATION: Grouping and Aggregation

## Introduction

table, aggregate, split, and group_by + summarize. By the end of this lesson you will be able to: Count categories with table(); Compute group-wise means with aggregate(); Use dplyr group_by + summarize.

## Key Concepts

### 1. Count categories with table()

Target: Count categories with table(). Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# Factors for grouping; table() for counts
colors <- factor(c("red", "blue", "red", "green"))
print(table(colors))
# blue  green   red
#    1      1     2

```
### 2. Compute group-wise means with aggregate()

Target: Compute group-wise means with aggregate(). Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# aggregate(): group-wise summaries the base way
df <- data.frame(group = c("a", "a", "b", "b"),
                 value = c(1, 2, 10, 20))
print(aggregate(value ~ group, data = df, FUN = mean))

```
### 3. Use dplyr group_by + summarize

Target: Use dplyr group_by + summarize. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# split(): divide a vector by groups
groups <- c("x", "y", "x", "y")
values <- c(1, 10, 2, 20)
print(split(values, groups))    # list of x-values and y-values

```
### 4. Count categories with table()

Target: Count categories with table(). Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# dplyr::group_by + summarize (tidyverse way)
# library(dplyr)
# df |> group_by(group) |> summarize(avg = mean(value))
print("group_by + summarize is the modern idiom")

```

## Practice Questions

1. What is the key idea behind "Grouping and Aggregation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Grouping and Aggregation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Grouping and Aggregation"
1. "Provide advanced patterns and performance considerations for Grouping and Aggregation"

## Key Takeaways

- Master the core ideas of Grouping and Aggregation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
