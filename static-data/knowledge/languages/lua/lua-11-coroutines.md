---
{
  "title": "Coroutines",
  "description": "Cooperative multitasking, generators, and state machines.",
  "type": "lesson",
  "order": 11,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create coroutines",
    "Build generators",
    "Model state machines",
    "Compare with threads"
  ],
  "knowledge_refs": [
    "lua/lua-11-coroutines"
  ],
  "prerequisites": [
    "LUA-10"
  ],
  "references": [
    {
      "title": "Lua — Coroutines",
      "url": "https://www.lua.org/manual/5.4/manual.html#6.2"
    },
    {
      "title": "PiL — Coroutines",
      "url": "https://www.lua.org/pil/9.html"
    },
    {
      "title": "PiL — Generators",
      "url": "https://www.lua.org/pil/9.3.html"
    }
  ]
}
---

# LUA-11-COROUTINES: Coroutines

## Introduction

Cooperative multitasking, generators, and state machines. By the end of this lesson you will be able to: Create coroutines; Build generators; Model state machines; Compare with threads.

## Key Concepts

### 1. Create coroutines

Target: Create coroutines. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- Coroutines: cooperative multitasking
local co = coroutine.create(function()
  print("coroutine started")
  coroutine.yield("first pause")
  print("coroutine resumed")
  return "done"
end)

print(coroutine.status(co))     -- suspended
local ok, val = coroutine.resume(co)
print(val)                      -- first pause
print(coroutine.status(co))     -- suspended
coroutine.resume(co)            -- coroutine resumed
print(coroutine.status(co))     -- dead
```
### 2. Build generators

Target: Build generators. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- Generators with coroutines
function range_generator(n)
  return coroutine.wrap(function()
    for i = 1, n do
      coroutine.yield(i)
    end
  end)
end

for i in range_generator(3) do
  print(i)     -- 1, 2, 3
end
-- coroutine.wrap returns a function you can iterate.
```
### 3. Model state machines

Target: Model state machines. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- Coroutine-based state machine
local function state_machine()
  local state = "idle"
  while true do
    local cmd = coroutine.yield(state)
    if cmd == "start" then
      state = "running"
    elseif cmd == "stop" then
      state = "idle"
    end
  end
end

local machine = coroutine.wrap(state_machine)
print(machine())        -- idle
print(machine("start")) -- running
print(machine("stop"))  -- idle
-- Coroutines can receive values via yield/ resume.
```
### 4. Compare with threads

Target: Compare with threads. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- Coroutines vs threads
-- Coroutines: cooperative, single-threaded, explicit yields
-- Threads: preemptive, parallel, complex synchronization
-- Lua coroutines are cheap and safe (no data races).
local co = coroutine.create(function()
  local sum = 0
  for i = 1, 100 do
    sum = sum + i
    if i % 50 == 0 then coroutine.yield(sum) end
  end
  return sum
end)

print(coroutine.resume(co))    -- true 1275 (first 50)
print(coroutine.resume(co))    -- true 5050 (all 100)
```

## Practice Questions

1. What is the key idea behind "Coroutines"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Coroutines with analogies and real-world examples"
1. "Show me common mistakes beginners make with Coroutines"
1. "Provide advanced patterns and performance considerations for Coroutines"

## Key Takeaways

- Master the core ideas of Coroutines through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
