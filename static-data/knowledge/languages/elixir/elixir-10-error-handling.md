---
{
  "title": "Error Handling",
  "description": "try/rescue, errors as values, raise, and with.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Handle exceptions with try/rescue",
    "Treat errors as values",
    "Use raise and bang functions",
    "Compose with with"
  ],
  "knowledge_refs": [
    "elixir/elixir-10-error-handling"
  ],
  "prerequisites": [
    "ELIXIR-09"
  ],
  "references": [
    {
      "title": "Elixir — try, catch, rescue",
      "url": "https://elixir-lang.org/getting-started/try-catch-and-rescue.html"
    },
    {
      "title": "Elixir — Errors",
      "url": "https://hexdocs.pm/elixir/errors.html"
    },
    {
      "title": "Elixir — with special form",
      "url": "https://hexdocs.pm/elixir/Kernel.SpecialForms.html#with/1"
    }
  ]
}
---

# ELIXIR-10-ERROR-HANDLING: Error Handling

## Introduction

try/rescue, errors as values, raise, and with. By the end of this lesson you will be able to: Handle exceptions with try/rescue; Treat errors as values; Use raise and bang functions; Compose with with.

## Key Concepts

### 1. Handle exceptions with try/rescue

Target: Handle exceptions with try/rescue. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# try/rescue: handling exceptions (rare in Elixir)
defmodule Safe do
  def divide(a, b) do
    try do
      {:ok, a / b}
    rescue
      ArithmeticError -> {:error, "division by zero"}
    end
  end
end

IO.inspect(Safe.divide(1, 0))  # {:error, "division by zero"}
```
### 2. Treat errors as values

Target: Treat errors as values. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# The Elixir philosophy: errors are values, not exceptions
defmodule Parse do
  def to_int(str) do
    case Integer.parse(str) do
      {n, _} -> {:ok, n}
      :error -> {:error, "not an integer"}
    end
  end
end

IO.inspect(Parse.to_int("42"))     # {:ok, 42}
IO.inspect(Parse.to_int("abc"))    # {:error, "not an integer"}
# Handle errors at the boundary; let the happy path flow.
```
### 3. Use raise and bang functions

Target: Use raise and bang functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# raise and the bang functions
defmodule Db do
  def connect!(url) do
    if url == "" do
      raise ArgumentError, "empty url"
    end
    :connected
  end
end

IO.puts(Db.connect!("postgres://localhost/db"))
# Db.connect!("") would raise.
# The ! convention marks functions that raise on failure.
```
### 4. Compose with with

Target: Compose with with. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# Error handling with with: early-exit pipelines
defmodule Flow do
  def run do
    with {:ok, a} <- step1(),
         {:ok, b} <- step2(a) do
      {:ok, a + b}
    else
      {:error, reason} -> {:error, reason}
    end
  end

  defp step1, do: {:ok, 10}
  defp step2(x), do: {:ok, x * 2}
end

IO.inspect(Flow.run())  # {:ok, 30}
# with stops at the first non-matching clause.
```

## Practice Questions

1. What is the key idea behind "Error Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Error Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Error Handling"
1. "Provide advanced patterns and performance considerations for Error Handling"

## Key Takeaways

- Master the core ideas of Error Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
