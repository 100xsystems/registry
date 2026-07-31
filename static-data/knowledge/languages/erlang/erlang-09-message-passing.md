---
{
  "title": "Message Passing",
  "description": "send/receive, PIDs, selective receive, and timeouts.",
  "type": "lesson",
  "order": 9,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Send messages with !",
    "Receive with patterns",
    "Use self() and PIDs",
    "Match selectively with timeouts"
  ],
  "knowledge_refs": [
    "erlang/erlang-09-message-passing"
  ],
  "prerequisites": [
    "ERLANG-08"
  ],
  "references": [
    {
      "title": "Erlang — Processes",
      "url": "https://www.erlang.org/doc/reference_manual/processes.html"
    },
    {
      "title": "Erlang — receive",
      "url": "https://www.erlang.org/doc/reference_manual/expressions.html#receive"
    },
    {
      "title": "Learn You Some Erlang — Concurrency",
      "url": "https://learnyousomeerlang.com/the-hoe"
    }
  ]
}
---

# ERLANG-09-MESSAGE-PASSING: Message Passing

## Introduction

send/receive, PIDs, selective receive, and timeouts. By the end of this lesson you will be able to: Send messages with !; Receive with patterns; Use self() and PIDs; Match selectively with timeouts.

## Key Concepts

### 1. Send messages with !

Target: Send messages with !. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% The receive expression: message passing
-module(echo).
-export([run/0]).

run() ->
    Parent = self(),
    spawn(fun() ->
        receive
            {msg, M} -> Parent ! {reply, M}
        end
    end),
    io:format("~p~n", [self()]).
    % Messages are sent with ! and received with receive.
```
### 2. Receive with patterns

Target: Receive with patterns. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% Send and receive with pattern matching
-module(pingpong).
-export([run/0]).

run() ->
    Parent = self(),
    spawn(fun() -> Parent ! {ping, "from child"} end),
    receive
        {ping, Msg} -> io:format("got: ~s~n", [Msg])
    after 1000 ->
        io:format("timeout~n")
    end.
    % receive blocks until a matching message arrives
```
### 3. Use self() and PIDs

Target: Use self() and PIDs. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% Process identity and self()
-module(pids).
-export([run/0]).

run() ->
    Pid = self(),
    io:format("parent pid: ~p~n", [Pid]),
    Other = spawn(fun() ->
        io:format("child pid: ~p~n", [self()])
    end),
    io:format("spawned: ~p~n", [Other]).
    % Each process has a unique PID; Pid ! Msg targets it.
```
### 4. Match selectively with timeouts

Target: Match selectively with timeouts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% Selective receive: matching specific messages
-module(selective).
-export([run/0]).

run() ->
    Parent = self(),
    spawn(fun() ->
        Parent ! {low, 1},
        Parent ! {high, 2},
        Parent ! {low, 3}
    end),
    receive {high, V} -> io:format("high: ~p~n", [V]) end,
    receive {low, L1} -> io:format("low: ~p~n", [L1]) end.
    % The first receive skips lows to find the high message.
```

## Practice Questions

1. What is the key idea behind "Message Passing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Message Passing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Message Passing"
1. "Provide advanced patterns and performance considerations for Message Passing"

## Key Takeaways

- Master the core ideas of Message Passing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
