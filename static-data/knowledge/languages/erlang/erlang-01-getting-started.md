---
{
  "title": "Getting Started with Erlang",
  "description": "Modules, exports, atoms, variables, and the Erlang shell.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write and compile an Erlang module",
    "Explore with the Erlang shell",
    "Define and export functions",
    "Use atoms and single assignment"
  ],
  "knowledge_refs": [
    "erlang/erlang-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "Erlang — Getting Started",
      "url": "https://www.erlang.org/doc/system/getting_started.html"
    },
    {
      "title": "Erlang — System Documentation",
      "url": "https://www.erlang.org/docs"
    },
    {
      "title": "Erlang — The Shell",
      "url": "https://www.erlang.org/doc/apps/erts/erl_cmd.html"
    }
  ]
}
---

# ERLANG-01-GETTING-STARTED: Getting Started with Erlang

## Introduction

Modules, exports, atoms, variables, and the Erlang shell. By the end of this lesson you will be able to: Write and compile an Erlang module; Explore with the Erlang shell; Define and export functions; Use atoms and single assignment.

## Key Concepts

### 1. Write and compile an Erlang module

Target: Write and compile an Erlang module. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% Your first Erlang program
-module(hello).
-export([world/0]).

world() ->
    io:format("Hello, 100X Systems!~n").
%% Compile: erlc hello.erl   Run: erl -noshell -eval 'hello:world()'
%% Every statement ends with a period (.)
```
### 2. Explore with the Erlang shell

Target: Explore with the Erlang shell. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% The Erlang shell (erl)
%% 1> 1 + 2.
%% 3
%% 2> io:format("hi~n").
%% hi
%% 3> halt().
%% The shell evaluates one expression per line, ending with a dot.
io:format("Shell expressions end with a period.~n").
```
### 3. Define and export functions

Target: Define and export functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% Modules, exports, and functions
-module(calc).
-export([add/2, multiply/2]).

add(A, B) -> A + B.
multiply(A, B) -> A * B.

%% Functions are named with arity: add/2 means two arguments.
%% Only exported functions are callable from outside.
run() ->
    io:format("~p~n", [calc:add(3, 4)]).
```
### 4. Use atoms and single assignment

Target: Use atoms and single assignment. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% Atoms and variables
-module(types_demo).
-export([run/0]).

run() ->
    Atom = ok,              % atoms are lowercase constants
    Value = 42,             % variables start with a capital letter
    io:format("~p ~p~n", [Atom, Value]).
%% Variables can be bound only ONCE (single assignment).
```

## Practice Questions

1. What is the key idea behind "Getting Started with Erlang"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Erlang with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Erlang"
1. "Provide advanced patterns and performance considerations for Getting Started with Erlang"

## Key Takeaways

- Master the core ideas of Getting Started with Erlang through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
