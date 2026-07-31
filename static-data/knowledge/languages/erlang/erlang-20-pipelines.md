---
{
  "title": "Process Pipelines and Servers",
  "description": "Process pipelines, worker pools, caches, health checks.",
  "type": "lesson",
  "order": 20,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Chain process stages",
    "Build worker pools",
    "Implement a cache server",
    "Design heartbeat health"
  ],
  "knowledge_refs": [
    "erlang/erlang-20-pipelines"
  ],
  "prerequisites": [
    "ERLANG-19"
  ],
  "references": [
    {
      "title": "Erlang — Process patterns",
      "url": "https://learnyousomeerlang.com/the-hitchhikers-guide-to-concurrency"
    },
    {
      "title": "OTP — Design Principles",
      "url": "https://www.erlang.org/doc/design_principles/des_prim.html"
    },
    {
      "title": "Erlang — gen_server examples",
      "url": "https://www.erlang.org/doc/apps/stdlib/gen_server.html#gen_server-examples"
    }
  ]
}
---

# ERLANG-20-PIPELINES: Process Pipelines and Servers

## Introduction

Process pipelines, worker pools, caches, health checks. By the end of this lesson you will be able to: Chain process stages; Build worker pools; Implement a cache server; Design heartbeat health.

## Key Concepts

### 1. Chain process stages

Target: Chain process stages. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% A complete process-based pipeline
-module(pipeline).
-export([run/0]).

run() ->
    io:format("Chain processes with message passing:~n"),
    io:format("source -> filter -> sink~n"),
    io:format("Each stage is a process with a receive loop.~n"),
    io:format("Backpressure comes from receive blocking.~n").
    % Process pipelines are the classic Erlang architecture.
```
### 2. Build worker pools

Target: Build worker pools. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% A small worker pool
-module(pool).
-export([run/0]).

run() ->
    Parent = self(),
    [spawn(fun() -> Parent ! {result, X * 2} end) || X <- [1, 2, 3, 4]],
    Results = [receive {result, R} -> R end || _ <- [1, 2, 3, 4]],
    io:format("~p~n", [lists:sort(Results)]).
    % [2, 4, 6, 8] — gather results from concurrent workers.
```
### 3. Implement a cache server

Target: Implement a cache server. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% Building a mini in-memory cache
-module(cache).
-export([start/0, put/3, get/2]).
-export([loop/1]).

start() -> spawn(fun() -> loop(#{}) end).

put(Pid, K, V) -> Pid ! {put, K, V}.
get(Pid, K) ->
    Pid ! {get, self(), K},
    receive {value, V} -> V after 500 -> not_found end.

loop(Store) ->
    receive
        {put, K, V} -> loop(Store#{K => V});
        {get, Pid, K} ->
            Pid ! {value, maps:get(K, Store, not_found)},
            loop(Store)
    end.

run() ->
    Pid = cache:start(),
    cache:put(Pid, name, "Alice"),
    io:format("~p~n", [cache:get(Pid, name)]),   % "Alice"
    io:format("~p~n", [cache:get(Pid, age)]).    % not_found
    % A stateful server in ~15 lines — the Erlang essence.
```
### 4. Design heartbeat health

Target: Design heartbeat health. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% The heartbeat pattern: monitoring health
-module(health).
-export([run/0]).

run() ->
    io:format("A process sends periodic heartbeats.~n"),
    io:format("A monitor watches for missed beats.~n"),
    io:format("Missing beats trigger a restart or alert.~n"),
    io:format("OTP supervisors handle this automatically.~n").
    % Health checks keep distributed systems self-healing.
```

## Practice Questions

1. What is the key idea behind "Process Pipelines and Servers"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Process Pipelines and Servers with analogies and real-world examples"
1. "Show me common mistakes beginners make with Process Pipelines and Servers"
1. "Provide advanced patterns and performance considerations for Process Pipelines and Servers"

## Key Takeaways

- Master the core ideas of Process Pipelines and Servers through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
