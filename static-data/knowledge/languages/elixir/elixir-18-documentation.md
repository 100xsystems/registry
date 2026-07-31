---
{
  "title": "Documentation and Code Organisation",
  "description": "@moduledoc, @doc, module attributes, and project layout.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write module documentation",
    "Use module attributes",
    "Accumulate attributes",
    "Organise project code"
  ],
  "knowledge_refs": [
    "elixir/elixir-18-documentation"
  ],
  "prerequisites": [
    "ELIXIR-17"
  ],
  "references": [
    {
      "title": "Elixir — Writing Documentation",
      "url": "https://hexdocs.pm/elixir/writing-documentation.html"
    },
    {
      "title": "Elixir — Module Attributes",
      "url": "https://elixir-lang.org/getting-started/module-attributes.html"
    },
    {
      "title": "Elixir — Umbrella projects",
      "url": "https://hexdocs.pm/mix/Mix.Tasks.New.Umbrella.html"
    }
  ]
}
---

# ELIXIR-18-DOCUMENTATION: Documentation and Code Organisation

## Introduction

@moduledoc, @doc, module attributes, and project layout. By the end of this lesson you will be able to: Write module documentation; Use module attributes; Accumulate attributes; Organise project code.

## Key Concepts

### 1. Write module documentation

Target: Write module documentation. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# The @moduledoc and @doc attributes
defmodule Docs do
  @moduledoc "The Docs module explains documentation."

  @doc """
  Returns the double of a number.

  ## Examples
      iex> Docs.double(21)
      42
  """
  def double(x), do: x * 2
end

IO.puts(Docs.double(21))   # 42
# Documentation is a first-class citizen in Elixir.
```
### 2. Use module attributes

Target: Use module attributes. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# Module attributes as constants
defmodule Config do
  @app_name "MyApp"
  @version "1.0.0"

  def app_name, do: @app_name
  def version, do: @version
end

IO.puts(Config.app_name())
IO.puts(Config.version())
# Attributes are compile-time constants.
```
### 3. Accumulate attributes

Target: Accumulate attributes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# Module attributes accumulated (pattern)
defmodule Routes do
  # Register the attribute so assignments accumulate
  Module.register_attribute(__MODULE__, :routes, accumulate: true)

  @routes {:get, "/"}
  @routes {:get, "/about"}
  @routes {:post, "/submit"}

  def all_routes do
    @routes   # accumulated in reverse order of definition
  end
end

IO.inspect(Routes.all_routes())
# [{:post, "/submit"}, {:get, "/about"}, {:get, "/"}]
```
### 4. Organise project code

Target: Organise project code. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# Code organisation: apps and umbrella projects
# A typical layout:
#   lib/
#     my_app.ex
#     my_app/
#       application.ex
#       supervisor.ex
#   test/
#     my_app_test.exs
#   mix.exs
IO.puts("lib/ holds source; test/ holds tests")
# Umbrella projects group multiple apps with shared boundaries.
```

## Practice Questions

1. What is the key idea behind "Documentation and Code Organisation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Documentation and Code Organisation with analogies and real-world examples"
1. "Show me common mistakes beginners make with Documentation and Code Organisation"
1. "Provide advanced patterns and performance considerations for Documentation and Code Organisation"

## Key Takeaways

- Master the core ideas of Documentation and Code Organisation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
