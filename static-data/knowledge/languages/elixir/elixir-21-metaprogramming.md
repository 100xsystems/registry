---
{
  "title": "Metaprogramming and the Ecosystem",
  "description": "Macros, quote/unquote, Ecto, and Phoenix.",
  "type": "lesson",
  "order": 21,
  "duration": "75 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Write basic macros",
    "Understand quote and unquote",
    "Use Ecto for databases",
    "Build web apps with Phoenix"
  ],
  "knowledge_refs": [
    "elixir/elixir-21-metaprogramming"
  ],
  "prerequisites": [
    "ELIXIR-20"
  ],
  "references": [
    {
      "title": "Elixir — Metaprogramming",
      "url": "https://elixir-lang.org/getting-started/meta/quote-and-unquote.html"
    },
    {
      "title": "Ecto — Getting Started",
      "url": "https://hexdocs.pm/ecto/Ecto.html"
    },
    {
      "title": "Phoenix — Framework",
      "url": "https://hexdocs.pm/phoenix/overview.html"
    }
  ]
}
---

# ELIXIR-21-METAPROGRAMMING: Metaprogramming and the Ecosystem

## Introduction

Macros, quote/unquote, Ecto, and Phoenix. By the end of this lesson you will be able to: Write basic macros; Understand quote and unquote; Use Ecto for databases; Build web apps with Phoenix.

## Key Concepts

### 1. Write basic macros

Target: Write basic macros. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elixir
# Metaprogramming: macros intro
defmodule MyMacros do
  defmacro unless_else(condition, do: block, else: else_block) do
    quote do
      if !unquote(condition) do
        unquote(block)
      else
        unquote(else_block)
      end
    end
  end
end

defmodule Demo do
  import MyMacros

  def run do
    unless_else false do
      IO.puts("false branch runs")
    else
      IO.puts("true branch")
    end
  end
end

Demo.run()
# Macros transform code at compile time.
```
### 2. Understand quote and unquote

Target: Understand quote and unquote. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elixir
# quote and unquote
IO.inspect(quote do: 1 + 2)
# {:+, [context: Elixir, import: Kernel], [1, 2]}

# unquote injects values into quoted expressions:
x = 42
IO.inspect(quote do: x)
# {:x, [context: Elixir, import: Kernel], nil}
# (x refers to the variable, not its value)
IO.inspect(quote do: unquote(x))
# 42 — the value is inlined
```
### 3. Use Ecto for databases

Target: Use Ecto for databases. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elixir
# Ecto: database access and queries
# defmodule Post do
#   use Ecto.Schema
#   schema "posts" do
#     field :title, :string
#     field :views, :integer, default: 0
#   end
# end
#
# Repo.get!(Post, 1)
# Repo.all(from p in Post, where: p.views > 100)
IO.puts("Ecto provides schemas, queries, and changesets")
```
### 4. Build web apps with Phoenix

Target: Build web apps with Phoenix. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elixir
# Phoenix: the web framework
# mix phx.new my_app
# mix phx.server
# defmodule MyAppWeb.PageController do
#   use MyAppWeb, :controller
#   def index(conn, _params) do
#     render(conn, "index.html")
#   end
# end
IO.puts("Phoenix: channels, live view, and the web layer")
IO.puts("The Elixir ecosystem: Ecto + Phoenix + OTP")
```

## Practice Questions

1. What is the key idea behind "Metaprogramming and the Ecosystem"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Metaprogramming and the Ecosystem with analogies and real-world examples"
1. "Show me common mistakes beginners make with Metaprogramming and the Ecosystem"
1. "Provide advanced patterns and performance considerations for Metaprogramming and the Ecosystem"

## Key Takeaways

- Master the core ideas of Metaprogramming and the Ecosystem through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
