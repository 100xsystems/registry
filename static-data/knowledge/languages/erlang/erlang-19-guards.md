---
{
  "title": "Guards in Depth",
  "description": "Guard reference, type guards, pattern vs guard, case everywhere.",
  "type": "lesson",
  "order": 19,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use guard functions",
    "Compose guard expressions",
    "Combine patterns and guards",
    "Use case as an expression"
  ],
  "knowledge_refs": [
    "erlang/erlang-19-guards"
  ],
  "prerequisites": [
    "ERLANG-18"
  ],
  "references": [
    {
      "title": "Erlang — Guards",
      "url": "https://www.erlang.org/doc/reference_manual/expressions.html#guards"
    },
    {
      "title": "Learn You Some Erlang — Guards",
      "url": "https://learnyousomeerlang.com/syntax-in-functions#guards!"
    },
    {
      "title": "Erlang — Built-in Functions",
      "url": "https://www.erlang.org/doc/reference_manual/functions.html"
    }
  ]
}
---

# ERLANG-19-GUARDS: Guards in Depth

## Introduction

Guard reference, type guards, pattern vs guard, case everywhere. By the end of this lesson you will be able to: Use guard functions; Compose guard expressions; Combine patterns and guards; Use case as an expression.

## Key Concepts

### 1. Use guard functions

Target: Use guard functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% Guard expressions reference
-module(guards_ref).
-export([run/0]).

run() ->
    io:format("is_integer/1, is_atom/1, is_list/1, is_map/1~n"),
    io:format("is_tuple/1, is_binary/1, is_boolean/1~n"),
    io:format("Comparisons: =:=, ==, <, >, =<, >=~n"),
    io:format("Composed with , (and) and ; (or).~n").
    % Guards are the only places allowed in function heads.
```
### 2. Compose guard expressions

Target: Compose guard expressions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% Guard usage in depth
-module(guard_use).
-export([run/0]).

run() ->
    io:format("~p~n", [classify(42)]),    % integer
    io:format("~p~n", [classify("s")]),   % string
    io:format("~p~n", [classify(3.14)]).  % other

classify(X) when is_integer(X) -> integer;
classify(X) when is_list(X) -> string;
classify(_) -> other.
    % Each clause guards on the argument's type.
```
### 3. Combine patterns and guards

Target: Combine patterns and guards. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% Pattern matching vs guards: when to use each
-module(pat_vs_guard).
-export([run/0]).

run() ->
    io:format("Patterns match STRUCTURE (shape, binding).~n"),
    io:format("Guards test VALUES (types, comparisons).~n"),
    io:format("Use patterns to destructure, guards to filter.~n"),
    io:format("Combine them: [H | T] when H > 10 -> ...~n").
    % They compose: pattern first, guard second.
```
### 4. Use case as an expression

Target: Use case as an expression. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% The case of matching: expressions everywhere
-module(match_everywhere).
-export([run/0]).

run() ->
    Result = case {1, 2} of
        {A, B} when A < B -> {increasing, A, B};
        _ -> other
    end,
    io:format("~p~n", [Result]).
    % {increasing, 1, 2} — case is an expression returning a value.
```

## Practice Questions

1. What is the key idea behind "Guards in Depth"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Guards in Depth with analogies and real-world examples"
1. "Show me common mistakes beginners make with Guards in Depth"
1. "Provide advanced patterns and performance considerations for Guards in Depth"

## Key Takeaways

- Master the core ideas of Guards in Depth through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
