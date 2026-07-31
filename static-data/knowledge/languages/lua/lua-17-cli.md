---
{
  "title": "Command-Line Tools",
  "description": "arg handling, environment, and small CLI programs.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Parse arguments",
    "Use the arg table",
    "Read environment variables",
    "Build a CLI tool"
  ],
  "knowledge_refs": [
    "lua/lua-17-cli"
  ],
  "prerequisites": [
    "LUA-16"
  ],
  "references": [
    {
      "title": "Lua — arg",
      "url": "https://www.lua.org/manual/5.4/manual.html#6.1"
    },
    {
      "title": "PiL — Command-Line",
      "url": "https://www.lua.org/pil/1.1.html"
    },
    {
      "title": "Lua — package.config",
      "url": "https://www.lua.org/manual/5.4/manual.html#6.3"
    }
  ]
}
---

# LUA-17-CLI: Command-Line Tools

## Introduction

arg handling, environment, and small CLI programs. By the end of this lesson you will be able to: Parse arguments; Use the arg table; Read environment variables; Build a CLI tool.

## Key Concepts

### 1. Parse arguments

Target: Parse arguments. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```lua
-- The argparse-style manual parsing
local args = {}
for i = 1, #arg do
  local a = arg[i]
  if a == "--verbose" then
    args.verbose = true
  elseif a:match("^--name=") then
    args.name = a:match("^--name=(.+)$")
  end
end

print(args.verbose)    -- nil or true
print(args.name)
-- The global `arg` table holds command-line arguments.
```
### 2. Use the arg table

Target: Use the arg table. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```lua
-- Standard arg table
print(#arg)            -- number of arguments
print(arg[0])          -- script name
print(arg[1])          -- first argument
-- arg is a global table available to the script.
```
### 3. Read environment variables

Target: Read environment variables. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```lua
-- Environment variables and process info
print(os.getenv("HOME"))          -- home directory
print(os.getenv("PATH"))          -- path
local sep = package.config:sub(1, 1)   -- path separator
print("sep: " .. sep)
-- package.config gives platform details.
```
### 4. Build a CLI tool

Target: Build a CLI tool. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```lua
-- A small CLI tool
local function main(args)
  local name = args[1] or "world"
  local count = tonumber(args[2]) or 1
  for i = 1, count do
    print("Hello, " .. name .. "!")
  end
end

main(arg)
-- run: lua cli.lua Alice 3
-- Hello, Alice!
-- Hello, Alice!
-- Hello, Alice!
```

## Practice Questions

1. What is the key idea behind "Command-Line Tools"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Command-Line Tools with analogies and real-world examples"
1. "Show me common mistakes beginners make with Command-Line Tools"
1. "Provide advanced patterns and performance considerations for Command-Line Tools"

## Key Takeaways

- Master the core ideas of Command-Line Tools through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
