---
{
  "title": "Tables",
  "description": "Tables as arrays and maps, constructors, iteration, and the table library.",
  "type": "lesson",
  "order": 5,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use tables as arrays",
    "Use tables as dictionaries",
    "Iterate with pairs and ipairs",
    "Use the table library"
  ],
  "knowledge_refs": [
    "lua/lua-05-tables"
  ],
  "prerequisites": [
    "LUA-04"
  ],
  "references": [
    {
      "title": "Lua — Tables",
      "url": "https://www.lua.org/manual/5.4/manual.html#6.6"
    },
    {
      "title": "PiL — Tables",
      "url": "https://www.lua.org/pil/2.5.html"
    },
    {
      "title": "PiL — Table Library",
      "url": "https://www.lua.org/pil/19.html"
    }
  ]
}
---

# LUA-05-TABLES: Tables

## Introduction

Tables as arrays and maps, constructors, iteration, and the table library. By the end of this lesson you will be able to: Use tables as arrays; Use tables as dictionaries; Iterate with pairs and ipairs; Use the table library.

## Key Concepts

### 1. Use tables as arrays

Target: Use tables as arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- Tables: Lua's universal data structure
local arr = {10, 20, 30}          -- array-like
print(arr[1])                     -- 10 — 1-indexed!
print(#arr)                       -- 3 — length

local dict = {name = "Alice", age = 30}
print(dict.name)                  -- Alice
print(dict["age"])                -- 30
-- Tables are both arrays AND maps.
```
### 2. Use tables as dictionaries

Target: Use tables as dictionaries. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- Table constructors in detail
local t = {
  "first",                          -- t[1]
  "second",                         -- t[2]
  x = 1,                            -- t.x
  ["key with spaces"] = 2,          -- t["key with spaces"]
  nested = { inner = true },        -- t.nested.inner
}
print(t[1], t.x, t["key with spaces"])
print(t.nested.inner)              -- true
```
### 3. Iterate with pairs and ipairs

Target: Iterate with pairs and ipairs. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- Iterating tables
local t = {name = "Alice", age = 30, city = "NYC"}

-- pairs: any order
for k, v in pairs(t) do
  print(k, v)
end

-- ipairs: ordered, numeric keys only
local arr = {"a", "b", "c"}
for i, v in ipairs(arr) do
  print(i, v)
end
```
### 4. Use the table library

Target: Use the table library. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- Table library
local t = {3, 1, 2}
table.sort(t)
print(t[1], t[2], t[3])      -- 1 2 3

table.insert(t, 4)            -- append
table.remove(t, 1)            -- remove first
print(#t)                     -- 3

local concat = table.concat({1, 2, 3}, "-")
print(concat)                 -- 1-2-3
```

## Practice Questions

1. What is the key idea behind "Tables"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Tables with analogies and real-world examples"
1. "Show me common mistakes beginners make with Tables"
1. "Provide advanced patterns and performance considerations for Tables"

## Key Takeaways

- Master the core ideas of Tables through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
