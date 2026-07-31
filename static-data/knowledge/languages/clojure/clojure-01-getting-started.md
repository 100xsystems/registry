---
{
  "title": "Getting Started with Clojure",
  "description": "Installation, the REPL, forms, namespaces, and Java interop.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write and run a Clojure program",
    "Explore with the REPL",
    "Understand forms as data",
    "Use namespaces and Java interop"
  ],
  "knowledge_refs": [
    "clojure/clojure-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "Clojure — Getting Started",
      "url": "https://clojure.org/guides/getting_started"
    },
    {
      "title": "Clojure — Reference",
      "url": "https://clojure.org/reference"
    },
    {
      "title": "Clojure — REPL and Main",
      "url": "https://clojure.org/guides/repl/basics"
    }
  ]
}
---

# CLOJURE-01-GETTING-STARTED: Getting Started with Clojure

## Introduction

Installation, the REPL, forms, namespaces, and Java interop. By the end of this lesson you will be able to: Write and run a Clojure program; Explore with the REPL; Understand forms as data; Use namespaces and Java interop.

## Key Concepts

### 1. Write and run a Clojure program

Target: Write and run a Clojure program. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; Your first Clojure program
(println "Hello, 100X Systems!")
;; run: clojure -M hello.clj   ->   Hello, 100X Systems!
;; or with Leiningen: lein run
```
### 2. Explore with the REPL

Target: Explore with the REPL. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; The REPL: interactive exploration
;; user=> (+ 1 2)
;; 3
;; user=> (str "Hello" " " "Clojure")
;; "Hello Clojure"
(println (* 6 7))   ; 42 — everything is a prefix expression
```
### 3. Understand forms as data

Target: Understand forms as data. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; Forms: code is data (homoiconic)
(println (+ 1 2 3))        ; 6 — function call
(println '(1 2 3))         ; (1 2 3) — quoted list, NOT a call
(println :keyword)         ; :keyword — a keyword literal
(println {:a 1 :b 2})      ; {:a 1, :b 2} — a map literal
;; Clojure code IS Clojure data.
```
### 4. Use namespaces and Java interop

Target: Use namespaces and Java interop. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; Namespaces and the dot syntax for Java interop
(ns hello.core)

(defn greet [name]
  (str "Hello, " name "!"))

(println (greet "World"))
(println (.toUpperCase "clojure"))  ; CLOJURE — Java method call
(println (Math/sqrt 16))             ; 4.0 — Java static method
```

## Practice Questions

1. What is the key idea behind "Getting Started with Clojure"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Clojure with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Clojure"
1. "Provide advanced patterns and performance considerations for Getting Started with Clojure"

## Key Takeaways

- Master the core ideas of Getting Started with Clojure through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
