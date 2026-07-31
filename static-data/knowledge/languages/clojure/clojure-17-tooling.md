---
{
  "title": "Tooling and Testing",
  "description": "Leiningen, deps.edn, clojure.test, and the REPL workflow.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Manage projects with Leiningen",
    "Write clojure.test tests",
    "Assert with is",
    "Develop REPL-driven"
  ],
  "knowledge_refs": [
    "clojure/clojure-17-tooling"
  ],
  "prerequisites": [
    "CLOJURE-16"
  ],
  "references": [
    {
      "title": "Leiningen — Getting Started",
      "url": "https://leiningen.org/"
    },
    {
      "title": "Clojure — clojure.test",
      "url": "https://clojure.github.io/clojure/clojure.test-api.html"
    },
    {
      "title": "Clojure — REPL workflow",
      "url": "https://clojure.org/guides/repl/guidelines"
    }
  ]
}
---

# CLOJURE-17-TOOLING: Tooling and Testing

## Introduction

Leiningen, deps.edn, clojure.test, and the REPL workflow. By the end of this lesson you will be able to: Manage projects with Leiningen; Write clojure.test tests; Assert with is; Develop REPL-driven.

## Key Concepts

### 1. Manage projects with Leiningen

Target: Manage projects with Leiningen. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; lein and deps.edn tooling
;; lein new app my-app     -> project scaffold
;; lein repl               -> REPL with the project loaded
;; lein test               -> run tests
;; lein run                -> run the app
;; clojure -M:test         -> run tests via deps.edn aliases
(println "Leiningen and tools.deps manage Clojure projects")
```
### 2. Write clojure.test tests

Target: Write clojure.test tests. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; clojure.test: the built-in test library
(ns my-app.core-test
  (:require [clojure.test :refer [deftest is testing run-tests]]))

(deftest addition-test
  (testing "addition"
    (is (= 4 (+ 2 2)))
    (is (= 5 (+ 2 3)))))

(run-tests)
;; Ran 1 tests containing 2 assertions. 0 failures.
```
### 3. Assert with is

Target: Assert with is. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; Property-based and rich assertions
(deftest data-test
  (is (= {:a 1} {:a 1}))
  (is (even? 4))
  (is (thrown? ArithmeticException (/ 1 0))))

(run-tests)
;; is supports =, predicates, and thrown? — no special API.
```
### 4. Develop REPL-driven

Target: Develop REPL-driven. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; The REPL-driven workflow
;; Start a REPL, evaluate forms incrementally:
;;   (require 'my-app.core)
;;   (my-app.core/greet "REPL")
;;   (def x 42)  ; redefine as you explore
;; The REPL becomes the development environment itself.
(println "REPL-driven development is the Clojure workflow")
```

## Practice Questions

1. What is the key idea behind "Tooling and Testing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Tooling and Testing with analogies and real-world examples"
1. "Show me common mistakes beginners make with Tooling and Testing"
1. "Provide advanced patterns and performance considerations for Tooling and Testing"

## Key Takeaways

- Master the core ideas of Tooling and Testing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
