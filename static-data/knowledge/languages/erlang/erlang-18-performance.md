---
{
  "title": "Performance",
  "description": "List performance, accumulators, efficient strings, timeouts.",
  "type": "lesson",
  "order": 18,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Choose list operations wisely",
    "Use the accumulator pattern",
    "Prefer binaries for strings",
    "Bound waits with timeouts"
  ],
  "knowledge_refs": [
    "erlang/erlang-18-performance"
  ],
  "prerequisites": [
    "ERLANG-17"
  ],
  "references": [
    {
      "title": "Erlang — Efficiency Guide",
      "url": "https://www.erlang.org/doc/efficiency_guide/introduction.html"
    },
    {
      "title": "Erlang — List Handling",
      "url": "https://www.erlang.org/doc/efficiency_guide/listHandling.html"
    },
    {
      "title": "Erlang — Process Efficiency",
      "url": "https://www.erlang.org/doc/efficiency_guide/processes.html"
    }
  ]
}
---

# ERLANG-18-PERFORMANCE: Performance

## Introduction

List performance, accumulators, efficient strings, timeouts. By the end of this lesson you will be able to: Choose list operations wisely; Use the accumulator pattern; Prefer binaries for strings; Bound waits with timeouts.

## Key Concepts

### 1. Choose list operations wisely

Target: Choose list operations wisely. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% Lists: performance characteristics
-module(list_perf).
-export([run/0]).

run() ->
    io:format("Prepend ([X | L]) is O(1).~n"),
    io:format("Append (L ++ [X]) is O(N) — copy the left side.~n"),
    io:format("Access (lists:nth) is O(N).~n"),
    io:format("Build lists by prepending, reverse at the end.~n").
    % Lists are singly-linked; choose access patterns wisely.
```
### 2. Use the accumulator pattern

Target: Use the accumulator pattern. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% The classic accumulator pattern
-module(accum).
-export([run/0]).

run() ->
    L = build(5, []),
    io:format("~p~n", [L]),        % [5, 4, 3, 2, 1] — built by prepend
    io:format("~p~n", [lists:reverse(L)]).  % [1, 2, 3, 4, 5]

build(0, Acc) -> Acc;
build(N, Acc) -> build(N - 1, [N | Acc]).
    % Prepend then reverse is the idiomatic way to build lists.
```
### 3. Prefer binaries for strings

Target: Prefer binaries for strings. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% Efficient string handling
-module(eff_str).
-export([run/0]).

run() ->
    io:format("Binaries are compact and fast to copy.~n"),
    io:format("Binary syntax matches patterns without allocation.~n"),
    io:format("Strings as lists waste 8 bytes per char.~n"),
    io:format("Prefer <<\"...\">> binaries for text.~n").
    % Binaries use reference counting — cheap sharing.
```
### 4. Bound waits with timeouts

Target: Bound waits with timeouts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% Timeouts and the after clause
-module(timeouts).
-export([run/0]).

run() ->
    Parent = self(),
    spawn(fun() -> timer:sleep(2000), Parent ! late end),
    receive
        Msg -> io:format("got ~p~n", [Msg])
    after 500 ->
        io:format("timed out after 500ms~n")
    end.
    % The after clause prevents infinite blocking.
```

## Practice Questions

1. What is the key idea behind "Performance"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Performance with analogies and real-world examples"
1. "Show me common mistakes beginners make with Performance"
1. "Provide advanced patterns and performance considerations for Performance"

## Key Takeaways

- Master the core ideas of Performance through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
