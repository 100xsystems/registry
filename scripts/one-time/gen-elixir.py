#!/usr/bin/env python3
"""Generate the 21-lesson Elixir curriculum at Python/JS/Java depth.
Uses the shared gen_lib template. Exact refs from elixir-lang.org docs.
Each lesson has 4 sub-topics, each with its OWN distinct code sample.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import main as run_gen  # noqa: E402

LANGUAGE = 'elixir'

BASE = os.path.join(os.path.dirname(__file__), '..', '..', 'static-data', 'knowledge', 'languages', 'elixir')

CODE = {
    1: [
        '''# Your first Elixir program
defmodule Hello do
  def world do
    IO.puts("Hello, 100X Systems!")
  end
end

Hello.world()
# run: elixir hello.exs  ->  Hello, 100X Systems!''',
        '''# IEx interactive shell and basic expressions
# iex> 1 + 2
# 3
# iex> "Elixir" |> String.upcase()
# "ELIXIR"
IO.puts(Enum.map(1..5, &(&1 * &1)) |> Enum.join(", "))
# 1, 4, 9, 16, 25''',
        '''# Modules, functions, and the dot syntax
defmodule Math do
  def add(a, b), do: a + b
  def multiply(a, b), do: a * b
end

IO.puts(Math.add(3, 4))       # 7
IO.puts(Math.multiply(3, 4))  # 12''',
        '''# Pattern matching basics with =
{a, b, c} = {:ok, 42, "hello"}
IO.puts("#{a} #{b} #{c}")
# {:ok, 42, "hello"} destructured in one expression.
# The = operator is a match, not an assignment.''',
    ],
    2: [
        '''# Immutable values: rebinding vs mutation
x = 1
x = x + 1            # rebinding — a NEW binding, x is never mutated
IO.puts(x)           # 2

list = [1, 2, 3]
new_list = [0 | list]        # prepend, original untouched
IO.inspect(list)             # [1, 2, 3]
IO.inspect(new_list)         # [0, 1, 2, 3]
# Everything is immutable; "changes" produce new values.''',
        '''# Data types: atoms, strings, numbers, booleans
IO.inspect(:ok)                    # atom
IO.inspect("double quoted")        # binary string
IO.inspect('single quoted')        # charlist (list of codepoints)
IO.inspect(42)                     # integer
IO.inspect(3.14)                   # float
IO.inspect(true)                   # boolean (an atom)
IO.inspect(nil)                    # nil (an atom)
# Atoms are constants whose name is their value.''',
        '''# Arithmetic and division
IO.inspect(10 / 2)     # 5.0 — always returns a float
IO.inspect(div(10, 3)) # 3 — integer division
IO.inspect(rem(10, 3)) # 1 — remainder
IO.inspect(10 ** 2)    # 100 — exponentiation''',
        '''# String basics: interpolation and concatenation
name = "Elixir"
IO.puts("Hello, #{name}!")        # interpolation
IO.puts("a" <> "b")               # concatenation -> "ab"
IO.puts(String.length("héllo"))   # 5 — counts graphemes
IO.puts(String.upcase("hello"))   # HELLO
# Strings are UTF-8 binaries, not arrays of bytes.''',
    ],
    3: [
        '''# case: pattern matching with guards
defmodule Describe do
  def of(x) do
    case x do
      0 -> "zero"
      n when n < 0 -> "negative"
      n when n > 0 -> "positive"
      _ -> "unknown"
    end
  end
end

IO.puts(Describe.of(-5))  # negative''',
        '''# cond: the else-if chain
defmodule Rating do
  def label(score) do
    cond do
      score >= 90 -> "excellent"
      score >= 70 -> "good"
      score >= 50 -> "fair"
      true -> "poor"
    end
  end
end

IO.puts(Rating.label(85))  # good''',
        '''# if / unless
if true do
  IO.puts("if runs")
end

unless false do
  IO.puts("unless runs when false")
end

# if is a macro returning a value:
result = if 1 + 1 == 2, do: "math works", else: "broken"
IO.puts(result)''',
        '''# Multiple function clauses via pattern matching
defmodule Fact do
  def of(0), do: 1
  def of(n) when n > 0, do: n * of(n - 1)
end

IO.puts(Fact.of(5))   # 120
# The first matching clause wins — no if/else needed.''',
    ],
    4: [
        '''# Enum: the bread-and-butter of collections
IO.inspect(Enum.map([1, 2, 3], &(&1 * 2)))        # [2, 4, 6]
IO.inspect(Enum.filter([1, 2, 3, 4], &(&1 > 2)))  # [3, 4]
IO.inspect(Enum.reduce([1, 2, 3], 0, &(&1 + &2))) # 6
IO.inspect(Enum.sum([1, 2, 3]))                   # 6''',
        '''# List operations
list = [3, 1, 2]
IO.inspect(Enum.sort(list))            # [1, 2, 3]
IO.inspect(Enum.reverse(list))         # [2, 1, 3]
IO.inspect(Enum.max(list))             # 3
IO.inspect(Enum.min(list))             # 1
IO.inspect(length(list))               # 3
IO.inspect([1, 2] ++ [3, 4])           # [1, 2, 3, 4]
IO.inspect([1, 2, 3] -- [2])           # [1, 3]''',
        '''# Map operations
m = %{name: "Alice", age: 30}
IO.inspect(m[:name])           # Alice — access syntax
IO.inspect(Map.get(m, :age))   # 30
m2 = Map.put(m, :city, "NYC")  # new map, m unchanged
IO.inspect(Map.keys(m2))       # [:name, :age, :city]
IO.inspect(Map.has_key?(m, :name))  # true''',
        '''# Comprehensions
squares = for n <- 1..5, do: n * n
IO.inspect(squares)   # [1, 4, 9, 16, 25]

even_squares = for n <- 1..10, rem(n, 2) == 0, do: n * n
IO.inspect(even_squares)  # [4, 16, 36, 64, 100]

pairs = for a <- [1, 2], b <- ["x", "y"], do: {a, b}
IO.inspect(pairs)
# [{1, "x"}, {1, "y"}, {2, "x"}, {2, "y"}]''',
    ],
    5: [
        '''# Anonymous functions and capture syntax
double = fn x -> x * 2 end
IO.puts(double.(4))            # 8 — note the dot for calling

square = &(&1 * &1)
IO.puts(square.(5))            # 25

# Pipes compose functions left to right:
result = 1..10
  |> Enum.map(&(&1 * &1))
  |> Enum.filter(&(&1 > 20))
  |> Enum.sum()
IO.puts(result)   # 4+9+16+25+36+49+64+81+100 = 384''',
        '''# Higher-order functions: passing functions around
add_one = &(&1 + 1)
IO.inspect(Enum.map([1, 2, 3], add_one))   # [2, 3, 4]

apply_twice = fn f, x -> f.(f.(x)) end
IO.puts(apply_twice.(add_one, 5))          # 7''',
        '''# Closures capture their environment
defmodule Counter do
  def make(start) do
    fn -> start end
  end
end

get = Counter.make(100)
IO.puts(get.())     # 100 — the closure keeps start alive

# A counter that captures and returns a tuple:
make_counter = fn ->
  count = 0
  fn -> count = count + 1; count end
end
# (In Elixir, rebinding inside the closure creates a new
#  binding each call — use Agent/Process for real state.)''',
        '''# Function composition with the pipe operator
defmodule Pipe do
  def run do
    42
    |> Integer.to_string()
    |> String.reverse()
    |> String.to_integer()
  end
end

IO.puts(Pipe.run())  # 24
# The pipe threads the previous result as the first arg.''',
    ],
    6: [
        '''# Recursion: the Elixir way to loop
defmodule Count do
  def up_to(0), do: 0
  def up_to(n), do: n + up_to(n - 1)
end

IO.puts(Count.up_to(5))   # 15 (5+4+3+2+1+0)''',
        '''# Tail-call recursion with an accumulator
defmodule Sum do
  def of(list), do: do_sum(list, 0)
  defp do_sum([], acc), do: acc
  defp do_sum([h | t], acc), do: do_sum(t, acc + h)
end

IO.puts(Sum.of([1, 2, 3, 4]))   # 10
# The recursive call is the LAST thing evaluated — tail call
# optimized, so deep recursion never blows the stack.''',
        '''# Recursing over linked lists
defmodule Len do
  def of([]), do: 0
  def of([_h | t]), do: 1 + Len.of(t)
end

IO.puts(Len.of([1, 2, 3]))   # 3
# Each step peels off the head; the tail is the rest.''',
        '''# List recursion building results
defmodule Evens do
  def only(list), do: collect(list, [])
  defp collect([], acc), do: Enum.reverse(acc)
  defp collect([h | t], acc) when rem(h, 2) == 0,
    do: collect(t, [h | acc])
  defp collect([_h | t], acc), do: collect(t, acc)
end

IO.inspect(Evens.only([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]''',
    ],
    7: [
        '''# Tuples: fixed-size containers
t = {:ok, 42}
IO.inspect(elem(t, 0))    # :ok
IO.inspect(elem(t, 1))    # 42
t2 = put_elem(t, 1, 100)
IO.inspect(t2)            # {:ok, 100}
IO.inspect(tuple_size(t)) # 2''',
        '''# The {:ok, result} / {:error, reason} convention
defmodule Div do
  def divide(a, b) do
    if b == 0 do
      {:error, "division by zero"}
    else
      {:ok, a / b}
    end
  end
end

case Div.divide(10, 2) do
  {:ok, v} -> IO.puts("result: #{v}")
  {:error, msg} -> IO.puts("error: #{msg}")
end''',
        '''# Pattern matching tuples with case
defmodule Result do
  def handle({:ok, value}), do: "ok: #{value}"
  def handle({:error, reason}), do: "error: #{reason}"
end

IO.puts(Result.handle({:ok, 7}))      # ok: 7
IO.puts(Result.handle({:error, :oops})) # error: oops''',
        '''# Structs: maps with a shape
defmodule User do
  defstruct [:name, :age, :city]
end

u = %User{name: "Alice", age: 30}
IO.inspect(u.name)              # "Alice"
u2 = %{u | age: 31}             # update syntax
IO.inspect(u2.age)              # 31
IO.inspect(u.age)               # 30 — original unchanged
# Structs enforce their keys and provide defaults.''',
    ],
    8: [
        '''# Keyword lists: two-element tuples, ordered, duplicates allowed
kw = [name: "Alice", age: 30]
IO.inspect(kw[:name])        # "Alice"
IO.inspect(kw[:age])         # 30
kw2 = [name: "Bob", name: "Charlie"]  # duplicates allowed
IO.inspect(kw2[:name])       # "Bob" — first match
# Keyword lists are just [name: "Alice"] == [{:name, "Alice"}]''',
        '''# Keyword list operations
kw = [a: 1, b: 2]
IO.inspect(Keyword.get(kw, :a))      # 1
IO.inspect(Keyword.get(kw, :z, 99))  # 99 — default
IO.inspect(Keyword.put(kw, :c, 3))   # [a: 1, b: 2, c: 3]
IO.inspect(Keyword.keys(kw))         # [:a, :b]
IO.inspect(Keyword.values(kw))       # [1, 2]
IO.inspect(Keyword.has_key?(kw, :b)) # true''',
        '''# Maps vs keyword lists: when to use which
map = %{name: "Alice", age: 30}        # unordered, unique keys
IO.inspect(map.name)                   # dot access
IO.inspect(map[:name])                 # bracket access
IO.inspect(Map.fetch(map, :age))       # {:ok, 30}
IO.inspect(Map.fetch(map, :nope))      # :error
# Use maps for large/lookup-heavy data; keywords for options.''',
        '''# Sets
set = MapSet.new([1, 2, 3])
IO.inspect(MapSet.member?(set, 2))   # true
IO.inspect(MapSet.size(set))         # 3
set2 = MapSet.new([3, 4, 5])
IO.inspect(MapSet.union(set, set2))  # MapSet.new([1, 2, 3, 4, 5])
IO.inspect(MapSet.intersection(set, set2))  # MapSet.new([3])
IO.inspect(MapSet.difference(set, set2))    # MapSet.new([1, 2])''',
    ],
    9: [
        '''# Pattern matching in function heads
defmodule Greet do
  def hello(%{name: name}), do: "Hello, #{name}!"
  def hello(_), do: "Hello, stranger!"
end

IO.puts(Greet.hello(%{name: "Alice"}))   # Hello, Alice!
IO.puts(Greet.hello(%{}))                # Hello, stranger!''',
        '''# Guards: validating function arguments
defmodule Age do
  def classify(n) when is_integer(n) and n >= 18, do: "adult"
  def classify(n) when is_integer(n), do: "minor"
  def classify(_), do: "not a number"
end

IO.puts(Age.classify(21))   # adult
IO.puts(Age.classify(10))   # minor
IO.puts(Age.classify("x"))  # not a number''',
        '''# Pinning with ^: matching existing values
x = 10
case 10 do
  ^x -> "matches the pinned value"
  _ -> "no match"
end
# Without ^, x would be REBOUND inside the clause.''',
        '''# Match on list shapes
defmodule Listy do
  def describe([]), do: "empty"
  def describe([x]), do: "one element: #{x}"
  def describe([x | rest]), do: "#{x} plus #{length(rest)} more"
end

IO.puts(Listy.describe([]))          # empty
IO.puts(Listy.describe([42]))        # one element: 42
IO.puts(Listy.describe([1, 2, 3]))   # 1 plus 2 more''',
    ],
    10: [
        '''# try/rescue: handling exceptions (rare in Elixir)
defmodule Safe do
  def divide(a, b) do
    try do
      {:ok, a / b}
    rescue
      ArithmeticError -> {:error, "division by zero"}
    end
  end
end

IO.inspect(Safe.divide(1, 0))  # {:error, "division by zero"}''',
        '''# The Elixir philosophy: errors are values, not exceptions
defmodule Parse do
  def to_int(str) do
    case Integer.parse(str) do
      {n, _} -> {:ok, n}
      :error -> {:error, "not an integer"}
    end
  end
end

IO.inspect(Parse.to_int("42"))     # {:ok, 42}
IO.inspect(Parse.to_int("abc"))    # {:error, "not an integer"}
# Handle errors at the boundary; let the happy path flow.''',
        '''# raise and the bang functions
defmodule Db do
  def connect!(url) do
    if url == "" do
      raise ArgumentError, "empty url"
    end
    :connected
  end
end

IO.puts(Db.connect!("postgres://localhost/db"))
# Db.connect!("") would raise.
# The ! convention marks functions that raise on failure.''',
        '''# Error handling with with: early-exit pipelines
defmodule Flow do
  def run do
    with {:ok, a} <- step1(),
         {:ok, b} <- step2(a) do
      {:ok, a + b}
    else
      {:error, reason} -> {:error, reason}
    end
  end

  defp step1, do: {:ok, 10}
  defp step2(x), do: {:ok, x * 2}
end

IO.inspect(Flow.run())  # {:ok, 30}
# with stops at the first non-matching clause.''',
    ],
    11: [
        '''# Processes: lightweight concurrency
pid = spawn(fn -> IO.puts("I am process #{inspect(self())}") end)
IO.puts("parent: #{inspect(self())}")
IO.puts("child: #{inspect(pid)}")
# Each spawn creates an isolated, independent process.''',
        '''# Send and receive: message passing
parent = self()

spawn(fn ->
  send(parent, {:hello, "from child"})
end)

receive do
  {:hello, msg} -> IO.puts("got: #{msg}")
after
  1000 -> IO.puts("timeout")
end
# Message passing is THE concurrency primitive in Elixir.''',
        '''# Process state with recursion (a mini Agent)
defmodule Counter do
  def start(initial) do
    spawn(fn -> loop(initial) end)
  end

  defp loop(count) do
    receive do
      {:get, caller} ->
        send(caller, count)
        loop(count)
      {:inc} ->
        loop(count + 1)
    end
  end
end

pid = Counter.start(5)
send(pid, {:inc})
send(pid, {:get, self()})
receive do
  n -> IO.puts("count is #{n}")   # 6
end''',
        '''# Linking and monitoring processes
# spawn_link crashes the parent if the child crashes:
parent = self()
spawn_link(fn -> raise "child boom" end)

receive do
  {:EXIT, _pid, reason} -> IO.puts("child died: #{inspect(reason)}")
after
  500 -> IO.puts("no exit message")
end
# Links propagate crashes; monitors observe without dying.''',
    ],
    12: [
        '''# Agent: shared state with a simple API
{:ok, agent} = Agent.start_link(fn -> 0 end)
Agent.update(agent, fn count -> count + 1 end)
Agent.update(agent, fn count -> count + 1 end)
IO.puts(Agent.get(agent, fn count -> count end))  # 2''',
        '''# Task: one-off asynchronous work
task = Task.async(fn ->
  Process.sleep(100)
  21 * 2
end)

IO.puts("doing other work...")
result = Task.await(task, 1000)
IO.puts(result)   # 42
# Task.async/await is the simplest parallel abstraction.''',
        '''# Task with error handling
task = Task.async(fn -> {:ok, 1 + 1} end)

case Task.yield(task, 1000) || Task.shutdown(task) do
  {:ok, {:ok, value}} -> IO.puts("value: #{value}")
  _ -> IO.puts("task failed or timed out")
end''',
        '''# GenServer: the core OTP behaviour
defmodule Bank do
  use GenServer

  def start_link(balance) do
    GenServer.start_link(__MODULE__, balance, name: __MODULE__)
  end

  def balance, do: GenServer.call(__MODULE__, :balance)
  def deposit(amount), do: GenServer.call(__MODULE__, {:deposit, amount})

  @impl true
  def init(balance), do: {:ok, balance}

  @impl true
  def handle_call(:balance, _from, bal), do: {:reply, bal, bal}

  @impl true
  def handle_call({:deposit, amt}, _from, bal),
    do: {:reply, :ok, bal + amt}
end

Bank.start_link(100)
Bank.deposit(50)
IO.puts(Bank.balance())   # 150''',
    ],
    13: [
        '''# Streams: lazy, composable enumerables
stream = 1..10_000_000
  |> Stream.map(&(&1 * &1))
  |> Stream.filter(&(&1 > 1_000_000))

IO.inspect(Enum.take(stream, 3))   # [1002001, 1008016, 1014049]
# Streams compute on demand — no intermediate lists.''',
        '''# Streams for infinite data
natural = Stream.iterate(1, &(&1 + 1))
IO.inspect(Enum.take(natural, 5))   # [1, 2, 3, 4, 5]

# Fibonacci as a stream:
fibs = Stream.unfold({0, 1}, fn {a, b} -> {a, {b, a + b}} end)
IO.inspect(Enum.take(fibs, 8))      # [0, 1, 1, 2, 3, 5, 8, 13]''',
        '''# Stream.cycle and Stream.repeatedly
cycled = Stream.cycle(["a", "b"])
IO.inspect(Enum.take(cycled, 5))   # ["a", "b", "a", "b", "a"]

repeated = Stream.repeatedly(fn -> :rand.uniform(100) end)
IO.inspect(Enum.take(repeated, 3))  # three random numbers''',
        '''# Streaming file processing
# Reads lines lazily from a file, transforms, writes out:
result =
  "data.txt"
  |> File.stream!()
  |> Stream.map(&String.trim/1)
  |> Stream.reject(&(&1 == ""))
  |> Enum.count()

IO.puts("non-empty lines: #{result}")
# Without Stream, the whole file would load into memory.''',
    ],
    14: [
        '''# The pipe operator: read it left to right
"hello world"
|> String.split()
|> Enum.map(&String.capitalize/1)
|> Enum.join(" ")
|> IO.puts()
# Hello World''',
        '''# Pipes with function capture and args
[1, 2, 3, 4]
|> Enum.filter(&(&1 > 2))
|> Enum.map(&(&1 * 10))
|> Enum.join(",")
|> IO.puts()
# 30,40''',
        '''# Captures: &(&1 + 1) shorthand
add = &(&1 + &1)
IO.puts(add.(3))            # 6

# Named function capture with arity:
mapped = Enum.map([1, 2, 3], &Integer.to_string/1)
IO.inspect(mapped)          # ["1", "2", "3"]''',
        '''# Operator as function captures
IO.inspect(Enum.reduce([1, 2, 3], 0, &+/2))    # 6
IO.inspect(Enum.reduce([1, 2, 3], 1, &*/2))    # 6
IO.inspect(Enum.sort([3, 1, 2], &>=/2))        # [3, 2, 1]
# &+/2 captures the + operator as a two-arg function.''',
    ],
    15: [
        '''# Modules, public/private functions
defmodule Calc do
  def add(a, b), do: a + b        # public
  defp secret, do: :hidden        # private

  def double(x), do: x * 2
end

IO.puts(Calc.add(2, 3))
IO.puts(Calc.double(4))
# Calc.secret() would raise UndefinedFunctionError.''',
        '''# Function default arguments
defmodule Greet do
  def hello(name, greeting \\ "Hello") do
    "#{greeting}, #{name}!"
  end
end

IO.puts(Greet.hello("Alice"))            # Hello, Alice!
IO.puts(Greet.hello("Bob", "Hey"))       # Hey, Bob!
# Defaults must be defined in a header clause.''',
        '''# Multi-clause functions with different arities
defmodule Shape do
  def area({:square, s}), do: s * s
  def area({:rect, w, h}), do: w * h
  def area({:circle, r}), do: 3.14159 * r * r
end

IO.puts(Shape.area({:square, 4}))   # 16
IO.puts(Shape.area({:circle, 2}))   # 12.56636''',
        '''# Import, alias, and require
import Enum, only: [map: 2, sum: 1]
alias MyApp.Utils.Helper, as: H

IO.inspect(map([1, 2], &(&1 * 2)))   # [2, 4]
IO.inspect(sum([1, 2, 3]))           # 6

# Aliasing lets you reference H instead of the full name.''',
    ],
    16: [
        '''# Protocols: polymorphism without inheritance
defprotocol Size do
  def size(data)
end

defimpl Size, for: List do
  def size(list), do: length(list)
end

defimpl Size, for: Map do
  def size(map), do: map_size(map)
end

defimpl Size, for: BitString do
  def size(str), do: String.length(str)
end

IO.puts(Size.size([1, 2, 3]))    # 3
IO.puts(Size.size(%{a: 1}))      # 1
IO.puts(Size.size("hello"))      # 5
# Protocols dispatch on the data type.''',
        '''# Implementing a protocol for your own struct
defprotocol Greet do
  def hello(entity)
end

defmodule Human do
  defstruct [:name]
end

defimpl Greet, for: Human do
  def hello(%Human{name: n}), do: "Hello, #{n}!"
end

IO.puts(Greet.hello(%Human{name: "Alice"}))
# New types can implement the protocol without editing it.''',
        '''# Behaviours: interfaces for modules
defmodule Worker do
  @callback perform(args :: term) :: term
  @optional_callbacks perform: 1
end

defmodule MyWorker do
  @behaviour Worker

  @impl Worker
  def perform(input), do: {:processed, input}
end

IO.inspect(MyWorker.perform(:data))
# @impl raises a warning if the callback signature drifts.''',
        '''# The String.Chars protocol: to_string
IO.puts(to_string(42))          # "42"
IO.puts("#{42}")                # uses String.Chars

defmodule Point do
  defstruct [:x, :y]
  defimpl String.Chars do
    def to_string(%Point{x: x, y: y}), do: "Point(#{x}, #{y})"
  end
end

IO.puts("#{struct(Point, x: 1, y: 2)}")   # Point(1, 2)''',
    ],
    17: [
        '''# Mix: the project tool
# mix new my_app        -> creates a project scaffold
# mix run               -> runs the app
# mix test              -> runs tests
# mix deps.get          -> fetches dependencies
# mix format            -> formats code (elixir formatter)
# mix compile           -> compiles
IO.puts("Mix manages projects, deps, tests, and releases")''',
        '''# Dependencies in mix.exs
defmodule MyApp.MixProject do
  use Mix.Project

  def project do
    [
      app: :my_app,
      version: "0.1.0",
      elixir: "~> 1.16",
      deps: deps()
    ]
  end

  defp deps do
    [
      {:jason, "~> 1.4"},
      {:plug, "~> 1.15"}
    ]
  end
end

IO.puts("deps defined in mix.exs, fetched with mix deps.get")''',
        '''# ExUnit: testing
defmodule CalcTest do
  use ExUnit.Case, async: true

  test "addition" do
    assert 2 + 2 == 4
  end

  test "raises on invalid" do
    assert_raise ArgumentError, fn -> raise ArgumentError end
  end
end

# Run with: mix test
IO.puts("ExUnit is built into Elixir")''',
        '''# doctest: documentation as tests
defmodule Math do
  @doc """
  Adds two numbers.

      iex> Math.add(2, 3)
      5
  """
  def add(a, b), do: a + b
end

# mix test runs the iex> examples automatically.
IO.puts("doctests verify documentation examples")''',
    ],
    18: [
        '''# The @moduledoc and @doc attributes
defmodule Docs do
  @moduledoc "The Docs module explains documentation."

  @doc """
  Returns the double of a number.

  ## Examples
      iex> Docs.double(21)
      42
  """
  def double(x), do: x * 2
end

IO.puts(Docs.double(21))   # 42
# Documentation is a first-class citizen in Elixir.''',
        '''# Module attributes as constants
defmodule Config do
  @app_name "MyApp"
  @version "1.0.0"

  def app_name, do: @app_name
  def version, do: @version
end

IO.puts(Config.app_name())
IO.puts(Config.version())
# Attributes are compile-time constants.''',
        '''# Module attributes accumulated (pattern)
defmodule Routes do
  # Register the attribute so assignments accumulate
  Module.register_attribute(__MODULE__, :routes, accumulate: true)

  @routes {:get, "/"}
  @routes {:get, "/about"}
  @routes {:post, "/submit"}

  def all_routes do
    @routes   # accumulated in reverse order of definition
  end
end

IO.inspect(Routes.all_routes())
# [{:post, "/submit"}, {:get, "/about"}, {:get, "/"}]''',
        '''# Code organisation: apps and umbrella projects
# A typical layout:
#   lib/
#     my_app.ex
#     my_app/
#       application.ex
#       supervisor.ex
#   test/
#     my_app_test.exs
#   mix.exs
IO.puts("lib/ holds source; test/ holds tests")
# Umbrella projects group multiple apps with shared boundaries.''',
    ],
    19: [
        '''# OTP: the library that made Erlang famous
# OTP = Open Telecom Platform: behaviours, supervision, distribution
# Core behaviours: GenServer, Supervisor, Application, Task, Agent
IO.puts("OTP provides fault-tolerant building blocks")
IO.puts("GenServer   -> stateful servers")
IO.puts("Supervisor  -> restarts children on crash")''',
        '''# Supervision tree: restart on failure
defmodule MyApp do
  use Application

  def start(_type, _args) do
    children = [
      {Bank, 100},
      {Task.Supervisor, name: MyApp.TaskSupervisor}
    ]

    opts = [strategy: :one_for_one, name: MyApp.Supervisor]
    Supervisor.start_link(children, opts)
  end
end

IO.puts("Supervisors declare children and restart strategies")
# one_for_one restarts only the crashed child.''',
        '''# Supervisor restart strategies
# :one_for_one    - restart only the crashed child
# :one_for_all    - restart all children
# :rest_for_one   - restart the crashed child and those after it
IO.puts("Choosing the strategy controls blast radius")
IO.puts("one_for_one is the default and most common")''',
        '''# Application callbacks
defmodule ConfigApp do
  use Application

  @impl true
  def start(_type, _args) do
    IO.puts("application starting")
    # Return a supervisor spec:
    Supervisor.start_link([], strategy: :one_for_one)
  end
end

IO.puts("The Application behaviour defines the app lifecycle")
# mix run starts the application; config/ sets environment.''',
    ],
    20: [
        '''# The |> pipeline in real code
defmodule TextStats do
  def analyze(text) do
    text
    |> String.split()
    |> Enum.map(&String.downcase/1)
    |> Enum.frequencies()
    |> Enum.max_by(fn {_w, c} -> c end)
  end
end

IO.inspect(TextStats.analyze("the quick the brown the fox"))
# {"the", 3}''',
        '''# Building a small CLI-ish pipeline
defmodule WordCounter do
  def run(lines) do
    lines
    |> Enum.flat_map(&String.split/1)
    |> Enum.reduce(%{}, fn word, acc ->
      Map.update(acc, word, 1, &(&1 + 1))
    end)
    |> Enum.sort_by(fn {_w, c} -> -c end)
    |> Enum.take(3)
  end
end

IO.inspect(WordCounter.run(["hi ho", "hi again", "hi"]))
# [{"hi", 3}, {"ho", 1}, {"again", 1}]''',
        '''# Pattern: data transformation pipeline with structs
defmodule Order do
  defstruct [:id, :total]
end

orders = [
  %Order{id: 1, total: 100},
  %Order{id: 2, total: 50},
  %Order{id: 3, total: 200}
]

total =
  orders
  |> Enum.map(& &1.total)
  |> Enum.sum()

IO.puts("order total: #{total}")   # 350''',
        '''# Guarding pipelines with Enum.reduce
defmodule RunningMax do
  def over(list) do
    list
    |> Enum.reduce(0, fn x, acc -> max(x, acc) end)
  end
end

IO.puts(RunningMax.over([3, 9, 4, 11, 2]))   # 11
# reduce threads an accumulator through the whole list.''',
    ],
    21: [
        '''# Metaprogramming: macros intro
defmodule MyMacros do
  defmacro unless_else(condition, do: block, else: else_block) do
    quote do
      if !unquote(condition) do
        unquote(block)
      else
        unquote(else_block)
      end
    end
  end
end

defmodule Demo do
  import MyMacros

  def run do
    unless_else false do
      IO.puts("false branch runs")
    else
      IO.puts("true branch")
    end
  end
end

Demo.run()
# Macros transform code at compile time.''',
        '''# quote and unquote
IO.inspect(quote do: 1 + 2)
# {:+, [context: Elixir, import: Kernel], [1, 2]}

# unquote injects values into quoted expressions:
x = 42
IO.inspect(quote do: x)
# {:x, [context: Elixir, import: Kernel], nil}
# (x refers to the variable, not its value)
IO.inspect(quote do: unquote(x))
# 42 — the value is inlined''',
        '''# Ecto: database access and queries
# defmodule Post do
#   use Ecto.Schema
#   schema "posts" do
#     field :title, :string
#     field :views, :integer, default: 0
#   end
# end
#
# Repo.get!(Post, 1)
# Repo.all(from p in Post, where: p.views > 100)
IO.puts("Ecto provides schemas, queries, and changesets")''',
        '''# Phoenix: the web framework
# mix phx.new my_app
# mix phx.server
# defmodule MyAppWeb.PageController do
#   use MyAppWeb, :controller
#   def index(conn, _params) do
#     render(conn, "index.html")
#   end
# end
IO.puts("Phoenix: channels, live view, and the web layer")
IO.puts("The Elixir ecosystem: Ecto + Phoenix + OTP")''',
    ],
}

LESSONS = [
    dict(slug='elixir-01-getting-started', title='Getting Started with Elixir',
         desc='Installation, IEx, modules, functions, and pattern matching basics.',
         dur='45 min', diff='beginner', prereq=[],
         objs=['Write and run your first Elixir program',
               'Explore interactively with IEx',
               'Define modules and functions',
               'Match values with the = operator'],
         refs=[dict(title='Elixir — Getting Started', url='https://elixir-lang.org/getting-started/introduction.html'),
               dict(title='Elixir — Installation', url='https://elixir-lang.org/install.html'),
               dict(title='Elixir — IEx', url='https://hexdocs.pm/iex/IEx.html')]),
    dict(slug='elixir-02-values-types', title='Values, Types, and Immutability',
         desc='Immutable data, atoms, strings, numbers, and booleans.',
         dur='45 min', diff='beginner', prereq=['ELIXIR-01'],
         objs=['Explain immutability and rebinding',
               'Use atoms, strings, and numbers',
               'Perform arithmetic and division',
               'Manipulate strings'],
         refs=[dict(title='Elixir — Basic Types', url='https://elixir-lang.org/getting-started/basic-types.html'),
               dict(title='Elixir — Strings', url='https://elixir-lang.org/getting-started/basic-types.html#strings'),
               dict(title='Elixir — Operators', url='https://hexdocs.pm/elixir/operators.html')]),
    dict(slug='elixir-03-control-flow', title='Control Flow',
         desc='case, cond, if/unless, and pattern-matched function clauses.',
         dur='45 min', diff='beginner', prereq=['ELIXIR-02'],
         objs=['Match with case and guards',
               'Chain conditions with cond',
               'Use if and unless',
               'Write multi-clause functions'],
         refs=[dict(title='Elixir — case, cond, if', url='https://elixir-lang.org/getting-started/case-cond-and-if.html'),
               dict(title='Elixir — Pattern Matching', url='https://elixir-lang.org/getting-started/pattern-matching.html'),
               dict(title='Elixir — Guards', url='https://hexdocs.pm/elixir/guards.html')]),
    dict(slug='elixir-04-enumerable', title='Collections and Enum',
         desc='Enum, lists, maps, and comprehensions.',
         dur='60 min', diff='intermediate', prereq=['ELIXIR-03'],
         objs=['Transform collections with Enum',
               'Build and manipulate lists',
               'Work with maps',
               'Write list comprehensions'],
         refs=[dict(title='Elixir — Enum module', url='https://hexdocs.pm/elixir/Enum.html'),
               dict(title='Elixir — Lists and Tuples', url='https://elixir-lang.org/getting-started/basic-types.html#linked-lists'),
               dict(title='Elixir — Comprehensions', url='https://elixir-lang.org/getting-started/comprehensions.html')]),
    dict(slug='elixir-05-functions', title='Functions and the Pipe',
         desc='Anonymous functions, captures, closures, and the pipe operator.',
         dur='60 min', diff='intermediate', prereq=['ELIXIR-04'],
         objs=['Define anonymous functions',
               'Use the capture syntax',
               'Understand closures',
               'Compose with pipes'],
         refs=[dict(title='Elixir — Anonymous Functions', url='https://elixir-lang.org/getting-started/modules-and-functions.html#anonymous-functions'),
               dict(title='Elixir — The Pipe Operator', url='https://elixir-lang.org/getting-started/enumerables-and-streams.html#the-pipe-operator'),
               dict(title='Elixir — Captures', url='https://hexdocs.pm/elixir/Kernel.SpecialForms.html#&/1')]),
    dict(slug='elixir-06-recursion', title='Recursion',
         desc='Recursive thinking, tail calls, and building results.',
         dur='60 min', diff='intermediate', prereq=['ELIXIR-05'],
         objs=['Loop with recursion',
               'Use tail-call recursion',
               'Recurse over linked lists',
               'Build results recursively'],
         refs=[dict(title='Elixir — Recursion', url='https://elixir-lang.org/getting-started/recursion.html'),
               dict(title='Elixir — Tail Calls', url='https://hexdocs.pm/elixir/Kernel.html#def/2'),
               dict(title='Elixir School — Recursion', url='https://elixirschool.com/en/lessons/basics/collections')]),
    dict(slug='elixir-07-tuples-structs', title='Tuples and Structs',
         desc='Tuples, the {:ok, _}/{:error, _} convention, and structs.',
         dur='60 min', diff='intermediate', prereq=['ELIXIR-06'],
         objs=['Use tuples',
               'Follow the ok/error convention',
               'Match tuple results',
               'Define and update structs'],
         refs=[dict(title='Elixir — Tuples', url='https://elixir-lang.org/getting-started/basic-types.html#tuples'),
               dict(title='Elixir — Structs', url='https://elixir-lang.org/getting-started/structs.html'),
               dict(title='Elixir — Case (ok/error)', url='https://elixir-lang.org/getting-started/case-cond-and-if.html')]),
    dict(slug='elixir-08-keywords-maps-sets', title='Keyword Lists, Maps, and Sets',
         desc='Keyword lists, map vs keyword trade-offs, and MapSet.',
         dur='60 min', diff='intermediate', prereq=['ELIXIR-07'],
         objs=['Use keyword lists',
               'Manipulate keyword lists',
               'Compare maps and keyword lists',
               'Use sets'],
         refs=[dict(title='Elixir — Keyword Lists and Maps', url='https://elixir-lang.org/getting-started/keywords-and-maps.html'),
               dict(title='Elixir — MapSet', url='https://hexdocs.pm/elixir/MapSet.html'),
               dict(title='Elixir — Keyword module', url='https://hexdocs.pm/elixir/Keyword.html')]),
    dict(slug='elixir-09-pattern-matching', title='Pattern Matching in Depth',
         desc='Function-head matching, guards, pinning, and list patterns.',
         dur='60 min', diff='intermediate', prereq=['ELIXIR-08'],
         objs=['Match in function heads',
               'Write guards',
               'Pin values with ^',
               'Match list shapes'],
         refs=[dict(title='Elixir — Pattern Matching', url='https://elixir-lang.org/getting-started/pattern-matching.html'),
               dict(title='Elixir — Guards reference', url='https://hexdocs.pm/elixir/guards.html'),
               dict(title='Elixir — Multi-clause functions', url='https://elixir-lang.org/getting-started/modules-and-functions.html#default-arguments')]),
    dict(slug='elixir-10-error-handling', title='Error Handling',
         desc='try/rescue, errors as values, raise, and with.',
         dur='60 min', diff='intermediate', prereq=['ELIXIR-09'],
         objs=['Handle exceptions with try/rescue',
               'Treat errors as values',
               'Use raise and bang functions',
               'Compose with with'],
         refs=[dict(title='Elixir — try, catch, rescue', url='https://elixir-lang.org/getting-started/try-catch-and-rescue.html'),
               dict(title='Elixir — Errors', url='https://hexdocs.pm/elixir/errors.html'),
               dict(title='Elixir — with special form', url='https://hexdocs.pm/elixir/Kernel.SpecialForms.html#with/1')]),
    dict(slug='elixir-11-processes', title='Processes and Message Passing',
         desc='spawn, send/receive, process state, links, and monitors.',
         dur='75 min', diff='advanced', prereq=['ELIXIR-10'],
         objs=['Spawn lightweight processes',
               'Pass messages with send/receive',
               'Hold state in a process loop',
               'Link and monitor processes'],
         refs=[dict(title='Elixir — Processes', url='https://elixir-lang.org/getting-started/processes.html'),
               dict(title='Elixir — send/2 and receive', url='https://hexdocs.pm/elixir/Kernel.html#send/2'),
               dict(title='Elixir — spawn_link', url='https://hexdocs.pm/elixir/Kernel.html#spawn_link/1')]),
    dict(slug='elixir-12-agents-tasks-genserver', title='Agents, Tasks, and GenServer',
         desc='Agent for state, Task for async work, GenServer for servers.',
         dur='75 min', diff='advanced', prereq=['ELIXIR-11'],
         objs=['Use Agents for shared state',
               'Run async work with Tasks',
               'Handle Task results',
               'Build a GenServer'],
         refs=[dict(title='Elixir — Agent', url='https://hexdocs.pm/elixir/Agent.html'),
               dict(title='Elixir — Task', url='https://hexdocs.pm/elixir/Task.html'),
               dict(title='Elixir — GenServer', url='https://hexdocs.pm/elixir/GenServer.html')]),
    dict(slug='elixir-13-streams', title='Streams and Lazy Evaluation',
         desc='Lazy enumerables, infinite streams, and streaming files.',
         dur='75 min', diff='advanced', prereq=['ELIXIR-12'],
         objs=['Build lazy streams',
               'Iterate infinite data',
               'Cycle and repeat values',
               'Stream files line by line'],
         refs=[dict(title='Elixir — Enumerables and Streams', url='https://elixir-lang.org/getting-started/enumerables-and-streams.html'),
               dict(title='Elixir — Stream module', url='https://hexdocs.pm/elixir/Stream.html'),
               dict(title='Elixir School — Streams', url='https://elixirschool.com/en/lessons/basics/enum')]),
    dict(slug='elixir-14-pipes-captures', title='Pipes and Captures',
         desc='The pipe operator, capture syntax, and operator captures.',
         dur='60 min', diff='intermediate', prereq=['ELIXIR-13'],
         objs=['Read pipelines left to right',
               'Chain transforms with pipes',
               'Use capture shorthand',
               'Capture operators'],
         refs=[dict(title='Elixir — The Pipe Operator', url='https://elixir-lang.org/getting-started/enumerables-and-streams.html#the-pipe-operator'),
               dict(title='Elixir — & capture', url='https://hexdocs.pm/elixir/Kernel.SpecialForms.html#&/1'),
               dict(title='Elixir School — Pipe Operator', url='https://elixirschool.com/en/lessons/basics/pipe-operator')]),
    dict(slug='elixir-15-modules', title='Modules and Functions',
         desc='Public/private functions, defaults, clauses, import, alias.',
         dur='60 min', diff='intermediate', prereq=['ELIXIR-14'],
         objs=['Structure modules',
               'Use default arguments',
               'Write multi-clause functions',
               'Import and alias modules'],
         refs=[dict(title='Elixir — Modules', url='https://elixir-lang.org/getting-started/modules-and-functions.html'),
               dict(title='Elixir — import/alias/require', url='https://elixir-lang.org/getting-started/alias-require-and-import.html'),
               dict(title='Elixir — defp', url='https://hexdocs.pm/elixir/Kernel.html#defp/2')]),
    dict(slug='elixir-16-protocols-behaviours', title='Protocols and Behaviours',
         desc='Protocols for polymorphism, behaviours as interfaces.',
         dur='75 min', diff='advanced', prereq=['ELIXIR-15'],
         objs=['Define protocols',
               'Implement protocols for structs',
               'Use behaviours',
               'Extend built-in protocols'],
         refs=[dict(title='Elixir — Protocols', url='https://elixir-lang.org/getting-started/protocols.html'),
               dict(title='Elixir — Behaviours', url='https://elixir-lang.org/getting-started/modules-and-functions.html#behaviours'),
               dict(title='Elixir — String.Chars', url='https://hexdocs.pm/elixir/String.Chars.html')]),
    dict(slug='elixir-17-mix-tooling', title='Mix and Tooling',
         desc='Mix projects, deps, ExUnit, doctests, and the formatter.',
         dur='60 min', diff='intermediate', prereq=['ELIXIR-16'],
         objs=['Scaffold projects with Mix',
               'Declare dependencies',
               'Write ExUnit tests',
               'Verify code with doctests'],
         refs=[dict(title='Mix — Getting Started', url='https://hexdocs.pm/mix/Mix.html'),
               dict(title='Elixir — ExUnit', url='https://hexdocs.pm/ex_unit/ExUnit.html'),
               dict(title='Elixir — doctest', url='https://hexdocs.pm/elixir/Code.html#fetch_docs/1')]),
    dict(slug='elixir-18-documentation', title='Documentation and Code Organisation',
         desc='@moduledoc, @doc, module attributes, and project layout.',
         dur='60 min', diff='intermediate', prereq=['ELIXIR-17'],
         objs=['Write module documentation',
               'Use module attributes',
               'Accumulate attributes',
               'Organise project code'],
         refs=[dict(title='Elixir — Writing Documentation', url='https://hexdocs.pm/elixir/writing-documentation.html'),
               dict(title='Elixir — Module Attributes', url='https://elixir-lang.org/getting-started/module-attributes.html'),
               dict(title='Elixir — Umbrella projects', url='https://hexdocs.pm/mix/Mix.Tasks.New.Umbrella.html')]),
    dict(slug='elixir-19-otp', title='OTP and Supervision',
         desc='OTP behaviours, supervision trees, and application callbacks.',
         dur='75 min', diff='advanced', prereq=['ELIXIR-18'],
         objs=['Explain OTP behaviours',
               'Design supervision trees',
               'Choose restart strategies',
               'Implement Application callbacks'],
         refs=[dict(title='Elixir — OTP Design Principles', url='https://erlang.org/doc/design_principles/des_prim.html'),
               dict(title='Elixir — Supervisor', url='https://hexdocs.pm/elixir/Supervisor.html'),
               dict(title='Elixir — Application', url='https://hexdocs.pm/elixir/Application.html')]),
    dict(slug='elixir-20-pipelines', title='Real-World Pipelines',
         desc='Text analysis, word counting, struct pipelines, and reduce.',
         dur='75 min', diff='advanced', prereq=['ELIXIR-19'],
         objs=['Analyse text with pipelines',
               'Count words with reduce',
               'Transform struct collections',
               'Run a running maximum'],
         refs=[dict(title='Elixir — Enum.reduce', url='https://hexdocs.pm/elixir/Enum.html#reduce/3'),
               dict(title='Elixir School — Enum', url='https://elixirschool.com/en/lessons/basics/enum'),
               dict(title='Elixir — Map.update', url='https://hexdocs.pm/elixir/Map.html#update/4')]),
    dict(slug='elixir-21-metaprogramming', title='Metaprogramming and the Ecosystem',
         desc='Macros, quote/unquote, Ecto, and Phoenix.',
         dur='75 min', diff='expert', prereq=['ELIXIR-20'],
         objs=['Write basic macros',
               'Understand quote and unquote',
               'Use Ecto for databases',
               'Build web apps with Phoenix'],
         refs=[dict(title='Elixir — Metaprogramming', url='https://elixir-lang.org/getting-started/meta/quote-and-unquote.html'),
               dict(title='Ecto — Getting Started', url='https://hexdocs.pm/ecto/Ecto.html'),
               dict(title='Phoenix — Framework', url='https://hexdocs.pm/phoenix/overview.html')]),
]


if __name__ == '__main__':
    run_gen(LANGUAGE, 'elixir', LESSONS, CODE, BASE)
