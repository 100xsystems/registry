---
{
  "title": "Processes and Message Passing",
  "description": "spawn, send/receive, process state, links, and monitors.",
  "type": "lesson",
  "order": 11,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Spawn lightweight processes",
    "Pass messages with send/receive",
    "Hold state in a process loop",
    "Link and monitor processes"
  ],
  "knowledge_refs": [
    "elixir/elixir-11-processes"
  ],
  "prerequisites": [
    "ELIXIR-10"
  ],
  "references": [
    {
      "title": "Elixir — Processes",
      "url": "https://elixir-lang.org/getting-started/processes.html"
    },
    {
      "title": "Elixir — send/2 and receive",
      "url": "https://hexdocs.pm/elixir/Kernel.html#send/2"
    },
    {
      "title": "Elixir — spawn_link",
      "url": "https://hexdocs.pm/elixir/Kernel.html#spawn_link/1"
    }
  ]
}
---

# ELIXIR-11-PROCESSES: Processes and Message Passing

## Introduction

spawn, send/receive, process state, links, and monitors. By the end of this lesson you will be able to: Spawn lightweight processes; Pass messages with send/receive; Hold state in a process loop; Link and monitor processes.

## Key Concepts

### 1. Spawn lightweight processes

Target: Spawn lightweight processes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# Processes: lightweight concurrency
pid = spawn(fn -> IO.puts("I am process #{inspect(self())}") end)
IO.puts("parent: #{inspect(self())}")
IO.puts("child: #{inspect(pid)}")
# Each spawn creates an isolated, independent process.
```
### 2. Pass messages with send/receive

Target: Pass messages with send/receive. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# Send and receive: message passing
parent = self()

spawn(fn ->
  send(parent, {:hello, "from child"})
end)

receive do
  {:hello, msg} -> IO.puts("got: #{msg}")
after
  1000 -> IO.puts("timeout")
end
# Message passing is THE concurrency primitive in Elixir.
```
### 3. Hold state in a process loop

Target: Hold state in a process loop. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# Process state with recursion (a mini Agent)
defmodule Counter do
  def start(initial) do
    spawn(fn -> loop(initial) end)
  end

  defp loop(count) do
    receive do
      {:get, caller} ->
        send(caller, count)
        loop(count)
      {:inc} ->
        loop(count + 1)
    end
  end
end

pid = Counter.start(5)
send(pid, {:inc})
send(pid, {:get, self()})
receive do
  n -> IO.puts("count is #{n}")   # 6
end
```
### 4. Link and monitor processes

Target: Link and monitor processes. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# Linking and monitoring processes
# spawn_link crashes the parent if the child crashes:
parent = self()
spawn_link(fn -> raise "child boom" end)

receive do
  {:EXIT, _pid, reason} -> IO.puts("child died: #{inspect(reason)}")
after
  500 -> IO.puts("no exit message")
end
# Links propagate crashes; monitors observe without dying.
```

## Practice Questions

1. What is the key idea behind "Processes and Message Passing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Processes and Message Passing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Processes and Message Passing"
1. "Provide advanced patterns and performance considerations for Processes and Message Passing"

## Key Takeaways

- Master the core ideas of Processes and Message Passing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
