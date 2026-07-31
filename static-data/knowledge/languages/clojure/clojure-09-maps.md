---
{
  "title": "Maps in Depth",
  "description": "Keywords as functions, update/merge, nested access, records.",
  "type": "lesson",
  "order": 9,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use keywords as functions",
    "Update and merge maps",
    "Navigate nested maps",
    "Define records"
  ],
  "knowledge_refs": [
    "clojure/clojure-09-maps"
  ],
  "prerequisites": [
    "CLOJURE-08"
  ],
  "references": [
    {
      "title": "Clojure — Maps",
      "url": "https://clojure.org/reference/data_structures#Maps"
    },
    {
      "title": "ClojureDocs — update",
      "url": "https://clojuredocs.org/clojure.core/update"
    },
    {
      "title": "ClojureDocs — get-in",
      "url": "https://clojuredocs.org/clojure.core/get-in"
    }
  ]
}
---

# CLOJURE-09-MAPS: Maps in Depth

## Introduction

Keywords as functions, update/merge, nested access, records. By the end of this lesson you will be able to: Use keywords as functions; Update and merge maps; Navigate nested maps; Define records.

## Key Concepts

### 1. Use keywords as functions

Target: Use keywords as functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; Keywords as functions for map lookup
(def m {:name "Alice" :age 30})
(println (:name m))             ; Alice
(println (:age m))              ; 30
(println (:city m :unknown))    ; :unknown — default value
(println (map :name [{:name "A"} {:name "B"}]))
;; ("A" "B") — pull a key from each map
```
### 2. Update and merge maps

Target: Update and merge maps. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; Update and merge maps
(def m {:count 0})
(println (update m :count inc))       ; {:count 1}
(println (update m :count + 5))       ; {:count 5}
(println (merge {:a 1} {:b 2}))       ; {:a 1, :b 2}
(println (merge-with + {:a 1} {:a 2})) ; {:a 3}
;; update applies a function to an existing key
```
### 3. Navigate nested maps

Target: Navigate nested maps. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; Nested map access and update
(def config {:db {:host "localhost" :port 5432}})
(println (get-in config [:db :host]))     ; localhost
(println (assoc-in config [:db :port] 5433))
;; {:db {:host "localhost", :port 5433}}
(println (update-in config [:db :port] inc))
;; {:db {:host "localhost", :port 5433}}
;; get-in/assoc-in/update-in navigate nested structures.
```
### 4. Define records

Target: Define records. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; Records: maps with a type
(defrecord Person [name age])

(def alice (->Person "Alice" 30))
(println (:name alice))        ; Alice
(println (assoc alice :age 31))
;; #user.Person{:name "Alice", :age 31}
(println (map? alice))         ; true — records ARE maps
;; defrecord gives you maps plus a type and protocols.
```

## Practice Questions

1. What is the key idea behind "Maps in Depth"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Maps in Depth with analogies and real-world examples"
1. "Show me common mistakes beginners make with Maps in Depth"
1. "Provide advanced patterns and performance considerations for Maps in Depth"

## Key Takeaways

- Master the core ideas of Maps in Depth through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
