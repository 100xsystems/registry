---
{
  "title": "Control Flow",
  "description": "if, when, cond, case, and condp.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Branch with if and when",
    "Chain with cond",
    "Dispatch with case",
    "Compare with condp"
  ],
  "knowledge_refs": [
    "clojure/clojure-03-control-flow"
  ],
  "prerequisites": [
    "CLOJURE-02"
  ],
  "references": [
    {
      "title": "Clojure — Control Flow",
      "url": "https://clojure.org/guides/learn/flow"
    },
    {
      "title": "ClojureDocs — cond",
      "url": "https://clojuredocs.org/clojure.core/cond"
    },
    {
      "title": "ClojureDocs — case",
      "url": "https://clojuredocs.org/clojure.core/case"
    }
  ]
}
---

# CLOJURE-03-CONTROL-FLOW: Control Flow

## Introduction

if, when, cond, case, and condp. By the end of this lesson you will be able to: Branch with if and when; Chain with cond; Dispatch with case; Compare with condp.

## Key Concepts

### 1. Branch with if and when

Target: Branch with if and when. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; if, if-not, when
(println (if (> 3 2) "yes" "no"))        ; yes
(println (if-not (> 3 2) "yes" "no"))    ; no
(when true
  (println "when runs")
  (println "multiple forms"))
;; when returns nil if the condition is false.
```
### 2. Chain with cond

Target: Chain with cond. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; cond: the else-if chain
(defn grade [score]
  (cond
    (>= score 90) "A"
    (>= score 75) "B"
    (>= score 50) "C"
    :else "D"))

(println (grade 85))   ; B
;; :else is just a truthy keyword — the catch-all.
```
### 3. Dispatch with case

Target: Dispatch with case. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; case: dispatch on constant values
(defn fruit-type [fruit]
  (case fruit
    :apple  "tree fruit"
    :banana "tropical"
    "unknown"))

(println (fruit-type :apple))    ; tree fruit
(println (fruit-type :mango))    ; unknown
```
### 4. Compare with condp

Target: Compare with condp. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; condp and predicate dispatch
(defn classify [n]
  (condp > n
    10 "small"
    100 "medium"
    "large"))

(println (classify 5))     ; small
(println (classify 50))    ; medium
(println (classify 500))   ; large
;; condp compares each value against the test expression.
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
