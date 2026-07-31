---
{
  "title": "Fault Tolerance",
  "description": "Links, monitors, exits, and try/catch.",
  "type": "lesson",
  "order": 10,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Link process lifetimes",
    "Monitor without coupling",
    "Catch exceptions",
    "Distinguish throw/error/exit"
  ],
  "knowledge_refs": [
    "erlang/erlang-10-fault-tolerance"
  ],
  "prerequisites": [
    "ERLANG-09"
  ],
  "references": [
    {
      "title": "Erlang — Errors and Error Handling",
      "url": "https://www.erlang.org/doc/reference_manual/errors.html"
    },
    {
      "title": "Erlang — Links and Monitors",
      "url": "https://www.erlang.org/doc/reference_manual/processes.html#links"
    },
    {
      "title": "Learn You Some Erlang — Errors",
      "url": "https://learnyousomeerlang.com/errors-and-exceptions"
    }
  ]
}
---

# ERLANG-10-FAULT-TOLERANCE: Fault Tolerance

## Introduction

Links, monitors, exits, and try/catch. By the end of this lesson you will be able to: Link process lifetimes; Monitor without coupling; Catch exceptions; Distinguish throw/error/exit.

## Key Concepts

### 1. Link process lifetimes

Target: Link process lifetimes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% Links: crash propagation between processes
-module(links).
-export([run/0]).

run() ->
    process_flag(trap_exit, true),
    spawn_link(fun() -> erlang:error(boom) end),
    receive
        {'EXIT', _Pid, Reason} ->
            io:format("child died: ~p~n", [Reason])
    after 500 ->
        io:format("no exit message~n")
    end.
    % spawn_link ties lifetimes; trapping exits catches them.
```
### 2. Monitor without coupling

Target: Monitor without coupling. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% Monitors: observe without coupling
-module(monitors).
-export([run/0]).

run() ->
    Pid = spawn(fun() -> erlang:error(oops) end),
    Ref = erlang:monitor(process, Pid),
    receive
        {'DOWN', Ref, process, Pid, Reason} ->
            io:format("monitored process down: ~p~n", [Reason])
    after 500 ->
        io:format("still running~n")
    end.
    % Monitors send DOWN; links kill — monitors observe.
```
### 3. Catch exceptions

Target: Catch exceptions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% try/catch: handling exceptions
-module(try_demo).
-export([run/0]).

run() ->
    try
        erlang:error(badarg)
    catch
        error:badarg -> io:format("caught badarg~n");
        _:Reason -> io:format("other: ~p~n", [Reason])
    end.
    % try/catch catches errors, exits, and throws.
```
### 4. Distinguish throw/error/exit

Target: Distinguish throw/error/exit. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% throw, error, and exit — the three exception classes
-module(exceptions).
-export([demo/0]).

demo() ->
    try
        throw(not_found)
    catch
        throw:Value -> {thrown, Value}
    end.

run() ->
    io:format("~p~n", [exceptions:demo()]).
    % {thrown, not_found}
    % error -> for programmer errors, exit -> for process death
```

## Practice Questions

1. What is the key idea behind "Fault Tolerance"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Fault Tolerance with analogies and real-world examples"
1. "Show me common mistakes beginners make with Fault Tolerance"
1. "Provide advanced patterns and performance considerations for Fault Tolerance"

## Key Takeaways

- Master the core ideas of Fault Tolerance through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
