---
{
  "title": "Threads and Concurrency",
  "description": "Thread.new, Mutex, Queue, Fiber.",
  "type": "lesson",
  "order": 20,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create and join threads",
    "Synchronize with Mutex",
    "Use Queue for producer/consumer",
    "Understand fibers"
  ],
  "knowledge_refs": [
    "ruby/ruby-20-concurrency"
  ],
  "prerequisites": [
    "RUBY-19"
  ],
  "references": [
    {
      "title": "Ruby — Thread",
      "url": "https://docs.ruby-lang.org/en/master/Thread.html"
    },
    {
      "title": "Ruby — Mutex",
      "url": "https://docs.ruby-lang.org/en/master/Mutex.html"
    },
    {
      "title": "Ruby — Queue",
      "url": "https://docs.ruby-lang.org/en/master/Queue.html"
    }
  ]
}
---

# RUBY-20-CONCURRENCY: Threads and Concurrency

## Introduction

Thread.new, Mutex, Queue, Fiber. By the end of this lesson you will be able to: Create and join threads; Synchronize with Mutex; Use Queue for producer/consumer; Understand fibers.

## Key Concepts

### 1. Create and join threads

Target: Create and join threads. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
# threads: concurrent execution
threads = 3.times.map do |i|
  Thread.new { sleep(rand * 0.1); puts "thread #{i}" }
end
threads.each(&:join)
puts "all done"
```
### 2. Synchronize with Mutex

Target: Synchronize with Mutex. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
# thread safety with Mutex
require "thread"
mutex = Mutex.new
counter = 0
threads = 10.times.map do
  Thread.new do
    100.times { mutex.synchronize { counter += 1 } }
  end
end
threads.each(&:join)
p counter   # 1000
```
### 3. Use Queue for producer/consumer

Target: Use Queue for producer/consumer. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
# Queue: thread-safe producer/consumer
require "thread"
q = Queue.new
producer = Thread.new { 5.times { |i| q << i } }
consumer = Thread.new { 5.times { p q.pop } }
[producer, consumer].each(&:join)
```
### 4. Understand fibers

Target: Understand fibers. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
# Fiber: cooperative concurrency
f = Fiber.new do
  3.times do |i|
    Fiber.yield i
  end
  "done"
end
p f.resume   # 0
p f.resume   # 1
p f.resume   # 2
p f.resume   # done
```

## Practice Questions

1. What is the key idea behind "Threads and Concurrency"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Threads and Concurrency with analogies and real-world examples"
1. "Show me common mistakes beginners make with Threads and Concurrency"
1. "Provide advanced patterns and performance considerations for Threads and Concurrency"

## Key Takeaways

- Master the core ideas of Threads and Concurrency through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
