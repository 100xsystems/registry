---
{
  "title": "Protocols and Multimethods",
  "description": "Protocols, extend-type, records, and multimethods.",
  "type": "lesson",
  "order": 16,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define protocols",
    "Extend existing types",
    "Use core protocols",
    "Dispatch with multimethods"
  ],
  "knowledge_refs": [
    "clojure/clojure-16-protocols"
  ],
  "prerequisites": [
    "CLOJURE-15"
  ],
  "references": [
    {
      "title": "Clojure — Protocols",
      "url": "https://clojure.org/reference/protocols"
    },
    {
      "title": "Clojure — Multimethods",
      "url": "https://clojure.org/reference/multimethods"
    },
    {
      "title": "ClojureDocs — defrecord",
      "url": "https://clojuredocs.org/clojure.core/defrecord"
    }
  ]
}
---

# CLOJURE-16-PROTOCOLS: Protocols and Multimethods

## Introduction

Protocols, extend-type, records, and multimethods. By the end of this lesson you will be able to: Define protocols; Extend existing types; Use core protocols; Dispatch with multimethods.

## Key Concepts

### 1. Define protocols

Target: Define protocols. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; Protocols: polymorphism on types
(defprotocol Shape
  (area [s])
  (perimeter [s]))

(defrecord Square [side]
  Shape
  (area [s] (* side side))
  (perimeter [s] (* 4 side)))

(println (area (->Square 4)))       ; 16
(println (perimeter (->Square 4)))  ; 16
;; defrecord implements the protocol for the new type.
```
### 2. Extend existing types

Target: Extend existing types. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; extend-type and extend-protocol
(defprotocol Greet
  (greet [x]))

(extend-type String
  Greet
  (greet [s] (str "Hello, " s "!")))

(extend-type Number
  Greet
  (greet [n] (str "Number " n)))

(println (greet "Alice"))   ; Hello, Alice!
(println (greet 42))        ; Number 42
;; Extend protocols to existing types without modifying them.
```
### 3. Use core protocols

Target: Use core protocols. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; Core protocols in action
(println (seq [1 2 3]))      ; (1 2 3) — Seqable
(println (count {:a 1}))     ; 1 — Counted
(println (assoc {} :a 1))    ; {:a 1} — Associative
(println (conj #{} 1))       ; #{1} — Conjable
;; The core sequence functions all go through protocols.
```
### 4. Dispatch with multimethods

Target: Dispatch with multimethods. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; Multimethods: dispatch on anything
(defmulti area :shape)

(defmethod area :square [{:keys [side]}]
  (* side side))

(defmethod area :circle [{:keys [radius]}]
  (* Math/PI radius radius))

(println (area {:shape :square :side 4}))   ; 16
(println (area {:shape :circle :radius 2}))
;; 12.566370614359172 — dispatch on any value
```

## Practice Questions

1. What is the key idea behind "Protocols and Multimethods"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Protocols and Multimethods with analogies and real-world examples"
1. "Show me common mistakes beginners make with Protocols and Multimethods"
1. "Provide advanced patterns and performance considerations for Protocols and Multimethods"

## Key Takeaways

- Master the core ideas of Protocols and Multimethods through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
