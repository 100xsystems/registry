---
{
  "title": "Binaries and I/O",
  "description": "Binary matching, request parsing, building, and files.",
  "type": "lesson",
  "order": 15,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Match binary patterns",
    "Parse request-like data",
    "Build and split binaries",
    "Read and write files"
  ],
  "knowledge_refs": [
    "erlang/erlang-15-binaries-io"
  ],
  "prerequisites": [
    "ERLANG-14"
  ],
  "references": [
    {
      "title": "Erlang — Bit Syntax",
      "url": "https://www.erlang.org/doc/programming_examples/bit_syntax.html"
    },
    {
      "title": "Erlang — file module",
      "url": "https://www.erlang.org/doc/apps/kernel/file.html"
    },
    {
      "title": "Learn You Some Erlang — Binaries",
      "url": "https://learnyousomeerlang.com/starting-out-for-real#binaries"
    }
  ]
}
---

# ERLANG-15-BINARIES-IO: Binaries and I/O

## Introduction

Binary matching, request parsing, building, and files. By the end of this lesson you will be able to: Match binary patterns; Parse request-like data; Build and split binaries; Read and write files.

## Key Concepts

### 1. Match binary patterns

Target: Match binary patterns. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% Basic pattern matching with binaries
-module(bin_match).
-export([run/0]).

run() ->
    <<"GET ", Path/binary>> = <<"GET /index.html">>,
    io:format("path: ~s~n", [Path]),
    <<Head:8, Rest/binary>> = <<1, 2, 3>>,
    io:format("~p ~p~n", [Head, Rest]).
    % Bit syntax can destructure binary data directly.
```
### 2. Parse request-like data

Target: Parse request-like data. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% Matching HTTP-like requests
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
    % {post, "/login"}
```
### 3. Build and split binaries

Target: Build and split binaries. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% Building and splitting binaries
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
    % "abc" "def" — slice with size patterns
```
### 4. Read and write files

Target: Read and write files. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% I/O from files
-module(io_demo).
-export([run/0]).

run() ->
    ok = file:write_file("/tmp/demo.txt", "hello file\n"),
    {ok, Data} = file:read_file("/tmp/demo.txt"),
    io:format("read: ~s", [Data]),
    {ok, Lines} = file:consult("/tmp/nums.txt"),
    io:format("~p~n", [Lines]).
    % file:consult reads Erlang terms from a file.
```

## Practice Questions

1. What is the key idea behind "Binaries and I/O"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Binaries and I/O with analogies and real-world examples"
1. "Show me common mistakes beginners make with Binaries and I/O"
1. "Provide advanced patterns and performance considerations for Binaries and I/O"

## Key Takeaways

- Master the core ideas of Binaries and I/O through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
