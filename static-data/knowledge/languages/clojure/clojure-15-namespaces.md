---
{
  "title": "Namespaces and Interop",
  "description": "require, refer, project layout, and Java interop.",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Require and alias namespaces",
    "Refer specific symbols",
    "Structure the classpath",
    "Call into the JVM"
  ],
  "knowledge_refs": [
    "clojure/clojure-15-namespaces"
  ],
  "prerequisites": [
    "CLOJURE-14"
  ],
  "references": [
    {
      "title": "Clojure — Namespaces",
      "url": "https://clojure.org/reference/namespaces"
    },
    {
      "title": "Clojure — Java Interop",
      "url": "https://clojure.org/reference/java_interop"
    },
    {
      "title": "Clojure — deps.edn",
      "url": "https://clojure.org/guides/deps_and_cli"
    }
  ]
}
---

# CLOJURE-15-NAMESPACES: Namespaces and Interop

## Introduction

require, refer, project layout, and Java interop. By the end of this lesson you will be able to: Require and alias namespaces; Refer specific symbols; Structure the classpath; Call into the JVM.

## Key Concepts

### 1. Require and alias namespaces

Target: Require and alias namespaces. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; Namespaces: organising code
;; (ns my-app.core (:require [clojure.string :as str]))
(require '[clojure.string :as str])
(println (str/join "-" [2026 7 31]))   ; "2026-7-31"
(println (str/upper-case "hello"))     ; HELLO
;; Aliasing keeps namespaces concise.
```
### 2. Refer specific symbols

Target: Refer specific symbols. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; refer and refer-clojure
;; (use 'clojure.string) — avoid; use require instead.
(require '[clojure.set :refer [union intersection]])
(println (union #{1 2} #{3}))         ; #{1 3 2}
(println (intersection #{1 2 3} #{3})) ; #{3}
;; refer pulls specific symbols into scope.
```
### 3. Structure the classpath

Target: Structure the classpath. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; The classpath and project structure
;; src/my_app/core.clj       -> namespace my-app.core
;; test/my_app/core_test.clj -> tests
;; deps.edn lists dependencies:
;; {:deps {org.clojure/clojure {:mvn/version "1.11.1"}}}
(println "deps.edn manages dependencies and paths")
```
### 4. Call into the JVM

Target: Call into the JVM. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; Java interop: calling into the JVM
(println (System/currentTimeMillis))  ; epoch millis
(println (.length "hello"))           ; 5 — instance method
(println (Math/floor 3.7))            ; 3.0 — static method
(println (java.util.UUID/randomUUID))
;; a random UUID — full Java ecosystem available
```

## Practice Questions

1. What is the key idea behind "Namespaces and Interop"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Namespaces and Interop with analogies and real-world examples"
1. "Show me common mistakes beginners make with Namespaces and Interop"
1. "Provide advanced patterns and performance considerations for Namespaces and Interop"

## Key Takeaways

- Master the core ideas of Namespaces and Interop through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
