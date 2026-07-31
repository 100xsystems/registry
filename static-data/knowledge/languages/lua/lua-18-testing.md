---
{
  "title": "Testing",
  "description": "Assertions, pcall-based runners, busted, and the test cycle.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write assertion tests",
    "Use busted-style suites",
    "Unit test modules",
    "Apply the red-green-refactor cycle"
  ],
  "knowledge_refs": [
    "lua/lua-18-testing"
  ],
  "prerequisites": [
    "LUA-17"
  ],
  "references": [
    {
      "title": "busted — Lua testing",
      "url": "https://lunarmodules.github.io/busted/"
    },
    {
      "title": "LuaUnit — unit testing",
      "url": "https://github.com/bluebird75/luaunit"
    },
    {
      "title": "PiL — Assertions",
      "url": "https://www.lua.org/pil/8.2.html"
    }
  ]
}
---

# LUA-18-TESTING: Testing

## Introduction

Assertions, pcall-based runners, busted, and the test cycle. By the end of this lesson you will be able to: Write assertion tests; Use busted-style suites; Unit test modules; Apply the red-green-refactor cycle.

## Key Concepts

### 1. Write assertion tests

Target: Write assertion tests. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- Testing with a simple assertion framework
local function describe(name, fn)
  io.write(name .. " ... ")
  local ok, err = pcall(fn)
  if ok then
    print("PASS")
  else
    print("FAIL: " .. tostring(err))
  end
end

describe("addition", function()
  assert(1 + 1 == 2)
end)

describe("failing test", function()
  assert(2 + 2 == 5)
end)
```
### 2. Use busted-style suites

Target: Use busted-style suites. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- Busted-style expectations (conceptual)
-- busted is the popular Lua testing framework
-- describe("math", function()
--   it("adds", function()
--     assert.are.equal(4, 2 + 2)
--   end)
-- end)
print("busted: describe/it blocks, spies, and mocks")
print("run with: busted spec/")
```
### 3. Unit test modules

Target: Unit test modules. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- Unit test for the counter module
local make_counter = require("counter")   -- assume module

local c = make_counter()
assert(c() == 1, "first call returns 1")
assert(c() == 2, "second call returns 2")

-- A poor-man's test runner over pcall:
local tests = { {"first", c() == 1}, {"second", c() == 2} }
for _, t in ipairs(tests) do
  print(t[1], t[2] and "PASS" or "FAIL")
end
```
### 4. Apply the red-green-refactor cycle

Target: Apply the red-green-refactor cycle. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- The test cycle
print("1. Write the failing test")
print("2. Run it — red")
print("3. Implement the module")
print("4. Run again — green")
print("5. Refactor, keeping tests green")
-- Lua's simplicity makes tests quick to write.
```

## Practice Questions

1. What is the key idea behind "Testing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing"
1. "Provide advanced patterns and performance considerations for Testing"

## Key Takeaways

- Master the core ideas of Testing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
