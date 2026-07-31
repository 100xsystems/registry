---
{
  "title": "Tuples and Records",
  "description": "Tuples, the ok/error convention, and records as named tuples.",
  "type": "lesson",
  "order": 5,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Build and access tuples",
    "Return ok/error results",
    "Match tuples in heads",
    "Define and use records"
  ],
  "knowledge_refs": [
    "erlang/erlang-05-tuples-records"
  ],
  "prerequisites": [
    "ERLANG-04"
  ],
  "references": [
    {
      "title": "Erlang — Tuples",
      "url": "https://www.erlang.org/doc/reference_manual/data_types.html#tuple"
    },
    {
      "title": "Erlang — Records",
      "url": "https://www.erlang.org/doc/programming_examples/records.html"
    },
    {
      "title": "Learn You Some Erlang — Records",
      "url": "https://learnyousomeerlang.com/records"
    }
  ]
}
---

# ERLANG-05-TUPLES-RECORDS: Tuples and Records

## Introduction

Tuples, the ok/error convention, and records as named tuples. By the end of this lesson you will be able to: Build and access tuples; Return ok/error results; Match tuples in heads; Define and use records.

## Key Concepts

### 1. Build and access tuples

Target: Build and access tuples. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% Tuples: fixed-size containers
-module(tups).
-export([run/0]).

run() ->
    T = {ok, 42},
    io:format("~p~n", [element(1, T)]),   % ok
    io:format("~p~n", [element(2, T)]),   % 42
    io:format("~p~n", [setelement(2, T, 100)]),  % {ok, 100}
    io:format("~p~n", [tuple_size(T)]).   % 2
```
### 2. Return ok/error results

Target: Return ok/error results. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% The {ok, Value} / {error, Reason} convention
-module(div1).
-export([divide/2]).

divide(A, B) ->
    case B of
        0 -> {error, division_by_zero};
        _ -> {ok, A / B}
    end.

run() ->
    io:format("~p~n", [div1:divide(10, 2)]),   % {ok, 5.0}
    io:format("~p~n", [div1:divide(1, 0)]).    % {error, division_by_zero}
```
### 3. Match tuples in heads

Target: Match tuples in heads. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% Matching tuples in function heads
-module(result).
-export([handle/1]).

handle({ok, Value}) -> {result, Value};
handle({error, Reason}) -> {failure, Reason}.

run() ->
    io:format("~p~n", [result:handle({ok, 7})]),        % {result, 7}
    io:format("~p~n", [result:handle({error, timeout})]).
    % {failure, timeout}
```
### 4. Define and use records

Target: Define and use records. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% Records: named tuples
-module(users).
-export([run/0]).
-record(user, {name, age}).

run() ->
    U = #user{name = "Alice", age = 30},
    io:format("~p~n", [U#user.name]),        % "Alice"
    io:format("~p~n", [U#user.age]),         % 30
    U2 = U#user{age = 31},
    io:format("~p~n", [U2#user.age]).        % 31
%% Records are tuples with a tagged first element.
```

## Practice Questions

1. What is the key idea behind "Tuples and Records"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Tuples and Records with analogies and real-world examples"
1. "Show me common mistakes beginners make with Tuples and Records"
1. "Provide advanced patterns and performance considerations for Tuples and Records"

## Key Takeaways

- Master the core ideas of Tuples and Records through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
