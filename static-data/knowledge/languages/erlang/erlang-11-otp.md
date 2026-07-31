---
{
  "title": "OTP Behaviours",
  "description": "gen_server, supervisors, and applications.",
  "type": "lesson",
  "order": 11,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Use gen_server",
    "Design supervisors",
    "Understand restart strategies",
    "Package applications"
  ],
  "knowledge_refs": [
    "erlang/erlang-11-otp"
  ],
  "prerequisites": [
    "ERLANG-10"
  ],
  "references": [
    {
      "title": "OTP Design Principles",
      "url": "https://www.erlang.org/doc/design_principles/des_prim.html"
    },
    {
      "title": "Erlang — gen_server",
      "url": "https://www.erlang.org/doc/apps/stdlib/gen_server.html"
    },
    {
      "title": "Learn You Some Erlang — OTP",
      "url": "https://learnyousomeerlang.com/clients-and-servers"
    }
  ]
}
---

# ERLANG-11-OTP: OTP Behaviours

## Introduction

gen_server, supervisors, and applications. By the end of this lesson you will be able to: Use gen_server; Design supervisors; Understand restart strategies; Package applications.

## Key Concepts

### 1. Use gen_server

Target: Use gen_server. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% OTP: the Open Telecom Platform
-module(otp_intro).
-export([run/0]).

run() ->
    io:format("OTP provides: gen_server, supervisor, application~n"),
    io:format("gen_event, gen_statem, and the standard library~n"),
    io:format("Behaviours give you battle-tested skeletons.~n").
    % OTP is the Erlang runtime's standard library of patterns.
```
### 2. Design supervisors

Target: Design supervisors. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% gen_server: the core behaviour
-module(counter).
-behaviour(gen_server).
-export([start_link/0, inc/0, get/0]).
-export([init/1, handle_call/3, handle_cast/2]).

start_link() -> gen_server:start_link({local, ?MODULE}, ?MODULE, 0, []).

inc() -> gen_server:cast(?MODULE, inc).
get() -> gen_server:call(?MODULE, get).

init(Count) -> {ok, Count}.

handle_call(get, _From, Count) -> {reply, Count, Count};
handle_call(_Req, _From, Count) -> {reply, ok, Count}.

handle_cast(inc, Count) -> {noreply, Count + 1}.

run() ->
    counter:start_link(),
    counter:inc(),
    counter:inc(),
    io:format("~p~n", [counter:get()]).   % 2
    % handle_call is synchronous; handle_cast is fire-and-forget.
```
### 3. Understand restart strategies

Target: Understand restart strategies. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% Supervisors: restart on failure
-module(super_intro).
-export([run/0]).

run() ->
    io:format("A supervisor starts and monitors children.~n"),
    io:format("If a child crashes, the supervisor restarts it.~n"),
    io:format("Restart strategies: one_for_one, one_for_all,~n"),
    io:format("rest_for_one, and simple_one_for_one.~n").
    % The supervision tree is the core fault-tolerance model.
```
### 4. Package applications

Target: Package applications. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% Application: the OTP packaging unit
-module(my_app).
-behaviour(application).
-export([start/2, stop/1, init/1]).

start(_Type, _Args) ->
    io:format("application starting~n"),
    %% supervisor:start_link/2 takes (CallbackModule, Args); the
    %% callback's init/1 returns the child spec.
    {ok, Pid} = supervisor:start_link(?MODULE, []),
    {ok, Pid}.

%% The application module doubles as the supervisor callback:
init([]) ->
    {ok, {{one_for_one, 5, 10}, []}}.

stop(_State) ->
    io:format("application stopping~n"),
    ok.
    % Applications bundle code, processes, and config together.
```

## Practice Questions

1. What is the key idea behind "OTP Behaviours"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain OTP Behaviours with analogies and real-world examples"
1. "Show me common mistakes beginners make with OTP Behaviours"
1. "Provide advanced patterns and performance considerations for OTP Behaviours"

## Key Takeaways

- Master the core ideas of OTP Behaviours through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
