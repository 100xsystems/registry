---
{
  "title": "Mix and Tooling",
  "description": "Mix projects, deps, ExUnit, doctests, and the formatter.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Scaffold projects with Mix",
    "Declare dependencies",
    "Write ExUnit tests",
    "Verify code with doctests"
  ],
  "knowledge_refs": [
    "elixir/elixir-17-mix-tooling"
  ],
  "prerequisites": [
    "ELIXIR-16"
  ],
  "references": [
    {
      "title": "Mix — Getting Started",
      "url": "https://hexdocs.pm/mix/Mix.html"
    },
    {
      "title": "Elixir — ExUnit",
      "url": "https://hexdocs.pm/ex_unit/ExUnit.html"
    },
    {
      "title": "Elixir — doctest",
      "url": "https://hexdocs.pm/elixir/Code.html#fetch_docs/1"
    }
  ]
}
---

# ELIXIR-17-MIX-TOOLING: Mix and Tooling

## Introduction

Mix projects, deps, ExUnit, doctests, and the formatter. By the end of this lesson you will be able to: Scaffold projects with Mix; Declare dependencies; Write ExUnit tests; Verify code with doctests.

## Key Concepts

### 1. Scaffold projects with Mix

Target: Scaffold projects with Mix. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# Mix: the project tool
# mix new my_app        -> creates a project scaffold
# mix run               -> runs the app
# mix test              -> runs tests
# mix deps.get          -> fetches dependencies
# mix format            -> formats code (elixir formatter)
# mix compile           -> compiles
IO.puts("Mix manages projects, deps, tests, and releases")
```
### 2. Declare dependencies

Target: Declare dependencies. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# Dependencies in mix.exs
defmodule MyApp.MixProject do
  use Mix.Project

  def project do
    [
      app: :my_app,
      version: "0.1.0",
      elixir: "~> 1.16",
      deps: deps()
    ]
  end

  defp deps do
    [
      {:jason, "~> 1.4"},
      {:plug, "~> 1.15"}
    ]
  end
end

IO.puts("deps defined in mix.exs, fetched with mix deps.get")
```
### 3. Write ExUnit tests

Target: Write ExUnit tests. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# ExUnit: testing
defmodule CalcTest do
  use ExUnit.Case, async: true

  test "addition" do
    assert 2 + 2 == 4
  end

  test "raises on invalid" do
    assert_raise ArgumentError, fn -> raise ArgumentError end
  end
end

# Run with: mix test
IO.puts("ExUnit is built into Elixir")
```
### 4. Verify code with doctests

Target: Verify code with doctests. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# doctest: documentation as tests
defmodule Math do
  @doc """
  Adds two numbers.

      iex> Math.add(2, 3)
      5
  """
  def add(a, b), do: a + b
end

# mix test runs the iex> examples automatically.
IO.puts("doctests verify documentation examples")
```

## Practice Questions

1. What is the key idea behind "Mix and Tooling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Mix and Tooling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Mix and Tooling"
1. "Provide advanced patterns and performance considerations for Mix and Tooling"

## Key Takeaways

- Master the core ideas of Mix and Tooling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
