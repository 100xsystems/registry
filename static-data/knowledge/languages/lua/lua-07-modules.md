---
{
  "title": "Modules and Packages",
  "description": "Module patterns, require, encapsulation, and namespaces.",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write modules",
    "Load with require",
    "Encapsulate private state",
    "Use tables as namespaces"
  ],
  "knowledge_refs": [
    "lua/lua-07-modules"
  ],
  "prerequisites": [
    "LUA-06"
  ],
  "references": [
    {
      "title": "PiL — Modules",
      "url": "https://www.lua.org/pil/15.html"
    },
    {
      "title": "Lua — require",
      "url": "https://www.lua.org/manual/5.4/manual.html#6.3"
    },
    {
      "title": "LuaRocks — the package manager",
      "url": "https://luarocks.org/"
    }
  ]
}
---

# LUA-07-MODULES: Modules and Packages

## Introduction

Module patterns, require, encapsulation, and namespaces. By the end of this lesson you will be able to: Write modules; Load with require; Encapsulate private state; Use tables as namespaces.

## Key Concepts

### 1. Write modules

Target: Write modules. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- Modules: organizing code
-- save as mymath.lua
local M = {}

function M.add(a, b) return a + b end
function M.multiply(a, b) return a * b end

return M
-- Usage: local mymath = require("mymath")
```
### 2. Load with require

Target: Load with require. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- require and package loading
local mymath = require("mymath")
print(mymath.add(2, 3))        -- 5
-- require caches modules; it runs the file ONCE.
-- package.path controls where require looks.
```
### 3. Encapsulate private state

Target: Encapsulate private state. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- Module pattern with locals (encapsulation)
local M = {}
local counter = 0        -- private state

function M.next()
  counter = counter + 1
  return counter
end

function M.get()
  return counter
end

return M
-- Usage: local gen = require("generator")
```
### 4. Use tables as namespaces

Target: Use tables as namespaces. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- Tables as namespaces
local string_utils = {
  trim = function(s)
    return (s:gsub("^%s+", ""):gsub("%s+$", ""))
  end,
  split = function(s, sep)
    local parts = {}
    for part in (s .. sep):gmatch("(.-)" .. sep) do
      table.insert(parts, part)
    end
    return parts
  end,
}

print(string_utils.trim("  hello  "))     -- hello
print(#string_utils.split("a,b,c", ","))  -- 3
```

## Practice Questions

1. What is the key idea behind "Modules and Packages"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Modules and Packages with analogies and real-world examples"
1. "Show me common mistakes beginners make with Modules and Packages"
1. "Provide advanced patterns and performance considerations for Modules and Packages"

## Key Takeaways

- Master the core ideas of Modules and Packages through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
