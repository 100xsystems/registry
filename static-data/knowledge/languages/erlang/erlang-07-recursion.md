---
{
  "title": "Recursion",
  "description": "Recursive loops, tail calls, accumulators, and list building.",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Loop with recursion",
    "Use tail-recursive accumulators",
    "Build lists recursively",
    "Peel lists with patterns"
  ],
  "knowledge_refs": [
    "erlang/erlang-07-recursion"
  ],
  "prerequisites": [
    "ERLANG-06"
  ],
  "references": [
    {
      "title": "Erlang — Recursion",
      "url": "https://www.erlang.org/doc/system/syntax.html"
    },
    {
      "title": "Learn You Some Erlang — Recursion",
      "url": "https://learnyousomeerlang.com/recursion"
    },
    {
      "title": "Erlang — Efficiency Guide (tail calls)",
      "url": "https://www.erlang.org/doc/efficiency_guide/functions.html"
    }
  ]
}
---

# ERLANG-07-RECURSION: Recursion

## Introduction

Recursive loops, tail calls, accumulators, and list building. By the end of this lesson you will be able to: Loop with recursion; Use tail-recursive accumulators; Build lists recursively; Peel lists with patterns.

## Key Concepts

### 1. Loop with recursion

Target: Loop with recursion. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% Recursion: the Erlang way to loop
-module(count).
-export([up_to/1]).

up_to(0) -> 0;
up_to(N) -> N + up_to(N - 1).

run() ->
    io:format("~p~n", [count:up_to(5)]).   % 15 (5+4+3+2+1+0)
```
### 2. Use tail-recursive accumulators

Target: Use tail-recursive accumulators. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% Tail-recursion with an accumulator
-module(sum).
-export([of/1]).

of(L) -> sum(L, 0).

sum([], Acc) -> Acc;
sum([H | T], Acc) -> sum(T, Acc + H).

run() ->
    io:format("~p~n", [sum:of([1, 2, 3, 4])]).   % 10
%% The recursive call is the last expression — tail call
%% optimized, so the stack never grows.
```
### 3. Build lists recursively

Target: Build lists recursively. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% Recursive list building
-module(evens).
-export([only/1]).

only(L) -> collect(L, []).

collect([], Acc) -> lists:reverse(Acc);
collect([H | T], Acc) when H rem 2 =:= 0 -> collect(T, [H | Acc]);
collect([_ | T], Acc) -> collect(T, Acc).

run() ->
    io:format("~p~n", [evens:only([1, 2, 3, 4, 5, 6])]).
    % [2, 4, 6] — reverse at the end keeps order
```
### 4. Peel lists with patterns

Target: Peel lists with patterns. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% The classic length with pattern matching
-module(len).
-export([of/1]).

of([]) -> 0;
of([_ | T]) -> 1 + of(T).

run() ->
    io:format("~p~n", [len:of([1, 2, 3])]).   % 3
%% Each step peels the head and recurses on the tail.
```

## Practice Questions

1. What is the key idea behind "Recursion"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Recursion with analogies and real-world examples"
1. "Show me common mistakes beginners make with Recursion"
1. "Provide advanced patterns and performance considerations for Recursion"

## Key Takeaways

- Master the core ideas of Recursion through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
