---
{
  "title": "Atoms, Refs, and Agents",
  "description": "Synchronous atoms, coordinated refs, and async agents.",
  "type": "lesson",
  "order": 11,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Mutate with atoms",
    "Coordinate with refs and dosync",
    "Update asynchronously with agents",
    "Choose the right reference type"
  ],
  "knowledge_refs": [
    "clojure/clojure-11-atoms-refs-agents"
  ],
  "prerequisites": [
    "CLOJURE-10"
  ],
  "references": [
    {
      "title": "Clojure — Atoms",
      "url": "https://clojure.org/reference/atoms"
    },
    {
      "title": "Clojure — Refs and Transactions",
      "url": "https://clojure.org/reference/refs"
    },
    {
      "title": "Clojure — Agents",
      "url": "https://clojure.org/reference/agents"
    }
  ]
}
---

# CLOJURE-11-ATOMS-REFS-AGENTS: Atoms, Refs, and Agents

## Introduction

Synchronous atoms, coordinated refs, and async agents. By the end of this lesson you will be able to: Mutate with atoms; Coordinate with refs and dosync; Update asynchronously with agents; Choose the right reference type.

## Key Concepts

### 1. Mutate with atoms

Target: Mutate with atoms. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; Atoms: thread-safe mutable references
(def counter (atom 0))
(swap! counter inc)
(swap! counter inc)
(println @counter)   ; 2 — deref with @
;; swap! applies a function atomically.
```
### 2. Coordinate with refs and dosync

Target: Coordinate with refs and dosync. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; Atoms: more operations
(def state (atom {:count 0}))
(swap! state update :count inc)
(swap! state update :count + 10)
(println @state)          ; {:count 11}
(reset! state {:count 0})
(println @state)          ; {:count 0}
(println (compare-and-set! state {:count 0} {:count 100}))
;; true — CAS-style update
```
### 3. Update asynchronously with agents

Target: Update asynchronously with agents. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; Refs: coordinated changes (STM)
(def account-a (ref 100))
(def account-b (ref 50))

(dosync
  (alter account-a - 30)
  (alter account-b + 30))

(println @account-a)   ; 70
(println @account-b)   ; 80
;; dosync retries until the whole transaction commits.
```
### 4. Choose the right reference type

Target: Choose the right reference type. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; Agents: asynchronous state updates
(def log-agent (agent []))
(send log-agent conj :started)
(send log-agent conj :finished)
(await log-agent)
(println @log-agent)   ; [:started :finished]
;; send queues actions; await blocks until they run.
```

## Practice Questions

1. What is the key idea behind "Atoms, Refs, and Agents"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Atoms, Refs, and Agents with analogies and real-world examples"
1. "Show me common mistakes beginners make with Atoms, Refs, and Agents"
1. "Provide advanced patterns and performance considerations for Atoms, Refs, and Agents"

## Key Takeaways

- Master the core ideas of Atoms, Refs, and Agents through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
