---
{
  "title": "Metatables",
  "description": "__index, __newindex, operator metamethods, and __tostring.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Customize lookup with __index",
    "Intercept assignment with __newindex",
    "Overload operators",
    "Customize printing with __tostring"
  ],
  "knowledge_refs": [
    "lua/lua-06-metatables"
  ],
  "prerequisites": [
    "LUA-05"
  ],
  "references": [
    {
      "title": "Lua — Metatables",
      "url": "https://www.lua.org/manual/5.4/manual.html#2.4"
    },
    {
      "title": "PiL — Metatables",
      "url": "https://www.lua.org/pil/13.html"
    },
    {
      "title": "Lua — Metamethods list",
      "url": "https://www.lua.org/manual/5.4/manual.html#6.1"
    }
  ]
}
---

# LUA-06-METATABLES: Metatables

## Introduction

__index, __newindex, operator metamethods, and __tostring. By the end of this lesson you will be able to: Customize lookup with __index; Intercept assignment with __newindex; Overload operators; Customize printing with __tostring.

## Key Concepts

### 1. Customize lookup with __index

Target: Customize lookup with __index. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- Metatables: customize table behavior
local mt = {}
mt.__index = function(table, key)
  return "default for " .. key
end

local t = setmetatable({}, mt)
print(t.missing)     -- default for missing
-- __index is called when a key is not found.
```
### 2. Intercept assignment with __newindex

Target: Intercept assignment with __newindex. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- __index with a fallback table (inheritance)
local base = {greeting = "Hello"}
local child = setmetatable({}, {__index = base})
print(child.greeting)   -- Hello — inherited from base

-- __newindex: intercept new key assignment
local track = setmetatable({}, {
  __newindex = function(t, k, v)
    print("setting " .. k .. " = " .. tostring(v))
    rawset(t, k, v)
  end
})
track.name = "Alice"    -- setting name = Alice
```
### 3. Overload operators

Target: Overload operators. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- Operator metamethods
local Point = {}
Point.__add = function(a, b)
  return {x = a.x + b.x, y = a.y + b.y}
end

local p1 = setmetatable({x = 1, y = 2}, Point)
local p2 = setmetatable({x = 10, y = 20}, Point)
local p3 = p1 + p2        -- uses __add
print(p3.x, p3.y)         -- 11 22
-- Other metamethods: __sub, __mul, __eq, __lt, __tostring, ...
```
### 4. Customize printing with __tostring

Target: Customize printing with __tostring. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- __tostring: custom printing
local Account = {}
Account.__tostring = function(self)
  return "Account(" .. self.owner .. ", $" .. self.balance .. ")"
end

local acc = setmetatable({owner = "Alice", balance = 100}, Account)
print(acc)    -- Account(Alice, $100)
-- print() calls __tostring automatically.
```

## Practice Questions

1. What is the key idea behind "Metatables"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Metatables with analogies and real-world examples"
1. "Show me common mistakes beginners make with Metatables"
1. "Provide advanced patterns and performance considerations for Metatables"

## Key Takeaways

- Master the core ideas of Metatables through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
