---
{
  "title": "Concurrency in Depth",
  "description": "The concurrency model, dynamic vars, STM, and identity.",
  "type": "lesson",
  "order": 19,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Compare reference types",
    "Use dynamic vars",
    "Run STM transactions",
    "Reason about identity vs value"
  ],
  "knowledge_refs": [
    "clojure/clojure-19-concurrency"
  ],
  "prerequisites": [
    "CLOJURE-18"
  ],
  "references": [
    {
      "title": "Clojure — Concurrency",
      "url": "https://clojure.org/reference/concurrency_and_parallelism"
    },
    {
      "title": "ClojureDocs — binding",
      "url": "https://clojuredocs.org/clojure.core/binding"
    },
    {
      "title": "ClojureDocs — dosync",
      "url": "https://clojuredocs.org/clojure.core/dosync"
    }
  ]
}
---

# CLOJURE-19-CONCURRENCY: Concurrency in Depth

## Introduction

The concurrency model, dynamic vars, STM, and identity. By the end of this lesson you will be able to: Compare reference types; Use dynamic vars; Run STM transactions; Reason about identity vs value.

## Key Concepts

### 1. Compare reference types

Target: Compare reference types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; Concurrency model overview
;; - Atoms: uncoordinated synchronous updates
;; - Refs: coordinated transactional updates (STM)
;; - Agents: asynchronous updates
;; - Futures/Promises: parallel computation and handoff
;; - Vars: dynamic, thread-local state
(println "Clojure's concurrency is built on immutable state")
```
### 2. Use dynamic vars

Target: Use dynamic vars. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; Dynamic vars: thread-local bindings
(def ^:dynamic *debug* false)

(defn log [msg]
  (when *debug*
    (println "DEBUG:" msg)))

(binding [*debug* true]
  (log "visible"))       ; DEBUG: visible
(log "hidden")           ; nothing — back to default
```
### 3. Run STM transactions

Target: Run STM transactions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; The STM transaction
(def cart (ref []))
(dosync
  (alter cart conj :item-1)
  (alter cart conj :item-2))
(println @cart)   ; [:item-1 :item-2]
;; refs + dosync give multi-ref atomic updates.
```
### 4. Reason about identity vs value

Target: Reason about identity vs value. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; State vs identity: the Clojure philosophy
;; - Identity: a stable name (an atom, a ref)
;; - Value: the immutable snapshot at a moment (@atom)
;; - Change: swap! to a NEW value, never mutation
(def n (atom 0))
(swap! n + 1)
(swap! n + 1)
(println @n)   ; 2
;; n always refers to the atom; its VALUE changed twice.
```

## Practice Questions

1. What is the key idea behind "Concurrency in Depth"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Concurrency in Depth with analogies and real-world examples"
1. "Show me common mistakes beginners make with Concurrency in Depth"
1. "Provide advanced patterns and performance considerations for Concurrency in Depth"

## Key Takeaways

- Master the core ideas of Concurrency in Depth through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
