#!/usr/bin/env python3
"""Generate the 21-lesson Julia curriculum at Python/JS/Java depth.
Uses the shared gen_lib template. Exact refs from docs.julialang.org.
Each lesson has 4 sub-topics, each with its OWN distinct code sample.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import main as run_gen  # noqa: E402

LANGUAGE = 'julia'

BASE = os.path.join(os.path.dirname(__file__), '..', '..', 'static-data', 'knowledge', 'languages', 'julia')

CODE = {
    1: [
        '''# Your first Julia program
println("Hello, 100X Systems!")

# Run with: julia hello.jl  ->  Hello, 100X Systems!
''',
        '''# The REPL: julia  (press ) to enter package mode, ? for help)
# Arithmetic is immediate and precise by default:
println(2^10)        # 1024 — ^ is exponentiation, NOT bitwise
println(7 / 2)       # 3.5 — float division (not integer!)
println(7 ÷ 2)       # 3   — integer division
''',
        '''# Julia is dynamically typed but JIT-compiled to native code
function greet(name)
    return "Hello, " * name * "!"
end

println(greet("Julia"))  # Hello, Julia!
''',
        '''# Scripts, packages, and one-liners
# julia -e 'println(1 + 1)'
# julia script.jl arg1 arg2
println("Startup is fast because of precompilation")
''',
    ],
    2: [
        '''# Core types: Int, Float64, Bool, Char, String
println(typeof(42))        # Int64
println(typeof(3.14))      # Float64
println(typeof(true))      # Bool
println(typeof('a'))       # Char (single quotes!)
println(typeof("hi"))      # String (double quotes)
''',
        '''# Integer types — pick the size you need
println(typemax(Int8))     # 127
println(typemax(UInt64))   # 18446744073709551615
x = 10
println(x isa Integer)     # true
''',
        '''# Float behavior: NaN, Inf, and precision
println(1.0 / 0.0)         # Inf
println(0.0 / 0.0)         # NaN
println(0.1 + 0.2)         # 0.30000000000000004 — same IEEE as everywhere
''',
        '''# Nothing, missing, and nothingness
println(nothing)           # nothing — Julia's null
println(missing)           # missing — propagates through calculations
println(1 + missing)       # missing
''',
    ],
    3: [
        '''# Variables: convention is lowercase with underscores
name = "Ada"
age = 36
const GRAVITY = 9.81      # const cannot be rebound (warning if you try)
println(name * " is " * string(age) * " years old")
''',
        '''# Scoping: global vs local
x = 10                     # global
function f()
    y = 20                 # local
    return x + y           # global x is readable
end
println(f())               # 30
''',
        '''# Soft vs hard scope: loops introduce a new scope
sum_ = 0
for i in 1:5
    global sum_ += i       # need `global` to mutate outer var
end
println(sum_)              # 15
''',
        '''# let blocks create fresh local scopes
f = let
    counter = 0
    () -> (counter += 1; counter)
end
println(f())               # 1
println(f())               # 2 — closure keeps state
''',
    ],
    4: [
        '''# Arithmetic operators
println(7 % 4)             # 3 — remainder
println(2^10)              # 1024 — power
println(div(7, 2))         # 3 — integer division
println(rem(7, 2))         # 1 — remainder
''',
        '''# Comparison and chained comparisons
println(1 < 2 < 3)         # true — chaining works natively!
println(1 == 1.0)          # true — numeric equality
println(1 === 1.0)         # false — identical types
''',
        '''# Logical operators: && and || short-circuit
x = nothing
y = x !== nothing && x + 1
println(y)                 # false
z = x !== nothing || "fallback"
println(z)                 # "fallback"
''',
        '''# Bitwise operations
println(0b1100 & 0b1010)   # 0b1000 = 8
println(0b1100 | 0b1010)   # 0b1110 = 14
println(0b1100 ⊻ 0b1010)   # 0b0110 = 6 (xor)
println(1 << 4)            # 16
''',
    ],
    5: [
        '''# Functions: the return keyword is optional (last expression wins)
add(a, b) = a + b          # one-line function definition
function mul(a, b)
    a * b                  # implicit return
end
println(add(2, 3))         # 5
println(mul(2, 3))         # 6
''',
        '''# Optional and keyword arguments
function greet(name; punctuation="!")
    return "Hello, " * name * punctuation
end
println(greet("Julia"))              # Hello, Julia!
println(greet("Julia"; punctuation="?"))  # Hello, Julia?
''',
        '''# Anonymous functions and do blocks
doubles = map(x -> x * 2, [1, 2, 3])
println(doubles)           # [2, 4, 6]

# do block = multi-line anonymous function
total = sum([1, 2, 3, 4]) do x
    x > 2 ? x : 0
end
println(total)             # 7
''',
        '''# Varargs and splatting
function total(args...)
    sum(args)
end
println(total(1, 2, 3, 4)) # 10
nums = [1, 2, 3]
println(total(nums...))    # 6 — splat a collection
''',
    ],
    6: [
        '''# Multiple dispatch: the heart of Julia
describe(x::Int) = "an integer: $x"
describe(x::Float64) = "a float: $x"
describe(x::String) = "a string: $x"

println(describe(42))      # an integer: 42
println(describe(4.2))     # a float: 4.2
println(describe("x"))     # a string: x
''',
        '''# Dispatch on multiple arguments
combine(a::Number, b::Number) = a + b
combine(a::String, b::String) = a * b
combine(a::String, b::Number) = a * string(b)

println(combine(2, 3))     # 5
println(combine("a", "b")) # "ab"
println(combine("x", 2))   # "x2"
''',
        '''# Abstract types enable generic code
abstract type Animal end

struct Dog <: Animal
    name::String
end

speak(a::Dog) = "Woof! I am $(a.name)"
println(speak(Dog("Rex"))) # Woof! I am Rex
''',
        '''# Method specificity: Julia picks the most specific match
f(x) = "generic: $x"
f(x::Number) = "number: $x"
f(x::Int) = "int: $x"

println(f("a"))            # generic: a
println(f(2.5))            # number: 2.5
println(f(2))              # int: 2
''',
    ],
    7: [
        '''# if / elseif / else
function grade(score)
    if score >= 90
        "A"
    elseif score >= 80
        "B"
    else
        "C"
    end
end
println(grade(95))         # A
''',
        '''# Ternary and short-circuit evaluation
x = 5
label = x > 3 ? "big" : "small"
println(label)             # big
println(x > 3 && "yes")    # "yes" — && returns last value
''',
        '''# for loops: ranges, arrays, and nested
total = 0
for i in 1:10
    global total += i      # `global` needed at top level (soft scope)
end
println(total)             # 55

for (i, v) in enumerate(["a", "b"])
    println("$i -> $v")
end
''',
        '''# while loops and break/continue
n = 0
while true
    global n += 1
    n >= 5 && break
end
println(n)                 # 5

for i in 1:10
    i % 2 == 0 && continue
    print(i, " ")
end
# 1 3 5 7 9
''',
    ],
    8: [
        '''# Strings are immutable byte sequences with UTF-8 support
s = "héllo"
println(length(s))         # 5 — character count
println(ncodeunits(s))     # 6 — bytes
println(uppercase(s))      # HÉLLO
''',
        '''# String interpolation — the idiomatic way to build strings
name = "Julia"
version = 1.9
println("Welcome to $name v$version")
println("2 + 2 = $(2 + 2)")   # 2 + 2 = 4
''',
        '''# String functions: split, join, replace, startswith
println(split("a,b,c", ","))       # ["a", "b", "c"]
println(join(["x", "y"], "-"))     # "x-y"
println(replace("banana", "a" => "o"))  # "bonono"
println(startswith("hello", "he")) # true
''',
        '''# Unicode identifiers and raw strings
α = 2.0
β = 3.0
println(α * β)             # 6.0

raw_path = raw"C:\\Users\\ada"
println(raw_path)          # C:\\Users\\ada — no escaping
''',
    ],
    9: [
        '''# Arrays: homogeneous, 1-based indexed, column-major
v = [10, 20, 30]
println(v[1])              # 10 — indexing starts at 1!
println(v[end])            # 30
println(length(v))         # 3
''',
        '''# Comprehensions and generator expressions
squares = [x^2 for x in 1:5]
println(squares)           # [1, 4, 9, 16, 25]

even_squares = [x^2 for x in 1:10 if iseven(x)]
println(even_squares)      # [4, 16, 36, 64, 100]
''',
        '''# Broadcasting: the dot applies a function elementwise
nums = [1, 2, 3]
println(nums .+ 10)        # [11, 12, 13]
println(sin.(nums))        # elementwise sin

# .= mutates in place
nums .= nums .* 2
println(nums)              # [2, 4, 6]
''',
        '''# Matrices: 2D arrays
M = [1 2; 3 4]             # 2x2 matrix
println(M[1, 2])           # 2 — row 1, col 2
println(size(M))           # (2, 2)
println(M')                # adjoint (transpose for reals)
''',
    ],
    10: [
        '''# Tuples: immutable, heterogeneous
t = (1, "two", 3.0)
println(t[1])              # 1
a, b, c = t                # destructuring
println("$a $b $c")        # 1 two 3.0
''',
        '''# NamedTuples: tuples with named fields
person = (name="Ada", age=36)
println(person.name)       # Ada
println(person.age)        # 36
''',
        '''# Dictionaries: mutable key-value maps
d = Dict("a" => 1, "b" => 2)
d["c"] = 3
println(keys(d))           # collection of keys
println(haskey(d, "a"))    # true
println(get(d, "z", 0))    # 0 — default value
''',
        '''# Sets and push!/pop! for mutable collections
s = Set([1, 2, 2, 3])
println(s)                 # Set([2, 3, 1]) — duplicates removed

stack = Int[]
push!(stack, 1, 2, 3)
println(pop!(stack))       # 3
println(stack)             # [1, 2]
''',
    ],
    11: [
        '''# Structs: immutable by default with concrete field types
struct Point
    x::Float64
    y::Float64
end

p = Point(1.0, 2.0)
println(p.x)               # 1.0
''',
        '''# Mutable structs for stateful objects
mutable struct Counter
    value::Int
end

function increment!(c::Counter)
    c.value += 1
end

c = Counter(0)
increment!(c)
increment!(c)
println(c.value)           # 2
''',
        '''# Default constructors and inner constructors
struct Circle
    radius::Float64
    Circle(r) = new(r)     # inner constructor validates
end

c = Circle(2.5)
println(c.radius)          # 2.5
''',
        '''# Field access and property mutation (immutable -> new object)
struct Rect
    w::Float64
    h::Float64
end

area(r::Rect) = r.w * r.h
r = Rect(3.0, 4.0)
println(area(r))           # 12.0
''',
    ],
    12: [
        '''# Parametric types: parameterize on the element type
struct Box{T}
    contents::T
end

b1 = Box(42)               # Box{Int64}
b2 = Box("hi")             # Box{String}
println(b1.contents)       # 42
''',
        '''# Union types and Any
x::Union{Int, String} = 42
println(x)                 # 42
y::Any = "anything"
println(y)                 # anything
''',
        '''# Type hierarchy: Int <: Signed <: Integer <: Real <: Number
println(Int <: Integer)    # true
println(Integer <: Real)   # true
println(Real <: Number)    # true
''',
        '''# Type annotations give performance AND safety
function scale(x::Float64, k::Float64)
    x * k
end

println(scale(2.0, 3.0))   # 6.0
# scale(2, 3) would throw MethodError — that is a feature!
''',
    ],
    13: [
        '''# Modules: namespaces for related code
module Greetings
    export hello
    hello(name) = "Hello, $name!"
    secret() = "internal only"
end

using .Greetings
println(hello("Julia"))    # Hello, Julia!
''',
        '''# Package management with Pkg
# using Pkg; Pkg.add("DataFrames")
# Pkg.activate("myproject")   # local environment
# Pkg.status()                # list installed packages
println("Packages live in environments, not globally")
''',
        '''# import vs using: qualified access
import Statistics
data = [1.0, 2.0, 3.0]
println(Statistics.mean(data))   # 2.0
''',
        '''# include: pull in other source files
# include("helpers.jl")       # runs that file in current scope
# The convention: one module per file for libraries
println("Modular code keeps projects navigable")
''',
    ],
    14: [
        '''# Symbols and expressions: code is data
s = :x
println(typeof(s))         # Symbol
expr = :(a + b)
println(expr.args)         # [:+, :a, :b] — the AST
''',
        '''# quote and eval: building expressions programmatically
ex = quote
    x = 40
    x + 2
end
println(eval(ex))          # 42
''',
        '''# Macros: functions on expressions, expanded at parse time
macro shout(ex)
    return :(uppercase($(esc(ex))))
end

println(@shout "hello")    # HELLO
''',
        '''# @time and @show — built-in utility macros
@show 2 + 2                # 2 + 2 = 4
@time sum(1:1_000_000)     # prints elapsed time
''',
    ],
    15: [
        '''# try/catch/finally for graceful error handling
try
    error("something broke")
catch e
    println("caught: ", e) # caught: ErrorException("something broke")
finally
    println("cleanup ran")
end
''',
        '''# throw to raise your own exceptions
function check_age(age)
    age < 0 && throw(ArgumentError("age cannot be negative"))
    return "ok"
end

println(check_age(30))     # ok
# check_age(-1) throws ArgumentError
''',
        '''# Capturing exception details with `catch e`
try
    x = 1 + "a"            # MethodError
catch e
    println(typeof(e))     # MethodError
    println(e.f)           # +  (the failing function)
end
''',
        '''# Errors are values-like: use try/catch to build safe wrappers
function safe_sqrt(x)
    try
        sqrt(x)
    catch
        NaN
    end
end

println(safe_sqrt(-1.0))   # NaN
println(safe_sqrt(9.0))    # 3.0
''',
    ],
    16: [
        '''# File I/O: read and write text files
open("hello.txt", "w") do io
    write(io, "Hello, Julia!\\n")
    write(io, "Second line\\n")
end
println(read("hello.txt", String))  # full file as one String
''',
        '''# readlines and per-line processing
open("hello.txt") do io
    for line in eachline(io)
        println(uppercase(line))
    end
end
''',
        '''# CSV without dependencies — manual parse
data = "name,age\\nAda,36\\nGrace,85\\n"
for row in split(data, "\\n"; keepempty=false)
    fields = split(row, ",")
    println("$fields[1] is $fields[2] years old")
end
''',
        '''# Standard library: JSON3/CSV come from packages
# using CSV, DataFrames
# df = CSV.read("data.csv", DataFrame)
# df[df.age .> 30, :name]
println("For heavy data work add: CSV.jl, DataFrames.jl, JSON3.jl")
''',
    ],
    17: [
        '''# Ranges: the lazy sequence workhorse
r = 1:10
println(length(r))         # 10
println(collect(r))        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
println(1:2:10)            # 1:2:10 (step 2)
''',
        '''# Generators: lazy, composeable pipelines
gen = (x^2 for x in 1:5 if isodd(x))
println(gen)               # Base.Generator — lazy!
println(collect(gen))      # [1, 9, 25]
''',
        '''# Iterators: enumerate, zip, take, drop
println(collect(zip([1, 2], ["a", "b"])))
# [(1, "a"), (2, "b")]

for (i, v) in enumerate(["x", "y"])
    println("$i=$v")
end
''',
        '''# reduce and mapreduce
println(reduce(+, 1:5))             # 15
println(mapreduce(x -> x^2, +, 1:5))  # 55
println(foldl(*, 1:5))              # 120
''',
    ],
    18: [
        '''# missing vs nothing vs NaN — three different things
println(typeof(missing))   # Missing
println(typeof(nothing))   # Nothing
println(typeof(NaN))       # Float64

# missing propagates: 1 + missing == missing
println(ismissing(1 + missing))  # true
''',
        '''# skipmissing: drop missing values from a collection
data = [1, missing, 3, missing, 5]
println(collect(skipmissing(data)))  # [1, 3, 5]
println(sum(skipmissing(data)))      # 9
''',
        '''# coerce with something() and fallbacks
x = nothing
println(something(x, "default"))   # "default"

y = 42
println(something(y, "default"))   # 42
''',
        '''# Working with missing in real data
data = [1.0, missing, 3.0]
# mean(data) errors without Statistics
using Statistics
println(mean(skipmissing(data)))    # 2.0
''',
    ],
    19: [
        '''# Multithreading with @threads
results = zeros(Int, 8)
Threads.@threads for i in 1:8
    results[i] = i^2
end
println(results)           # [1, 4, 9, 16, 25, 36, 49, 64]
# Run with: julia -t 4 script.jl
''',
        '''# Tasks and @async / @sync for concurrency
@sync begin
    @async println("task 1 started")
    @async println("task 2 started")
end
# Tasks are lightweight — thousands are fine
''',
        '''# Channels: message passing between tasks
ch = Channel{Int}(32)
@async for i in 1:5
    put!(ch, i^2)
end

println(take!(ch))         # 1
println(take!(ch))         # 4
''',
        '''# Distributed computing: @spawn (requires Distributed)
# using Distributed; addprocs(4)
# r = @spawn sum(1:1_000_000)
# println(fetch(r))
println("Distributed.jl scales to clusters")
''',
    ],
    20: [
        '''# Performance: type stability matters
function sum_positive(xs)
    s = 0                  # annotate for stability: s = 0.0
    for x in xs
        x > 0 && (s += x)
    end
    s
end
println(sum_positive([1, -2, 3]))  # 4
''',
        '''# @code_warntype reveals type instability
function unstable(x)
    x > 0 ? 1 : 1.0        # Union{Int64, Float64} — boxed!
end

# @code_warntype unstable(1)
println("Avoid Union return types for hot loops")
''',
        '''# @time and @btime for measuring performance
using Printf
@time sum(1:1_000_000)     # prints allocation + time

# @btime from BenchmarkTools is even better:
# using BenchmarkTools; @btime sum(1:1_000_000)
''',
        '''# The performance mantra: global scope is slow
function fast(xs)
    s = 0.0
    for x in xs
        s += x
    end
    s
end
println(fast(1.0:1_000_000.0))  # 5.000005e11
''',
    ],
    21: [
        '''# The ecosystem: DataFrames + Plots + DifferentialEquations
# using DataFrames
# df = DataFrame(name=["Ada", "Grace"], age=[36, 85])
# df[df.age .> 40, :name]  # filter

# using Plots
# plot(1:10, sin.(1:10))
println("Julia's ecosystem: scientific, data, and web")
''',
        '''# The JuliaHub / JuliaLang community
# julialang.org       — official docs and downloads
# JuliaAcademy        — free interactive courses
# Discourse           — the friendly community forum
println("Learning Julia: docs.julialang.org is the source of truth")
''',
        '''# Projects: Julia 1.9+ has built-in project workflows
# julia --project=. script.jl   # activate local env
# Pkg.instantiate()             # install deps from Project.toml
println("Project.toml + Manifest.toml pin your dependencies")
''',
        '''# Next steps: advanced topics to explore
# 1. Multiple dispatch mastery — design generic interfaces
# 2. Metaprogramming — write your own macros
# 3. GPU computing — CUDA.jl for arrays
# 4. Package development — the official package guideline
println("You now have a complete foundation in Julia")
''',
    ],
}

LESSONS = [
    dict(
        slug='julia-01-getting-started',
        title='Getting Started with Julia',
        desc='REPL, scripts, and the Julia execution model.',
        diff='beginner',
        dur=20,
        objs=[
            'Run Julia code in the REPL and from script files',
            'Explain how Julia JIT-compiles dynamically typed code',
            'Use basic arithmetic and function definitions',
        ],
        prereq=[],
        refs=[dict(title='Julia Manual — Getting Started', url='https://docs.julialang.org/en/v1/manual/getting-started/'),
              dict(title='Julia in VS Code — docs', url='https://code.visualstudio.com/docs/languages/julia'),
              dict(title='Julia Academy — free courses', url='https://juliaacademy.com/')]),
    dict(
        slug='julia-02-values-types',
        title='Values and Types',
        desc='Core types: integers, floats, booleans, chars, strings.',
        diff='beginner',
        dur=25,
        objs=[
            'Identify the core scalar types in Julia',
            'Use typeof() to inspect types at runtime',
            'Explain the differences between nothing, missing, and NaN',
        ],
        prereq=['julia-01-getting-started'],
        refs=[dict(title='Julia Manual — Integers and Floating-Point', url='https://docs.julialang.org/en/v1/manual/integers-and-floating-point-numbers/'),
              dict(title='Julia Manual — Strings', url='https://docs.julialang.org/en/v1/manual/strings/'),
              dict(title='Julia Manual — Missing Values', url='https://docs.julialang.org/en/v1/manual/missing/')]),
    dict(
        slug='julia-03-variables-scoping',
        title='Variables and Scoping',
        desc='Assignment, const, local vs global scope, and closures.',
        diff='beginner',
        dur=25,
        objs=[
            'Declare and rebind variables correctly',
            'Understand local vs global scope rules',
            'Build closures with let blocks',
        ],
        prereq=['julia-01-getting-started'],
        refs=[dict(title='Julia Manual — Variables', url='https://docs.julialang.org/en/v1/manual/variables/'),
              dict(title='Julia Manual — Scope of Variables', url='https://docs.julialang.org/en/v1/manual/variables-and-scoping/'),
              dict(title='Julia Manual — Closures', url='https://docs.julialang.org/en/v1/manual/faq/')]),
    dict(
        slug='julia-04-arithmetic-operators',
        title='Arithmetic and Operators',
        desc='Numeric operators, chained comparisons, and bitwise ops.',
        diff='beginner',
        dur=25,
        objs=[
            'Use arithmetic, comparison, and logical operators',
            'Explain short-circuit evaluation of && and ||',
            'Apply bitwise operators to integers',
        ],
        prereq=['julia-02-values-types'],
        refs=[dict(title='Julia Manual — Mathematical Operations', url='https://docs.julialang.org/en/v1/manual/mathematical-operations/'),
              dict(title='Julia Manual — Numeric Literal Coefficients', url='https://docs.julialang.org/en/v1/manual/mathematical-operations/#Numeric-Literal-Coefficients')]),
    dict(
        slug='julia-05-functions',
        title='Functions',
        desc='Definitions, keyword arguments, anonymous functions, splatting.',
        diff='beginner',
        dur=30,
        objs=[
            'Define functions in one line and multi-line form',
            'Use optional and keyword arguments',
            'Write anonymous functions and do blocks',
        ],
        prereq=['julia-01-getting-started'],
        refs=[dict(title='Julia Manual — Functions', url='https://docs.julialang.org/en/v1/manual/functions/'),
              dict(title='Julia Manual — Do-Block Syntax', url='https://docs.julialang.org/en/v1/manual/functions/#Do-Block-Syntax-for-Function-Arguments'),
              dict(title='Julia Manual — Varargs', url='https://docs.julialang.org/en/v1/manual/functions/#Varargs-Functions')]),
    dict(
        slug='julia-06-multiple-dispatch',
        title='Multiple Dispatch',
        desc='Method definitions, abstract types, and dispatch specificity.',
        diff='intermediate',
        dur=35,
        objs=[
            'Define multiple methods for the same function name',
            'Use abstract types to write generic code',
            'Explain how Julia picks the most specific method',
        ],
        prereq=['julia-05-functions'],
        refs=[dict(title='Julia Manual — Methods', url='https://docs.julialang.org/en/v1/manual/methods/'),
              dict(title='Julia Manual — Types', url='https://docs.julialang.org/en/v1/manual/types/'),
              dict(title='Julia Manual — Constructors', url='https://docs.julialang.org/en/v1/manual/constructors/')]),
    dict(
        slug='julia-07-control-flow',
        title='Control Flow',
        desc='if/elseif, ternary, short-circuit, and loops.',
        diff='beginner',
        dur=25,
        objs=[
            'Write conditional branches with if/elseif/else',
            'Use ternary operators and short-circuiting',
            'Iterate with for and while loops',
        ],
        prereq=['julia-01-getting-started'],
        refs=[dict(title='Julia Manual — Control Flow', url='https://docs.julialang.org/en/v1/manual/control-flow/'),
              dict(title='Julia Manual — Scope of Variables (loops)', url='https://docs.julialang.org/en/v1/manual/variables-and-scoping/')]),
    dict(
        slug='julia-08-strings-text',
        title='Strings and Text',
        desc='UTF-8 handling, interpolation, and string functions.',
        diff='beginner',
        dur=25,
        objs=[
            'Explain UTF-8 semantics of Julia strings',
            'Use string interpolation idiomatically',
            'Apply split, join, replace, and case functions',
        ],
        prereq=['julia-02-values-types'],
        refs=[dict(title='Julia Manual — Strings', url='https://docs.julialang.org/en/v1/manual/strings/'),
              dict(title='Julia Manual — Unicode Input', url='https://docs.julialang.org/en/v1/manual/unicode-input/')]),
    dict(
        slug='julia-09-arrays',
        title='Arrays',
        desc='Vectors, comprehensions, broadcasting, and matrices.',
        diff='intermediate',
        dur=35,
        objs=[
            'Create and index arrays (1-based indexing!)',
            'Write array comprehensions with filters',
            'Apply functions elementwise with broadcasting',
        ],
        prereq=['julia-02-values-types'],
        refs=[dict(title='Julia Manual — Arrays', url='https://docs.julialang.org/en/v1/manual/arrays/'),
              dict(title='Julia Manual — Broadcasting', url='https://docs.julialang.org/en/v1/manual/arrays/#Broadcasting'),
              dict(title='Julia Manual — Array Comprehensions', url='https://docs.julialang.org/en/v1/manual/arrays/#Comprehensions')]),
    dict(
        slug='julia-10-tuples-dicts',
        title='Tuples, NamedTuples, and Dictionaries',
        desc='Immutable tuples, keyed maps, and sets.',
        diff='beginner',
        dur=30,
        objs=[
            'Create and destructure tuples',
            'Use NamedTuples for labeled data',
            'Work with Dicts and Sets',
        ],
        prereq=['julia-09-arrays'],
        refs=[dict(title='Julia Manual — Composite Types (Tuple)', url='https://docs.julialang.org/en/v1/manual/types/#Composite-Types'),
              dict(title='Julia Standard Library — Dict', url='https://docs.julialang.org/en/v1/base/collections/')]),
    dict(
        slug='julia-11-structs',
        title='Composite Types and Structs',
        desc='Immutable and mutable structs, inner constructors.',
        diff='intermediate',
        dur=35,
        objs=[
            'Define immutable structs with typed fields',
            'Define mutable structs for stateful objects',
            'Write inner constructors with validation',
        ],
        prereq=['julia-06-multiple-dispatch'],
        refs=[dict(title='Julia Manual — Composite Types', url='https://docs.julialang.org/en/v1/manual/types/#Composite-Types'),
              dict(title='Julia Manual — Constructors', url='https://docs.julialang.org/en/v1/manual/constructors/')]),
    dict(
        slug='julia-12-parametric-types',
        title='Abstract and Parametric Types',
        desc='Type parameters, unions, and the type hierarchy.',
        diff='intermediate',
        dur=35,
        objs=[
            'Parameterize structs with type variables',
            'Use Union types to allow multiple types',
            'Navigate the type hierarchy with <:',
        ],
        prereq=['julia-11-structs'],
        refs=[dict(title='Julia Manual — Parametric Types', url='https://docs.julialang.org/en/v1/manual/types/#Parametric-Types'),
              dict(title='Julia Manual — UnionAll Types', url='https://docs.julialang.org/en/v1/manual/types/#UnionAll-Types')]),
    dict(
        slug='julia-13-modules-packages',
        title='Modules and Packages',
        desc='Namespaces, Pkg management, import vs using.',
        diff='intermediate',
        dur=30,
        objs=[
            'Create and use modules with export',
            'Add and manage packages with Pkg',
            'Distinguish import from using',
        ],
        prereq=['julia-05-functions'],
        refs=[dict(title='Julia Manual — Modules', url='https://docs.julialang.org/en/v1/manual/modules/'),
              dict(title='Pkg — Package Manager Docs', url='https://pkgdocs.julialang.org/'),
              dict(title='Julia Manual — Code Loading', url='https://docs.julialang.org/en/v1/manual/code-loading/')]),
    dict(
        slug='julia-14-metaprogramming',
        title='Metaprogramming',
        desc='Symbols, expressions, macros, and code-as-data.',
        diff='expert',
        dur=40,
        objs=[
            'Explain that Julia code is representable as data',
            'Build and evaluate expression trees',
            'Write macros that transform code at parse time',
        ],
        prereq=['julia-12-parametric-types'],
        refs=[dict(title='Julia Manual — Metaprogramming', url='https://docs.julialang.org/en/v1/manual/metaprogramming/'),
              dict(title='Julia Manual — Macros', url='https://docs.julialang.org/en/v1/manual/metaprogramming/#Macros'),
              dict(title='Julia Manual — Generated Functions', url='https://docs.julialang.org/en/v1/manual/metaprogramming/#Generated-functions')]),
    dict(
        slug='julia-15-errors-exceptions',
        title='Errors and Exceptions',
        desc='try/catch/finally, throw, and error handling patterns.',
        diff='intermediate',
        dur=30,
        objs=[
            'Use try/catch/finally blocks correctly',
            'Throw typed exceptions with throw()',
            'Build safe wrappers around fallible code',
        ],
        prereq=['julia-07-control-flow'],
        refs=[dict(title='Julia Manual — Control Flow (try/catch)', url='https://docs.julialang.org/en/v1/manual/control-flow/#Exception-Handling'),
              dict(title='Julia Base — Exceptions Reference', url='https://docs.julialang.org/en/v1/base/base/#Exceptions')]),
    dict(
        slug='julia-16-file-io',
        title='File I/O',
        desc='Reading and writing files, parsing CSV-like data.',
        diff='intermediate',
        dur=30,
        objs=[
            'Read and write text files with open and do blocks',
            'Process files line by line with eachline',
            'Parse delimited data into structured form',
        ],
        prereq=['julia-07-control-flow'],
        refs=[dict(title='Julia Base — I/O and Network', url='https://docs.julialang.org/en/v1/base/io-network/'),
              dict(title='CSV.jl — Documentation', url='https://csv.juliadata.org/stable/'),
              dict(title='DataFrames.jl — Documentation', url='https://dataframes.juliadata.org/stable/')]),
    dict(
        slug='julia-17-generators-iterators',
        title='Generators and Iterators',
        desc='Ranges, lazy generators, zip/enumerate, reduce.',
        diff='intermediate',
        dur=30,
        objs=[
            'Create ranges with start:step:stop',
            'Use lazy generators instead of eager arrays',
            'Combine iterators with zip and enumerate',
        ],
        prereq=['julia-09-arrays'],
        refs=[dict(title='Julia Manual — Iteration', url='https://docs.julialang.org/en/v1/manual/interfaces/#man-interface-iteration'),
              dict(title='Julia Base — Iteration Utilities', url='https://docs.julialang.org/en/v1/base/iterators/')]),
    dict(
        slug='julia-18-missing-nothing',
        title='Missing, Nothing, and NaN',
        desc='Handling absent and undefined values idiomatically.',
        diff='intermediate',
        dur=25,
        objs=[
            'Distinguish missing, nothing, and NaN',
            'Use skipmissing to clean data',
            'Apply something() for fallback values',
        ],
        prereq=['julia-02-values-types'],
        refs=[dict(title='Julia Manual — Missing Values', url='https://docs.julialang.org/en/v1/manual/missing/'),
              dict(title='Julia Base — Missing Reference', url='https://docs.julialang.org/en/v1/base/base/#Base.Missing')]),
    dict(
        slug='julia-19-parallelism-concurrency',
        title='Parallelism and Concurrency',
        desc='Threads, tasks, channels, and distributed computing.',
        diff='expert',
        dur=45,
        objs=[
            'Run parallel loops with Threads.@threads',
            'Spawn and coordinate tasks with @async and @sync',
            'Pass data between tasks with Channels',
        ],
        prereq=['julia-09-arrays'],
        refs=[dict(title='Julia Manual — Parallel Computing', url='https://docs.julialang.org/en/v1/manual/parallel-computing/'),
              dict(title='Julia Manual — Multi-Threading', url='https://docs.julialang.org/en/v1/manual/multithreading/'),
              dict(title='Julia Manual — Channels', url='https://docs.julialang.org/en/v1/manual/parallel-computing/#Channels')]),
    dict(
        slug='julia-20-performance-type-stability',
        title='Performance and Type Stability',
        desc='Type stability, @code_warntype, and allocation-free code.',
        diff='expert',
        dur=40,
        objs=[
            'Explain why type stability drives performance',
            'Use @code_warntype and @time to diagnose hotspots',
            'Avoid Union return types and global scope in hot loops',
        ],
        prereq=['julia-12-parametric-types'],
        refs=[dict(title='Julia Manual — Performance Tips', url='https://docs.julialang.org/en/v1/manual/performance-tips/'),
              dict(title='Julia Manual — @code_warntype', url='https://docs.julialang.org/en/v1/base/base/#Base.@code_warntype'),
              dict(title='BenchmarkTools.jl', url='https://github.com/JuliaCI/BenchmarkTools.jl')]),
    dict(
        slug='julia-21-ecosystem-next-steps',
        title='Ecosystem and Next Steps',
        desc='DataFrames, Plots, the community, and advanced topics.',
        diff='intermediate',
        dur=20,
        objs=[
            'Name the key packages in the Julia ecosystem',
            'Set up a reproducible project environment',
            'Identify the next advanced topics to explore',
        ],
        prereq=['julia-13-modules-packages'],
        refs=[dict(title='JuliaLang — Official Site', url='https://julialang.org/'),
              dict(title='Julia Manual — Home', url='https://docs.julialang.org/en/v1/'),
              dict(title='JuliaHub — Ecosystem Portal', url='https://juliahub.com/'),
              dict(title='Julia Discourse — Community Forum', url='https://discourse.julialang.org/')]),
]


if __name__ == '__main__':
    run_gen(LANGUAGE, 'julia', LESSONS, CODE, BASE)
