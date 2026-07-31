---
{
  "title": "Control Flow",
  "description": "if/elseif/else, while, for, repeat, and goto.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Branch with if and elseif",
    "Loop with while",
    "Use numeric and generic for",
    "Control flow with repeat and goto"
  ],
  "knowledge_refs": [
    "lua/lua-03-control-flow"
  ],
  "prerequisites": [
    "LUA-02"
  ],
  "references": [
    {
      "title": "Lua — Control Structures",
      "url": "https://www.lua.org/manual/5.4/manual.html#3.3"
    },
    {
      "title": "PiL — Control Structures",
      "url": "https://www.lua.org/pil/4.html"
    },
    {
      "title": "Lua — goto",
      "url": "https://www.lua.org/manual/5.4/manual.html#3.3.4"
    }
  ]
}
---

# LUA-03-CONTROL-FLOW: Control Flow

## Introduction

if/elseif/else, while, for, repeat, and goto. By the end of this lesson you will be able to: Branch with if and elseif; Loop with while; Use numeric and generic for; Control flow with repeat and goto.

## Key Concepts

### 1. Branch with if and elseif

Target: Branch with if and elseif. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- if / elseif / else
local score = 85
if score >= 90 then
  print("A")
elseif score >= 75 then
  print("B")
elseif score >= 50 then
  print("C")
else
  print("D")
end
-- Output: B
```
### 2. Loop with while

Target: Loop with while. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- while loops
local i = 0
while i < 3 do
  print("i = " .. i)
  i = i + 1
end
-- Output: i = 0, i = 1, i = 2
```
### 3. Use numeric and generic for

Target: Use numeric and generic for. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- for loops: numeric and generic
for i = 1, 5 do
  io.write(i .. " ")
end
print()
for i = 10, 2, -2 do
  io.write(i .. " ")
end
print()
-- generic for over a table:
for k, v in pairs({a = 1, b = 2}) do
  print(k, v)
end
```
### 4. Control flow with repeat and goto

Target: Control flow with repeat and goto. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- repeat ... until and loop control
local x = 0
repeat
  x = x + 1
until x >= 3
print(x)              -- 3 — condition checked at the END

for i = 1, 10 do
  if i == 3 then break end      -- exit the loop
  if i % 2 == 0 then
    goto continue               -- skip to next iteration (Lua 5.2+)
  end
  print("odd", i)
  ::continue::
end
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
