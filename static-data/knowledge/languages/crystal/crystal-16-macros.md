---
{
  "title": "Macros",
  "description": "Compile-time metaprogramming.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write macros",
    "Use macro methods",
    "Generate code",
    "Inspect types"
  ],
  "knowledge_refs": [
    "crystal/crystal-16-macros"
  ],
  "prerequisites": [
    "Crystal-15: Fibers and Channels"
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

# CRYSTAL-16-MACROS: Macros

## Introduction

Compile-time metaprogramming. By the end of this lesson you will be able to: Write macros; Use macro methods; Generate code; Inspect types.

## Key Concepts

### 1. Write macros

Target: Write macros. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```crystal
macro define_getter(name)
  def {{name.id}}
    @{{name.id}}
  end
end

class Person
  @name = "Ada"
  define_getter(name)
end

puts Person.new.name
```
### 2. Use macro methods

Target: Use macro methods. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```crystal
macro hello
  "hello from macro"
end

puts hello
```
### 3. Generate code

Target: Generate code. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```crystal
macro assert_not_nil(expr)
  {% if expr.is_a?(NilLiteral) %}
    raise "nil detected"
  {% end %}
end
```
### 4. Inspect types

Target: Inspect types. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```crystal
macro list_methods(klass)
  {{ klass.methods.map(&.name.stringify) }}
end
```

## Practice Questions

1. What is the key idea behind "Macros"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Macros with analogies and real-world examples"
1. "Show me common mistakes beginners make with Macros"
1. "Provide advanced patterns and performance considerations for Macros"

## Key Takeaways

- Master the core ideas of Macros through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
