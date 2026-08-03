---
{
  "title": "String Handling",
  "description": "String methods and templates.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use string methods",
    "Interpolate GStrings",
    "Split and join",
    "Use regex operators"
  ],
  "knowledge_refs": [
    "groovy/groovy-06-strings"
  ],
  "prerequisites": [
    "Groovy-05: Closures"
  ],
  "references": [
    {
      "title": "Groovy Documentation",
      "url": "https://groovy-lang.org/documentation.html",
      "description": "Official docs"
    },
    {
      "title": "Groovy Tutorial (Groovy-lang)",
      "url": "https://groovy-lang.org/single-page-documentation.html",
      "description": "Official reference"
    },
    {
      "title": "Groovy in Action",
      "url": "https://www.manning.com/books/groovy-in-action-second-edition",
      "description": "Book"
    }
  ]
}
---

# GROOVY-06-STRINGS: String Handling

## Introduction

String methods and templates. By the end of this lesson you will be able to: Use string methods; Interpolate GStrings; Split and join; Use regex operators.

## Key Concepts

### 1. Use string methods

Target: Use string methods. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
def s = "hello world"
println s.length()
println s.toUpperCase()
```
### 2. Interpolate GStrings

Target: Interpolate GStrings. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
def name = "Ada"
println "Hi $name"
```
### 3. Split and join

Target: Split and join. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
println "a,b,c".split(",").join(" | ")
```
### 4. Use regex operators

Target: Use regex operators. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
def text = "hello 123"
assert text ==~ /.*\d+.*/
```

## Practice Questions

1. What is the key idea behind "String Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain String Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with String Handling"
1. "Provide advanced patterns and performance considerations for String Handling"

## Key Takeaways

- Master the core ideas of String Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
