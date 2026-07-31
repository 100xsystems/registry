#!/usr/bin/env python3
"""Generate the 21-lesson Erlang curriculum at Python/JS/Java depth.
Uses the shared gen_lib template. Exact refs from erlang.org docs.
Each lesson has 4 sub-topics, each with its OWN distinct code sample.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import main as run_gen  # noqa: E402

LANGUAGE = 'erlang'

BASE = os.path.join(os.path.dirname(__file__), '..', '..', 'static-data', 'knowledge', 'languages', 'erlang')

CODE = {
    1: [
        '''%% Your first Erlang program
-module(hello).
-export([world/0]).

world() ->
    io:format("Hello, 100X Systems!~n").
%% Compile: erlc hello.erl   Run: erl -noshell -eval 'hello:world()'
%% Every statement ends with a period (.)''',
        '''%% The Erlang shell (erl)
%% 1> 1 + 2.
%% 3
%% 2> io:format("hi~n").
%% hi
%% 3> halt().
%% The shell evaluates one expression per line, ending with a dot.
io:format("Shell expressions end with a period.~n").''',
        '''%% Modules, exports, and functions
-module(calc).
-export([add/2, multiply/2]).

add(A, B) -> A + B.
multiply(A, B) -> A * B.

%% Functions are named with arity: add/2 means two arguments.
%% Only exported functions are callable from outside.
run() ->
    io:format("~p~n", [calc:add(3, 4)]).''',
        '''%% Atoms and variables
-module(types_demo).
-export([run/0]).

run() ->
    Atom = ok,              % atoms are lowercase constants
    Value = 42,             % variables start with a capital letter
    io:format("~p ~p~n", [Atom, Value]).
%% Variables can be bound only ONCE (single assignment).''',
    ],
    2: [
        '''%% Numbers and arithmetic
-module(nums).
-export([run/0]).

run() ->
    io:format("~p~n", [1 + 2]),
    io:format("~p~n", [10 - 3]),
    io:format("~p~n", [4 * 5]),
    io:format("~p~n", [10 / 3]),     % always a float: 3.333...
    io:format("~p~n", [10 div 3]),   % integer division: 3
    io:format("~p~n", [10 rem 3]),   % remainder: 1
    io:format("~p~n", [2#1010]).     % binary literal: 10''',
        '''%% Strings are lists of integers
-module(strs).
-export([run/0]).

run() ->
    S = "hello",
    io:format("~p~n", [length(S)]),        % 5
    io:format("~s~n", ["hello" ++ " world"]),  % concatenation
    io:format("~p~n", [hd("abc")]),        % 97 (the 'a' codepoint)
    io:format("~p~n", [[H | _] = "xyz"]),
    H = 120.                               % first char of "xyz"''',
        '''%% The format directive in depth
-module(fmt).
-export([run/0]).

run() ->
    io:format("~p~n", [{a, 1}]),     % ~p prints any term
    io:format("~w~n", [{a, 1}]),     % ~w prints without pretty-printing
    io:format("~b~n", [255]),        % ~b prints as decimal... use ~p
    io:format("~.2f~n", [3.14159]),  % 3.14
    io:format("~-10s|~n", ["left"]). % padded string''',
        '''%% Booleans and guards
-module(bools).
-export([run/0]).

run() ->
    io:format("~p~n", [true]),
    io:format("~p~n", [false]),
    io:format("~p~n", [1 < 2]),
    io:format("~p~n", [3 >= 3]),
    io:format("~p~n", [not false]),
    io:format("~p~n", [true and 1 < 2]).
%% true/false are atoms; comparisons work on any terms.''',
    ],
    3: [
        '''%% case expressions
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
    io:format("~s~n", [describe(-5)]).   % negative''',
        '''%% if expressions
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
%% The final `true ->` clause is the else.''',
        '''%% Pattern matching in function clauses
-module(fact).
-export([of/1]).

of(0) -> 1;
of(N) when N > 0 -> N * of(N - 1).

run() ->
    io:format("~p~n", [fact:of(5)]).   % 120
%% Clauses are tried top to bottom; first match wins.''',
        '''%% Guards: validating arguments
-module(guards).
-export([day_type/1]).

day_type(Day) when Day >= 1, Day =< 5 -> workday;
day_type(Day) when Day =:= 6; Day =:= 7 -> weekend;
day_type(_) -> invalid.

run() ->
    io:format("~p~n", [day_type(3)]),     % workday
    io:format("~p~n", [day_type(7)]),     % weekend
    io:format("~p~n", [day_type(0)]).     % invalid''',
    ],
    4: [
        '''%% Lists: the fundamental data structure
-module(lists_demo).
-export([run/0]).

run() ->
    L = [1, 2, 3],
    io:format("~p~n", [hd(L)]),        % 1
    io:format("~p~n", [tl(L)]),        % [2, 3]
    io:format("~p~n", [length(L)]),    % 3
    io:format("~p~n", [[0 | L]]),      % [0, 1, 2, 3]
    io:format("~p~n", [L ++ [4]]).     % [1, 2, 3, 4]''',
        '''%% List comprehension
-module(comps).
-export([run/0]).

run() ->
    Squares = [X * X || X <- [1, 2, 3, 4, 5]],
    io:format("~p~n", [Squares]),      % [1, 4, 9, 16, 25]
    Evens = [X || X <- [1, 2, 3, 4, 5, 6], X rem 2 =:= 0],
    io:format("~p~n", [Evens]).        % [2, 4, 6]''',
        '''%% The lists module
-module(lists_util).
-export([run/0]).

run() ->
    io:format("~p~n", [lists:map(fun(X) -> X * 2 end, [1, 2, 3])]),
    io:format("~p~n", [lists:filter(fun(X) -> X > 1 end, [1, 2, 3])]),
    io:format("~p~n", [lists:sum([1, 2, 3, 4])]),
    io:format("~p~n", [lists:reverse([1, 2, 3])]),
    io:format("~p~n", [lists:sort([3, 1, 2])]),
    io:format("~p~n", [lists:max([3, 9, 4])]).''',
        '''%% Fold (reduce) and foldl vs foldr
-module(folds).
-export([run/0]).

run() ->
    io:format("~p~n", [lists:foldl(fun(A, B) -> A + B end, 0, [1, 2, 3, 4])]),
    % 10
    io:format("~p~n", [lists:foldr(fun(A, B) -> [A | B] end, [], [1, 2, 3])]),
    % [1, 2, 3] — foldr processes right to left''',
    ],
    5: [
        '''%% Tuples: fixed-size containers
-module(tups).
-export([run/0]).

run() ->
    T = {ok, 42},
    io:format("~p~n", [element(1, T)]),   % ok
    io:format("~p~n", [element(2, T)]),   % 42
    io:format("~p~n", [setelement(2, T, 100)]),  % {ok, 100}
    io:format("~p~n", [tuple_size(T)]).   % 2''',
        '''%% The {ok, Value} / {error, Reason} convention
-module(div1).
-export([divide/2]).

divide(A, B) ->
    case B of
        0 -> {error, division_by_zero};
        _ -> {ok, A / B}
    end.

run() ->
    io:format("~p~n", [div1:divide(10, 2)]),   % {ok, 5.0}
    io:format("~p~n", [div1:divide(1, 0)]).    % {error, division_by_zero}''',
        '''%% Matching tuples in function heads
-module(result).
-export([handle/1]).

handle({ok, Value}) -> {result, Value};
handle({error, Reason}) -> {failure, Reason}.

run() ->
    io:format("~p~n", [result:handle({ok, 7})]),        % {result, 7}
    io:format("~p~n", [result:handle({error, timeout})]).
    % {failure, timeout}''',
        '''%% Records: named tuples
-module(users).
-export([run/0]).
-record(user, {name, age}).

run() ->
    U = #user{name = "Alice", age = 30},
    io:format("~p~n", [U#user.name]),        % "Alice"
    io:format("~p~n", [U#user.age]),         % 30
    U2 = U#user{age = 31},
    io:format("~p~n", [U2#user.age]).        % 31
%% Records are tuples with a tagged first element.''',
    ],
    6: [
        '''%% Pattern matching fundamentals
-module(match).
-export([run/0]).

run() ->
    {A, B} = {1, 2},          % match binds A=1, B=2
    [H | T] = [10, 20, 30],   % H=10, T=[20,30]
    io:format("~p ~p ~p ~p~n", [A, B, H, T]),
    io:format("~p~n", [1 + 1 =:= 2]).   % true — exact equality''',
        '''%% Matching in case with patterns
-module(matcher).
-export([check/1]).

check([]) -> empty;
check([_]) -> one;
check([_ | Rest]) -> {many, length(Rest) + 1}.

run() ->
    io:format("~p~n", [matcher:check([])]),        % empty
    io:format("~p~n", [matcher:check([42])]),      % one
    io:format("~p~n", [matcher:check([1, 2, 3])]). % {many, 3}''',
        '''%% Matching maps
-module(maps_demo).
-export([run/0]).

run() ->
    M = #{name => "Alice", age => 30},
    io:format("~p~n", [maps:get(name, M)]),      % "Alice"
    io:format("~p~n", [maps:get(age, M)]),       % 30
    io:format("~p~n", [maps:get(city, M, n/a)]), % n/a — default
    io:format("~p~n", [maps:keys(M)]),           % [age, name]
    #{age := Age} = M,
    io:format("~p~n", [Age]).                    % 30 — match syntax''',
        '''%% Pattern: transform with map/filter
-module(transform).
-export([run/0]).

run() ->
    Numbers = [1, 2, 3, 4, 5, 6],
    Doubled = [X * 2 || X <- Numbers],
    Evens = [X || X <- Numbers, X rem 2 =:= 0],
    io:format("~p~n", [Doubled]),   % [2, 4, 6, 8, 10, 12]
    io:format("~p~n", [Evens]).     % [2, 4, 6]''',
    ],
    7: [
        '''%% Recursion: the Erlang way to loop
-module(count).
-export([up_to/1]).

up_to(0) -> 0;
up_to(N) -> N + up_to(N - 1).

run() ->
    io:format("~p~n", [count:up_to(5)]).   % 15 (5+4+3+2+1+0)''',
        '''%% Tail-recursion with an accumulator
-module(sum).
-export([of/1]).

of(L) -> sum(L, 0).

sum([], Acc) -> Acc;
sum([H | T], Acc) -> sum(T, Acc + H).

run() ->
    io:format("~p~n", [sum:of([1, 2, 3, 4])]).   % 10
%% The recursive call is the last expression — tail call
%% optimized, so the stack never grows.''',
        '''%% Recursive list building
-module(evens).
-export([only/1]).

only(L) -> collect(L, []).

collect([], Acc) -> lists:reverse(Acc);
collect([H | T], Acc) when H rem 2 =:= 0 -> collect(T, [H | Acc]);
collect([_ | T], Acc) -> collect(T, Acc).

run() ->
    io:format("~p~n", [evens:only([1, 2, 3, 4, 5, 6])]).
    % [2, 4, 6] — reverse at the end keeps order''',
        '''%% The classic length with pattern matching
-module(len).
-export([of/1]).

of([]) -> 0;
of([_ | T]) -> 1 + of(T).

run() ->
    io:format("~p~n", [len:of([1, 2, 3])]).   % 3
%% Each step peels the head and recurses on the tail.''',
    ],
    8: [
        '''%% Anonymous functions (funs)
-module(funs).
-export([run/0]).

run() ->
    Double = fun(X) -> X * 2 end,
    io:format("~p~n", [Double(4)]),          % 8
    io:format("~p~n", [fun(X) -> X + 1 end(5)]),  % 6
    Add = fun(A, B) -> A + B end,
    io:format("~p~n", [Add(3, 4)]).          % 7''',
        '''%% Higher-order functions
-module(hof).
-export([run/0]).

run() ->
    ApplyTwice = fun(F, X) -> F(F(X)) end,
    Inc = fun(N) -> N + 1 end,
    io:format("~p~n", [ApplyTwice(Inc, 5)]),   % 7
    io:format("~p~n", [lists:map(fun(N) -> N * N end, [1, 2, 3])]).
    % [1, 4, 9]''',
        '''%% Function references: fun module:function/arity
-module(refs).
-export([run/0]).

run() ->
    io:format("~p~n", [lists:map(fun erlang:abs/1, [-1, 2, -3])]),
    % [1, 2, 3]
    io:format("~p~n", [lists:map(fun lists:reverse/1, [[1, 2], [3, 4]])]).
    % [[2, 1], [4, 3]]''',
        '''%% Closures: capturing the environment
-module(clos).
-export([make_add/1]).

make_add(N) -> fun(X) -> X + N end.

run() ->
    Add10 = clos:make_add(10),
    io:format("~p~n", [Add10(5)]),     % 15
    Add100 = clos:make_add(100),
    io:format("~p~n", [Add100(1)]).    % 101''',
    ],
    9: [
        '''%% The receive expression: message passing
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
    % Messages are sent with ! and received with receive.''',
        '''%% Send and receive with pattern matching
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
    % receive blocks until a matching message arrives''',
        '''%% Process identity and self()
-module(pids).
-export([run/0]).

run() ->
    Pid = self(),
    io:format("parent pid: ~p~n", [Pid]),
    Other = spawn(fun() ->
        io:format("child pid: ~p~n", [self()])
    end),
    io:format("spawned: ~p~n", [Other]).
    % Each process has a unique PID; Pid ! Msg targets it.''',
        '''%% Selective receive: matching specific messages
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
    % The first receive skips lows to find the high message.''',
    ],
    10: [
        '''%% Links: crash propagation between processes
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
    % spawn_link ties lifetimes; trapping exits catches them.''',
        '''%% Monitors: observe without coupling
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
    % Monitors send DOWN; links kill — monitors observe.''',
        '''%% try/catch: handling exceptions
-module(try_demo).
-export([run/0]).

run() ->
    try
        erlang:error(badarg)
    catch
        error:badarg -> io:format("caught badarg~n");
        _:Reason -> io:format("other: ~p~n", [Reason])
    end.
    % try/catch catches errors, exits, and throws.''',
        '''%% throw, error, and exit — the three exception classes
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
    % error -> for programmer errors, exit -> for process death''',
    ],
    11: [
        '''%% OTP: the Open Telecom Platform
-module(otp_intro).
-export([run/0]).

run() ->
    io:format("OTP provides: gen_server, supervisor, application~n"),
    io:format("gen_event, gen_statem, and the standard library~n"),
    io:format("Behaviours give you battle-tested skeletons.~n").
    % OTP is the Erlang runtime's standard library of patterns.''',
        '''%% gen_server: the core behaviour
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
    % handle_call is synchronous; handle_cast is fire-and-forget.''',
        '''%% Supervisors: restart on failure
-module(super_intro).
-export([run/0]).

run() ->
    io:format("A supervisor starts and monitors children.~n"),
    io:format("If a child crashes, the supervisor restarts it.~n"),
    io:format("Restart strategies: one_for_one, one_for_all,~n"),
    io:format("rest_for_one, and simple_one_for_one.~n").
    % The supervision tree is the core fault-tolerance model.''',
        '''%% Application: the OTP packaging unit
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
    % Applications bundle code, processes, and config together.''',
    ],
    12: [
        '''%% The process dictionary: thread-local storage
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
    % should live in gen_servers where it is visible.''',
        '''%% ets: the Erlang term store
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
    % ets tables are fast in-memory key-value stores.''',
        '''%% Parallel map with spawn
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
    % Each element runs in its own lightweight process.''',
        '''%% Timing and performance with timer
-module(timing).
-export([run/0]).

run() ->
    {Time, Result} = timer:tc(fun() ->
        lists:sum([X * X || X <- lists:seq(1, 1000)])
    end),
    io:format("result: ~p in ~p microseconds~n", [Result, Time]).
    % timer:tc/1 measures the execution time of a fun.''',
    ],
    13: [
        '''%% Maps: modern key-value store
-module(maps_more).
-export([run/0]).

run() ->
    M0 = #{a => 1, b => 2},
    M1 = maps:put(c, 3, M0),
    io:format("~p~n", [maps:size(M1)]),      % 3
    io:format("~p~n", [maps:is_key(a, M1)]), % true
    io:format("~p~n", [maps:remove(a, M1)]). % #{b => 2, c => 3}
    % Map updates return NEW maps; originals are untouched.''',
        '''%% Map update and merge
-module(map_updates).
-export([run/0]).

run() ->
    M = #{count => 0},
    io:format("~p~n", [maps:update(count, 10, M)]),   % #{count => 10}
    io:format("~p~n", [maps:update_with(count, fun(N) -> N + 1 end, M)]),
    % #{count => 1}
    io:format("~p~n", [maps:merge(#{a => 1}, #{b => 2})]).
    % #{a => 1, b => 2}''',
        '''%% Binary and bit syntax
-module(bins).
-export([run/0]).

run() ->
    <<A, B, C>> = <<1, 2, 3>>,
    io:format("~p ~p ~p~n", [A, B, C]),
    <<X:16>> = <<1, 0>>,           % 16-bit big-endian int
    io:format("~p~n", [X]),        % 256
    Bin = <<"hello">>,
    io:format("~p~n", [binary:part(Bin, 1, 3)]).
    % <<"ell">> — bit syntax slices binaries efficiently.''',
        '''%% Strings vs binaries: the modern choice
-module(str_bin).
-export([run/0]).

run() ->
    Bin = <<"hello">>,
    io:format("~p~n", [byte_size(Bin)]),        % 5
    io:format("~p~n", [binary:bin_to_list(Bin)]),
    % [104, 101, 108, 108, 111]
    io:format("~p~n", [unicode:characters_to_binary("héllo")]).
    % UTF-8 binary — binaries are the efficient string type.''',
    ],
    14: [
        '''%% OTP supervision tree structure
-module(tree).
-export([run/0]).

run() ->
    io:format("Application -> Supervisor -> Workers~n"),
    io:format("Workers: gen_server, gen_event, gen_statem~n"),
    io:format("Supervisors watch and restart their children.~n"),
    io:format("Crash isolation: one worker dying doesn't kill all.~n").
    % The tree is the backbone of fault-tolerant systems.''',
        '''%% A supervisor callback module
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
    % restart only on abnormal exit.''',
        '''%% Restart intensity and timing
-module(intensity).
-export([run/0]).

run() ->
    io:format("Max restarts in a window limits restart storms.~n"),
    io:format("{one_for_one, 5, 10} = 5 restarts in 10 seconds~n"),
    io:format("If exceeded, the supervisor itself shuts down.~n").
    % This prevents a crash loop from churning forever.''',
        '''%% Worker vs supervisor: the two roles
-module(roles).
-export([run/0]).

run() ->
    io:format("Workers: do the work, hold the state.~n"),
    io:format("Supervisors: manage workers, never do work.~n"),
    io:format("This separation gives clean crash isolation.~n").
    % A supervisor that does work can't reliably restart itself.''',
    ],
    15: [
        '''%% Basic pattern matching with binaries
-module(bin_match).
-export([run/0]).

run() ->
    <<"GET ", Path/binary>> = <<"GET /index.html">>,
    io:format("path: ~s~n", [Path]),
    <<Head:8, Rest/binary>> = <<1, 2, 3>>,
    io:format("~p ~p~n", [Head, Rest]).
    % Bit syntax can destructure binary data directly.''',
        '''%% Matching HTTP-like requests
-module(http_parse).
-export([parse/1]).

parse(Bin) ->
    case Bin of
        <<"GET ", Path/binary>> -> {get, binary_to_list(Path)};
        <<"POST ", Path/binary>> -> {post, binary_to_list(Path)};
        _ -> error
    end.

run() ->
    io:format("~p~n", [http_parse:parse(<<"GET /users">>)]),
    % {get, "/users"}
    io:format("~p~n", [http_parse:parse(<<"POST /login">>)]).
    % {post, "/login"}''',
        '''%% Building and splitting binaries
-module(bin_build).
-export([run/0]).

run() ->
    Version = 2,
    Name = "app",
    Bin = <<Name/binary, "-v", Version:8>>,
    io:format("~p~n", [Bin]),         % <<"app-v", 2>>
    io:format("~s~n", [Bin]),
    <<Prefix:3/binary, Suffix/binary>> = <<"abcdef">>,
    io:format("~s ~s~n", [Prefix, Suffix]).
    % "abc" "def" — slice with size patterns''',
        '''%% I/O from files
-module(io_demo).
-export([run/0]).

run() ->
    ok = file:write_file("/tmp/demo.txt", "hello file\\n"),
    {ok, Data} = file:read_file("/tmp/demo.txt"),
    io:format("read: ~s", [Data]),
    {ok, Lines} = file:consult("/tmp/nums.txt"),
    io:format("~p~n", [Lines]).
    % file:consult reads Erlang terms from a file.''',
    ],
    16: [
        '''%% Basic tests with EUnit
-module(calc_test).
-include_lib("eunit/include/eunit.hrl").

add_test() -> ?assertEqual(4, calc:add(2, 2)).

run() ->
    io:format("Run with: eunit:test(calc_test).~n").
    % EUnit auto-discovers functions ending in _test.''',
        '''%% EUnit assertions and generators
-module(feature_test).
-include_lib("eunit/include/eunit.hrl").

lists_test() ->
    ?assertEqual([2, 4], lists:map(fun(X) -> X * 2 end, [1, 2])),
    ?assert(lists:all(fun is_integer/1, [1, 2, 3])),
    ?assertError(badarith, 1 / 0).

run() ->
    io:format("assertEqual, assert, assertError and more.~n").
    % Test functions can be grouped with test generators.''',
        '''%% Common Test: integration testing
-module(feature_SUITE).
-include_lib("common_test/include/ct.hrl").
-export([all/0, simple/1]).

all() -> [simple].

simple(_Config) ->
    Result = 1 + 1,
    {comment, "1 + 1"} = {comment, "1 + 1"},
    Result = 2,
    ok.
    % Common Test is the full integration testing framework.''',
        '''%% The test-driven workflow
-module(tdd).
-export([run/0]).

run() ->
    io:format("1. Write a failing test (EUnit or CT).~n"),
    io:format("2. Run it: the test fails.~n"),
    io:format("3. Implement the module.~n"),
    io:format("4. Re-run: the test passes.~n"),
    io:format("5. Refactor and repeat.~n").
    % The compiler + test runner make TDD fast.''',
    ],
    17: [
        '''%% Code hot-loading: changing code at runtime
-module(hot).
-export([run/0]).

run() ->
    io:format("Erlang supports code reloading in production.~n"),
    io:format("Two versions of a module can coexist.~n"),
    io:format("Old calls finish; new calls use the new version.~n").
    % Hot upgrades power systems that run for years.''',
        '''%% Distributed Erlang: nodes and messages
-module(dist).
-export([run/0]).

run() ->
    io:format("Start nodes: erl -sname node1 -setcookie abc~n"),
    io:format("Connect: node1:net_adm:ping('node2@host').~n"),
    io:format("Message passing works across nodes seamlessly.~n"),
    io:format("spawn/4 and rpc:call/4 run code on remote nodes.~n").
    % Distribution is built into the runtime.''',
        '''%% Mnesia: the distributed database
-module(mnesia_intro).
-export([run/0]).

run() ->
    io:format("Mnesia is a distributed DBMS for Erlang.~n"),
    io:format("Tables can be in RAM, on disk, or both.~n"),
    io:format("Replication keeps copies across nodes.~n"),
    io:format("Transactions provide atomic updates.~n").
    % Mnesia integrates deeply with the runtime.''',
        '''%% Observability: tracing and logging
-module(obs).
-export([run/0]).

run() ->
    io:format("erlang:trace/3 captures process activity.~n"),
    io:format("logger is the standard logging API.~n"),
    io:format("observer:start() opens the GUI tool.~n"),
    io:format("recon provides production introspection.~n").
    % Observability is critical for long-running systems.''',
    ],
    18: [
        '''%% Lists: performance characteristics
-module(list_perf).
-export([run/0]).

run() ->
    io:format("Prepend ([X | L]) is O(1).~n"),
    io:format("Append (L ++ [X]) is O(N) — copy the left side.~n"),
    io:format("Access (lists:nth) is O(N).~n"),
    io:format("Build lists by prepending, reverse at the end.~n").
    % Lists are singly-linked; choose access patterns wisely.''',
        '''%% The classic accumulator pattern
-module(accum).
-export([run/0]).

run() ->
    L = build(5, []),
    io:format("~p~n", [L]),        % [5, 4, 3, 2, 1] — built by prepend
    io:format("~p~n", [lists:reverse(L)]).  % [1, 2, 3, 4, 5]

build(0, Acc) -> Acc;
build(N, Acc) -> build(N - 1, [N | Acc]).
    % Prepend then reverse is the idiomatic way to build lists.''',
        '''%% Efficient string handling
-module(eff_str).
-export([run/0]).

run() ->
    io:format("Binaries are compact and fast to copy.~n"),
    io:format("Binary syntax matches patterns without allocation.~n"),
    io:format("Strings as lists waste 8 bytes per char.~n"),
    io:format("Prefer <<\\"...\\">> binaries for text.~n").
    % Binaries use reference counting — cheap sharing.''',
        '''%% Timeouts and the after clause
-module(timeouts).
-export([run/0]).

run() ->
    Parent = self(),
    spawn(fun() -> timer:sleep(2000), Parent ! late end),
    receive
        Msg -> io:format("got ~p~n", [Msg])
    after 500 ->
        io:format("timed out after 500ms~n")
    end.
    % The after clause prevents infinite blocking.''',
    ],
    19: [
        '''%% Guard expressions reference
-module(guards_ref).
-export([run/0]).

run() ->
    io:format("is_integer/1, is_atom/1, is_list/1, is_map/1~n"),
    io:format("is_tuple/1, is_binary/1, is_boolean/1~n"),
    io:format("Comparisons: =:=, ==, <, >, =<, >=~n"),
    io:format("Composed with , (and) and ; (or).~n").
    % Guards are the only places allowed in function heads.''',
        '''%% Guard usage in depth
-module(guard_use).
-export([run/0]).

run() ->
    io:format("~p~n", [classify(42)]),    % integer
    io:format("~p~n", [classify("s")]),   % string
    io:format("~p~n", [classify(3.14)]).  % other

classify(X) when is_integer(X) -> integer;
classify(X) when is_list(X) -> string;
classify(_) -> other.
    % Each clause guards on the argument's type.''',
        '''%% Pattern matching vs guards: when to use each
-module(pat_vs_guard).
-export([run/0]).

run() ->
    io:format("Patterns match STRUCTURE (shape, binding).~n"),
    io:format("Guards test VALUES (types, comparisons).~n"),
    io:format("Use patterns to destructure, guards to filter.~n"),
    io:format("Combine them: [H | T] when H > 10 -> ...~n").
    % They compose: pattern first, guard second.''',
        '''%% The case of matching: expressions everywhere
-module(match_everywhere).
-export([run/0]).

run() ->
    Result = case {1, 2} of
        {A, B} when A < B -> {increasing, A, B};
        _ -> other
    end,
    io:format("~p~n", [Result]).
    % {increasing, 1, 2} — case is an expression returning a value.''',
    ],
    20: [
        '''%% A complete process-based pipeline
-module(pipeline).
-export([run/0]).

run() ->
    io:format("Chain processes with message passing:~n"),
    io:format("source -> filter -> sink~n"),
    io:format("Each stage is a process with a receive loop.~n"),
    io:format("Backpressure comes from receive blocking.~n").
    % Process pipelines are the classic Erlang architecture.''',
        '''%% A small worker pool
-module(pool).
-export([run/0]).

run() ->
    Parent = self(),
    [spawn(fun() -> Parent ! {result, X * 2} end) || X <- [1, 2, 3, 4]],
    Results = [receive {result, R} -> R end || _ <- [1, 2, 3, 4]],
    io:format("~p~n", [lists:sort(Results)]).
    % [2, 4, 6, 8] — gather results from concurrent workers.''',
        '''%% Building a mini in-memory cache
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
    % A stateful server in ~15 lines — the Erlang essence.''',
        '''%% The heartbeat pattern: monitoring health
-module(health).
-export([run/0]).

run() ->
    io:format("A process sends periodic heartbeats.~n"),
    io:format("A monitor watches for missed beats.~n"),
    io:format("Missing beats trigger a restart or alert.~n"),
    io:format("OTP supervisors handle this automatically.~n").
    % Health checks keep distributed systems self-healing.''',
    ],
    21: [
        '''%% GenServer call vs cast in depth
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
    % {q, count, n, 2} — casts are async, calls are sync.''',
        '''%% Timeouts in gen_server calls
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
    % Default call timeout is 5000ms.''',
        '''%% gen_statem: state machines as OTP
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
    % State machines handle complex protocols cleanly.''',
        '''%% The Erlang philosophy recap
-module(philosophy).
-export([run/0]).

run() ->
    io:format("Let it crash: isolate failures, restart, keep going.~n"),
    io:format("Everything is a process; communicate with messages.~n"),
    io:format("Immutable data + pattern matching = clarity.~n"),
    io:format("OTP behaviours encode decades of battle testing.~n").
    % Concurrency, fault-tolerance, and distribution built in.''',
    ],
}

LESSONS = [
    dict(slug='erlang-01-getting-started', title='Getting Started with Erlang',
         desc='Modules, exports, atoms, variables, and the Erlang shell.',
         dur='45 min', diff='beginner', prereq=[],
         objs=['Write and compile an Erlang module',
               'Explore with the Erlang shell',
               'Define and export functions',
               'Use atoms and single assignment'],
         refs=[dict(title='Erlang — Getting Started', url='https://www.erlang.org/doc/system/getting_started.html'),
               dict(title='Erlang — System Documentation', url='https://www.erlang.org/docs'),
               dict(title='Erlang — The Shell', url='https://www.erlang.org/doc/apps/erts/erl_cmd.html')]),
    dict(slug='erlang-02-values-types', title='Values and Types',
         desc='Numbers, strings as lists, format directives, and booleans.',
         dur='45 min', diff='beginner', prereq=['ERLANG-01'],
         objs=['Do integer and float arithmetic',
               'Manipulate strings and charlists',
               'Use io:format directives',
               'Understand booleans and comparisons'],
         refs=[dict(title='Erlang — Data Types', url='https://www.erlang.org/doc/reference_manual/data_types.html'),
               dict(title='Erlang — io:format directives', url='https://www.erlang.org/doc/apps/stdlib/io.html'),
               dict(title='Learn You Some Erlang — Types', url='https://learnyousomeerlang.com/syntax-in-functions')]),
    dict(slug='erlang-03-control-flow', title='Control Flow',
         desc='case, if, pattern-matched clauses, and guards.',
         dur='45 min', diff='beginner', prereq=['ERLANG-02'],
         objs=['Match with case expressions',
               'Use if expressions',
               'Write multi-clause functions',
               'Validate with guards'],
         refs=[dict(title='Erlang — Expressions (case/if)', url='https://www.erlang.org/doc/reference_manual/expressions.html#case'),
               dict(title='Erlang — Guards', url='https://www.erlang.org/doc/reference_manual/expressions.html#guards'),
               dict(title='Learn You Some Erlang — Functions', url='https://learnyousomeerlang.com/syntax-in-functions')]),
    dict(slug='erlang-04-lists', title='Lists and the Lists Module',
         desc='List fundamentals, comprehensions, and the lists library.',
         dur='60 min', diff='intermediate', prereq=['ERLANG-03'],
         objs=['Use hd, tl, and cons',
               'Write list comprehensions',
               'Use the lists module',
               'Fold with foldl and foldr'],
         refs=[dict(title='Erlang — Lists', url='https://www.erlang.org/doc/efficiency_guide/listHandling.html'),
               dict(title='Erlang — List Comprehensions', url='https://www.erlang.org/doc/programming_examples/list_comprehensions.html'),
               dict(title='Erlang — lists module', url='https://www.erlang.org/doc/apps/stdlib/lists.html')]),
    dict(slug='erlang-05-tuples-records', title='Tuples and Records',
         desc='Tuples, the ok/error convention, and records as named tuples.',
         dur='60 min', diff='intermediate', prereq=['ERLANG-04'],
         objs=['Build and access tuples',
               'Return ok/error results',
               'Match tuples in heads',
               'Define and use records'],
         refs=[dict(title='Erlang — Tuples', url='https://www.erlang.org/doc/reference_manual/data_types.html#tuple'),
               dict(title='Erlang — Records', url='https://www.erlang.org/doc/programming_examples/records.html'),
               dict(title='Learn You Some Erlang — Records', url='https://learnyousomeerlang.com/records')]),
    dict(slug='erlang-06-pattern-matching', title='Pattern Matching',
         desc='Matching, destructuring, map patterns, and transforms.',
         dur='60 min', diff='intermediate', prereq=['ERLANG-05'],
         objs=['Match values with =',
               'Match in case and heads',
               'Work with map patterns',
               'Transform with comprehensions'],
         refs=[dict(title='Erlang — Pattern Matching', url='https://www.erlang.org/doc/reference_manual/patterns.html'),
               dict(title='Erlang — Maps', url='https://www.erlang.org/doc/reference_manual/data_types.html#map'),
               dict(title='Learn You Some Erlang — Pattern Matching', url='https://learnyousomeerlang.com/syntax-in-functions')]),
    dict(slug='erlang-07-recursion', title='Recursion',
         desc='Recursive loops, tail calls, accumulators, and list building.',
         dur='60 min', diff='intermediate', prereq=['ERLANG-06'],
         objs=['Loop with recursion',
               'Use tail-recursive accumulators',
               'Build lists recursively',
               'Peel lists with patterns'],
         refs=[dict(title='Erlang — Recursion', url='https://www.erlang.org/doc/system/syntax.html'),
               dict(title='Learn You Some Erlang — Recursion', url='https://learnyousomeerlang.com/recursion'),
               dict(title='Erlang — Efficiency Guide (tail calls)', url='https://www.erlang.org/doc/efficiency_guide/functions.html')]),
    dict(slug='erlang-08-funs', title='Anonymous Functions and Funs',
         desc='Anonymous functions, higher-order functions, and closures.',
         dur='60 min', diff='intermediate', prereq=['ERLANG-07'],
         objs=['Write anonymous functions',
               'Pass functions to higher-order functions',
               'Reference module functions',
               'Capture environments in closures'],
         refs=[dict(title='Erlang — Funs', url='https://www.erlang.org/doc/reference_manual/expressions.html#fun'),
               dict(title='Erlang — Functional Programming', url='https://www.erlang.org/doc/system/fun.html'),
               dict(title='Learn You Some Erlang — Higher Order Functions', url='https://learnyousomeerlang.com/higher-order-functions')]),
    dict(slug='erlang-09-message-passing', title='Message Passing',
         desc='send/receive, PIDs, selective receive, and timeouts.',
         dur='75 min', diff='advanced', prereq=['ERLANG-08'],
         objs=['Send messages with !',
               'Receive with patterns',
               'Use self() and PIDs',
               'Match selectively with timeouts'],
         refs=[dict(title='Erlang — Processes', url='https://www.erlang.org/doc/reference_manual/processes.html'),
               dict(title='Erlang — receive', url='https://www.erlang.org/doc/reference_manual/expressions.html#receive'),
               dict(title='Learn You Some Erlang — Concurrency', url='https://learnyousomeerlang.com/the-hoe')]),
    dict(slug='erlang-10-fault-tolerance', title='Fault Tolerance',
         desc='Links, monitors, exits, and try/catch.',
         dur='75 min', diff='advanced', prereq=['ERLANG-09'],
         objs=['Link process lifetimes',
               'Monitor without coupling',
               'Catch exceptions',
               'Distinguish throw/error/exit'],
         refs=[dict(title='Erlang — Errors and Error Handling', url='https://www.erlang.org/doc/reference_manual/errors.html'),
               dict(title='Erlang — Links and Monitors', url='https://www.erlang.org/doc/reference_manual/processes.html#links'),
               dict(title='Learn You Some Erlang — Errors', url='https://learnyousomeerlang.com/errors-and-exceptions')]),
    dict(slug='erlang-11-otp', title='OTP Behaviours',
         desc='gen_server, supervisors, and applications.',
         dur='75 min', diff='advanced', prereq=['ERLANG-10'],
         objs=['Use gen_server',
               'Design supervisors',
               'Understand restart strategies',
               'Package applications'],
         refs=[dict(title='OTP Design Principles', url='https://www.erlang.org/doc/design_principles/des_prim.html'),
               dict(title='Erlang — gen_server', url='https://www.erlang.org/doc/apps/stdlib/gen_server.html'),
               dict(title='Learn You Some Erlang — OTP', url='https://learnyousomeerlang.com/clients-and-servers')]),
    dict(slug='erlang-12-concurrency', title='Concurrency Utilities',
         desc='Process dictionary, ets, parallel map, and timing.',
         dur='75 min', diff='advanced', prereq=['ERLANG-11'],
         objs=['Use the process dictionary',
               'Store data in ets',
               'Parallelize with spawn',
               'Measure with timer'],
         refs=[dict(title='Erlang — ets', url='https://www.erlang.org/doc/apps/stdlib/ets.html'),
               dict(title='Erlang — process dictionary', url='https://www.erlang.org/doc/efficiency_guide/processes.html'),
               dict(title='Erlang — timer module', url='https://www.erlang.org/doc/apps/stdlib/timer.html')]),
    dict(slug='erlang-13-maps-binaries', title='Maps and Binaries',
         desc='Maps, map updates, bit syntax, and binaries as strings.',
         dur='75 min', diff='advanced', prereq=['ERLANG-12'],
         objs=['Build and update maps',
               'Merge and update maps',
               'Use bit syntax',
               'Work with binary strings'],
         refs=[dict(title='Erlang — Maps', url='https://www.erlang.org/doc/reference_manual/data_types.html#map'),
               dict(title='Erlang — Bit Syntax', url='https://www.erlang.org/doc/programming_examples/bit_syntax.html'),
               dict(title='Erlang — binary module', url='https://www.erlang.org/doc/apps/stdlib/binary.html')]),
    dict(slug='erlang-14-supervision', title='Supervision Trees',
         desc='Tree structure, supervisor callbacks, restart intensity.',
         dur='75 min', diff='advanced', prereq=['ERLANG-13'],
         objs=['Structure supervision trees',
               'Write supervisor callbacks',
               'Tune restart intensity',
               'Separate workers and supervisors'],
         refs=[dict(title='OTP — Supervision', url='https://www.erlang.org/doc/design_principles/sup_princ.html'),
               dict(title='Erlang — supervisor module', url='https://www.erlang.org/doc/apps/stdlib/supervisor.html'),
               dict(title='Learn You Some Erlang — Supervisors', url='https://learnyousomeerlang.com/supervisors')]),
    dict(slug='erlang-15-binaries-io', title='Binaries and I/O',
         desc='Binary matching, request parsing, building, and files.',
         dur='75 min', diff='advanced', prereq=['ERLANG-14'],
         objs=['Match binary patterns',
               'Parse request-like data',
               'Build and split binaries',
               'Read and write files'],
         refs=[dict(title='Erlang — Bit Syntax', url='https://www.erlang.org/doc/programming_examples/bit_syntax.html'),
               dict(title='Erlang — file module', url='https://www.erlang.org/doc/apps/kernel/file.html'),
               dict(title='Learn You Some Erlang — Binaries', url='https://learnyousomeerlang.com/starting-out-for-real#binaries')]),
    dict(slug='erlang-16-testing', title='Testing',
         desc='EUnit, assertions, Common Test, and the TDD workflow.',
         dur='60 min', diff='intermediate', prereq=['ERLANG-15'],
         objs=['Write EUnit tests',
               'Use EUnit assertions',
               'Run Common Test suites',
               'Apply the TDD workflow'],
         refs=[dict(title='EUnit — User Guide', url='https://www.erlang.org/doc/apps/eunit/chapter.html'),
               dict(title='Common Test — User Guide', url='https://www.erlang.org/doc/apps/common_test/index.html'),
               dict(title='Erlang — eunit module', url='https://www.erlang.org/doc/apps/eunit/index.html')]),
    dict(slug='erlang-17-distribution', title='Distribution and Hot Code',
         desc='Hot code loading, distributed nodes, Mnesia, observability.',
         dur='75 min', diff='advanced', prereq=['ERLANG-16'],
         objs=['Explain code hot-loading',
               'Connect distributed nodes',
               'Use Mnesia',
               'Trace and observe'],
         refs=[dict(title='Erlang — Distribution', url='https://www.erlang.org/doc/reference_manual/distributed.html'),
               dict(title='Erlang — Mnesia', url='https://www.erlang.org/doc/apps/mnesia/index.html'),
               dict(title='Erlang — Release Handling', url='https://www.erlang.org/doc/design_principles/release_handling.html')]),
    dict(slug='erlang-18-performance', title='Performance',
         desc='List performance, accumulators, efficient strings, timeouts.',
         dur='75 min', diff='advanced', prereq=['ERLANG-17'],
         objs=['Choose list operations wisely',
               'Use the accumulator pattern',
               'Prefer binaries for strings',
               'Bound waits with timeouts'],
         refs=[dict(title='Erlang — Efficiency Guide', url='https://www.erlang.org/doc/efficiency_guide/introduction.html'),
               dict(title='Erlang — List Handling', url='https://www.erlang.org/doc/efficiency_guide/listHandling.html'),
               dict(title='Erlang — Process Efficiency', url='https://www.erlang.org/doc/efficiency_guide/processes.html')]),
    dict(slug='erlang-19-guards', title='Guards in Depth',
         desc='Guard reference, type guards, pattern vs guard, case everywhere.',
         dur='75 min', diff='advanced', prereq=['ERLANG-18'],
         objs=['Use guard functions',
               'Compose guard expressions',
               'Combine patterns and guards',
               'Use case as an expression'],
         refs=[dict(title='Erlang — Guards', url='https://www.erlang.org/doc/reference_manual/expressions.html#guards'),
               dict(title='Learn You Some Erlang — Guards', url='https://learnyousomeerlang.com/syntax-in-functions#guards!'),
               dict(title='Erlang — Built-in Functions', url='https://www.erlang.org/doc/reference_manual/functions.html')]),
    dict(slug='erlang-20-pipelines', title='Process Pipelines and Servers',
         desc='Process pipelines, worker pools, caches, health checks.',
         dur='75 min', diff='advanced', prereq=['ERLANG-19'],
         objs=['Chain process stages',
               'Build worker pools',
               'Implement a cache server',
               'Design heartbeat health'],
         refs=[dict(title='Erlang — Process patterns', url='https://learnyousomeerlang.com/the-hitchhikers-guide-to-concurrency'),
               dict(title='OTP — Design Principles', url='https://www.erlang.org/doc/design_principles/des_prim.html'),
               dict(title='Erlang — gen_server examples', url='https://www.erlang.org/doc/apps/stdlib/gen_server.html#gen_server-examples')]),
    dict(slug='erlang-21-advanced-otp', title='Advanced OTP',
         desc='Call vs cast, timeouts, gen_statem, and the philosophy.',
         dur='75 min', diff='expert', prereq=['ERLANG-20'],
         objs=['Use call and cast correctly',
               'Set call timeouts',
               'Model with gen_statem',
               'Apply the Erlang philosophy'],
         refs=[dict(title='Erlang — gen_statem', url='https://www.erlang.org/doc/apps/stdlib/gen_statem.html'),
               dict(title='Erlang — gen_server call timeouts', url='https://www.erlang.org/doc/apps/stdlib/gen_server.html#call/3'),
               dict(title='Erlang — Philosophy (FAQ)', url='https://www.erlang.org/faq/introduction.html')]),
]


if __name__ == '__main__':
    run_gen(LANGUAGE, 'erlang', LESSONS, CODE, BASE)
