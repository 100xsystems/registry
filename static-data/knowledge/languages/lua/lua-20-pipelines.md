---
{
  "title": "Real-World Programs",
  "description": "Word counting, HTTP, JSON, and Redis scripting.",
  "type": "lesson",
  "order": 20,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Count words with patterns",
    "Fetch pages with LuaSocket",
    "Encode JSON with cjson",
    "Script Redis atomically"
  ],
  "knowledge_refs": [
    "lua/lua-20-pipelines"
  ],
  "prerequisites": [
    "LUA-19"
  ],
  "references": [
    {
      "title": "LuaSocket — networking",
      "url": "https://lunarmodules.github.io/luasocket/"
    },
    {
      "title": "lua-cjson — JSON",
      "url": "https://github.com/openresty/lua-cjson"
    },
    {
      "title": "Redis — Lua scripting",
      "url": "https://redis.io/docs/manual/programmability/eval-intro/"
    }
  ]
}
---

# LUA-20-PIPELINES: Real-World Programs

## Introduction

Word counting, HTTP, JSON, and Redis scripting. By the end of this lesson you will be able to: Count words with patterns; Fetch pages with LuaSocket; Encode JSON with cjson; Script Redis atomically.

## Key Concepts

### 1. Count words with patterns

Target: Count words with patterns. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- A complete word-counter CLI
local function count_words(text)
  local counts = {}
  for word in text:gmatch("%a+") do
    word = word:lower()
    counts[word] = (counts[word] or 0) + 1
  end
  return counts
end

local text = "The quick the brown the fox"
local counts = count_words(text)
for word, n in pairs(counts) do
  print(word, n)
end
-- the 3, quick 1, brown 1, fox 1
```
### 2. Fetch pages with LuaSocket

Target: Fetch pages with LuaSocket. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- Building a simple HTTP client (conceptual)
-- LuaSocket provides networking:
-- local http = require("socket.http")
-- local body = http.request("https://example.com")
-- print(body)
print("LuaSocket: http.request(url) fetches pages")
-- Combined with cjson you get JSON API clients.
```
### 3. Encode JSON with cjson

Target: Encode JSON with cjson. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- JSON with cjson
-- local cjson = require("cjson")
-- local obj = cjson.decode('{"name": "Alice"}')
-- print(obj.name)
-- local json = cjson.encode({x = 1, y = 2})
print("cjson encodes/decodes JSON between Lua and text")
-- Integration with web frameworks via OpenResty.
```
### 4. Script Redis atomically

Target: Script Redis atomically. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- The Redis scripting pattern
-- EVAL "return redis.call('GET', KEYS[1])" 1 mykey
-- Lua scripts run atomically inside Redis:
--   local val = redis.call('GET', KEYS[1])
--   redis.call('SET', KEYS[1], tonumber(val) + 1)
--   return redis.call('GET', KEYS[1])
print("Redis EVAL runs Lua atomically for counters")
-- This powers rate limiters, locks, and caches.
```

## Practice Questions

1. What is the key idea behind "Real-World Programs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Real-World Programs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Real-World Programs"
1. "Provide advanced patterns and performance considerations for Real-World Programs"

## Key Takeaways

- Master the core ideas of Real-World Programs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
