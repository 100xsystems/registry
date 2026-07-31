---
{
  "title": "Performance",
  "description": "Locals, table allocation, string building, and data structures.",
  "type": "lesson",
  "order": 19,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use locals for speed",
    "Preallocate tables",
    "Build strings with table.concat",
    "Choose the right structure"
  ],
  "knowledge_refs": [
    "lua/lua-19-performance"
  ],
  "prerequisites": [
    "LUA-18"
  ],
  "references": [
    {
      "title": "Lua — Performance Tips",
      "url": "https://www.lua.org/gems/sample.pdf"
    },
    {
      "title": "LuaJIT — performance",
      "url": "https://luajit.org/performance.html"
    },
    {
      "title": "PiL — Efficiency",
      "url": "https://www.lua.org/pil/11.html"
    }
  ]
}
---

# LUA-19-PERFORMANCE: Performance

## Introduction

Locals, table allocation, string building, and data structures. By the end of this lesson you will be able to: Use locals for speed; Preallocate tables; Build strings with table.concat; Choose the right structure.

## Key Concepts

### 1. Use locals for speed

Target: Use locals for speed. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- Performance: locals are faster
local sum = 0
local start = os.clock()
for i = 1, 10000000 do
  sum = sum + i
end
print("sum: " .. sum)
print("time: " .. (os.clock() - start) .. "s")
-- Local variables avoid global table lookups.
```
### 2. Preallocate tables

Target: Preallocate tables. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- Avoiding table reallocation
-- Pre-allocate array tables with the length hint:
local t = {}
for i = 1, 100000 do
  t[i] = i
end
print(#t)
-- Avoid growing tables one element at a time in hot loops
-- when you know the size ahead of time.
```
### 3. Build strings with table.concat

Target: Build strings with table.concat. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- String building: table.concat beats ..
local parts = {}
for i = 1, 1000 do
  parts[i] = "item " .. i
end
local joined = table.concat(parts, ", ")
print(#joined)
-- Repeated .. creates many intermediate strings;
-- table.concat builds one result efficiently.
```
### 4. Choose the right structure

Target: Choose the right structure. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- Choosing data structures
print("Arrays: table with 1..n integer keys")
print("Sets: table with keys, values ignored")
print("Queues: table.remove(t, 1) for FIFO")
print("Maps: table with any keys")
local set = {}
set["apple"] = true
set["banana"] = true
print(set["apple"] and "apple in set")   -- apple in set
print(set["cherry"] and "cherry in set") -- nil (not present)
```

## Practice Questions

1. What is the key idea behind "Performance"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Performance with analogies and real-world examples"
1. "Show me common mistakes beginners make with Performance"
1. "Provide advanced patterns and performance considerations for Performance"

## Key Takeaways

- Master the core ideas of Performance through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
