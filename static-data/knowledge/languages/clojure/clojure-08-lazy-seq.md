---
{
  "title": "Lazy Sequences",
  "description": "Laziness, infinite sequences, and on-demand computation.",
  "type": "lesson",
  "order": 8,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Build lazy sequences",
    "Create Fibonacci lazily",
    "Use range/repeat/repeatedly",
    "Control realization"
  ],
  "knowledge_refs": [
    "clojure/clojure-08-lazy-seq"
  ],
  "prerequisites": [
    "CLOJURE-07"
  ],
  "references": [
    {
      "title": "Clojure — Laziness",
      "url": "https://clojure.org/reference/lazy"
    },
    {
      "title": "ClojureDocs — lazy-seq",
      "url": "https://clojuredocs.org/clojure.core/lazy-seq"
    },
    {
      "title": "ClojureDocs — repeatedly",
      "url": "https://clojuredocs.org/clojure.core/repeatedly"
    }
  ]
}
---

# CLOJURE-08-LAZY-SEQ: Lazy Sequences

## Introduction

Laziness, infinite sequences, and on-demand computation. By the end of this lesson you will be able to: Build lazy sequences; Create Fibonacci lazily; Use range/repeat/repeatedly; Control realization.

## Key Concepts

### 1. Build lazy sequences

Target: Build lazy sequences. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; Lazy sequences: compute on demand
(def naturals (iterate inc 1))
(println (take 5 naturals))        ; (1 2 3 4 5)
(println (take 5 (map #(* % %) naturals)))
;; (1 4 9 16 25) — infinite source, finite consumption
```
### 2. Create Fibonacci lazily

Target: Create Fibonacci lazily. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; Fibonacci as a lazy sequence
(def fibs
  (lazy-seq
    (cons 0
          (lazy-seq
            (cons 1
                  (map + fibs (rest fibs)))))))

(println (take 10 fibs))
;; (0 1 1 2 3 5 8 13 21 34)
```
### 3. Use range/repeat/repeatedly

Target: Use range/repeat/repeatedly. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; range, repeat, repeatedly
(println (range 5))          ; (0 1 2 3 4)
(println (take 3 (repeat :x)))   ; (:x :x :x)
(println (take 3 (repeatedly rand)))
;; three random doubles between 0 and 1
```
### 4. Control realization

Target: Control realization. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; Laziness in pipelines
(defn process [coll]
  (->> coll
       (map #(do (println "mapping" %) (* % %)))
       (filter even?)
       (take 2)))

;; process realizes ONLY as much as needed:
(println (process (range 10)))
;; prints "mapping" for 0, 1, 2 only — stops after 2 evens.
```

## Practice Questions

1. What is the key idea behind "Lazy Sequences"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lazy Sequences with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lazy Sequences"
1. "Provide advanced patterns and performance considerations for Lazy Sequences"

## Key Takeaways

- Master the core ideas of Lazy Sequences through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
