---
{
  "title": "File I/O",
  "description": "Reading and writing CSV, text, and modern formats.",
  "type": "lesson",
  "order": 16,
  "duration": 30,
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read CSVs with read.csv",
    "Write data with write.csv",
    "Read raw text with readLines"
  ],
  "knowledge_refs": [
    "r/r-16-file-io"
  ],
  "prerequisites": [
    "r-09-lists-data-frames"
  ],
  "references": [
    {
      "title": "R for Data Science — Data Import",
      "url": "https://r4ds.hadley.nz/data-import"
    },
    {
      "title": "readr — Documentation",
      "url": "https://readr.tidyverse.org/"
    },
    {
      "title": "jsonlite — Documentation",
      "url": "https://cran.r-project.org/web/packages/jsonlite/vignettes/json-aaquickstart.html"
    }
  ]
}
---

# R-16-FILE-IO: File I/O

## Introduction

Reading and writing CSV, text, and modern formats. By the end of this lesson you will be able to: Read CSVs with read.csv; Write data with write.csv; Read raw text with readLines.

## Key Concepts

### 1. Read CSVs with read.csv

Target: Read CSVs with read.csv. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# Reading data: read.csv and read.table
# df <- read.csv("data.csv")
# df <- read.csv("data.csv", stringsAsFactors = FALSE)
print("read.csv is the base-R workhorse")

```
### 2. Write data with write.csv

Target: Write data with write.csv. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# Writing data: write.csv
df <- data.frame(name = c("Ada", "Grace"), age = c(36, 85))
write.csv(df, "people.csv", row.names = FALSE)
print(read.csv("people.csv"))

```
### 3. Read raw text with readLines

Target: Read raw text with readLines. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# readLines for raw text files
lines <- readLines(textConnection(c("line one", "line two")))
print(lines)                # "line one" "line two"

```
### 4. Read CSVs with read.csv

Target: Read CSVs with read.csv. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# Working with JSON and CSV via packages
# library(jsonlite)
# data <- jsonlite::fromJSON("data.json")
# library(readr)
# df <- readr::read_csv("data.csv")
print("jsonlite and readr handle modern formats")

```

## Practice Questions

1. What is the key idea behind "File I/O"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain File I/O with analogies and real-world examples"
1. "Show me common mistakes beginners make with File I/O"
1. "Provide advanced patterns and performance considerations for File I/O"

## Key Takeaways

- Master the core ideas of File I/O through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
