---
{
  "title": "Strings and Text",
  "description": "paste, sprintf, string functions, and regular expressions.",
  "type": "lesson",
  "order": 8,
  "duration": 25,
  "difficulty": "beginner",
  "learning_objectives": [
    "Build strings with paste and sprintf",
    "Manipulate strings with base functions",
    "Use regular expressions with grep and gsub"
  ],
  "knowledge_refs": [
    "r/r-08-strings-text"
  ],
  "prerequisites": [
    "r-02-values-types"
  ],
  "references": [
    {
      "title": "R for Data Science — Strings",
      "url": "https://r4ds.hadley.nz/strings"
    },
    {
      "title": "stringr — Tidyverse Docs",
      "url": "https://stringr.tidyverse.org/"
    }
  ]
}
---

# R-08-STRINGS-TEXT: Strings and Text

## Introduction

paste, sprintf, string functions, and regular expressions. By the end of this lesson you will be able to: Build strings with paste and sprintf; Manipulate strings with base functions; Use regular expressions with grep and gsub.

## Key Concepts

### 1. Build strings with paste and sprintf

Target: Build strings with paste and sprintf. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```r
# Strings: paste, paste0, and sprintf
print(paste("Hello", "R"))          # "Hello R"
print(paste0("Hello", "R"))         # "HelloR"
print(sprintf("%s scored %d", "Ada", 95))  # "Ada scored 95"

```
### 2. Manipulate strings with base functions

Target: Manipulate strings with base functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```r
# String manipulation: nchar, toupper, tolower
s <- "Hello, R"
print(nchar(s))             # 8
print(toupper(s))           # "HELLO, R"
print(tolower(s))           # "hello, r"

```
### 3. Use regular expressions with grep and gsub

Target: Use regular expressions with grep and gsub. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```r
# substring, substr, strsplit
s <- "a-b-c"
print(strsplit(s, "-")[[1]])    # "a" "b" "c"
print(substr("abcdef", 2, 4))   # "bcd"

```
### 4. Build strings with paste and sprintf

Target: Build strings with paste and sprintf. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```r
# Regular expressions: grep, gsub, grepl
text <- c("cat", "car", "dog")
print(grepl("ca", text))        # TRUE TRUE FALSE
print(gsub("a", "o", "banana")) # "bonono"

```

## Practice Questions

1. What is the key idea behind "Strings and Text"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings and Text with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings and Text"
1. "Provide advanced patterns and performance considerations for Strings and Text"

## Key Takeaways

- Master the core ideas of Strings and Text through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
