---
{
  "title": "Advanced OTP",
  "description": "Call vs cast, timeouts, gen_statem, and the philosophy.",
  "type": "lesson",
  "order": 21,
  "duration": "75 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Use call and cast correctly",
    "Set call timeouts",
    "Model with gen_statem",
    "Apply the Erlang philosophy"
  ],
  "knowledge_refs": [
    "erlang/erlang-21-advanced-otp"
  ],
  "prerequisites": [
    "ERLANG-20"
  ],
  "references": [
    {
      "title": "Erlang — gen_statem",
      "url": "https://www.erlang.org/doc/apps/stdlib/gen_statem.html"
    },
    {
      "title": "Erlang — gen_server call timeouts",
      "url": "https://www.erlang.org/doc/apps/stdlib/gen_server.html#call/3"
    },
    {
      "title": "Erlang — Philosophy (FAQ)",
      "url": "https://www.erlang.org/faq/introduction.html"
    }
  ]
}
---

# ERLANG-21-ADVANCED-OTP: Advanced OTP

## Introduction

Call vs cast, timeouts, gen_statem, and the philosophy. By the end of this lesson you will be able to: Use call and cast correctly; Set call timeouts; Model with gen_statem; Apply the Erlang philosophy.

## Key Concepts

### 1. Use call and cast correctly

Target: Use call and cast correctly. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% GenServer call vs cast in depth
-module(server).
-behaviour(gen_server).
-export([start_link/0, ask/1, fire/1]).
-export([init/1, handle_call/3, handle_cast/2]).

start_link() -> gen_server:start_link({local, ?MODULE}, ?MODULE, [], []).

ask(Q) -> gen_server:call(?MODULE, {ask, Q}).
fire(E) -> gen_server:cast(?MODULE, {fire, E}).

init([]) -> {ok, 0}.

handle_call({ask, Q}, _From, N) -> {reply, {q, Q, n, N}, N}.
handle_cast({fire, E}, N) -> {noreply, N + 1}.

run() ->
    server:start_link(),
    server:fire(hello),
    server:fire(world),
    io:format("~p~n", [server:ask(count)]).
    % {q, count, n, 2} — casts are async, calls are sync.
```
### 2. Set call timeouts

Target: Set call timeouts. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% Timeouts in gen_server calls
-module(slow_server).
-behaviour(gen_server).
-export([start_link/0, call_slow/0]).
-export([init/1, handle_call/3]).

start_link() -> gen_server:start_link(?MODULE, [], []).

call_slow() -> gen_server:call(?MODULE, slow, 500).

init([]) -> {ok, undefined}.

handle_call(slow, _From, S) ->
    timer:sleep(1000),
    {reply, done, S}.

run() ->
    io:format("A call that exceeds the timeout exits with timeout.~n"),
    io:format("Adjust the timeout per call: gen_server:call(Pid, Req, 5000).~n"),
    io:format("Infinite wait: gen_server:call(Pid, Req, infinity).~n").
    % Default call timeout is 5000ms.
```
### 3. Model with gen_statem

Target: Model with gen_statem. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% gen_statem: state machines as OTP
-module(stm).
-behaviour(gen_statem).
-export([start_link/0, submit/0]).
-export([init/1, callback_mode/0, handle_event/4]).

start_link() -> gen_statem:start_link({local, ?MODULE}, ?MODULE, draft, []).

submit() -> gen_statem:call(?MODULE, submit).

init(State) -> {ok, State}.
callback_mode() -> state_functions.

draft(Event, submit, _Data) -> {next_state, submitted, []}.

run() ->
    io:format("gen_statem models explicit states and transitions.~n"),
    io:format("Each state is a function handling its events.~n").
    % State machines handle complex protocols cleanly.
```
### 4. Apply the Erlang philosophy

Target: Apply the Erlang philosophy. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% The Erlang philosophy recap
-module(philosophy).
-export([run/0]).

run() ->
    io:format("Let it crash: isolate failures, restart, keep going.~n"),
    io:format("Everything is a process; communicate with messages.~n"),
    io:format("Immutable data + pattern matching = clarity.~n"),
    io:format("OTP behaviours encode decades of battle testing.~n").
    % Concurrency, fault-tolerance, and distribution built in.
```

## Practice Questions

1. What is the key idea behind "Advanced OTP"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Advanced OTP with analogies and real-world examples"
1. "Show me common mistakes beginners make with Advanced OTP"
1. "Provide advanced patterns and performance considerations for Advanced OTP"

## Key Takeaways

- Master the core ideas of Advanced OTP through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
