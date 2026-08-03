---
{
  "title": "Testing",
  "description": "Unit tests with munit.",
  "type": "lesson",
  "order": 20,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Set up munit",
    "Write tests",
    "Run tests",
    "Test across targets"
  ],
  "knowledge_refs": [
    "haxe/haxe-20-testing"
  ],
  "prerequisites": [
    "Haxe-19: Haxe on Node.js"
  ],
  "references": [
    {
      "title": "Haxe Documentation",
      "url": "https://haxe.org/documentation/",
      "description": "Official docs"
    },
    {
      "title": "Haxe Manual",
      "url": "https://haxe.org/manual/introduction.html",
      "description": "The language manual"
    },
    {
      "title": "Haxe Cookbook",
      "url": "https://code.haxe.org/",
      "description": "Community recipes"
    }
  ]
}
---

# HAXE-20-TESTING: Testing

## Introduction

Unit tests with munit. By the end of this lesson you will be able to: Set up munit; Write tests; Run tests; Test across targets.

## Key Concepts

### 1. Set up munit

Target: Set up munit. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
haxelib install munit
haxelib run munit test
```
### 2. Write tests

Target: Write tests. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
class MyTest extends haxe.unit.TestCase {
  public function testAdd() {
    assertEquals(4, 2 + 2);
  }
}
```
### 3. Run tests

Target: Run tests. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
var runner = new haxe.unit.TestRunner();
runner.add(new MyTest());
runner.run();
```
### 4. Test across targets

Target: Test across targets. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
assertEquals("HI", "hi".toUpperCase());
```

## Practice Questions

1. What is the key idea behind "Testing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing"
1. "Provide advanced patterns and performance considerations for Testing"

## Key Takeaways

- Master the core ideas of Testing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
