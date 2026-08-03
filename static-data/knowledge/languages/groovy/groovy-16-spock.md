---
{
  "title": "Testing with Spock",
  "description": "BDD-style testing framework.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write Spock specs",
    "Use given/when/then",
    "Use where blocks",
    "Mock collaborators"
  ],
  "knowledge_refs": [
    "groovy/groovy-16-spock"
  ],
  "prerequisites": [
    "Groovy-15: Gradle Builds"
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

# GROOVY-16-SPOCK: Testing with Spock

## Introduction

BDD-style testing framework. By the end of this lesson you will be able to: Write Spock specs; Use given/when/then; Use where blocks; Mock collaborators.

## Key Concepts

### 1. Write Spock specs

Target: Write Spock specs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```groovy
import spock.lang.Specification

class MathSpec extends Specification {
  def "addition works"() {
    expect:
    2 + 2 == 4
  }
}
```
### 2. Use given/when/then

Target: Use given/when/then. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```groovy
def "max returns larger"() {
  given:
  def a = 3
  def b = 5

  expect:
  Math.max(a, b) == 5
}
```
### 3. Use where blocks

Target: Use where blocks. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```groovy
def "sum of range"() {
  expect:
  (1..n).sum() == expected

  where:
  n  | expected
  1  | 1
  2  | 3
  3  | 6
}
```
### 4. Mock collaborators

Target: Mock collaborators. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```groovy
def "uses mocks"() {
  given:
  def service = Mock(Service)
  1 * service.call(_) >> "mocked"
}
```

## Practice Questions

1. What is the key idea behind "Testing with Spock"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with Spock with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing with Spock"
1. "Provide advanced patterns and performance considerations for Testing with Spock"

## Key Takeaways

- Master the core ideas of Testing with Spock through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
