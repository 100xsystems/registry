---
{
  "title": "Control Flow",
  "description": "case, if, pattern-matched clauses, and guards.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Match with case expressions",
    "Use if expressions",
    "Write multi-clause functions",
    "Validate with guards"
  ],
  "knowledge_refs": [
    "erlang/erlang-03-control-flow"
  ],
  "prerequisites": [
    "ERLANG-02"
  ],
  "references": [
    {
      "title": "Erlang — Expressions (case/if)",
      "url": "https://www.erlang.org/doc/reference_manual/expressions.html#case"
    },
    {
      "title": "Erlang — Guards",
      "url": "https://www.erlang.org/doc/reference_manual/expressions.html#guards"
    },
    {
      "title": "Learn You Some Erlang — Functions",
      "url": "https://learnyousomeerlang.com/syntax-in-functions"
    }
  ]
}
---

# ERLANG-03-CONTROL-FLOW: Control Flow

## Introduction

case, if, pattern-matched clauses, and guards. By the end of this lesson you will be able to: Match with case expressions; Use if expressions; Write multi-clause functions; Validate with guards.

## Key Concepts

### 1. Match with case expressions

Target: Match with case expressions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% case expressions
-module(case_demo).
-export([describe/1]).

describe(X) ->
    case X of
        0 -> "zero";
        N when N < 0 -> "negative";
        N when N > 0 -> "positive";
        _ -> "unknown"
    end.

run() ->
    io:format("~s~n", [describe(-5)]).   % negative
```
### 2. Use if expressions

Target: Use if expressions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% if expressions
-module(if_demo).
-export([classify/1]).

classify(Score) ->
    if
        Score >= 90 -> "excellent";
        Score >= 70 -> "good";
        Score >= 50 -> "fair";
        true -> "poor"
    end.

run() ->
    io:format("~s~n", [classify(85)]).   % good
%% if has no conditions syntax — guard expressions only.
%% The final `true ->` clause is the else.
```
### 3. Write multi-clause functions

Target: Write multi-clause functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% Pattern matching in function clauses
-module(fact).
-export([of/1]).

of(0) -> 1;
of(N) when N > 0 -> N * of(N - 1).

run() ->
    io:format("~p~n", [fact:of(5)]).   % 120
%% Clauses are tried top to bottom; first match wins.
```
### 4. Validate with guards

Target: Validate with guards. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% Guards: validating arguments
-module(guards).
-export([day_type/1]).

day_type(Day) when Day >= 1, Day =< 5 -> workday;
day_type(Day) when Day =:= 6; Day =:= 7 -> weekend;
day_type(_) -> invalid.

run() ->
    io:format("~p~n", [day_type(3)]),     % workday
    io:format("~p~n", [day_type(7)]),     % weekend
    io:format("~p~n", [day_type(0)]).     % invalid
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
