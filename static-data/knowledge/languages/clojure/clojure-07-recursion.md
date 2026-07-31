---
{
  "title": "Recursion",
  "description": "loop/recur, tail calls, and building results.",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Loop with loop/recur",
    "Write recursive functions",
    "Use tail-call optimization",
    "Build results with recur"
  ],
  "knowledge_refs": [
    "clojure/clojure-07-recursion"
  ],
  "prerequisites": [
    "CLOJURE-06"
  ],
  "references": [
    {
      "title": "Clojure — loop/recur",
      "url": "https://clojure.org/reference/special_forms#recur"
    },
    {
      "title": "ClojureDocs — recur",
      "url": "https://clojuredocs.org/clojure.core/recur"
    },
    {
      "title": "ClojureDocs — loop",
      "url": "https://clojuredocs.org/clojure.core/loop"
    }
  ]
}
---

# CLOJURE-07-RECURSION: Recursion

## Introduction

loop/recur, tail calls, and building results. By the end of this lesson you will be able to: Loop with loop/recur; Write recursive functions; Use tail-call optimization; Build results with recur.

## Key Concepts

### 1. Loop with loop/recur

Target: Loop with loop/recur. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; Recursion with loop/recur — tail-call optimized
(defn count-down [n]
  (loop [i n]
    (when (pos? i)
      (println i)
      (recur (dec i)))))

(count-down 3)
;; 3 2 1 — recur jumps to the loop, never grows the stack.
```
### 2. Write recursive functions

Target: Write recursive functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; Recursive functions with recur
(defn sum-to [n]
  (if (zero? n)
    0
    (+ n (sum-to (dec n)))))

(println (sum-to 100))   ; 5050
;; This version is NOT tail-recursive (the + wraps the call).
```
### 3. Use tail-call optimization

Target: Use tail-call optimization. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; Tail-recursive sum with an accumulator
(defn sum-acc [n]
  (loop [i n acc 0]
    (if (zero? i)
      acc
      (recur (dec i) (+ acc i)))))

(println (sum-acc 100))   ; 5050 — tail call optimized
;; recur must be in tail position.
```
### 4. Build results with recur

Target: Build results with recur. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; Building results with recur
(defn evens [coll]
  (loop [xs coll acc []]
    (if (empty? xs)
      acc
      (let [x (first xs)]
        (if (even? x)
          (recur (rest xs) (conj acc x))
          (recur (rest xs) acc))))))

(println (evens [1 2 3 4 5 6]))   ; [2 4 6]
```

## Practice Questions

1. What is the key idea behind "Recursion"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Recursion with analogies and real-world examples"
1. "Show me common mistakes beginners make with Recursion"
1. "Provide advanced patterns and performance considerations for Recursion"

## Key Takeaways

- Master the core ideas of Recursion through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
