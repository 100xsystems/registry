---
{
  "title": "Advanced Patterns",
  "description": "DI containers, event loops, observers, and the ecosystem.",
  "type": "lesson",
  "order": 21,
  "duration": "75 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Build a DI container",
    "Run event loops with coroutines",
    "Implement observers",
    "Navigate the ecosystem"
  ],
  "knowledge_refs": [
    "lua/lua-21-advanced-patterns"
  ],
  "prerequisites": [
    "LUA-20"
  ],
  "references": [
    {
      "title": "LuaRocks — packages",
      "url": "https://luarocks.org/"
    },
    {
      "title": "LÖVE — game framework",
      "url": "https://love2d.org/"
    },
    {
      "title": "OpenResty — web platform",
      "url": "https://openresty.org/en/"
    }
  ]
}
---

# LUA-21-ADVANCED-PATTERNS: Advanced Patterns

## Introduction

DI containers, event loops, observers, and the ecosystem. By the end of this lesson you will be able to: Build a DI container; Run event loops with coroutines; Implement observers; Navigate the ecosystem.

## Key Concepts

### 1. Build a DI container

Target: Build a DI container. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- A mini dependency-injection container
local Container = {}
Container.__index = Container

function Container.new()
  return setmetatable({services = {}}, Container)
end

function Container:register(name, factory)
  self.services[name] = {factory = factory, instance = nil}
end

function Container:resolve(name)
  local service = self.services[name]
  if not service then error("unknown service: " .. name) end
  if not service.instance then
    service.instance = service.factory(self)
  end
  return service.instance
end

local c = Container.new()
c:register("db", function() return {connected = true} end)
c:register("app", function(c)
  return {db = c:resolve("db")}
end)

local app = c:resolve("app")
print(app.db.connected)   -- true — same db instance
```
### 2. Run event loops with coroutines

Target: Run event loops with coroutines. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- Event loop pattern with coroutines
local queue = {}
local running = true

local function task(name)
  print("task " .. name .. " starting")
  coroutine.yield()
  print("task " .. name .. " finishing")
end

local tasks = {
  coroutine.create(function() task("A") end),
  coroutine.create(function() task("B") end),
}

for _, co in ipairs(tasks) do
  coroutine.resume(co)
end
-- A and B interleave cooperatively on one thread.
```
### 3. Implement observers

Target: Implement observers. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- A simple observer pattern
local Subject = {}
Subject.__index = Subject

function Subject.new()
  return setmetatable({observers = {}}, Subject)
end

function Subject:subscribe(fn)
  table.insert(self.observers, fn)
end

function Subject:notify(event)
  for _, fn in ipairs(self.observers) do
    fn(event)
  end
end

local subject = Subject.new()
subject:subscribe(function(e) print("A got " .. e) end)
subject:subscribe(function(e) print("B got " .. e) end)
subject:notify("update")
-- A got update
-- B got update
```
### 4. Navigate the ecosystem

Target: Navigate the ecosystem. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- The Lua ecosystem at a glance
print("LuaRocks: package manager")
print("LÖVE: 2D game framework")
print("OpenResty: web platform on NGINX")
print("Redis: scripting inside the datastore")
print("LuaJIT: high-performance JIT compiler")
-- From game engines to web servers to databases,
-- Lua's small size makes it the embedded language of choice.
```

## Practice Questions

1. What is the key idea behind "Advanced Patterns"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Advanced Patterns with analogies and real-world examples"
1. "Show me common mistakes beginners make with Advanced Patterns"
1. "Provide advanced patterns and performance considerations for Advanced Patterns"

## Key Takeaways

- Master the core ideas of Advanced Patterns through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
