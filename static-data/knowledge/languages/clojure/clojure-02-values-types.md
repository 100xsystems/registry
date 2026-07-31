---
{
  "title": "Values, Types, and Immutability",
  "description": "Immutable data, numbers, strings, keywords, and truthiness.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use immutable data structures",
    "Do arithmetic with ratios",
    "Manipulate strings and keywords",
    "Understand truthiness"
  ],
  "knowledge_refs": [
    "clojure/clojure-02-values-types"
  ],
  "prerequisites": [
    "CLOJURE-01"
  ],
  "references": [
    {
      "title": "Clojure — Data Structures",
      "url": "https://clojure.org/reference/data_structures"
    },
    {
      "title": "Clojure — Special Forms (if)",
      "url": "https://clojure.org/reference/special_forms"
    },
    {
      "title": "ClojureDocs — str",
      "url": "https://clojuredocs.org/clojure.core/str"
    }
  ]
}
---

# CLOJURE-02-VALUES-TYPES: Values, Types, and Immutability

## Introduction

Immutable data, numbers, strings, keywords, and truthiness. By the end of this lesson you will be able to: Use immutable data structures; Do arithmetic with ratios; Manipulate strings and keywords; Understand truthiness.

## Key Concepts

### 1. Use immutable data structures

Target: Use immutable data structures. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; Immutable data structures
(def v [1 2 3])
(def v2 (conj v 4))        ; v2 = [1 2 3 4]
(println v)                ; [1 2 3] — original untouched
(println v2)
;; Every "modification" returns a NEW structure.
```
### 2. Do arithmetic with ratios

Target: Do arithmetic with ratios. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; Numbers, arithmetic, and division
(println (+ 1 2 3))    ; 6
(println (- 10 3))     ; 7
(println (* 2 3 4))    ; 24
(println (/ 10 2))     ; 5 — ratio preserved when exact
(println (/ 1 3))      ; 1/3 — Clojure keeps exact ratios
(println (quot 10 3))  ; 3 — integer division
(println (rem 10 3))   ; 1 — remainder
(println (inc 41))     ; 42
(println (dec 43))     ; 42
```
### 3. Manipulate strings and keywords

Target: Manipulate strings and keywords. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; Strings and keywords
(println (str "con" "cat"))      ; "concat"
(println (count "hello"))        ; 5
(println (subs "hello" 1 3))     ; "el"
(println (clojure.string/upper-case "hi"))  ; "HI"
(println (clojure.string/join ", " [1 2 3])) ; "1, 2, 3"
;; Keywords are fast, self-evaluating identifiers:
(println (keyword "user"))       ; :user
(println (name :user))           ; "user"
```
### 4. Understand truthiness

Target: Understand truthiness. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; Booleans, nil, and truthiness
(println true)     ; true
(println false)    ; false
(println nil)      ; nil
(println (if nil :truthy :falsy))  ; :falsy — nil is falsey
(println (if 0 :truthy :falsy))    ; :truthy — 0 IS truthy!
(println (if "" :truthy :falsy))   ; :truthy — empty string too
;; Only nil and false are falsey in Clojure.
```

## Practice Questions

1. What is the key idea behind "Values, Types, and Immutability"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Values, Types, and Immutability with analogies and real-world examples"
1. "Show me common mistakes beginners make with Values, Types, and Immutability"
1. "Provide advanced patterns and performance considerations for Values, Types, and Immutability"

## Key Takeaways

- Master the core ideas of Values, Types, and Immutability through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
