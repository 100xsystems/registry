---
{
  "title": "Blocks, Procs, and Lambdas",
  "description": "yield, block params, proc vs lambda semantics, &block.",
  "type": "lesson",
  "order": 12,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Yield to blocks",
    "Pass blocks explicitly with &",
    "Distinguish proc vs lambda return semantics",
    "Use shorthand syntax (&:method)"
  ],
  "knowledge_refs": [
    "ruby/ruby-12-blocks-procs"
  ],
  "prerequisites": [
    "RUBY-11"
  ],
  "references": [
    {
      "title": "Ruby — Blocks",
      "url": "https://docs.ruby-lang.org/en/master/syntax/methods_rdoc.html#label-Block+Argument"
    },
    {
      "title": "Ruby — Proc",
      "url": "https://docs.ruby-lang.org/en/master/Proc.html"
    },
    {
      "title": "Ruby — Lambda",
      "url": "https://docs.ruby-lang.org/en/master/Proc.html#class-Proc-label-Lambda+semantics"
    }
  ]
}
---

# RUBY-12-BLOCKS-PROCS: Blocks, Procs, and Lambdas

## Introduction

yield, block params, proc vs lambda semantics, &block. By the end of this lesson you will be able to: Yield to blocks; Pass blocks explicitly with &; Distinguish proc vs lambda return semantics; Use shorthand syntax (&:method).

## Key Concepts

### 1. Yield to blocks

Target: Yield to blocks. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
# blocks: passed with do/end or braces
def call_block
  yield "from yield"
end
call_block { |m| puts m }
```
### 2. Pass blocks explicitly with &

Target: Pass blocks explicitly with &. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
def twice
  yield
  yield
end
twice { puts "hello" }
```
### 3. Distinguish proc vs lambda return semantics

Target: Distinguish proc vs lambda return semantics. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
# proc vs lambda: return semantics differ
def test_proc
  p = proc { return "from proc" }   # returns from METHOD
  p.call
  "unreachable"
end
def test_lambda
  l = -> { return "from lambda" }   # returns from LAMBDA only
  l.call
  "after lambda"
end
p test_proc
p test_lambda
```
### 4. Use shorthand syntax (&:method)

Target: Use shorthand syntax (&:method). Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
# &block captures a block as a proc
def each_arg(&blk)
  [1, 2, 3].each(&blk)
end
result = []
each_arg { |x| result << x * 10 }
p result   # [10, 20, 30]
```

## Practice Questions

1. What is the key idea behind "Blocks, Procs, and Lambdas"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Blocks, Procs, and Lambdas with analogies and real-world examples"
1. "Show me common mistakes beginners make with Blocks, Procs, and Lambdas"
1. "Provide advanced patterns and performance considerations for Blocks, Procs, and Lambdas"

## Key Takeaways

- Master the core ideas of Blocks, Procs, and Lambdas through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
