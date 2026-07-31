---
{
  "title": "Maps and Binaries",
  "description": "Maps, map updates, bit syntax, and binaries as strings.",
  "type": "lesson",
  "order": 13,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Build and update maps",
    "Merge and update maps",
    "Use bit syntax",
    "Work with binary strings"
  ],
  "knowledge_refs": [
    "erlang/erlang-13-maps-binaries"
  ],
  "prerequisites": [
    "ERLANG-12"
  ],
  "references": [
    {
      "title": "Erlang — Maps",
      "url": "https://www.erlang.org/doc/reference_manual/data_types.html#map"
    },
    {
      "title": "Erlang — Bit Syntax",
      "url": "https://www.erlang.org/doc/programming_examples/bit_syntax.html"
    },
    {
      "title": "Erlang — binary module",
      "url": "https://www.erlang.org/doc/apps/stdlib/binary.html"
    }
  ]
}
---

# ERLANG-13-MAPS-BINARIES: Maps and Binaries

## Introduction

Maps, map updates, bit syntax, and binaries as strings. By the end of this lesson you will be able to: Build and update maps; Merge and update maps; Use bit syntax; Work with binary strings.

## Key Concepts

### 1. Build and update maps

Target: Build and update maps. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% Maps: modern key-value store
-module(maps_more).
-export([run/0]).

run() ->
    M0 = #{a => 1, b => 2},
    M1 = maps:put(c, 3, M0),
    io:format("~p~n", [maps:size(M1)]),      % 3
    io:format("~p~n", [maps:is_key(a, M1)]), % true
    io:format("~p~n", [maps:remove(a, M1)]). % #{b => 2, c => 3}
    % Map updates return NEW maps; originals are untouched.
```
### 2. Merge and update maps

Target: Merge and update maps. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% Map update and merge
-module(map_updates).
-export([run/0]).

run() ->
    M = #{count => 0},
    io:format("~p~n", [maps:update(count, 10, M)]),   % #{count => 10}
    io:format("~p~n", [maps:update_with(count, fun(N) -> N + 1 end, M)]),
    % #{count => 1}
    io:format("~p~n", [maps:merge(#{a => 1}, #{b => 2})]).
    % #{a => 1, b => 2}
```
### 3. Use bit syntax

Target: Use bit syntax. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% Binary and bit syntax
-module(bins).
-export([run/0]).

run() ->
    <<A, B, C>> = <<1, 2, 3>>,
    io:format("~p ~p ~p~n", [A, B, C]),
    <<X:16>> = <<1, 0>>,           % 16-bit big-endian int
    io:format("~p~n", [X]),        % 256
    Bin = <<"hello">>,
    io:format("~p~n", [binary:part(Bin, 1, 3)]).
    % <<"ell">> — bit syntax slices binaries efficiently.
```
### 4. Work with binary strings

Target: Work with binary strings. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% Strings vs binaries: the modern choice
-module(str_bin).
-export([run/0]).

run() ->
    Bin = <<"hello">>,
    io:format("~p~n", [byte_size(Bin)]),        % 5
    io:format("~p~n", [binary:bin_to_list(Bin)]),
    % [104, 101, 108, 108, 111]
    io:format("~p~n", [unicode:characters_to_binary("héllo")]).
    % UTF-8 binary — binaries are the efficient string type.
```

## Practice Questions

1. What is the key idea behind "Maps and Binaries"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Maps and Binaries with analogies and real-world examples"
1. "Show me common mistakes beginners make with Maps and Binaries"
1. "Provide advanced patterns and performance considerations for Maps and Binaries"

## Key Takeaways

- Master the core ideas of Maps and Binaries through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
