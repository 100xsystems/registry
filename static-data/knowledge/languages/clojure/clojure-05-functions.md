---
{
  "title": "Functions",
  "description": "Anonymous functions, defn, arities, and destructuring.",
  "type": "lesson",
  "order": 5,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write anonymous functions",
    "Define named functions",
    "Use multiple arities",
    "Destructure collections"
  ],
  "knowledge_refs": [
    "clojure/clojure-05-functions"
  ],
  "prerequisites": [
    "CLOJURE-04"
  ],
  "references": [
    {
      "title": "Clojure — Functions",
      "url": "https://clojure.org/guides/learn/functions"
    },
    {
      "title": "ClojureDocs — defn",
      "url": "https://clojuredocs.org/clojure.core/defn"
    },
    {
      "title": "Clojure — Destructuring",
      "url": "https://clojure.org/guides/destructuring"
    }
  ]
}
---

# CLOJURE-05-FUNCTIONS: Functions

## Introduction

Anonymous functions, defn, arities, and destructuring. By the end of this lesson you will be able to: Write anonymous functions; Define named functions; Use multiple arities; Destructure collections.

## Key Concepts

### 1. Write anonymous functions

Target: Write anonymous functions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; Anonymous functions
(println ((fn [x] (* x x)) 6))       ; 36
(println (#(* % %) 7))               ; 49 — #() reader shorthand
(println (map #(* % 2) [1 2 3]))     ; (2 4 6)
;; % is the first arg, %2 the second, %& the rest.
```
### 2. Define named functions

Target: Define named functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; Named functions with defn
(defn square [x]
  (* x x))

(defn add [a b]
  (+ a b))

(println (square 5))        ; 25
(println (add 3 4))         ; 7
;; Last expression is the return value — no return keyword.
```
### 3. Use multiple arities

Target: Use multiple arities. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; Multi-arity functions
(defn greet
  ([name] (str "Hello, " name "!"))
  ([greeting name] (str greeting ", " name "!")))

(println (greet "Alice"))        ; Hello, Alice!
(println (greet "Hey" "Bob"))    ; Hey, Bob!
;; Each arity is its own clause with its own params.
```
### 4. Destructure collections

Target: Destructure collections. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; Destructuring: pull values out of collections
(defn describe [[a b c]]
  (str a " + " b " + " c))

(println (describe [1 2 3]))     ; 1 + 2 + 3

(defn person-info [{:keys [name age]}]
  (str name " is " age))

(println (person-info {:name "Alice" :age 30}))
;; Alice is 30
```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
