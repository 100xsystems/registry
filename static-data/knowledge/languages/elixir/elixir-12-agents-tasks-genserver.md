---
{
  "title": "Agents, Tasks, and GenServer",
  "description": "Agent for state, Task for async work, GenServer for servers.",
  "type": "lesson",
  "order": 12,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use Agents for shared state",
    "Run async work with Tasks",
    "Handle Task results",
    "Build a GenServer"
  ],
  "knowledge_refs": [
    "elixir/elixir-12-agents-tasks-genserver"
  ],
  "prerequisites": [
    "ELIXIR-11"
  ],
  "references": [
    {
      "title": "Elixir — Agent",
      "url": "https://hexdocs.pm/elixir/Agent.html"
    },
    {
      "title": "Elixir — Task",
      "url": "https://hexdocs.pm/elixir/Task.html"
    },
    {
      "title": "Elixir — GenServer",
      "url": "https://hexdocs.pm/elixir/GenServer.html"
    }
  ]
}
---

# ELIXIR-12-AGENTS-TASKS-GENSERVER: Agents, Tasks, and GenServer

## Introduction

Agent for state, Task for async work, GenServer for servers. By the end of this lesson you will be able to: Use Agents for shared state; Run async work with Tasks; Handle Task results; Build a GenServer.

## Key Concepts

### 1. Use Agents for shared state

Target: Use Agents for shared state. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# Agent: shared state with a simple API
{:ok, agent} = Agent.start_link(fn -> 0 end)
Agent.update(agent, fn count -> count + 1 end)
Agent.update(agent, fn count -> count + 1 end)
IO.puts(Agent.get(agent, fn count -> count end))  # 2
```
### 2. Run async work with Tasks

Target: Run async work with Tasks. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# Task: one-off asynchronous work
task = Task.async(fn ->
  Process.sleep(100)
  21 * 2
end)

IO.puts("doing other work...")
result = Task.await(task, 1000)
IO.puts(result)   # 42
# Task.async/await is the simplest parallel abstraction.
```
### 3. Handle Task results

Target: Handle Task results. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# Task with error handling
task = Task.async(fn -> {:ok, 1 + 1} end)

case Task.yield(task, 1000) || Task.shutdown(task) do
  {:ok, {:ok, value}} -> IO.puts("value: #{value}")
  _ -> IO.puts("task failed or timed out")
end
```
### 4. Build a GenServer

Target: Build a GenServer. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# GenServer: the core OTP behaviour
defmodule Bank do
  use GenServer

  def start_link(balance) do
    GenServer.start_link(__MODULE__, balance, name: __MODULE__)
  end

  def balance, do: GenServer.call(__MODULE__, :balance)
  def deposit(amount), do: GenServer.call(__MODULE__, {:deposit, amount})

  @impl true
  def init(balance), do: {:ok, balance}

  @impl true
  def handle_call(:balance, _from, bal), do: {:reply, bal, bal}

  @impl true
  def handle_call({:deposit, amt}, _from, bal),
    do: {:reply, :ok, bal + amt}
end

Bank.start_link(100)
Bank.deposit(50)
IO.puts(Bank.balance())   # 150
```

## Practice Questions

1. What is the key idea behind "Agents, Tasks, and GenServer"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Agents, Tasks, and GenServer with analogies and real-world examples"
1. "Show me common mistakes beginners make with Agents, Tasks, and GenServer"
1. "Provide advanced patterns and performance considerations for Agents, Tasks, and GenServer"

## Key Takeaways

- Master the core ideas of Agents, Tasks, and GenServer through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
