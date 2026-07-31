---
{
  "title": "Higher-Order Functions",
  "description": "First-class functions, composition, partial, apply.",
  "type": "lesson",
  "order": 14,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Pass functions as values",
    "Compose functions",
    "Partially apply functions",
    "Spread with apply"
  ],
  "knowledge_refs": [
    "clojure/clojure-14-higher-order"
  ],
  "prerequisites": [
    "CLOJURE-13"
  ],
  "references": [
    {
      "title": "ClojureDocs — comp",
      "url": "https://clojuredocs.org/clojure.core/comp"
    },
    {
      "title": "ClojureDocs — partial",
      "url": "https://clojuredocs.org/clojure.core/partial"
    },
    {
      "title": "ClojureDocs — apply",
      "url": "https://clojuredocs.org/clojure.core/apply"
    }
  ]
}
---

# CLOJURE-14-HIGHER-ORDER: Higher-Order Functions

## Introduction

First-class functions, composition, partial, apply. By the end of this lesson you will be able to: Pass functions as values; Compose functions; Partially apply functions; Spread with apply.

## Key Concepts

### 1. Pass functions as values

Target: Pass functions as values. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; Higher-order functions: pass functions around
(defn apply-twice [f x]
  (f (f x)))

(println (apply-twice inc 5))        ; 7
(println (apply-twice #(* % 2) 3))   ; 12
;; Functions are first-class values.
```
### 2. Compose functions

Target: Compose functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; Function composition
(def add1 (comp inc))
(def double-then-add (comp inc #(* % 2)))

(println (double-then-add 5))   ; 11 — inc applied LAST
;; comp composes right-to-left: (inc (* 5 2)).
(println ((comp str inc) 41))   ; "42"
```
### 3. Partially apply functions

Target: Partially apply functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; Partial application
(def add-100 (partial + 100))
(println (add-100 1))        ; 101
(println (add-100 50))       ; 150

(def multiply (partial * 3))
(println (multiply 4))       ; 12
;; partial fixes the first args, returns a waiting function.
```
### 4. Spread with apply

Target: Spread with apply. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; Calling functions as data with apply
(println (apply + [1 2 3]))        ; 6
(println (apply max [3 9 4]))      ; 9
(println (apply str ["a" "b" "c"])) ; "abc"
;; apply spreads a collection across a function's args.
```

## Practice Questions

1. What is the key idea behind "Higher-Order Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Higher-Order Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Higher-Order Functions"
1. "Provide advanced patterns and performance considerations for Higher-Order Functions"

## Key Takeaways

- Master the core ideas of Higher-Order Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
