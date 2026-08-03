---
{
  "title": "Iterators",
  "description": "Custom iteration.",
  "type": "lesson",
  "order": 14,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Implement Iterator",
    "Use iterator methods",
    "Build lazy sequences",
    "Use for with iterators"
  ],
  "knowledge_refs": [
    "haxe/haxe-14-iterators"
  ],
  "prerequisites": [
    "Haxe-13: Exceptions"
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

# HAXE-14-ITERATORS: Iterators

## Introduction

Custom iteration. By the end of this lesson you will be able to: Implement Iterator; Use iterator methods; Build lazy sequences; Use for with iterators.

## Key Concepts

### 1. Implement Iterator

Target: Implement Iterator. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```haxe
class Counter {
  var max:Int;
  public function new(m:Int) max = m;
  public function iterator() return new CounterIter(max);
}

class CounterIter {
  var current:Int = 0;
  var max:Int;
  public function new(m:Int) max = m;
  public function hasNext() return current < max;
  public function next() return current++;
}
```
### 2. Use iterator methods

Target: Use iterator methods. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```haxe
for (i in new Counter(3)) trace(i);
```
### 3. Build lazy sequences

Target: Build lazy sequences. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```haxe
class Doubler {
  public function iterator() { ... }
}
```
### 4. Use for with iterators

Target: Use for with iterators. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```haxe
// lambdas: [1,2,3].filter(n -> n > 1)
```

## Practice Questions

1. What is the key idea behind "Iterators"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Iterators with analogies and real-world examples"
1. "Show me common mistakes beginners make with Iterators"
1. "Provide advanced patterns and performance considerations for Iterators"

## Key Takeaways

- Master the core ideas of Iterators through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
