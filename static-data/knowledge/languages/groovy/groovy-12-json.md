---
{
  "title": "JSON and XML",
  "description": "Data interchange.",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Parse JSON",
    "Generate JSON",
    "Parse XML",
    "Slurp structures"
  ],
  "knowledge_refs": [
    "groovy/groovy-12-json"
  ],
  "prerequisites": [
    "Groovy-11: File I/O"
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

# GROOVY-12-JSON: JSON and XML

## Introduction

Data interchange. By the end of this lesson you will be able to: Parse JSON; Generate JSON; Parse XML; Slurp structures.

## Key Concepts

### 1. Parse JSON

Target: Parse JSON. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
import groovy.json.JsonSlurper
def data = new JsonSlurper().parseText('{"name": "Ada"}')
println data.name
```
### 2. Generate JSON

Target: Generate JSON. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
import groovy.json.JsonOutput
println JsonOutput.toJson([name: "Ada", age: 36])
```
### 3. Parse XML

Target: Parse XML. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
import groovy.xml.XmlSlurper
def xml = new XmlSlurper().parseText("<a><b>x</b></a>")
println xml.b.text()
```
### 4. Slurp structures

Target: Slurp structures. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
import groovy.json.JsonBuilder
def json = new JsonBuilder()
json.person { name "Ada" }
println json
```

## Practice Questions

1. What is the key idea behind "JSON and XML"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain JSON and XML with analogies and real-world examples"
1. "Show me common mistakes beginners make with JSON and XML"
1. "Provide advanced patterns and performance considerations for JSON and XML"

## Key Takeaways

- Master the core ideas of JSON and XML through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
