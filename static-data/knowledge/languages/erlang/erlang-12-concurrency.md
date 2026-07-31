---
{
  "title": "Concurrency Utilities",
  "description": "Process dictionary, ets, parallel map, and timing.",
  "type": "lesson",
  "order": 12,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use the process dictionary",
    "Store data in ets",
    "Parallelize with spawn",
    "Measure with timer"
  ],
  "knowledge_refs": [
    "erlang/erlang-12-concurrency"
  ],
  "prerequisites": [
    "ERLANG-11"
  ],
  "references": [
    {
      "title": "Erlang — ets",
      "url": "https://www.erlang.org/doc/apps/stdlib/ets.html"
    },
    {
      "title": "Erlang — process dictionary",
      "url": "https://www.erlang.org/doc/efficiency_guide/processes.html"
    },
    {
      "title": "Erlang — timer module",
      "url": "https://www.erlang.org/doc/apps/stdlib/timer.html"
    }
  ]
}
---

# ERLANG-12-CONCURRENCY: Concurrency Utilities

## Introduction

Process dictionary, ets, parallel map, and timing. By the end of this lesson you will be able to: Use the process dictionary; Store data in ets; Parallelize with spawn; Measure with timer.

## Key Concepts

### 1. Use the process dictionary

Target: Use the process dictionary. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% The process dictionary: thread-local storage
-module(pdict).
-export([run/0]).

run() ->
    put(name, "Alice"),
    io:format("~p~n", [get(name)]),     % "Alice"
    put(count, 1),
    put(count, 2),                      % overwrites
    io:format("~p~n", [get(count)]),    % 2
    erase().
    % The process dictionary is simple but frowned upon — state
    % should live in gen_servers where it is visible.
```
### 2. Store data in ets

Target: Store data in ets. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% ets: the Erlang term store
-module(ets_demo).
-export([run/0]).

run() ->
    Tab = ets:new(users, [set, public]),
    ets:insert(Tab, {1, "Alice"}),
    ets:insert(Tab, {2, "Bob"}),
    io:format("~p~n", [ets:lookup(Tab, 1)]),   % [{1, "Alice"}]
    io:format("~p~n", [ets:member(Tab, 2)]),   % true
    ets:delete(Tab, 1),
    io:format("~p~n", [ets:tab2list(Tab)]).    % [{2, "Bob"}]
    % ets tables are fast in-memory key-value stores.
```
### 3. Parallelize with spawn

Target: Parallelize with spawn. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% Parallel map with spawn
-module(pmap).
-export([run/0]).

run() ->
    Results = parallel_map(fun(X) -> X * X end, [1, 2, 3, 4]),
    io:format("~p~n", [Results]).
    % [1, 4, 9, 16]

parallel_map(F, L) ->
    Parent = self(),
    Pids = [spawn(fun() -> Parent ! {self(), F(X)} end) || X <- L],
    [receive {Pid, V} -> V end || Pid <- Pids].
    % Each element runs in its own lightweight process.
```
### 4. Measure with timer

Target: Measure with timer. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% Timing and performance with timer
-module(timing).
-export([run/0]).

run() ->
    {Time, Result} = timer:tc(fun() ->
        lists:sum([X * X || X <- lists:seq(1, 1000)])
    end),
    io:format("result: ~p in ~p microseconds~n", [Result, Time]).
    % timer:tc/1 measures the execution time of a fun.
```

## Practice Questions

1. What is the key idea behind "Concurrency Utilities"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Concurrency Utilities with analogies and real-world examples"
1. "Show me common mistakes beginners make with Concurrency Utilities"
1. "Provide advanced patterns and performance considerations for Concurrency Utilities"

## Key Takeaways

- Master the core ideas of Concurrency Utilities through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
