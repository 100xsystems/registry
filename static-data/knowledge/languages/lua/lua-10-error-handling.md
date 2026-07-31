---
{
  "title": "Error Handling",
  "description": "pcall, xpcall, error, and assert.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Catch errors with pcall",
    "Transform errors with xpcall",
    "Raise with error and assert",
    "Build try/catch patterns"
  ],
  "knowledge_refs": [
    "lua/lua-10-error-handling"
  ],
  "prerequisites": [
    "LUA-09"
  ],
  "references": [
    {
      "title": "PiL — Errors",
      "url": "https://www.lua.org/pil/8.3.html"
    },
    {
      "title": "PiL — Error Handling",
      "url": "https://www.lua.org/pil/8.4.html"
    },
    {
      "title": "Lua — pcall",
      "url": "https://www.lua.org/manual/5.4/manual.html#6.1"
    }
  ]
}
---

# LUA-10-ERROR-HANDLING: Error Handling

## Introduction

pcall, xpcall, error, and assert. By the end of this lesson you will be able to: Catch errors with pcall; Transform errors with xpcall; Raise with error and assert; Build try/catch patterns.

## Key Concepts

### 1. Catch errors with pcall

Target: Catch errors with pcall. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- Error handling with pcall
local ok, result = pcall(function()
  error("something went wrong")
end)

print(ok)              -- false
print(result)          -- something went wrong
-- pcall returns success, then the return value OR error message.
```
### 2. Transform errors with xpcall

Target: Transform errors with xpcall. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- xpcall with error handler
local ok, err = xpcall(function()
  error("boom")
end, function(e)
  return "handled: " .. e
end)

print(ok)              -- false
print(err)             -- handled: boom
-- xpcall lets you transform the error before it propagates.
```
### 3. Raise with error and assert

Target: Raise with error and assert. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- error() and assert()
function divide(a, b)
  if b == 0 then
    error("division by zero")
  end
  return a / b
end

local ok, err = pcall(divide, 10, 0)
print(err)             -- division by zero

-- assert fails fast on falsy:
local ok2 = assert(1 > 0, "this passes")
print(ok2)             -- true
```
### 4. Build try/catch patterns

Target: Build try/catch patterns. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- try/catch pattern with pcall
local function safe_call(fn, ...)
  local ok, result = pcall(fn, ...)
  if ok then
    return {success = true, value = result}
  else
    return {success = false, error = result}
  end
end

local r = safe_call(function(x)
  if x < 0 then error("negative") end
  return math.sqrt(x)
end, 9)

print(r.success, r.value)     -- true 3.0
-- Wrap fallible calls; handle results explicitly.
```

## Practice Questions

1. What is the key idea behind "Error Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Error Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Error Handling"
1. "Provide advanced patterns and performance considerations for Error Handling"

## Key Takeaways

- Master the core ideas of Error Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
