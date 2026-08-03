---
{
  "title": "File I/O",
  "description": "Reading and writing files, parsing CSV-like data.",
  "type": "lesson",
  "order": 16,
  "duration": "30 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read and write text files with open and do blocks",
    "Process files line by line with eachline",
    "Parse delimited data into structured form"
  ],
  "knowledge_refs": [
    "julia/julia-16-file-io"
  ],
  "prerequisites": [
    "julia-07-control-flow"
  ],
  "references": [
    {
      "title": "Julia Base — I/O and Network",
      "url": "https://docs.julialang.org/en/v1/base/io-network/"
    },
    {
      "title": "CSV.jl — Documentation",
      "url": "https://csv.juliadata.org/stable/"
    },
    {
      "title": "DataFrames.jl — Documentation",
      "url": "https://dataframes.juliadata.org/stable/"
    }
  ]
}
---

# JULIA-16-FILE-IO: File I/O

## Introduction

Reading and writing files, parsing CSV-like data. By the end of this lesson you will be able to: Read and write text files with open and do blocks; Process files line by line with eachline; Parse delimited data into structured form.

## Key Concepts

### 1. Read and write text files with open and do blocks

Target: Read and write text files with open and do blocks. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```julia
# File I/O: read and write text files
open("hello.txt", "w") do io
    write(io, "Hello, Julia!\n")
    write(io, "Second line\n")
end
println(read("hello.txt", String))  # full file as one String

```
### 2. Process files line by line with eachline

Target: Process files line by line with eachline. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```julia
# readlines and per-line processing
open("hello.txt") do io
    for line in eachline(io)
        println(uppercase(line))
    end
end

```
### 3. Parse delimited data into structured form

Target: Parse delimited data into structured form. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```julia
# CSV without dependencies — manual parse
data = "name,age\nAda,36\nGrace,85\n"
for row in split(data, "\n"; keepempty=false)
    fields = split(row, ",")
    println("$fields[1] is $fields[2] years old")
end

```
### 4. Read and write text files with open and do blocks

Target: Read and write text files with open and do blocks. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```julia
# Standard library: JSON3/CSV come from packages
# using CSV, DataFrames
# df = CSV.read("data.csv", DataFrame)
# df[df.age .> 30, :name]
println("For heavy data work add: CSV.jl, DataFrames.jl, JSON3.jl")

```

## Practice Questions

1. What is the key idea behind "File I/O"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain File I/O with analogies and real-world examples"
1. "Show me common mistakes beginners make with File I/O"
1. "Provide advanced patterns and performance considerations for File I/O"

## Key Takeaways

- Master the core ideas of File I/O through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
