---
{
  "title": "Object-Oriented Programming",
  "description": "The self pattern, colon methods, inheritance, and composition.",
  "type": "lesson",
  "order": 9,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Build classes with metatables",
    "Use colon method syntax",
    "Implement inheritance",
    "Compose objects"
  ],
  "knowledge_refs": [
    "lua/lua-09-oop"
  ],
  "prerequisites": [
    "LUA-08"
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
      "title": "PiL — Private State",
      "url": "https://www.lua.org/pil/16.4.html"
    }
  ]
}
---

# LUA-09-OOP: Object-Oriented Programming

## Introduction

The self pattern, colon methods, inheritance, and composition. By the end of this lesson you will be able to: Build classes with metatables; Use colon method syntax; Implement inheritance; Compose objects.

## Key Concepts

### 1. Build classes with metatables

Target: Build classes with metatables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- OOP with tables: the self pattern
Account = {}
Account.__index = Account

function Account.new(owner, balance)
  local self = setmetatable({}, Account)
  self.owner = owner
  self.balance = balance
  return self
end

function Account:deposit(amount)
  self.balance = self.balance + amount
end

local acc = Account.new("Alice", 100)
acc:deposit(50)
print(acc.balance)     -- 150
-- The colon adds an implicit self parameter.
```
### 2. Use colon method syntax

Target: Use colon method syntax. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- Colon vs dot method calls
Account = {}
Account.__index = Account

function Account.new(owner)
  return setmetatable({owner = owner}, Account)
end

function Account:describe()
  return "Account of " .. self.owner
end

local a = Account.new("Bob")
print(a:describe())        -- Account of Bob (colon: passes self)
print(a.describe(a))       -- same call written with dot
-- a:method(...) == a.method(a, ...)
```
### 3. Implement inheritance

Target: Implement inheritance. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- Inheritance through metatables
Account = {}
Account.__index = Account

function Account.new(balance)
  return setmetatable({balance = balance}, Account)
end

function Account:balance_str()
  return "$" .. self.balance
end

Savings = {}
Savings.__index = Savings
setmetatable(Savings, {__index = Account})

function Savings.new(balance, rate)
  local self = Account.new(balance)
  setmetatable(self, Savings)
  self.rate = rate
  return self
end

function Savings:interest()
  return self.balance * self.rate
end

local s = Savings.new(100, 0.05)
print(s:balance_str())     -- $100 — inherited
print(s:interest())        -- 5.0 — overridden
```
### 4. Compose objects

Target: Compose objects. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- Composition over inheritance
local logger = {
  log = function(self, msg)
    print("[" .. os.date("%H:%M:%S") .. "] " .. msg)
  end
}

local service = {}
service.logger = logger

function service.start()
  service.logger:log("starting")
  service.logger:log("ready")
end

service.start()
-- [time] starting
-- [time] ready
-- Compose objects by holding references to collaborators.
```

## Practice Questions

1. What is the key idea behind "Object-Oriented Programming"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Object-Oriented Programming with analogies and real-world examples"
1. "Show me common mistakes beginners make with Object-Oriented Programming"
1. "Provide advanced patterns and performance considerations for Object-Oriented Programming"

## Key Takeaways

- Master the core ideas of Object-Oriented Programming through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
