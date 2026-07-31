---
{
  "title": "Values and Types",
  "description": "Numbers, strings, the string library, booleans, and nil.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Do arithmetic with integers and floats",
    "Create and format strings",
    "Use the string library",
    "Understand truthiness"
  ],
  "knowledge_refs": [
    "lua/lua-02-values-types"
  ],
  "prerequisites": [
    "LUA-01"
  ],
  "references": [
    {
      "title": "Lua — Types",
      "url": "https://www.lua.org/manual/5.4/manual.html#2.1"
    },
    {
      "title": "Lua — String Library",
      "url": "https://www.lua.org/manual/5.4/manual.html#6.4"
    },
    {
      "title": "PiL — Types and Values",
      "url": "https://www.lua.org/pil/2.html"
    }
  ]
}
---

# LUA-02-VALUES-TYPES: Values and Types

## Introduction

Numbers, strings, the string library, booleans, and nil. By the end of this lesson you will be able to: Do arithmetic with integers and floats; Create and format strings; Use the string library; Understand truthiness.

## Key Concepts

### 1. Do arithmetic with integers and floats

Target: Do arithmetic with integers and floats. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- Numbers: integers and floats
print(10)             -- 10
print(3.14)           -- 3.14
print(10 / 3)         -- 3.3333333333333 (float division)
print(10 // 3)        -- 3 (floor division, Lua 5.3+)
print(10 % 3)         -- 1 (remainder)
print(2 ^ 10)         -- 1024.0 (exponent)
print(math.floor(3.7)) -- 3
print(math.maxinteger) -- largest integer
```
### 2. Create and format strings

Target: Create and format strings. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- Strings: quotes, escapes, and long brackets
local s1 = "double"
local s2 = 'single'
local s3 = [[long
string
here]]
print(s1, s2)
print(#s3)            -- 15 — multiline long string
print("line\nbreak")  -- escape sequences work
```
### 3. Use the string library

Target: Use the string library. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- String library
local s = "Hello, Lua"
print(string.upper(s))     -- HELLO, LUA
print(string.lower(s))     -- hello, lua
print(string.len(s))       -- 10
print(string.sub(s, 1, 5)) -- Hello
print(string.rep("ab", 3)) -- ababab
print(string.format("%d-%02d", 2026, 7))  -- 2026-07
```
### 4. Understand truthiness

Target: Understand truthiness. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- Booleans and nil
print(true)           -- true
print(false)          -- false
print(nil)            -- nil
local a               -- a is nil
print(a)              -- nil
-- Only false and nil are falsy; 0 and "" are truthy!
if 0 then print("0 is truthy") end
if "" then print("empty string is truthy") end
```

## Practice Questions

1. What is the key idea behind "Values and Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Values and Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Values and Types"
1. "Provide advanced patterns and performance considerations for Values and Types"

## Key Takeaways

- Master the core ideas of Values and Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
