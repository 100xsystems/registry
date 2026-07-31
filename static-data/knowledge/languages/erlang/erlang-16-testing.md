---
{
  "title": "Testing",
  "description": "EUnit, assertions, Common Test, and the TDD workflow.",
  "type": "lesson",
  "order": 16,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write EUnit tests",
    "Use EUnit assertions",
    "Run Common Test suites",
    "Apply the TDD workflow"
  ],
  "knowledge_refs": [
    "erlang/erlang-16-testing"
  ],
  "prerequisites": [
    "ERLANG-15"
  ],
  "references": [
    {
      "title": "EUnit — User Guide",
      "url": "https://www.erlang.org/doc/apps/eunit/chapter.html"
    },
    {
      "title": "Common Test — User Guide",
      "url": "https://www.erlang.org/doc/apps/common_test/index.html"
    },
    {
      "title": "Erlang — eunit module",
      "url": "https://www.erlang.org/doc/apps/eunit/index.html"
    }
  ]
}
---

# ERLANG-16-TESTING: Testing

## Introduction

EUnit, assertions, Common Test, and the TDD workflow. By the end of this lesson you will be able to: Write EUnit tests; Use EUnit assertions; Run Common Test suites; Apply the TDD workflow.

## Key Concepts

### 1. Write EUnit tests

Target: Write EUnit tests. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```erlang
%% Basic tests with EUnit
-module(calc_test).
-include_lib("eunit/include/eunit.hrl").

add_test() -> ?assertEqual(4, calc:add(2, 2)).

run() ->
    io:format("Run with: eunit:test(calc_test).~n").
    % EUnit auto-discovers functions ending in _test.
```
### 2. Use EUnit assertions

Target: Use EUnit assertions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```erlang
%% EUnit assertions and generators
-module(feature_test).
-include_lib("eunit/include/eunit.hrl").

lists_test() ->
    ?assertEqual([2, 4], lists:map(fun(X) -> X * 2 end, [1, 2])),
    ?assert(lists:all(fun is_integer/1, [1, 2, 3])),
    ?assertError(badarith, 1 / 0).

run() ->
    io:format("assertEqual, assert, assertError and more.~n").
    % Test functions can be grouped with test generators.
```
### 3. Run Common Test suites

Target: Run Common Test suites. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```erlang
%% Common Test: integration testing
-module(feature_SUITE).
-include_lib("common_test/include/ct.hrl").
-export([all/0, simple/1]).

all() -> [simple].

simple(_Config) ->
    Result = 1 + 1,
    {comment, "1 + 1"} = {comment, "1 + 1"},
    Result = 2,
    ok.
    % Common Test is the full integration testing framework.
```
### 4. Apply the TDD workflow

Target: Apply the TDD workflow. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```erlang
%% The test-driven workflow
-module(tdd).
-export([run/0]).

run() ->
    io:format("1. Write a failing test (EUnit or CT).~n"),
    io:format("2. Run it: the test fails.~n"),
    io:format("3. Implement the module.~n"),
    io:format("4. Re-run: the test passes.~n"),
    io:format("5. Refactor and repeat.~n").
    % The compiler + test runner make TDD fast.
```

## Practice Questions

1. What is the key idea behind "Testing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing"
1. "Provide advanced patterns and performance considerations for Testing"

## Key Takeaways

- Master the core ideas of Testing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
