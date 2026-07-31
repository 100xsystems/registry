---
{
  "title": "Anonymous Functions and Funs",
  "description": "Anonymous functions, higher-order functions, and closures.",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write anonymous functions",
    "Pass functions to higher-order functions",
    "Reference module functions",
    "Capture environments in closures"
  ],
  "knowledge_refs": [
    "erlang/erlang-08-funs"
  ],
  "prerequisites": [
    "ERLANG-07"
  ],
  "references": [
    {
      "title": "Erlang — Funs",
      "url": "https://www.erlang.org/doc/reference_manual/expressions.html#fun"
    },
    {
      "title": "Erlang — Functional Programming",
      "url": "https://www.erlang.org/doc/system/fun.html"
    },
    {
      "title": "Learn You Some Erlang — Higher Order Functions",
      "url": "https://learnyousomeerlang.com/higher-order-functions"
    }
  ]
}
---

# ERLANG-08-FUNS: Anonymous Functions and Funs

## Introduction

Anonymous functions, higher-order functions, and closures. By the end of this lesson you will be able to: Write anonymous functions; Pass functions to higher-order functions; Reference module functions; Capture environments in closures.

## Key Concepts

### 1. Write anonymous functions

Target: Write anonymous functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% Anonymous functions (funs)
-module(funs).
-export([run/0]).

run() ->
    Double = fun(X) -> X * 2 end,
    io:format("~p~n", [Double(4)]),          % 8
    io:format("~p~n", [fun(X) -> X + 1 end(5)]),  % 6
    Add = fun(A, B) -> A + B end,
    io:format("~p~n", [Add(3, 4)]).          % 7
```
### 2. Pass functions to higher-order functions

Target: Pass functions to higher-order functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% Higher-order functions
-module(hof).
-export([run/0]).

run() ->
    ApplyTwice = fun(F, X) -> F(F(X)) end,
    Inc = fun(N) -> N + 1 end,
    io:format("~p~n", [ApplyTwice(Inc, 5)]),   % 7
    io:format("~p~n", [lists:map(fun(N) -> N * N end, [1, 2, 3])]).
    % [1, 4, 9]
```
### 3. Reference module functions

Target: Reference module functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% Function references: fun module:function/arity
-module(refs).
-export([run/0]).

run() ->
    io:format("~p~n", [lists:map(fun erlang:abs/1, [-1, 2, -3])]),
    % [1, 2, 3]
    io:format("~p~n", [lists:map(fun lists:reverse/1, [[1, 2], [3, 4]])]).
    % [[2, 1], [4, 3]]
```
### 4. Capture environments in closures

Target: Capture environments in closures. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% Closures: capturing the environment
-module(clos).
-export([make_add/1]).

make_add(N) -> fun(X) -> X + N end.

run() ->
    Add10 = clos:make_add(10),
    io:format("~p~n", [Add10(5)]),     % 15
    Add100 = clos:make_add(100),
    io:format("~p~n", [Add100(1)]).    % 101
```

## Practice Questions

1. What is the key idea behind "Anonymous Functions and Funs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Anonymous Functions and Funs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Anonymous Functions and Funs"
1. "Provide advanced patterns and performance considerations for Anonymous Functions and Funs"

## Key Takeaways

- Master the core ideas of Anonymous Functions and Funs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
