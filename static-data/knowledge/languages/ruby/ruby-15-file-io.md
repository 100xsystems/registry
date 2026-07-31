---
{
  "title": "File I/O",
  "description": "File read/write, blocks, iteration, FileUtils.",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write and read files",
    "Use File.open with blocks",
    "Iterate lines efficiently",
    "Manipulate files with FileUtils"
  ],
  "knowledge_refs": [
    "ruby/ruby-15-file-io"
  ],
  "prerequisites": [
    "RUBY-14"
  ],
  "references": [
    {
      "title": "Ruby — File",
      "url": "https://docs.ruby-lang.org/en/master/File.html"
    },
    {
      "title": "Ruby — IO",
      "url": "https://docs.ruby-lang.org/en/master/IO.html"
    },
    {
      "title": "Ruby — FileUtils",
      "url": "https://docs.ruby-lang.org/en/master/FileUtils.html"
    }
  ]
}
---

# RUBY-15-FILE-IO: File I/O

## Introduction

File read/write, blocks, iteration, FileUtils. By the end of this lesson you will be able to: Write and read files; Use File.open with blocks; Iterate lines efficiently; Manipulate files with FileUtils.

## Key Concepts

### 1. Write and read files

Target: Write and read files. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
File.write("/tmp/notes.txt", "hello file\n")
p File.read("/tmp/notes.txt")
```
### 2. Use File.open with blocks

Target: Use File.open with blocks. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
File.open("/tmp/data.txt", "w") do |f|
  f.puts "line 1"
  f.puts "line 2"
end
p File.readlines("/tmp/data.txt")   # auto-closed by block
```
### 3. Iterate lines efficiently

Target: Iterate lines efficiently. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
File.foreach("/tmp/data.txt") { |line| puts line.upcase }
p File.exist?("/tmp/data.txt")
p File.size("/tmp/data.txt")
```
### 4. Manipulate files with FileUtils

Target: Manipulate files with FileUtils. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
require "fileutils"
FileUtils.mkdir_p("/tmp/a/b")
FileUtils.cp("/tmp/data.txt", "/tmp/a/b/copy.txt")
p Dir.glob("/tmp/a/**/*").first(5)
p Dir.children("/tmp/a")
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
