---
{
  "title": "Lists and Maps",
  "description": "Groovy collection literals.",
  "type": "lesson",
  "order": 4,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create lists",
    "Use list methods",
    "Create maps",
    "Iterate collections"
  ],
  "knowledge_refs": [
    "groovy/groovy-04-lists"
  ],
  "prerequisites": [
    "Groovy-03: Control Flow"
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

# GROOVY-04-LISTS: Lists and Maps

## Introduction

Groovy collection literals. By the end of this lesson you will be able to: Create lists; Use list methods; Create maps; Iterate collections.

## Key Concepts

### 1. Create lists

Target: Create lists. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
def nums = [1, 2, 3]
nums << 4
println nums
```
### 2. Use list methods

Target: Use list methods. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
def doubled = nums.collect { it * 2 }
```
### 3. Create maps

Target: Create maps. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
def person = [name: "Ada", age: 36]
println person.name
```
### 4. Iterate collections

Target: Iterate collections. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
person.each { k, v -> println "$k: $v" }
```

## Practice Questions

1. What is the key idea behind "Lists and Maps"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lists and Maps with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lists and Maps"
1. "Provide advanced patterns and performance considerations for Lists and Maps"

## Key Takeaways

- Master the core ideas of Lists and Maps through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
