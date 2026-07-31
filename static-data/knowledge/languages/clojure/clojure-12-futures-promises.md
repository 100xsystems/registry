---
{
  "title": "Futures, Promises, and Parallelism",
  "description": "Future, promise, pmap, and background tasks.",
  "type": "lesson",
  "order": 12,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Compute with futures",
    "Deliver with promises",
    "Parallelize with pmap",
    "Orchestrate background work"
  ],
  "knowledge_refs": [
    "clojure/clojure-12-futures-promises"
  ],
  "prerequisites": [
    "CLOJURE-11"
  ],
  "references": [
    {
      "title": "ClojureDocs — future",
      "url": "https://clojuredocs.org/clojure.core/future"
    },
    {
      "title": "ClojureDocs — promise",
      "url": "https://clojuredocs.org/clojure.core/promise"
    },
    {
      "title": "ClojureDocs — pmap",
      "url": "https://clojuredocs.org/clojure.core/pmap"
    }
  ]
}
---

# CLOJURE-12-FUTURES-PROMISES: Futures, Promises, and Parallelism

## Introduction

Future, promise, pmap, and background tasks. By the end of this lesson you will be able to: Compute with futures; Deliver with promises; Parallelize with pmap; Orchestrate background work.

## Key Concepts

### 1. Compute with futures

Target: Compute with futures. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; Futures: parallel computation
(def f (future
         (Thread/sleep 100)
         (* 6 7)))

(println "computing in the background...")
(println @f)   ; 42 — deref blocks until the future completes
```
### 2. Deliver with promises

Target: Deliver with promises. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; Promises: deliver values manually
(def p (promise))
(future (Thread/sleep 100) (deliver p :done))
(println "waiting...")
(println @p)   ; :done — blocks until someone delivers
```
### 3. Parallelize with pmap

Target: Parallelize with pmap. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; pmap: parallel map
(defn slow-double [x]
  (Thread/sleep 50)
  (* x 2))

;; pmap runs the function across threads:
(time (doall (pmap slow-double (range 4))))
;; ~50ms for 4 items (serial would be ~200ms)
```
### 4. Orchestrate background work

Target: Orchestrate background work. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; Agents + futures for background work
(def results (agent []))
(future
  (send results conj :task-a)
  (send results conj :task-b))
(await results)
(println @results)
;; [:task-b :task-a] — order depends on scheduling
```

## Practice Questions

1. What is the key idea behind "Futures, Promises, and Parallelism"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Futures, Promises, and Parallelism with analogies and real-world examples"
1. "Show me common mistakes beginners make with Futures, Promises, and Parallelism"
1. "Provide advanced patterns and performance considerations for Futures, Promises, and Parallelism"

## Key Takeaways

- Master the core ideas of Futures, Promises, and Parallelism through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
