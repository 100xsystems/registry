---
{
  "title": "Metaprogramming",
  "description": "Runtime method magic.",
  "type": "lesson",
  "order": 9,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use methodMissing",
    "Use propertyMissing",
    "Add dynamic methods",
    "Use Expando"
  ],
  "knowledge_refs": [
    "groovy/groovy-09-metaprogramming"
  ],
  "prerequisites": [
    "Groovy-08: Safe Navigation and Null Handling"
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

# GROOVY-09-METAPROGRAMMING: Metaprogramming

## Introduction

Runtime method magic. By the end of this lesson you will be able to: Use methodMissing; Use propertyMissing; Add dynamic methods; Use Expando.

## Key Concepts

### 1. Use methodMissing

Target: Use methodMissing. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
class Dynamic {
  def methodMissing(String name, args) {
    "called $name with $args"
  }
}

println new Dynamic().anything(1, 2)
```
### 2. Use propertyMissing

Target: Use propertyMissing. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
class Flex {
  def propertyMissing(String name) { "missing: $name" }
}
println new Flex().someProp
```
### 3. Add dynamic methods

Target: Add dynamic methods. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
def e = new Expando()
e.dynamicMethod = { println "hi" }
e.dynamicMethod()
```
### 4. Use Expando

Target: Use Expando. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
String.metaClass.shout = { delegate.toUpperCase() }
println "hello".shout()
```

## Practice Questions

1. What is the key idea behind "Metaprogramming"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Metaprogramming with analogies and real-world examples"
1. "Show me common mistakes beginners make with Metaprogramming"
1. "Provide advanced patterns and performance considerations for Metaprogramming"

## Key Takeaways

- Master the core ideas of Metaprogramming through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
