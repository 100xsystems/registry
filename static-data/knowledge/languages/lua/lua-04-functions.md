---
{
  "title": "Functions",
  "description": "Basic functions, multiple returns, variadics, and closures.",
  "type": "lesson",
  "order": 4,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define and call functions",
    "Return multiple values",
    "Write variadic functions",
    "Capture state in closures"
  ],
  "knowledge_refs": [
    "lua/lua-04-functions"
  ],
  "prerequisites": [
    "LUA-03"
  ],
  "references": [
    {
      "title": "Lua — Functions",
      "url": "https://www.lua.org/manual/5.4/manual.html#6.1"
    },
    {
      "title": "PiL — Functions",
      "url": "https://www.lua.org/pil/5.html"
    },
    {
      "title": "PiL — Closures",
      "url": "https://www.lua.org/pil/6.1.html"
    }
  ]
}
---

# LUA-04-FUNCTIONS: Functions

## Introduction

Basic functions, multiple returns, variadics, and closures. By the end of this lesson you will be able to: Define and call functions; Return multiple values; Write variadic functions; Capture state in closures.

## Key Concepts

### 1. Define and call functions

Target: Define and call functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- Functions: basic syntax
function add(a, b)
  return a + b
end

print(add(3, 4))      -- 7
-- Functions are first-class values in Lua.
```
### 2. Return multiple values

Target: Return multiple values. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- Local functions and multiple returns
local function greet(name)
  return "Hello, " .. name .. "!"
end

function returns_two()
  return 1, 2          -- multiple return values
end

local a, b = returns_two()
print(a, b)            -- 1 2
print(greet("World"))  -- Hello, World!
```
### 3. Write variadic functions

Target: Write variadic functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- Variadic functions
function sum(...)
  local total = 0
  for _, v in ipairs({...}) do
    total = total + v
  end
  return total
end

print(sum(1, 2, 3, 4))   -- 10
-- ... collects all extra arguments into a table.
```
### 4. Capture state in closures

Target: Capture state in closures. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- Closures: functions capturing state
function make_counter()
  local count = 0
  return function()
    count = count + 1
    return count
  end
end

local counter = make_counter()
print(counter())      -- 1
print(counter())      -- 2
print(counter())      -- 3
-- The closure remembers count between calls.
```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
