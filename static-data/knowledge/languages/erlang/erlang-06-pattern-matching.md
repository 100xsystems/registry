---
{
  "title": "Pattern Matching",
  "description": "Matching, destructuring, map patterns, and transforms.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Match values with =",
    "Match in case and heads",
    "Work with map patterns",
    "Transform with comprehensions"
  ],
  "knowledge_refs": [
    "erlang/erlang-06-pattern-matching"
  ],
  "prerequisites": [
    "ERLANG-05"
  ],
  "references": [
    {
      "title": "Erlang — Pattern Matching",
      "url": "https://www.erlang.org/doc/reference_manual/patterns.html"
    },
    {
      "title": "Erlang — Maps",
      "url": "https://www.erlang.org/doc/reference_manual/data_types.html#map"
    },
    {
      "title": "Learn You Some Erlang — Pattern Matching",
      "url": "https://learnyousomeerlang.com/syntax-in-functions"
    }
  ]
}
---

# ERLANG-06-PATTERN-MATCHING: Pattern Matching

## Introduction

Matching, destructuring, map patterns, and transforms. By the end of this lesson you will be able to: Match values with =; Match in case and heads; Work with map patterns; Transform with comprehensions.

## Key Concepts

### 1. Match values with =

Target: Match values with =. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% Pattern matching fundamentals
-module(match).
-export([run/0]).

run() ->
    {A, B} = {1, 2},          % match binds A=1, B=2
    [H | T] = [10, 20, 30],   % H=10, T=[20,30]
    io:format("~p ~p ~p ~p~n", [A, B, H, T]),
    io:format("~p~n", [1 + 1 =:= 2]).   % true — exact equality
```
### 2. Match in case and heads

Target: Match in case and heads. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% Matching in case with patterns
-module(matcher).
-export([check/1]).

check([]) -> empty;
check([_]) -> one;
check([_ | Rest]) -> {many, length(Rest) + 1}.

run() ->
    io:format("~p~n", [matcher:check([])]),        % empty
    io:format("~p~n", [matcher:check([42])]),      % one
    io:format("~p~n", [matcher:check([1, 2, 3])]). % {many, 3}
```
### 3. Work with map patterns

Target: Work with map patterns. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% Matching maps
-module(maps_demo).
-export([run/0]).

run() ->
    M = #{name => "Alice", age => 30},
    io:format("~p~n", [maps:get(name, M)]),      % "Alice"
    io:format("~p~n", [maps:get(age, M)]),       % 30
    io:format("~p~n", [maps:get(city, M, n/a)]), % n/a — default
    io:format("~p~n", [maps:keys(M)]),           % [age, name]
    #{age := Age} = M,
    io:format("~p~n", [Age]).                    % 30 — match syntax
```
### 4. Transform with comprehensions

Target: Transform with comprehensions. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% Pattern: transform with map/filter
-module(transform).
-export([run/0]).

run() ->
    Numbers = [1, 2, 3, 4, 5, 6],
    Doubled = [X * 2 || X <- Numbers],
    Evens = [X || X <- Numbers, X rem 2 =:= 0],
    io:format("~p~n", [Doubled]),   % [2, 4, 6, 8, 10, 12]
    io:format("~p~n", [Evens]).     % [2, 4, 6]
```

## Practice Questions

1. What is the key idea behind "Pattern Matching"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Pattern Matching with analogies and real-world examples"
1. "Show me common mistakes beginners make with Pattern Matching"
1. "Provide advanced patterns and performance considerations for Pattern Matching"

## Key Takeaways

- Master the core ideas of Pattern Matching through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
