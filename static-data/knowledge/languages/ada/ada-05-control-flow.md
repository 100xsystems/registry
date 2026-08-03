---
{
  "title": "Control Flow: if, case, loops",
  "description": "Conditionals, case statements, and loop forms.",
  "type": "lesson",
  "order": 5,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write if/elsif/else branches",
    "Use case statements",
    "Write all loop forms",
    "Use exit and loop labels"
  ],
  "knowledge_refs": [
    "ada/ada-05-control-flow"
  ],
  "prerequisites": [
    "Ada-04: Operators and Expressions"
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

# ADA-05-CONTROL-FLOW: Control Flow: if, case, loops

## Introduction

Conditionals, case statements, and loop forms. By the end of this lesson you will be able to: Write if/elsif/else branches; Use case statements; Write all loop forms; Use exit and loop labels.

## Key Concepts

### 1. Write if/elsif/else branches

Target: Write if/elsif/else branches. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ada
if score >= 90 then
   Ada.Text_IO.Put_Line ("A");
elsif score >= 80 then
   Ada.Text_IO.Put_Line ("B");
else
   Ada.Text_IO.Put_Line ("C");
end if;
```
### 2. Use case statements

Target: Use case statements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ada
case Direction is
   when North => Put ("N");
   when East  => Put ("E");
   when others => Put ("?");
end case;
```
### 3. Write all loop forms

Target: Write all loop forms. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ada
for i in 1 .. 10 loop
   Put (Integer'Image (i));
end loop;
```
### 4. Use exit and loop labels

Target: Use exit and loop labels. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ada
loop
   Get (Command);
   exit when Command = "quit";
end loop;
```

## Practice Questions

1. What is the key idea behind "Control Flow: if, case, loops"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow: if, case, loops with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow: if, case, loops"
1. "Provide advanced patterns and performance considerations for Control Flow: if, case, loops"

## Key Takeaways

- Master the core ideas of Control Flow: if, case, loops through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
