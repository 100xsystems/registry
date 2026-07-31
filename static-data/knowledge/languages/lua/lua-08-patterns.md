---
{
  "title": "Pattern Matching",
  "description": "match, find, gsub, captures, and character classes.",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Match with string:match",
    "Find positions with string:find",
    "Replace with gsub",
    "Capture groups"
  ],
  "knowledge_refs": [
    "lua/lua-08-patterns"
  ],
  "prerequisites": [
    "LUA-07"
  ],
  "references": [
    {
      "title": "Lua — Patterns",
      "url": "https://www.lua.org/manual/5.4/manual.html#6.4.1"
    },
    {
      "title": "PiL — Pattern Matching",
      "url": "https://www.lua.org/pil/20.html"
    },
    {
      "title": "Lua Patterns tutorial",
      "url": "https://www.lua.org/pil/20.2.html"
    }
  ]
}
---

# LUA-08-PATTERNS: Pattern Matching

## Introduction

match, find, gsub, captures, and character classes. By the end of this lesson you will be able to: Match with string:match; Find positions with string:find; Replace with gsub; Capture groups.

## Key Concepts

### 1. Match with string:match

Target: Match with string:match. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- Pattern matching: Lua's regex
local s = "The quick brown fox"
print(s:match("quick"))        -- quick — first match
print(s:find("brown"))         -- 11 15 — position range
print(s:gsub("o", "0"))        -- The quick br0wn f0x  2
-- Patterns: %a %d %w %s %p, + * ?, ^ $, (captures)
```
### 2. Find positions with string:find

Target: Find positions with string:find. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- Captures with patterns
local date = "2026-07-31"
local year, month, day = date:match("(%d+)-(%d+)-(%d+)")
print(year, month, day)      -- 2026 07 31

local email = "user@example.com"
local name, domain = email:match("([^@]+)@(.+)")
print(name, domain)          -- user example.com
```
### 3. Replace with gsub

Target: Replace with gsub. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- Common pattern recipes
local s = "  hello  world  "
for word in s:gmatch("%a+") do
  print(word)                -- hello, world
end

print(("hello"):upper())      -- HELLO
print(("42"):match("%d+"))    -- 42
print(("a1b2c3"):gsub("%d", "#"))   -- a#b#c#  3
-- The colon calls the string library on the value.
```
### 4. Capture groups

Target: Capture groups. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- Anchors and character classes
print(("abc123"):match("^abc"))     -- abc — starts with
print(("abc123"):match("123$"))     -- 123 — ends with
print(("hello"):match("h%a+"))      -- hello — %a letters
print(("x1y2"):match("%d%d"))       -- nil — no two digits in a row
print(("42.5"):match("%d+%.%d+"))   -- 42.5
-- %d digits, %a letters, %w alphanumerics, %s spaces
```

## Practice Questions

1. What is the key idea behind "Pattern Matching"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Pattern Matching with analogies and real-world examples"
1. "Show me common mistakes beginners make with Pattern Matching"
1. "Provide advanced patterns and performance considerations for Pattern Matching"

## Key Takeaways

- Master the core ideas of Pattern Matching through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
