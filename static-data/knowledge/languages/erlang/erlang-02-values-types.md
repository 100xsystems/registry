---
{
  "title": "Values and Types",
  "description": "Numbers, strings as lists, format directives, and booleans.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Do integer and float arithmetic",
    "Manipulate strings and charlists",
    "Use io:format directives",
    "Understand booleans and comparisons"
  ],
  "knowledge_refs": [
    "erlang/erlang-02-values-types"
  ],
  "prerequisites": [
    "ERLANG-01"
  ],
  "references": [
    {
      "title": "Erlang — Data Types",
      "url": "https://www.erlang.org/doc/reference_manual/data_types.html"
    },
    {
      "title": "Erlang — io:format directives",
      "url": "https://www.erlang.org/doc/apps/stdlib/io.html"
    },
    {
      "title": "Learn You Some Erlang — Types",
      "url": "https://learnyousomeerlang.com/syntax-in-functions"
    }
  ]
}
---

# ERLANG-02-VALUES-TYPES: Values and Types

## Introduction

Numbers, strings as lists, format directives, and booleans. By the end of this lesson you will be able to: Do integer and float arithmetic; Manipulate strings and charlists; Use io:format directives; Understand booleans and comparisons.

## Key Concepts

### 1. Do integer and float arithmetic

Target: Do integer and float arithmetic. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% Numbers and arithmetic
-module(nums).
-export([run/0]).

run() ->
    io:format("~p~n", [1 + 2]),
    io:format("~p~n", [10 - 3]),
    io:format("~p~n", [4 * 5]),
    io:format("~p~n", [10 / 3]),     % always a float: 3.333...
    io:format("~p~n", [10 div 3]),   % integer division: 3
    io:format("~p~n", [10 rem 3]),   % remainder: 1
    io:format("~p~n", [2#1010]).     % binary literal: 10
```
### 2. Manipulate strings and charlists

Target: Manipulate strings and charlists. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% Strings are lists of integers
-module(strs).
-export([run/0]).

run() ->
    S = "hello",
    io:format("~p~n", [length(S)]),        % 5
    io:format("~s~n", ["hello" ++ " world"]),  % concatenation
    io:format("~p~n", [hd("abc")]),        % 97 (the 'a' codepoint)
    io:format("~p~n", [[H | _] = "xyz"]),
    H = 120.                               % first char of "xyz"
```
### 3. Use io:format directives

Target: Use io:format directives. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% The format directive in depth
-module(fmt).
-export([run/0]).

run() ->
    io:format("~p~n", [{a, 1}]),     % ~p prints any term
    io:format("~w~n", [{a, 1}]),     % ~w prints without pretty-printing
    io:format("~b~n", [255]),        % ~b prints as decimal... use ~p
    io:format("~.2f~n", [3.14159]),  % 3.14
    io:format("~-10s|~n", ["left"]). % padded string
```
### 4. Understand booleans and comparisons

Target: Understand booleans and comparisons. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% Booleans and guards
-module(bools).
-export([run/0]).

run() ->
    io:format("~p~n", [true]),
    io:format("~p~n", [false]),
    io:format("~p~n", [1 < 2]),
    io:format("~p~n", [3 >= 3]),
    io:format("~p~n", [not false]),
    io:format("~p~n", [true and 1 < 2]).
%% true/false are atoms; comparisons work on any terms.
```

## Practice Questions

1. What is the key idea behind "Values and Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Values and Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Values and Types"
1. "Provide advanced patterns and performance considerations for Values and Types"

## Key Takeaways

- Master the core ideas of Values and Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
