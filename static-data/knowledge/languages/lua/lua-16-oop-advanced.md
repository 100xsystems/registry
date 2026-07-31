---
{
  "title": "Advanced OOP Patterns",
  "description": "Method chaining, duck typing, and singletons.",
  "type": "lesson",
  "order": 16,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Chain methods",
    "Apply duck typing",
    "Build singletons",
    "Design with composition"
  ],
  "knowledge_refs": [
    "lua/lua-16-oop-advanced"
  ],
  "prerequisites": [
    "LUA-15"
  ],
  "references": [
    {
      "title": "PiL — OOP",
      "url": "https://www.lua.org/pil/16.html"
    },
    {
      "title": "PiL — Inheritance",
      "url": "https://www.lua.org/pil/16.2.html"
    },
    {
      "title": "Lua Design Patterns",
      "url": "https://www.lua.org/pil/contents.html"
    }
  ]
}
---

# LUA-16-OOP-ADVANCED: Advanced OOP Patterns

## Introduction

Method chaining, duck typing, and singletons. By the end of this lesson you will be able to: Chain methods; Apply duck typing; Build singletons; Design with composition.

## Key Concepts

### 1. Chain methods

Target: Chain methods. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- Basic Object-Oriented Programming recap
local Animal = {}
Animal.__index = Animal

function Animal.new(name)
  return setmetatable({name = name}, Animal)
end

function Animal:speak()
  return self.name .. " makes a sound"
end

local dog = Animal.new("Rex")
print(dog:speak())    -- Rex makes a sound
-- The __index metatable provides method lookup.
```
### 2. Apply duck typing

Target: Apply duck typing. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- Method chaining
local Builder = {}
Builder.__index = Builder

function Builder.new()
  return setmetatable({parts = {}}, Builder)
end

function Builder:add(part)
  table.insert(self.parts, part)
  return self    -- return self to enable chaining
end

function Builder:build()
  return table.concat(self.parts, " + ")
end

local result = Builder.new():add("a"):add("b"):add("c"):build()
print(result)    -- a + b + c
-- Each method returns self for fluent chains.
```
### 3. Build singletons

Target: Build singletons. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- Duck typing: no interfaces needed
function process(shape)
  -- any object with an area() method works
  return shape:area()
end

local Circle = {}
Circle.__index = Circle
function Circle.new(r)
  return setmetatable({r = r}, Circle)
end
function Circle:area() return math.pi * self.r * self.r end

local Square = {}
Square.__index = Square
function Square.new(s)
  return setmetatable({s = s}, Square)
end
function Square:area() return self.s * self.s end

print(process(Circle.new(2)))   -- 12.566...
print(process(Square.new(3)))   -- 9
-- If it walks like a duck and quacks like a duck...
```
### 4. Design with composition

Target: Design with composition. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- OOP patterns: singleton
local Config = {}
Config.__index = Config
local instance

function Config.get()
  if not instance then
    instance = setmetatable({settings = {}}, Config)
  end
  return instance
end

function Config:set(key, value)
  self.settings[key] = value
end

Config.get():set("theme", "dark")
print(Config.get().settings.theme)   -- dark
-- Config.get() always returns the SAME instance.
```

## Practice Questions

1. What is the key idea behind "Advanced OOP Patterns"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Advanced OOP Patterns with analogies and real-world examples"
1. "Show me common mistakes beginners make with Advanced OOP Patterns"
1. "Provide advanced patterns and performance considerations for Advanced OOP Patterns"

## Key Takeaways

- Master the core ideas of Advanced OOP Patterns through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
