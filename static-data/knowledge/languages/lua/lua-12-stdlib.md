---
{
  "title": "Standard Library",
  "description": "os, io, math, and table utilities.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Work with dates and time",
    "Read and write files",
    "Use the math library",
    "Manipulate tables"
  ],
  "knowledge_refs": [
    "lua/lua-12-stdlib"
  ],
  "prerequisites": [
    "LUA-11"
  ],
  "references": [
    {
      "title": "Lua — Standard Libraries",
      "url": "https://www.lua.org/manual/5.4/manual.html#6"
    },
    {
      "title": "Lua — os library",
      "url": "https://www.lua.org/manual/5.4/manual.html#6.9"
    },
    {
      "title": "Lua — io library",
      "url": "https://www.lua.org/manual/5.4/manual.html#6.8"
    }
  ]
}
---

# LUA-12-STDLIB: Standard Library

## Introduction

os, io, math, and table utilities. By the end of this lesson you will be able to: Work with dates and time; Read and write files; Use the math library; Manipulate tables.

## Key Concepts

### 1. Work with dates and time

Target: Work with dates and time. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- Standard library: os and io
print(os.date("%Y-%m-%d %H:%M:%S"))    -- current time
print(os.time())                        -- epoch seconds
local start = os.clock()
-- ... do work ...
print("elapsed: " .. os.clock() - start .. "s")

-- File I/O:
local f = io.open("/tmp/demo.txt", "w")
f:write("hello file\n")
f:close()

local f2 = io.open("/tmp/demo.txt", "r")
print(f2:read("*a"))       -- hello file
f2:close()
```
### 2. Read and write files

Target: Read and write files. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- Reading lines from a file
local count = 0
for line in io.lines("/tmp/demo.txt") do
  count = count + 1
end
print(count)   -- number of lines

-- Writing with io.output:
io.output("/tmp/out.txt")
io.write("first line\n")
io.write("second line\n")
io.close()
print("wrote to /tmp/out.txt")
```
### 3. Use the math library

Target: Use the math library. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- math library
print(math.pi)             -- 3.1415926535898
print(math.abs(-5))        -- 5
print(math.max(3, 9, 4))   -- 9
print(math.min(3, 9, 4))   -- 3
print(math.random())       -- [0,1) float
math.randomseed(os.time())
print(math.random(1, 6))   -- random integer 1..6
print(math.sqrt(16))       -- 4.0
print(math.ceil(3.2))      -- 4
print(math.floor(3.8))     -- 3
```
### 4. Manipulate tables

Target: Manipulate tables. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- table and string shortcuts
local t = {}
table.insert(t, 10)
table.insert(t, 20)
print(#t)                  -- 2
table.insert(t, 1, 5)      -- insert at position 1
print(t[1])                -- 5

local s = "a,b,c"
print(string.gsub(s, ",", ";"))   -- a;b;c   2
-- The second return of gsub is the replacement count.
```

## Practice Questions

1. What is the key idea behind "Standard Library"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Standard Library with analogies and real-world examples"
1. "Show me common mistakes beginners make with Standard Library"
1. "Provide advanced patterns and performance considerations for Standard Library"

## Key Takeaways

- Master the core ideas of Standard Library through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
