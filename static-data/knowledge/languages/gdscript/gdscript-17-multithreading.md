---
{
  "title": "Threads and Async",
  "description": "Parallel work with signals.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Spawn threads",
    "Use async functions",
    "Use await",
    "Communicate between threads"
  ],
  "knowledge_refs": [
    "gdscript/gdscript-17-multithreading"
  ],
  "prerequisites": [
    "GDScript-16: Groups and Communication"
  ],
  "references": [
    {
      "title": "Godot Docs: GDScript",
      "url": "https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/index.html",
      "description": "Official documentation"
    },
    {
      "title": "GDScript Reference",
      "url": "https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html",
      "description": "Language reference"
    },
    {
      "title": "Godot Community",
      "url": "https://godotengine.org/community/",
      "description": "Community links"
    }
  ]
}
---

# GDSCRIPT-17-MULTITHREADING: Threads and Async

## Introduction

Parallel work with signals. By the end of this lesson you will be able to: Spawn threads; Use async functions; Use await; Communicate between threads.

## Key Concepts

### 1. Spawn threads

Target: Spawn threads. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```gdscript
var thread = Thread.new()
thread.start(_work)

func _work():
    print("in thread")
```
### 2. Use async functions

Target: Use async functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```gdscript
func load_data():
    var result = await get_tree().create_timer(1.0).timeout
    print("done")
```
### 3. Use await

Target: Use await. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```gdscript
var worker = WorkerThreadPool.add_task(_process_chunk)
await worker.wait_for_completion
```
### 4. Communicate between threads

Target: Communicate between threads. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```gdscript
await signal_completed
print("after signal")
```

## Practice Questions

1. What is the key idea behind "Threads and Async"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Threads and Async with analogies and real-world examples"
1. "Show me common mistakes beginners make with Threads and Async"
1. "Provide advanced patterns and performance considerations for Threads and Async"

## Key Takeaways

- Master the core ideas of Threads and Async through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
