---
{
  "title": "Templates",
  "description": "Text and HTML generation.",
  "type": "lesson",
  "order": 14,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use SimpleTemplateEngine",
    "Use GString templates",
    "Build HTML",
    "Render views"
  ],
  "knowledge_refs": [
    "groovy/groovy-14-templates"
  ],
  "prerequisites": [
    "Groovy-13: Scripting and groovysh"
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

# GROOVY-14-TEMPLATES: Templates

## Introduction

Text and HTML generation. By the end of this lesson you will be able to: Use SimpleTemplateEngine; Use GString templates; Build HTML; Render views.

## Key Concepts

### 1. Use SimpleTemplateEngine

Target: Use SimpleTemplateEngine. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
import groovy.text.SimpleTemplateEngine

def engine = new SimpleTemplateEngine()
def template = engine.createTemplate("Hello, \$name").make([name: "Ada"])
println template
```
### 2. Use GString templates

Target: Use GString templates. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
def tpl = "Hi $name, you are $age"
def out = new SimpleTemplateEngine().createTemplate(tpl).make(name: "Ada", age: 36)
println out
```
### 3. Build HTML

Target: Build HTML. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
def html = "<ul>${items.collect { "<li>$it</li>" }.join()}</ul>"
```
### 4. Render views

Target: Render views. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
engine.createTemplate(file).make(binding)
```

## Practice Questions

1. What is the key idea behind "Templates"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Templates with analogies and real-world examples"
1. "Show me common mistakes beginners make with Templates"
1. "Provide advanced patterns and performance considerations for Templates"

## Key Takeaways

- Master the core ideas of Templates through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
