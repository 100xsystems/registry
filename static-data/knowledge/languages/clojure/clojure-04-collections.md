---
{
  "title": "Collections",
  "description": "Vectors, lists, maps, and sets — the four core structures.",
  "type": "lesson",
  "order": 4,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use vectors for indexed access",
    "Use lists for linked sequences",
    "Look up and update maps",
    "Test set membership"
  ],
  "knowledge_refs": [
    "clojure/clojure-04-collections"
  ],
  "prerequisites": [
    "CLOJURE-03"
  ],
  "references": [
    {
      "title": "Clojure — Collections",
      "url": "https://clojure.org/reference/data_structures#Collections"
    },
    {
      "title": "ClojureDocs — assoc",
      "url": "https://clojuredocs.org/clojure.core/assoc"
    },
    {
      "title": "ClojureDocs — conj",
      "url": "https://clojuredocs.org/clojure.core/conj"
    }
  ]
}
---

# CLOJURE-04-COLLECTIONS: Collections

## Introduction

Vectors, lists, maps, and sets — the four core structures. By the end of this lesson you will be able to: Use vectors for indexed access; Use lists for linked sequences; Look up and update maps; Test set membership.

## Key Concepts

### 1. Use vectors for indexed access

Target: Use vectors for indexed access. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; Vectors: fast indexed access
(def v [10 20 30])
(println (nth v 1))          ; 20
(println (get v 2))          ; 30
(println (conj v 40))        ; [10 20 30 40] — appends to vector
(println (count v))          ; 3
(println (first v))          ; 10
(println (last v))           ; 30
```
### 2. Use lists for linked sequences

Target: Use lists for linked sequences. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; Lists: linked lists, fast prepend
(def lst '(1 2 3))
(println (first lst))        ; 1
(println (rest lst))         ; (2 3)
(println (conj lst 0))       ; (0 1 2 3) — PREPENDS to list
(println (count lst))        ; 3
;; Vectors conj at the end; lists conj at the front.
```
### 3. Look up and update maps

Target: Look up and update maps. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; Maps: key-value lookup
(def m {:name "Alice" :age 30})
(println (get m :name))        ; Alice
(println (m :age))             ; 30 — map as function!
(println (:name m))            ; Alice — keyword as function!
(println (assoc m :city "NYC"))
;; {:name "Alice", :age 30, :city "NYC"}
(println (dissoc m :age))      ; {:name "Alice"}
(println (contains? m :name))  ; true
```
### 4. Test set membership

Target: Test set membership. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; Sets: uniqueness and membership
(def s #{1 2 3})
(println (contains? s 2))      ; true
(println (conj s 4))           ; #{1 4 3 2}
(println (conj s 2))           ; #{1 3 2} — already there, no dup
(println (clojure.set/union #{1 2} #{2 3}))  ; #{1 3 2}
(println (clojure.set/intersection #{1 2 3} #{2 3 4})) ; #{3 2}
```

## Practice Questions

1. What is the key idea behind "Collections"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Collections with analogies and real-world examples"
1. "Show me common mistakes beginners make with Collections"
1. "Provide advanced patterns and performance considerations for Collections"

## Key Takeaways

- Master the core ideas of Collections through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
