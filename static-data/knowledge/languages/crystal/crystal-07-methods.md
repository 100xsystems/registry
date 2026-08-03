---
{
  "title": "Methods",
  "description": "Define methods with args and returns.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write methods",
    "Use default arguments",
    "Use named arguments",
    "Return values"
  ],
  "knowledge_refs": [
    "crystal/crystal-07-methods"
  ],
  "prerequisites": [
    "Crystal-06: Hashes and Sets"
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

# CRYSTAL-07-METHODS: Methods

## Introduction

Define methods with args and returns. By the end of this lesson you will be able to: Write methods; Use default arguments; Use named arguments; Return values.

## Key Concepts

### 1. Write methods

Target: Write methods. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
def add(a, b)
  a + b
end

puts add(2, 3)
```
### 2. Use default arguments

Target: Use default arguments. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
def greet(name, excited = false)
  excited ? "HI #{name.upcase}!" : "hi #{name}"
end
```
### 3. Use named arguments

Target: Use named arguments. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
def pow(base, exp)
  base ** exp
end

puts pow(base: 2, exp: 8)
```
### 4. Return values

Target: Return values. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
def describe(x : Int32 | String)
  case x
  when Int32 then "number #{x}"
  else "string #{x}"
  end
end
```

## Practice Questions

1. What is the key idea behind "Methods"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Methods with analogies and real-world examples"
1. "Show me common mistakes beginners make with Methods"
1. "Provide advanced patterns and performance considerations for Methods"

## Key Takeaways

- Master the core ideas of Methods through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
