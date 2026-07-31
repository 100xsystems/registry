---
{
  "title": "Sequences and Transforms",
  "description": "map, filter, reduce, threading macros, and the seq abstraction.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Transform with map/filter/reduce",
    "Use more sequence functions",
    "Thread with -> and ->>",
    "Accumulate with reduce"
  ],
  "knowledge_refs": [
    "clojure/clojure-06-sequences"
  ],
  "prerequisites": [
    "CLOJURE-05"
  ],
  "references": [
    {
      "title": "Clojure — Sequences",
      "url": "https://clojure.org/reference/sequences"
    },
    {
      "title": "ClojureDocs — reduce",
      "url": "https://clojuredocs.org/clojure.core/reduce"
    },
    {
      "title": "ClojureDocs — ->>",
      "url": "https://clojuredocs.org/clojure.core/-%3E%3E"
    }
  ]
}
---

# CLOJURE-06-SEQUENCES: Sequences and Transforms

## Introduction

map, filter, reduce, threading macros, and the seq abstraction. By the end of this lesson you will be able to: Transform with map/filter/reduce; Use more sequence functions; Thread with -> and ->>; Accumulate with reduce.

## Key Concepts

### 1. Transform with map/filter/reduce

Target: Transform with map/filter/reduce. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; Map, filter, reduce — the holy trinity
(println (map #(* % 2) [1 2 3]))        ; (2 4 6)
(println (filter even? [1 2 3 4]))      ; (2 4)
(println (reduce + [1 2 3 4]))          ; 10
(println (reduce #(str %1 %2) "" ["a" "b" "c"])) ; "abc"
```
### 2. Use more sequence functions

Target: Use more sequence functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; More sequence functions
(println (reduce + 100 [1 2 3]))    ; 106 — initial value
(println (map + [1 2] [10 20]))     ; (11 22) — multi-collection
(println (remove even? [1 2 3 4]))  ; (1 3)
(println (take 2 [1 2 3 4]))        ; (1 2)
(println (drop 2 [1 2 3 4]))        ; (3 4)
(println (sort [3 1 2]))            ; (1 2 3)
(println (reverse [1 2 3]))         ; (3 2 1)
```
### 3. Thread with -> and ->>

Target: Thread with -> and ->>. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; Threading macros: -> and ->>
(println (-> 5
            (* 2)
            (+ 1)))            ; 11 — threads as FIRST arg

(println (->> [3 1 2]
             (map inc)
             (filter even?)
             (reduce +)))      ; 6 — threads as LAST arg
;; ->> shines for sequence pipelines.
```
### 4. Accumulate with reduce

Target: Accumulate with reduce. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; reduce with an accumulator pattern
(defn word-count [words]
  (reduce (fn [acc w]
            (update acc w (fnil inc 0)))
          {}
          words))

(println (word-count ["a" "b" "a" "c" "a"]))
;; {"a" 3, "b" 1, "c" 1}
```

## Practice Questions

1. What is the key idea behind "Sequences and Transforms"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Sequences and Transforms with analogies and real-world examples"
1. "Show me common mistakes beginners make with Sequences and Transforms"
1. "Provide advanced patterns and performance considerations for Sequences and Transforms"

## Key Takeaways

- Master the core ideas of Sequences and Transforms through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
