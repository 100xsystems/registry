---
{
  "title": "Getting Started with Lua",
  "description": "Installing, printing, variables, and comments.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write and run a Lua script",
    "Use basic expressions",
    "Declare global and local variables",
    "Write comments"
  ],
  "knowledge_refs": [
    "lua/lua-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "Lua — Getting Started",
      "url": "https://www.lua.org/start.html"
    },
    {
      "title": "Lua — Reference Manual",
      "url": "https://www.lua.org/manual/5.4/"
    },
    {
      "title": "Programming in Lua (PiL)",
      "url": "https://www.lua.org/pil/"
    }
  ]
}
---

# LUA-01-GETTING-STARTED: Getting Started with Lua

## Introduction

Installing, printing, variables, and comments. By the end of this lesson you will be able to: Write and run a Lua script; Use basic expressions; Declare global and local variables; Write comments.

## Key Concepts

### 1. Write and run a Lua script

Target: Write and run a Lua script. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- Your first Lua program
print("Hello, 100X Systems!")
-- run: lua hello.lua   ->   Hello, 100X Systems!
-- Lua is a lightweight, embeddable scripting language.
```
### 2. Use basic expressions

Target: Use basic expressions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- The Lua interpreter and basic expressions
print(1 + 2)          -- 3
print(6 * 7)          -- 42
print("Hello" .. " " .. "Lua")   -- string concatenation
print(#"hello")       -- 5 — the length operator
-- Run interactively with: lua -i
```
### 3. Declare global and local variables

Target: Declare global and local variables. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- Variables: global by default
x = 10                -- global variable
local y = 20          -- local variable (preferred)
print(x + y)          -- 30
-- Locals are faster and scoped to their block.
```
### 4. Write comments

Target: Write comments. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- Comments and basic structure
-- line comment
--[[ block comment
     spanning multiple lines ]]
print("comments done")
-- Lua has no semicolon requirement; they are optional.
```

## Practice Questions

1. What is the key idea behind "Getting Started with Lua"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Lua with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Lua"
1. "Provide advanced patterns and performance considerations for Getting Started with Lua"

## Key Takeaways

- Master the core ideas of Getting Started with Lua through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
