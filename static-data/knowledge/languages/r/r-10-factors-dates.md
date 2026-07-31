---
{
  "title": "Factors, Dates, and Attributes",
  "description": "Categorical variables, ordered factors, and time handling.",
  "type": "lesson",
  "order": 10,
  "duration": 30,
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create and reorder factors",
    "Work with ordered factors",
    "Handle dates with as.Date and format"
  ],
  "knowledge_refs": [
    "r/r-10-factors-dates"
  ],
  "prerequisites": [
    "r-06-vectors-indexing"
  ],
  "references": [
    {
      "title": "An Introduction to R — Factors",
      "url": "https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Factors"
    },
    {
      "title": "R for Data Science — Dates and Times",
      "url": "https://r4ds.hadley.nz/datetimes"
    }
  ]
}
---

# R-10-FACTORS-DATES: Factors, Dates, and Attributes

## Introduction

Categorical variables, ordered factors, and time handling. By the end of this lesson you will be able to: Create and reorder factors; Work with ordered factors; Handle dates with as.Date and format.

## Key Concepts

### 1. Create and reorder factors

Target: Create and reorder factors. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# Factors: categorical variables with levels
sizes <- factor(c("S", "M", "L", "M"))
print(levels(sizes))        # "L" "M" "S"
print(table(sizes))         # counts per level

```
### 2. Work with ordered factors

Target: Work with ordered factors. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# Ordered factors preserve natural order
ratings <- factor(c("low", "high", "medium"),
                  levels = c("low", "medium", "high"),
                  ordered = TRUE)
print(ratings[2] > ratings[1])  # TRUE

```
### 3. Handle dates with as.Date and format

Target: Handle dates with as.Date and format. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# Dates and times: as.Date and POSIXct
d <- as.Date("2026-07-28")
print(d + 1)                # "2026-07-29"
print(format(d, "%A"))      # day of week

```
### 4. Create and reorder factors

Target: Create and reorder factors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# Attributes: metadata attached to objects
v <- 1:3
attr(v, "my_note") <- "hello"
print(attributes(v))        # my_note attribute

```

## Practice Questions

1. What is the key idea behind "Factors, Dates, and Attributes"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Factors, Dates, and Attributes with analogies and real-world examples"
1. "Show me common mistakes beginners make with Factors, Dates, and Attributes"
1. "Provide advanced patterns and performance considerations for Factors, Dates, and Attributes"

## Key Takeaways

- Master the core ideas of Factors, Dates, and Attributes through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
