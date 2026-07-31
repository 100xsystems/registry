---
{
  "title": "Supervision Trees",
  "description": "Tree structure, supervisor callbacks, restart intensity.",
  "type": "lesson",
  "order": 14,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Structure supervision trees",
    "Write supervisor callbacks",
    "Tune restart intensity",
    "Separate workers and supervisors"
  ],
  "knowledge_refs": [
    "erlang/erlang-14-supervision"
  ],
  "prerequisites": [
    "ERLANG-13"
  ],
  "references": [
    {
      "title": "OTP — Supervision",
      "url": "https://www.erlang.org/doc/design_principles/sup_princ.html"
    },
    {
      "title": "Erlang — supervisor module",
      "url": "https://www.erlang.org/doc/apps/stdlib/supervisor.html"
    },
    {
      "title": "Learn You Some Erlang — Supervisors",
      "url": "https://learnyousomeerlang.com/supervisors"
    }
  ]
}
---

# ERLANG-14-SUPERVISION: Supervision Trees

## Introduction

Tree structure, supervisor callbacks, restart intensity. By the end of this lesson you will be able to: Structure supervision trees; Write supervisor callbacks; Tune restart intensity; Separate workers and supervisors.

## Key Concepts

### 1. Structure supervision trees

Target: Structure supervision trees. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% OTP supervision tree structure
-module(tree).
-export([run/0]).

run() ->
    io:format("Application -> Supervisor -> Workers~n"),
    io:format("Workers: gen_server, gen_event, gen_statem~n"),
    io:format("Supervisors watch and restart their children.~n"),
    io:format("Crash isolation: one worker dying doesn't kill all.~n").
    % The tree is the backbone of fault-tolerant systems.
```
### 2. Write supervisor callbacks

Target: Write supervisor callbacks. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% A supervisor callback module
-module(sup).
-behaviour(supervisor).
-export([start_link/0, init/1]).

start_link() ->
    supervisor:start_link({local, ?MODULE}, ?MODULE, []).

init([]) ->
    Children = [
        {counter, {counter, start_link, []},
         permanent, 5000, worker, [counter]}
    ],
    {ok, {{one_for_one, 5, 10}, Children}}.
    % {strategy, max_restarts, max_time}
    % permanent: always restart; temporary: never; transient:
    % restart only on abnormal exit.
```
### 3. Tune restart intensity

Target: Tune restart intensity. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% Restart intensity and timing
-module(intensity).
-export([run/0]).

run() ->
    io:format("Max restarts in a window limits restart storms.~n"),
    io:format("{one_for_one, 5, 10} = 5 restarts in 10 seconds~n"),
    io:format("If exceeded, the supervisor itself shuts down.~n").
    % This prevents a crash loop from churning forever.
```
### 4. Separate workers and supervisors

Target: Separate workers and supervisors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% Worker vs supervisor: the two roles
-module(roles).
-export([run/0]).

run() ->
    io:format("Workers: do the work, hold the state.~n"),
    io:format("Supervisors: manage workers, never do work.~n"),
    io:format("This separation gives clean crash isolation.~n").
    % A supervisor that does work can't reliably restart itself.
```

## Practice Questions

1. What is the key idea behind "Supervision Trees"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Supervision Trees with analogies and real-world examples"
1. "Show me common mistakes beginners make with Supervision Trees"
1. "Provide advanced patterns and performance considerations for Supervision Trees"

## Key Takeaways

- Master the core ideas of Supervision Trees through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
