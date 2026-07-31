---
{
  "title": "Testing with Minitest",
  "description": "assertions, test classes, describe/it, mocks.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write Minitest test classes",
    "Use assertions effectively",
    "Use describe/it style",
    "Mock collaborators"
  ],
  "knowledge_refs": [
    "ruby/ruby-19-testing"
  ],
  "prerequisites": [
    "RUBY-18"
  ],
  "references": [
    {
      "title": "Minitest Documentation",
      "url": "https://docs.seattlerb.org/minitest/"
    },
    {
      "title": "Ruby — Minitest Guide",
      "url": "https://www.ruby-lang.org/en/documentation/"
    },
    {
      "title": "Minitest GitHub",
      "url": "https://github.com/minitest/minitest"
    }
  ]
}
---

# RUBY-19-TESTING: Testing with Minitest

## Introduction

assertions, test classes, describe/it, mocks. By the end of this lesson you will be able to: Write Minitest test classes; Use assertions effectively; Use describe/it style; Mock collaborators.

## Key Concepts

### 1. Write Minitest test classes

Target: Write Minitest test classes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
# minitest
require "minitest/autorun"
class TestCalc < Minitest::Test
  def test_addition
    assert_equal 5, 2 + 3
  end
  def test_truthy
    assert 1 == 1
  end
end
```
### 2. Use assertions effectively

Target: Use assertions effectively. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
# assert basics
require "minitest/autorun"
class TestArray < Minitest::Test
  def test_sort
    assert_equal [1, 2, 3], [3, 1, 2].sort
    refute [1].empty?
    assert_includes [1, 2], 2
  end
end
```
### 3. Use describe/it style

Target: Use describe/it style. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
# describe/it style
require "minitest/autorun"
describe "String" do
  it "upcases" do
    _("hi".upcase).must_equal "HI"
  end
end
```
### 4. Mock collaborators

Target: Mock collaborators. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
# testing with mocks
require "minitest/autorun"
class Service
  def initialize(client); @client = client; end
  def run; @client.fetch("key"); end
end
describe Service do
  it "delegates" do
    client = Minitest::Mock.new
    client.expect(:fetch, "value", ["key"])
    assert_equal "value", Service.new(client).run
  end
end
```

## Practice Questions

1. What is the key idea behind "Testing with Minitest"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with Minitest with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing with Minitest"
1. "Provide advanced patterns and performance considerations for Testing with Minitest"

## Key Takeaways

- Master the core ideas of Testing with Minitest through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
