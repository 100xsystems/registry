#!/usr/bin/env python3
"""Generate the 21-lesson Lua curriculum at Python/JS/Java depth.
Uses the shared gen_lib template. Exact refs from lua.org docs.
Each lesson has 4 sub-topics, each with its OWN distinct code sample.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import main as run_gen  # noqa: E402

LANGUAGE = 'lua'

BASE = os.path.join(os.path.dirname(__file__), '..', '..', 'static-data', 'knowledge', 'languages', 'lua')

CODE = {
    1: [
        '''-- Your first Lua program
print("Hello, 100X Systems!")
-- run: lua hello.lua   ->   Hello, 100X Systems!
-- Lua is a lightweight, embeddable scripting language.''',
        '''-- The Lua interpreter and basic expressions
print(1 + 2)          -- 3
print(6 * 7)          -- 42
print("Hello" .. " " .. "Lua")   -- string concatenation
print(#"hello")       -- 5 — the length operator
-- Run interactively with: lua -i''',
        '''-- Variables: global by default
x = 10                -- global variable
local y = 20          -- local variable (preferred)
print(x + y)          -- 30
-- Locals are faster and scoped to their block.''',
        '''-- Comments and basic structure
-- line comment
--[[ block comment
     spanning multiple lines ]]
print("comments done")
-- Lua has no semicolon requirement; they are optional.''',
    ],
    2: [
        '''-- Numbers: integers and floats
print(10)             -- 10
print(3.14)           -- 3.14
print(10 / 3)         -- 3.3333333333333 (float division)
print(10 // 3)        -- 3 (floor division, Lua 5.3+)
print(10 % 3)         -- 1 (remainder)
print(2 ^ 10)         -- 1024.0 (exponent)
print(math.floor(3.7)) -- 3
print(math.maxinteger) -- largest integer''',
        '''-- Strings: quotes, escapes, and long brackets
local s1 = "double"
local s2 = 'single'
local s3 = [[long
string
here]]
print(s1, s2)
print(#s3)            -- 15 — multiline long string
print("line\\nbreak")  -- escape sequences work''',
        '''-- String library
local s = "Hello, Lua"
print(string.upper(s))     -- HELLO, LUA
print(string.lower(s))     -- hello, lua
print(string.len(s))       -- 10
print(string.sub(s, 1, 5)) -- Hello
print(string.rep("ab", 3)) -- ababab
print(string.format("%d-%02d", 2026, 7))  -- 2026-07''',
        '''-- Booleans and nil
print(true)           -- true
print(false)          -- false
print(nil)            -- nil
local a               -- a is nil
print(a)              -- nil
-- Only false and nil are falsy; 0 and "" are truthy!
if 0 then print("0 is truthy") end
if "" then print("empty string is truthy") end''',
    ],
    3: [
        '''-- if / elseif / else
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
-- Output: B''',
        '''-- while loops
local i = 0
while i < 3 do
  print("i = " .. i)
  i = i + 1
end
-- Output: i = 0, i = 1, i = 2''',
        '''-- for loops: numeric and generic
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
end''',
        '''-- repeat ... until and loop control
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
end''',
    ],
    4: [
        '''-- Functions: basic syntax
function add(a, b)
  return a + b
end

print(add(3, 4))      -- 7
-- Functions are first-class values in Lua.''',
        '''-- Local functions and multiple returns
local function greet(name)
  return "Hello, " .. name .. "!"
end

function returns_two()
  return 1, 2          -- multiple return values
end

local a, b = returns_two()
print(a, b)            -- 1 2
print(greet("World"))  -- Hello, World!''',
        '''-- Variadic functions
function sum(...)
  local total = 0
  for _, v in ipairs({...}) do
    total = total + v
  end
  return total
end

print(sum(1, 2, 3, 4))   -- 10
-- ... collects all extra arguments into a table.''',
        '''-- Closures: functions capturing state
function make_counter()
  local count = 0
  return function()
    count = count + 1
    return count
  end
end

local counter = make_counter()
print(counter())      -- 1
print(counter())      -- 2
print(counter())      -- 3
-- The closure remembers count between calls.''',
    ],
    5: [
        '''-- Tables: Lua's universal data structure
local arr = {10, 20, 30}          -- array-like
print(arr[1])                     -- 10 — 1-indexed!
print(#arr)                       -- 3 — length

local dict = {name = "Alice", age = 30}
print(dict.name)                  -- Alice
print(dict["age"])                -- 30
-- Tables are both arrays AND maps.''',
        '''-- Table constructors in detail
local t = {
  "first",                          -- t[1]
  "second",                         -- t[2]
  x = 1,                            -- t.x
  ["key with spaces"] = 2,          -- t["key with spaces"]
  nested = { inner = true },        -- t.nested.inner
}
print(t[1], t.x, t["key with spaces"])
print(t.nested.inner)              -- true''',
        '''-- Iterating tables
local t = {name = "Alice", age = 30, city = "NYC"}

-- pairs: any order
for k, v in pairs(t) do
  print(k, v)
end

-- ipairs: ordered, numeric keys only
local arr = {"a", "b", "c"}
for i, v in ipairs(arr) do
  print(i, v)
end''',
        '''-- Table library
local t = {3, 1, 2}
table.sort(t)
print(t[1], t[2], t[3])      -- 1 2 3

table.insert(t, 4)            -- append
table.remove(t, 1)            -- remove first
print(#t)                     -- 3

local concat = table.concat({1, 2, 3}, "-")
print(concat)                 -- 1-2-3''',
    ],
    6: [
        '''-- Metatables: customize table behavior
local mt = {}
mt.__index = function(table, key)
  return "default for " .. key
end

local t = setmetatable({}, mt)
print(t.missing)     -- default for missing
-- __index is called when a key is not found.''',
        '''-- __index with a fallback table (inheritance)
local base = {greeting = "Hello"}
local child = setmetatable({}, {__index = base})
print(child.greeting)   -- Hello — inherited from base

-- __newindex: intercept new key assignment
local track = setmetatable({}, {
  __newindex = function(t, k, v)
    print("setting " .. k .. " = " .. tostring(v))
    rawset(t, k, v)
  end
})
track.name = "Alice"    -- setting name = Alice''',
        '''-- Operator metamethods
local Point = {}
Point.__add = function(a, b)
  return {x = a.x + b.x, y = a.y + b.y}
end

local p1 = setmetatable({x = 1, y = 2}, Point)
local p2 = setmetatable({x = 10, y = 20}, Point)
local p3 = p1 + p2        -- uses __add
print(p3.x, p3.y)         -- 11 22
-- Other metamethods: __sub, __mul, __eq, __lt, __tostring, ...''',
        '''-- __tostring: custom printing
local Account = {}
Account.__tostring = function(self)
  return "Account(" .. self.owner .. ", $" .. self.balance .. ")"
end

local acc = setmetatable({owner = "Alice", balance = 100}, Account)
print(acc)    -- Account(Alice, $100)
-- print() calls __tostring automatically.''',
    ],
    7: [
        '''-- Modules: organizing code
-- save as mymath.lua
local M = {}

function M.add(a, b) return a + b end
function M.multiply(a, b) return a * b end

return M
-- Usage: local mymath = require("mymath")''',
        '''-- require and package loading
local mymath = require("mymath")
print(mymath.add(2, 3))        -- 5
-- require caches modules; it runs the file ONCE.
-- package.path controls where require looks.''',
        '''-- Module pattern with locals (encapsulation)
local M = {}
local counter = 0        -- private state

function M.next()
  counter = counter + 1
  return counter
end

function M.get()
  return counter
end

return M
-- Usage: local gen = require("generator")''',
        '''-- Tables as namespaces
local string_utils = {
  trim = function(s)
    return (s:gsub("^%s+", ""):gsub("%s+$", ""))
  end,
  split = function(s, sep)
    local parts = {}
    for part in (s .. sep):gmatch("(.-)" .. sep) do
      table.insert(parts, part)
    end
    return parts
  end,
}

print(string_utils.trim("  hello  "))     -- hello
print(#string_utils.split("a,b,c", ","))  -- 3''',
    ],
    8: [
        '''-- Pattern matching: Lua's regex
local s = "The quick brown fox"
print(s:match("quick"))        -- quick — first match
print(s:find("brown"))         -- 11 15 — position range
print(s:gsub("o", "0"))        -- The quick br0wn f0x  2
-- Patterns: %a %d %w %s %p, + * ?, ^ $, (captures)''',
        '''-- Captures with patterns
local date = "2026-07-31"
local year, month, day = date:match("(%d+)-(%d+)-(%d+)")
print(year, month, day)      -- 2026 07 31

local email = "user@example.com"
local name, domain = email:match("([^@]+)@(.+)")
print(name, domain)          -- user example.com''',
        '''-- Common pattern recipes
local s = "  hello  world  "
for word in s:gmatch("%a+") do
  print(word)                -- hello, world
end

print(("hello"):upper())      -- HELLO
print(("42"):match("%d+"))    -- 42
print(("a1b2c3"):gsub("%d", "#"))   -- a#b#c#  3
-- The colon calls the string library on the value.''',
        '''-- Anchors and character classes
print(("abc123"):match("^abc"))     -- abc — starts with
print(("abc123"):match("123$"))     -- 123 — ends with
print(("hello"):match("h%a+"))      -- hello — %a letters
print(("x1y2"):match("%d%d"))       -- nil — no two digits in a row
print(("42.5"):match("%d+%.%d+"))   -- 42.5
-- %d digits, %a letters, %w alphanumerics, %s spaces''',
    ],
    9: [
        '''-- OOP with tables: the self pattern
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
-- The colon adds an implicit self parameter.''',
        '''-- Colon vs dot method calls
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
-- a:method(...) == a.method(a, ...)''',
        '''-- Inheritance through metatables
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
print(s:interest())        -- 5.0 — overridden''',
        '''-- Composition over inheritance
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
-- Compose objects by holding references to collaborators.''',
    ],
    10: [
        '''-- Error handling with pcall
local ok, result = pcall(function()
  error("something went wrong")
end)

print(ok)              -- false
print(result)          -- something went wrong
-- pcall returns success, then the return value OR error message.''',
        '''-- xpcall with error handler
local ok, err = xpcall(function()
  error("boom")
end, function(e)
  return "handled: " .. e
end)

print(ok)              -- false
print(err)             -- handled: boom
-- xpcall lets you transform the error before it propagates.''',
        '''-- error() and assert()
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
print(ok2)             -- true''',
        '''-- try/catch pattern with pcall
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
-- Wrap fallible calls; handle results explicitly.''',
    ],
    11: [
        '''-- Coroutines: cooperative multitasking
local co = coroutine.create(function()
  print("coroutine started")
  coroutine.yield("first pause")
  print("coroutine resumed")
  return "done"
end)

print(coroutine.status(co))     -- suspended
local ok, val = coroutine.resume(co)
print(val)                      -- first pause
print(coroutine.status(co))     -- suspended
coroutine.resume(co)            -- coroutine resumed
print(coroutine.status(co))     -- dead''',
        '''-- Generators with coroutines
function range_generator(n)
  return coroutine.wrap(function()
    for i = 1, n do
      coroutine.yield(i)
    end
  end)
end

for i in range_generator(3) do
  print(i)     -- 1, 2, 3
end
-- coroutine.wrap returns a function you can iterate.''',
        '''-- Coroutine-based state machine
local function state_machine()
  local state = "idle"
  while true do
    local cmd = coroutine.yield(state)
    if cmd == "start" then
      state = "running"
    elseif cmd == "stop" then
      state = "idle"
    end
  end
end

local machine = coroutine.wrap(state_machine)
print(machine())        -- idle
print(machine("start")) -- running
print(machine("stop"))  -- idle
-- Coroutines can receive values via yield/ resume.''',
        '''-- Coroutines vs threads
-- Coroutines: cooperative, single-threaded, explicit yields
-- Threads: preemptive, parallel, complex synchronization
-- Lua coroutines are cheap and safe (no data races).
local co = coroutine.create(function()
  local sum = 0
  for i = 1, 100 do
    sum = sum + i
    if i % 50 == 0 then coroutine.yield(sum) end
  end
  return sum
end)

print(coroutine.resume(co))    -- true 1275 (first 50)
print(coroutine.resume(co))    -- true 5050 (all 100)''',
    ],
    12: [
        '''-- Standard library: os and io
print(os.date("%Y-%m-%d %H:%M:%S"))    -- current time
print(os.time())                        -- epoch seconds
local start = os.clock()
-- ... do work ...
print("elapsed: " .. os.clock() - start .. "s")

-- File I/O:
local f = io.open("/tmp/demo.txt", "w")
f:write("hello file\\n")
f:close()

local f2 = io.open("/tmp/demo.txt", "r")
print(f2:read("*a"))       -- hello file
f2:close()''',
        '''-- Reading lines from a file
local count = 0
for line in io.lines("/tmp/demo.txt") do
  count = count + 1
end
print(count)   -- number of lines

-- Writing with io.output:
io.output("/tmp/out.txt")
io.write("first line\\n")
io.write("second line\\n")
io.close()
print("wrote to /tmp/out.txt")''',
        '''-- math library
print(math.pi)             -- 3.1415926535898
print(math.abs(-5))        -- 5
print(math.max(3, 9, 4))   -- 9
print(math.min(3, 9, 4))   -- 3
print(math.random())       -- [0,1) float
math.randomseed(os.time())
print(math.random(1, 6))   -- random integer 1..6
print(math.sqrt(16))       -- 4.0
print(math.ceil(3.2))      -- 4
print(math.floor(3.8))     -- 3''',
        '''-- table and string shortcuts
local t = {}
table.insert(t, 10)
table.insert(t, 20)
print(#t)                  -- 2
table.insert(t, 1, 5)      -- insert at position 1
print(t[1])                -- 5

local s = "a,b,c"
print(string.gsub(s, ",", ";"))   -- a;b;c   2
-- The second return of gsub is the replacement count.''',
    ],
    13: [
        '''-- Variable number of arguments and select
function first_and_last(...)
  local args = {...}
  return args[1], args[#args]
end

local first, last = first_and_last("a", "b", "c")
print(first, last)      -- a c

print(select("#", 1, 2, 3))    -- 3 — count of arguments
print(select(2, "a", "b", "c")) -- b c — from the 2nd on''',
        '''-- Multiple assignment and swapping
local a, b = 1, 2
print(a, b)            -- 1 2
a, b = b, a            -- swap!
print(a, b)            -- 2 1

local x, y, z = 1, 2    -- z is nil
print(x, y, z)          -- 1 2 nil

local _, second = table.unpack({10, 20, 30})
print(second)           -- 20 — _ discards the first''',
        '''-- Short-circuit evaluation
local a = nil
local result = a or "default"
print(result)          -- default

local b = 42
print(b and "set" or "unset")   -- set — common idiom

-- Chained defaults:
local config = {name = "Alice"}
local name = config.name or config.fallback or "anonymous"
print(name)            -- Alice''',
        '''-- The truthiness gotcha
-- In Lua, ONLY nil and false are falsy.
print(0 and "zero is truthy")      -- zero is truthy
print("" and "empty is truthy")    -- empty is truthy
print(nil and "never")             -- nil
print(false or "fallback")         -- fallback
-- This matters in conditions and defaults.''',
    ],
    14: [
        '''-- Weak tables: memory management
local cache = setmetatable({}, {
  __mode = "v"     -- weak values: collectable when unused
})

cache[1] = {expensive = true}
collectgarbage()
print(cache[1])    -- nil — the value was collected
-- Weak tables let caches release memory under pressure.''',
        '''-- collectgarbage and memory
print(collectgarbage("count"))    -- KB in use
local t = {}
for i = 1, 100000 do t[i] = i end
print(collectgarbage("count"))
t = nil
collectgarbage("collect")         -- force a full collection
print(collectgarbage("count"))
-- Lua manages memory automatically with GC.''',
        '''-- Upvalues and shared state
local function make_cache()
  local cache = {}
  return {
    get = function(k) return cache[k] end,
    set = function(k, v) cache[k] = v end,
  }
end

local c = make_cache()
c.set("a", 1)
print(c.get("a"))      -- 1
print(c.get("b"))      -- nil
-- Upvalues (cache) are shared by all closures created in scope.''',
        '''-- The module cache pattern
local loaded = {}
function load_or_build(name, builder)
  if not loaded[name] then
    loaded[name] = builder()
  end
  return loaded[name]
end

local first = load_or_build("x", function() return {n = 42} end)
local second = load_or_build("x", function() return {n = 0} end)
print(first == second)    -- true — same cached instance
print(first.n)            -- 42''',
    ],
    15: [
        '''-- Embedding Lua: the C API surface
-- // In C:
-- lua_State *L = luaL_newstate();
-- luaL_openlibs(L);
-- luaL_dofile(L, "script.lua");
-- lua_close(L);
print("Lua embeds into C apps via the lua_State API")
-- Integration points: calling Lua functions, sharing tables,
-- registering C functions callable from Lua.''',
        '''-- LuaJIT and performance
print("LuaJIT compiles hot paths to machine code")
print("FFI lets you call C functions directly")
print("Interpreter: simple, portable, predictable")
-- LuaJIT is a drop-in, much faster implementation.''',
        '''-- Lua versions at a glance
print("Lua 5.1: classic; LuaJIT tracks 5.1")
print("Lua 5.2: goto, _ENV")
print("Lua 5.3: integers, bitwise operators")
print("Lua 5.4: generational GC, to-be-closed vars")
print("LuaRocks is the package manager")
-- Version choice matters for compatibility.''',
        '''-- Lightweight server and game scripting
-- NGINX + OpenResty: Lua in the web server
-- LÖVE, Defold, Roblox: Lua in game engines
-- Redis: Lua scripts for atomic operations
print("Lua powers OpenResty, game engines, and Redis")
-- Redis EVAL runs Lua atomically on the server.''',
    ],
    16: [
        '''-- Basic Object-Oriented Programming recap
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
-- The __index metatable provides method lookup.''',
        '''-- Method chaining
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
-- Each method returns self for fluent chains.''',
        '''-- Duck typing: no interfaces needed
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
-- If it walks like a duck and quacks like a duck...''',
        '''-- OOP patterns: singleton
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
-- Config.get() always returns the SAME instance.''',
    ],
    17: [
        '''-- The argparse-style manual parsing
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
-- The global `arg` table holds command-line arguments.''',
        '''-- Standard arg table
print(#arg)            -- number of arguments
print(arg[0])          -- script name
print(arg[1])          -- first argument
-- arg is a global table available to the script.''',
        '''-- Environment variables and process info
print(os.getenv("HOME"))          -- home directory
print(os.getenv("PATH"))          -- path
local sep = package.config:sub(1, 1)   -- path separator
print("sep: " .. sep)
-- package.config gives platform details.''',
        '''-- A small CLI tool
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
-- Hello, Alice!''',
    ],
    18: [
        '''-- Testing with a simple assertion framework
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
end)''',
        '''-- Busted-style expectations (conceptual)
-- busted is the popular Lua testing framework
-- describe("math", function()
--   it("adds", function()
--     assert.are.equal(4, 2 + 2)
--   end)
-- end)
print("busted: describe/it blocks, spies, and mocks")
print("run with: busted spec/")''',
        '''-- Unit test for the counter module
local make_counter = require("counter")   -- assume module

local c = make_counter()
assert(c() == 1, "first call returns 1")
assert(c() == 2, "second call returns 2")

-- A poor-man's test runner over pcall:
local tests = { {"first", c() == 1}, {"second", c() == 2} }
for _, t in ipairs(tests) do
  print(t[1], t[2] and "PASS" or "FAIL")
end''',
        '''-- The test cycle
print("1. Write the failing test")
print("2. Run it — red")
print("3. Implement the module")
print("4. Run again — green")
print("5. Refactor, keeping tests green")
-- Lua's simplicity makes tests quick to write.''',
    ],
    19: [
        '''-- Performance: locals are faster
local sum = 0
local start = os.clock()
for i = 1, 10000000 do
  sum = sum + i
end
print("sum: " .. sum)
print("time: " .. (os.clock() - start) .. "s")
-- Local variables avoid global table lookups.''',
        '''-- Avoiding table reallocation
-- Pre-allocate array tables with the length hint:
local t = {}
for i = 1, 100000 do
  t[i] = i
end
print(#t)
-- Avoid growing tables one element at a time in hot loops
-- when you know the size ahead of time.''',
        '''-- String building: table.concat beats ..
local parts = {}
for i = 1, 1000 do
  parts[i] = "item " .. i
end
local joined = table.concat(parts, ", ")
print(#joined)
-- Repeated .. creates many intermediate strings;
-- table.concat builds one result efficiently.''',
        '''-- Choosing data structures
print("Arrays: table with 1..n integer keys")
print("Sets: table with keys, values ignored")
print("Queues: table.remove(t, 1) for FIFO")
print("Maps: table with any keys")
local set = {}
set["apple"] = true
set["banana"] = true
print(set["apple"] and "apple in set")   -- apple in set
print(set["cherry"] and "cherry in set") -- nil (not present)''',
    ],
    20: [
        '''-- A complete word-counter CLI
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
-- the 3, quick 1, brown 1, fox 1''',
        '''-- Building a simple HTTP client (conceptual)
-- LuaSocket provides networking:
-- local http = require("socket.http")
-- local body = http.request("https://example.com")
-- print(body)
print("LuaSocket: http.request(url) fetches pages")
-- Combined with cjson you get JSON API clients.''',
        '''-- JSON with cjson
-- local cjson = require("cjson")
-- local obj = cjson.decode('{"name": "Alice"}')
-- print(obj.name)
-- local json = cjson.encode({x = 1, y = 2})
print("cjson encodes/decodes JSON between Lua and text")
-- Integration with web frameworks via OpenResty.''',
        '''-- The Redis scripting pattern
-- EVAL "return redis.call('GET', KEYS[1])" 1 mykey
-- Lua scripts run atomically inside Redis:
--   local val = redis.call('GET', KEYS[1])
--   redis.call('SET', KEYS[1], tonumber(val) + 1)
--   return redis.call('GET', KEYS[1])
print("Redis EVAL runs Lua atomically for counters")
-- This powers rate limiters, locks, and caches.''',
    ],
    21: [
        '''-- A mini dependency-injection container
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
print(app.db.connected)   -- true — same db instance''',
        '''-- Event loop pattern with coroutines
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
-- A and B interleave cooperatively on one thread.''',
        '''-- A simple observer pattern
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
-- B got update''',
        '''-- The Lua ecosystem at a glance
print("LuaRocks: package manager")
print("LÖVE: 2D game framework")
print("OpenResty: web platform on NGINX")
print("Redis: scripting inside the datastore")
print("LuaJIT: high-performance JIT compiler")
-- From game engines to web servers to databases,
-- Lua's small size makes it the embedded language of choice.''',
    ],
}

LESSONS = [
    dict(slug='lua-01-getting-started', title='Getting Started with Lua',
         desc='Installing, printing, variables, and comments.',
         dur='45 min', diff='beginner', prereq=[],
         objs=['Write and run a Lua script',
               'Use basic expressions',
               'Declare global and local variables',
               'Write comments'],
         refs=[dict(title='Lua — Getting Started', url='https://www.lua.org/start.html'),
               dict(title='Lua — Reference Manual', url='https://www.lua.org/manual/5.4/'),
               dict(title='Programming in Lua (PiL)', url='https://www.lua.org/pil/')]),
    dict(slug='lua-02-values-types', title='Values and Types',
         desc='Numbers, strings, the string library, booleans, and nil.',
         dur='45 min', diff='beginner', prereq=['LUA-01'],
         objs=['Do arithmetic with integers and floats',
               'Create and format strings',
               'Use the string library',
               'Understand truthiness'],
         refs=[dict(title='Lua — Types', url='https://www.lua.org/manual/5.4/manual.html#2.1'),
               dict(title='Lua — String Library', url='https://www.lua.org/manual/5.4/manual.html#6.4'),
               dict(title='PiL — Types and Values', url='https://www.lua.org/pil/2.html')]),
    dict(slug='lua-03-control-flow', title='Control Flow',
         desc='if/elseif/else, while, for, repeat, and goto.',
         dur='45 min', diff='beginner', prereq=['LUA-02'],
         objs=['Branch with if and elseif',
               'Loop with while',
               'Use numeric and generic for',
               'Control flow with repeat and goto'],
         refs=[dict(title='Lua — Control Structures', url='https://www.lua.org/manual/5.4/manual.html#3.3'),
               dict(title='PiL — Control Structures', url='https://www.lua.org/pil/4.html'),
               dict(title='Lua — goto', url='https://www.lua.org/manual/5.4/manual.html#3.3.4')]),
    dict(slug='lua-04-functions', title='Functions',
         desc='Basic functions, multiple returns, variadics, and closures.',
         dur='60 min', diff='intermediate', prereq=['LUA-03'],
         objs=['Define and call functions',
               'Return multiple values',
               'Write variadic functions',
               'Capture state in closures'],
         refs=[dict(title='Lua — Functions', url='https://www.lua.org/manual/5.4/manual.html#6.1'),
               dict(title='PiL — Functions', url='https://www.lua.org/pil/5.html'),
               dict(title='PiL — Closures', url='https://www.lua.org/pil/6.1.html')]),
    dict(slug='lua-05-tables', title='Tables',
         desc='Tables as arrays and maps, constructors, iteration, and the table library.',
         dur='60 min', diff='intermediate', prereq=['LUA-04'],
         objs=['Use tables as arrays',
               'Use tables as dictionaries',
               'Iterate with pairs and ipairs',
               'Use the table library'],
         refs=[dict(title='Lua — Tables', url='https://www.lua.org/manual/5.4/manual.html#6.6'),
               dict(title='PiL — Tables', url='https://www.lua.org/pil/2.5.html'),
               dict(title='PiL — Table Library', url='https://www.lua.org/pil/19.html')]),
    dict(slug='lua-06-metatables', title='Metatables',
         desc='__index, __newindex, operator metamethods, and __tostring.',
         dur='60 min', diff='intermediate', prereq=['LUA-05'],
         objs=['Customize lookup with __index',
               'Intercept assignment with __newindex',
               'Overload operators',
               'Customize printing with __tostring'],
         refs=[dict(title='Lua — Metatables', url='https://www.lua.org/manual/5.4/manual.html#2.4'),
               dict(title='PiL — Metatables', url='https://www.lua.org/pil/13.html'),
               dict(title='Lua — Metamethods list', url='https://www.lua.org/manual/5.4/manual.html#6.1')]),
    dict(slug='lua-07-modules', title='Modules and Packages',
         desc='Module patterns, require, encapsulation, and namespaces.',
         dur='60 min', diff='intermediate', prereq=['LUA-06'],
         objs=['Write modules',
               'Load with require',
               'Encapsulate private state',
               'Use tables as namespaces'],
         refs=[dict(title='PiL — Modules', url='https://www.lua.org/pil/15.html'),
               dict(title='Lua — require', url='https://www.lua.org/manual/5.4/manual.html#6.3'),
               dict(title='LuaRocks — the package manager', url='https://luarocks.org/')]),
    dict(slug='lua-08-patterns', title='Pattern Matching',
         desc='match, find, gsub, captures, and character classes.',
         dur='60 min', diff='intermediate', prereq=['LUA-07'],
         objs=['Match with string:match',
               'Find positions with string:find',
               'Replace with gsub',
               'Capture groups'],
         refs=[dict(title='Lua — Patterns', url='https://www.lua.org/manual/5.4/manual.html#6.4.1'),
               dict(title='PiL — Pattern Matching', url='https://www.lua.org/pil/20.html'),
               dict(title='Lua Patterns tutorial', url='https://www.lua.org/pil/20.2.html')]),
    dict(slug='lua-09-oop', title='Object-Oriented Programming',
         desc='The self pattern, colon methods, inheritance, and composition.',
         dur='75 min', diff='advanced', prereq=['LUA-08'],
         objs=['Build classes with metatables',
               'Use colon method syntax',
               'Implement inheritance',
               'Compose objects'],
         refs=[dict(title='PiL — OOP', url='https://www.lua.org/pil/16.html'),
               dict(title='PiL — Inheritance', url='https://www.lua.org/pil/16.2.html'),
               dict(title='PiL — Private State', url='https://www.lua.org/pil/16.4.html')]),
    dict(slug='lua-10-error-handling', title='Error Handling',
         desc='pcall, xpcall, error, and assert.',
         dur='60 min', diff='intermediate', prereq=['LUA-09'],
         objs=['Catch errors with pcall',
               'Transform errors with xpcall',
               'Raise with error and assert',
               'Build try/catch patterns'],
         refs=[dict(title='PiL — Errors', url='https://www.lua.org/pil/8.3.html'),
               dict(title='PiL — Error Handling', url='https://www.lua.org/pil/8.4.html'),
               dict(title='Lua — pcall', url='https://www.lua.org/manual/5.4/manual.html#6.1')]),
    dict(slug='lua-11-coroutines', title='Coroutines',
         desc='Cooperative multitasking, generators, and state machines.',
         dur='75 min', diff='advanced', prereq=['LUA-10'],
         objs=['Create coroutines',
               'Build generators',
               'Model state machines',
               'Compare with threads'],
         refs=[dict(title='Lua — Coroutines', url='https://www.lua.org/manual/5.4/manual.html#6.2'),
               dict(title='PiL — Coroutines', url='https://www.lua.org/pil/9.html'),
               dict(title='PiL — Generators', url='https://www.lua.org/pil/9.3.html')]),
    dict(slug='lua-12-stdlib', title='Standard Library',
         desc='os, io, math, and table utilities.',
         dur='60 min', diff='intermediate', prereq=['LUA-11'],
         objs=['Work with dates and time',
               'Read and write files',
               'Use the math library',
               'Manipulate tables'],
         refs=[dict(title='Lua — Standard Libraries', url='https://www.lua.org/manual/5.4/manual.html#6'),
               dict(title='Lua — os library', url='https://www.lua.org/manual/5.4/manual.html#6.9'),
               dict(title='Lua — io library', url='https://www.lua.org/manual/5.4/manual.html#6.8')]),
    dict(slug='lua-13-variadic-multi', title='Variadics and Multiple Values',
         desc='... variadics, select, multiple assignment, and defaults.',
         dur='60 min', diff='intermediate', prereq=['LUA-12'],
         objs=['Collect arguments with ...',
               'Use select',
               'Swap and unpack values',
               'Apply defaults idiomatically'],
         refs=[dict(title='Lua — Variadic Functions', url='https://www.lua.org/manual/5.4/manual.html#6.1'),
               dict(title='PiL — Variadic Functions', url='https://www.lua.org/pil/5.2.html'),
               dict(title='Lua — select', url='https://www.lua.org/manual/5.4/manual.html#6.1')]),
    dict(slug='lua-14-memory', title='Memory Management',
         desc='Weak tables, garbage collection, and upvalues.',
         dur='75 min', diff='advanced', prereq=['LUA-13'],
         objs=['Build weak tables',
               'Control garbage collection',
               'Share state via upvalues',
               'Cache with modules'],
         refs=[dict(title='PiL — Weak Tables', url='https://www.lua.org/pil/17.html'),
               dict(title='Lua — collectgarbage', url='https://www.lua.org/manual/5.4/manual.html#6.1'),
               dict(title='Lua — Garbage Collection', url='https://www.lua.org/manual/5.4/manual.html#2.5')]),
    dict(slug='lua-15-embedding', title='Embedding and Ecosystem',
         desc='The C API, LuaJIT, versions, and use cases.',
         dur='75 min', diff='advanced', prereq=['LUA-14'],
         objs=['Embed Lua in applications',
               'Understand LuaJIT',
               'Choose the right version',
               'Apply Lua in production'],
         refs=[dict(title='Lua — C API', url='https://www.lua.org/manual/5.4/manual.html#4'),
               dict(title='LuaJIT — homepage', url='https://luajit.org/'),
               dict(title='OpenResty — Lua on NGINX', url='https://openresty.org/en/')]),
    dict(slug='lua-16-oop-advanced', title='Advanced OOP Patterns',
         desc='Method chaining, duck typing, and singletons.',
         dur='75 min', diff='advanced', prereq=['LUA-15'],
         objs=['Chain methods',
               'Apply duck typing',
               'Build singletons',
               'Design with composition'],
         refs=[dict(title='PiL — OOP', url='https://www.lua.org/pil/16.html'),
               dict(title='PiL — Inheritance', url='https://www.lua.org/pil/16.2.html'),
               dict(title='Lua Design Patterns', url='https://www.lua.org/pil/contents.html')]),
    dict(slug='lua-17-cli', title='Command-Line Tools',
         desc='arg handling, environment, and small CLI programs.',
         dur='60 min', diff='intermediate', prereq=['LUA-16'],
         objs=['Parse arguments',
               'Use the arg table',
               'Read environment variables',
               'Build a CLI tool'],
         refs=[dict(title='Lua — arg', url='https://www.lua.org/manual/5.4/manual.html#6.1'),
               dict(title='PiL — Command-Line', url='https://www.lua.org/pil/1.1.html'),
               dict(title='Lua — package.config', url='https://www.lua.org/manual/5.4/manual.html#6.3')]),
    dict(slug='lua-18-testing', title='Testing',
         desc='Assertions, pcall-based runners, busted, and the test cycle.',
         dur='60 min', diff='intermediate', prereq=['LUA-17'],
         objs=['Write assertion tests',
               'Use busted-style suites',
               'Unit test modules',
               'Apply the red-green-refactor cycle'],
         refs=[dict(title='busted — Lua testing', url='https://lunarmodules.github.io/busted/'),
               dict(title='LuaUnit — unit testing', url='https://github.com/bluebird75/luaunit'),
               dict(title='PiL — Assertions', url='https://www.lua.org/pil/8.2.html')]),
    dict(slug='lua-19-performance', title='Performance',
         desc='Locals, table allocation, string building, and data structures.',
         dur='75 min', diff='advanced', prereq=['LUA-18'],
         objs=['Use locals for speed',
               'Preallocate tables',
               'Build strings with table.concat',
               'Choose the right structure'],
         refs=[dict(title='Lua — Performance Tips', url='https://www.lua.org/gems/sample.pdf'),
               dict(title='LuaJIT — performance', url='https://luajit.org/performance.html'),
               dict(title='PiL — Efficiency', url='https://www.lua.org/pil/11.html')]),
    dict(slug='lua-20-pipelines', title='Real-World Programs',
         desc='Word counting, HTTP, JSON, and Redis scripting.',
         dur='75 min', diff='advanced', prereq=['LUA-19'],
         objs=['Count words with patterns',
               'Fetch pages with LuaSocket',
               'Encode JSON with cjson',
               'Script Redis atomically'],
         refs=[dict(title='LuaSocket — networking', url='https://lunarmodules.github.io/luasocket/'),
               dict(title='lua-cjson — JSON', url='https://github.com/openresty/lua-cjson'),
               dict(title='Redis — Lua scripting', url='https://redis.io/docs/manual/programmability/eval-intro/')]),
    dict(slug='lua-21-advanced-patterns', title='Advanced Patterns',
         desc='DI containers, event loops, observers, and the ecosystem.',
         dur='75 min', diff='expert', prereq=['LUA-20'],
         objs=['Build a DI container',
               'Run event loops with coroutines',
               'Implement observers',
               'Navigate the ecosystem'],
         refs=[dict(title='LuaRocks — packages', url='https://luarocks.org/'),
               dict(title='LÖVE — game framework', url='https://love2d.org/'),
               dict(title='OpenResty — web platform', url='https://openresty.org/en/')]),
]


if __name__ == '__main__':
    run_gen(LANGUAGE, 'lua', LESSONS, CODE, BASE)
