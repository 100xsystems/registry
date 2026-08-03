---
{
  "title": "Web Development with Grails",
  "description": "Full-stack web framework.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create Grails apps",
    "Define controllers",
    "Define domain classes",
    "Render views"
  ],
  "knowledge_refs": [
    "groovy/groovy-17-grails"
  ],
  "prerequisites": [
    "Groovy-16: Testing with Spock"
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

# GROOVY-17-GRAILS: Web Development with Grails

## Introduction

Full-stack web framework. By the end of this lesson you will be able to: Create Grails apps; Define controllers; Define domain classes; Render views.

## Key Concepts

### 1. Create Grails apps

Target: Create Grails apps. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
grails create-app myapp
```
### 2. Define controllers

Target: Define controllers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
class PersonController {
  def index() {
    [people: Person.list()]
  }
}
```
### 3. Define domain classes

Target: Define domain classes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
class Person {
  String name
  Integer age
  static constraints = {
    name blank: false
  }
}
```
### 4. Render views

Target: Render views. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
grails run-app
```

## Practice Questions

1. What is the key idea behind "Web Development with Grails"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Web Development with Grails with analogies and real-world examples"
1. "Show me common mistakes beginners make with Web Development with Grails"
1. "Provide advanced patterns and performance considerations for Web Development with Grails"

## Key Takeaways

- Master the core ideas of Web Development with Grails through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
