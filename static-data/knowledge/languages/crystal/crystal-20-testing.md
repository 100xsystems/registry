---
{
  "title": "Testing with Spec",
  "description": "Unit and integration tests.",
  "type": "lesson",
  "order": 20,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write specs",
    "Use matchers",
    "Run crystal spec",
    "Test web endpoints"
  ],
  "knowledge_refs": [
    "crystal/crystal-20-testing"
  ],
  "prerequisites": [
    "Crystal-19: Database Access"
  ],
  "references": [
    {
      "title": "Crystal Language Reference",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official docs"
    },
    {
      "title": "Crystal for Rubyists",
      "url": "https://crystal-lang.org/reference/guides/faq.html",
      "description": "Migration guide"
    },
    {
      "title": "Crystal Book",
      "url": "https://crystal-lang.org/reference/",
      "description": "Official reference book"
    },
    {
      "title": "Crystal Forum",
      "url": "https://forum.crystal-lang.org/",
      "description": "Community"
    }
  ]
}
---

# CRYSTAL-20-TESTING: Testing with Spec

## Introduction

Unit and integration tests. By the end of this lesson you will be able to: Write specs; Use matchers; Run crystal spec; Test web endpoints.

## Key Concepts

### 1. Write specs

Target: Write specs. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
require "spec"

describe "math" do
  it "adds" do
    (2 + 2).should eq(4)
  end
end
```
### 2. Use matchers

Target: Use matchers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
it "works with strings" do
  "hello".should contain("ell")
end
```
### 3. Run crystal spec

Target: Run crystal spec. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
crystal spec
```
### 4. Test web endpoints

Target: Test web endpoints. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
describe "counter" do
  it "increments" do
    c = Counter.new
    c.increment!
    c.count.should eq(1)
  end
end
```

## Practice Questions

1. What is the key idea behind "Testing with Spec"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with Spec with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing with Spec"
1. "Provide advanced patterns and performance considerations for Testing with Spec"

## Key Takeaways

- Master the core ideas of Testing with Spec through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
