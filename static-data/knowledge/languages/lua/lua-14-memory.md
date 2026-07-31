---
{
  "title": "Memory Management",
  "description": "Weak tables, garbage collection, and upvalues.",
  "type": "lesson",
  "order": 14,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Build weak tables",
    "Control garbage collection",
    "Share state via upvalues",
    "Cache with modules"
  ],
  "knowledge_refs": [
    "lua/lua-14-memory"
  ],
  "prerequisites": [
    "LUA-13"
  ],
  "references": [
    {
      "title": "PiL — Weak Tables",
      "url": "https://www.lua.org/pil/17.html"
    },
    {
      "title": "Lua — collectgarbage",
      "url": "https://www.lua.org/manual/5.4/manual.html#6.1"
    },
    {
      "title": "Lua — Garbage Collection",
      "url": "https://www.lua.org/manual/5.4/manual.html#2.5"
    }
  ]
}
---

# LUA-14-MEMORY: Memory Management

## Introduction

Weak tables, garbage collection, and upvalues. By the end of this lesson you will be able to: Build weak tables; Control garbage collection; Share state via upvalues; Cache with modules.

## Key Concepts

### 1. Build weak tables

Target: Build weak tables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- Weak tables: memory management
local cache = setmetatable({}, {
  __mode = "v"     -- weak values: collectable when unused
})

cache[1] = {expensive = true}
collectgarbage()
print(cache[1])    -- nil — the value was collected
-- Weak tables let caches release memory under pressure.
```
### 2. Control garbage collection

Target: Control garbage collection. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- collectgarbage and memory
print(collectgarbage("count"))    -- KB in use
local t = {}
for i = 1, 100000 do t[i] = i end
print(collectgarbage("count"))
t = nil
collectgarbage("collect")         -- force a full collection
print(collectgarbage("count"))
-- Lua manages memory automatically with GC.
```
### 3. Share state via upvalues

Target: Share state via upvalues. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- Upvalues and shared state
local function make_cache()
  local cache = {}
  return {
    get = function(k) return cache[k] end,
    set = function(k, v) cache[k] = v end,
  }
end

local c = make_cache()
c.set("a", 1)
print(c.get("a"))      -- 1
print(c.get("b"))      -- nil
-- Upvalues (cache) are shared by all closures created in scope.
```
### 4. Cache with modules

Target: Cache with modules. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- The module cache pattern
local loaded = {}
function load_or_build(name, builder)
  if not loaded[name] then
    loaded[name] = builder()
  end
  return loaded[name]
end

local first = load_or_build("x", function() return {n = 42} end)
local second = load_or_build("x", function() return {n = 0} end)
print(first == second)    -- true — same cached instance
print(first.n)            -- 42
```

## Practice Questions

1. What is the key idea behind "Memory Management"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Memory Management with analogies and real-world examples"
1. "Show me common mistakes beginners make with Memory Management"
1. "Provide advanced patterns and performance considerations for Memory Management"

## Key Takeaways

- Master the core ideas of Memory Management through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
