---
{
  "title": "Lists and the Lists Module",
  "description": "List fundamentals, comprehensions, and the lists library.",
  "type": "lesson",
  "order": 4,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use hd, tl, and cons",
    "Write list comprehensions",
    "Use the lists module",
    "Fold with foldl and foldr"
  ],
  "knowledge_refs": [
    "erlang/erlang-04-lists"
  ],
  "prerequisites": [
    "ERLANG-03"
  ],
  "references": [
    {
      "title": "Erlang — Lists",
      "url": "https://www.erlang.org/doc/efficiency_guide/listHandling.html"
    },
    {
      "title": "Erlang — List Comprehensions",
      "url": "https://www.erlang.org/doc/programming_examples/list_comprehensions.html"
    },
    {
      "title": "Erlang — lists module",
      "url": "https://www.erlang.org/doc/apps/stdlib/lists.html"
    }
  ]
}
---

# ERLANG-04-LISTS: Lists and the Lists Module

## Introduction

List fundamentals, comprehensions, and the lists library. By the end of this lesson you will be able to: Use hd, tl, and cons; Write list comprehensions; Use the lists module; Fold with foldl and foldr.

## Key Concepts

### 1. Use hd, tl, and cons

Target: Use hd, tl, and cons. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% Lists: the fundamental data structure
-module(lists_demo).
-export([run/0]).

run() ->
    L = [1, 2, 3],
    io:format("~p~n", [hd(L)]),        % 1
    io:format("~p~n", [tl(L)]),        % [2, 3]
    io:format("~p~n", [length(L)]),    % 3
    io:format("~p~n", [[0 | L]]),      % [0, 1, 2, 3]
    io:format("~p~n", [L ++ [4]]).     % [1, 2, 3, 4]
```
### 2. Write list comprehensions

Target: Write list comprehensions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% List comprehension
-module(comps).
-export([run/0]).

run() ->
    Squares = [X * X || X <- [1, 2, 3, 4, 5]],
    io:format("~p~n", [Squares]),      % [1, 4, 9, 16, 25]
    Evens = [X || X <- [1, 2, 3, 4, 5, 6], X rem 2 =:= 0],
    io:format("~p~n", [Evens]).        % [2, 4, 6]
```
### 3. Use the lists module

Target: Use the lists module. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% The lists module
-module(lists_util).
-export([run/0]).

run() ->
    io:format("~p~n", [lists:map(fun(X) -> X * 2 end, [1, 2, 3])]),
    io:format("~p~n", [lists:filter(fun(X) -> X > 1 end, [1, 2, 3])]),
    io:format("~p~n", [lists:sum([1, 2, 3, 4])]),
    io:format("~p~n", [lists:reverse([1, 2, 3])]),
    io:format("~p~n", [lists:sort([3, 1, 2])]),
    io:format("~p~n", [lists:max([3, 9, 4])]).
```
### 4. Fold with foldl and foldr

Target: Fold with foldl and foldr. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% Fold (reduce) and foldl vs foldr
-module(folds).
-export([run/0]).

run() ->
    io:format("~p~n", [lists:foldl(fun(A, B) -> A + B end, 0, [1, 2, 3, 4])]),
    % 10
    io:format("~p~n", [lists:foldr(fun(A, B) -> [A | B] end, [], [1, 2, 3])]),
    % [1, 2, 3] — foldr processes right to left
```

## Practice Questions

1. What is the key idea behind "Lists and the Lists Module"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lists and the Lists Module with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lists and the Lists Module"
1. "Provide advanced patterns and performance considerations for Lists and the Lists Module"

## Key Takeaways

- Master the core ideas of Lists and the Lists Module through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
