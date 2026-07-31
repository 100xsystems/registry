---
{
  "title": "Variadics and Multiple Values",
  "description": "... variadics, select, multiple assignment, and defaults.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Collect arguments with ...",
    "Use select",
    "Swap and unpack values",
    "Apply defaults idiomatically"
  ],
  "knowledge_refs": [
    "lua/lua-13-variadic-multi"
  ],
  "prerequisites": [
    "LUA-12"
  ],
  "references": [
    {
      "title": "Lua — Variadic Functions",
      "url": "https://www.lua.org/manual/5.4/manual.html#6.1"
    },
    {
      "title": "PiL — Variadic Functions",
      "url": "https://www.lua.org/pil/5.2.html"
    },
    {
      "title": "Lua — select",
      "url": "https://www.lua.org/manual/5.4/manual.html#6.1"
    }
  ]
}
---

# LUA-13-VARIADIC-MULTI: Variadics and Multiple Values

## Introduction

... variadics, select, multiple assignment, and defaults. By the end of this lesson you will be able to: Collect arguments with ...; Use select; Swap and unpack values; Apply defaults idiomatically.

## Key Concepts

### 1. Collect arguments with ...

Target: Collect arguments with .... Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- Variable number of arguments and select
function first_and_last(...)
  local args = {...}
  return args[1], args[#args]
end

local first, last = first_and_last("a", "b", "c")
print(first, last)      -- a c

print(select("#", 1, 2, 3))    -- 3 — count of arguments
print(select(2, "a", "b", "c")) -- b c — from the 2nd on
```
### 2. Use select

Target: Use select. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- Multiple assignment and swapping
local a, b = 1, 2
print(a, b)            -- 1 2
a, b = b, a            -- swap!
print(a, b)            -- 2 1

local x, y, z = 1, 2    -- z is nil
print(x, y, z)          -- 1 2 nil

local _, second = table.unpack({10, 20, 30})
print(second)           -- 20 — _ discards the first
```
### 3. Swap and unpack values

Target: Swap and unpack values. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- Short-circuit evaluation
local a = nil
local result = a or "default"
print(result)          -- default

local b = 42
print(b and "set" or "unset")   -- set — common idiom

-- Chained defaults:
local config = {name = "Alice"}
local name = config.name or config.fallback or "anonymous"
print(name)            -- Alice
```
### 4. Apply defaults idiomatically

Target: Apply defaults idiomatically. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- The truthiness gotcha
-- In Lua, ONLY nil and false are falsy.
print(0 and "zero is truthy")      -- zero is truthy
print("" and "empty is truthy")    -- empty is truthy
print(nil and "never")             -- nil
print(false or "fallback")         -- fallback
-- This matters in conditions and defaults.
```

## Practice Questions

1. What is the key idea behind "Variadics and Multiple Values"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Variadics and Multiple Values with analogies and real-world examples"
1. "Show me common mistakes beginners make with Variadics and Multiple Values"
1. "Provide advanced patterns and performance considerations for Variadics and Multiple Values"

## Key Takeaways

- Master the core ideas of Variadics and Multiple Values through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
