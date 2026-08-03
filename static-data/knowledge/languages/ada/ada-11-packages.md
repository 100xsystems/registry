---
{
  "title": "Packages and Visibility",
  "description": "Spec/body separation and encapsulation.",
  "type": "lesson",
  "order": 11,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write package specifications",
    "Write package bodies",
    "Control visibility with private",
    "Use child packages"
  ],
  "knowledge_refs": [
    "ada/ada-11-packages"
  ],
  "prerequisites": [
    "Ada-10: Exceptions"
  ],
  "references": [
    {
      "title": "Ada Reference Manual",
      "url": "https://www.adaic.org/resources/add_content/standards/",
      "description": "The official language standard"
    },
    {
      "title": "Learn Ada",
      "url": "https://learn.adacore.com/",
      "description": "AdaCore official interactive course"
    },
    {
      "title": "Ada Programming (Wikibooks)",
      "url": "https://en.wikibooks.org/wiki/Ada_Programming",
      "description": "Community textbook"
    }
  ]
}
---

# ADA-11-PACKAGES: Packages and Visibility

## Introduction

Spec/body separation and encapsulation. By the end of this lesson you will be able to: Write package specifications; Write package bodies; Control visibility with private; Use child packages.

## Key Concepts

### 1. Write package specifications

Target: Write package specifications. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
package Greetings is
   procedure Hello;
end Greetings;
```
### 2. Write package bodies

Target: Write package bodies. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
package body Greetings is
   procedure Hello is
   begin
      Ada.Text_IO.Put_Line ("Hello!");
   end Hello;
end Greetings;
```
### 3. Control visibility with private

Target: Control visibility with private. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
package Counter is
private
   Value : Integer := 0;
end Counter;
```
### 4. Use child packages

Target: Use child packages. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
package Greetings.Friendly is
   procedure Hi;
end Greetings.Friendly;
```

## Practice Questions

1. What is the key idea behind "Packages and Visibility"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Packages and Visibility with analogies and real-world examples"
1. "Show me common mistakes beginners make with Packages and Visibility"
1. "Provide advanced patterns and performance considerations for Packages and Visibility"

## Key Takeaways

- Master the core ideas of Packages and Visibility through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
