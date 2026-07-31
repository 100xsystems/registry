---
{
  "title": "Binding and Scope",
  "description": "def, let, destructuring, and scope rules.",
  "type": "lesson",
  "order": 13,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define with def",
    "Bind locally with let",
    "Destructure in let",
    "Compare def and let scope"
  ],
  "knowledge_refs": [
    "clojure/clojure-13-scope"
  ],
  "prerequisites": [
    "CLOJURE-12"
  ],
  "references": [
    {
      "title": "Clojure — let",
      "url": "https://clojure.org/reference/special_forms#let"
    },
    {
      "title": "ClojureDocs — let",
      "url": "https://clojuredocs.org/clojure.core/let"
    },
    {
      "title": "Clojure — Special Forms",
      "url": "https://clojure.org/reference/special_forms"
    }
  ]
}
---

# CLOJURE-13-SCOPE: Binding and Scope

## Introduction

def, let, destructuring, and scope rules. By the end of this lesson you will be able to: Define with def; Bind locally with let; Destructure in let; Compare def and let scope.

## Key Concepts

### 1. Define with def

Target: Define with def. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; def: top-level values
(def pi 3.14159)
(def greeting "Hello")

(println pi)         ; 3.14159
(println greeting)   ; Hello
;; def binds a value to a global name in the namespace.
```
### 2. Bind locally with let

Target: Bind locally with let. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; let: local bindings
(let [x 10
      y 20]
  (println (+ x y)))   ; 30
;; bindings are sequential; later ones see earlier ones.
(let [a 1 b 2] (println a b))  ; 1 2
```
### 3. Destructure in let

Target: Destructure in let. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; let with destructuring
(let [[a b] [1 2]
      {:keys [name age]} {:name "Alice" :age 30}]
  (println a b name age))
;; 1 2 Alice 30
;; let is the workhorse for local scope.
```
### 4. Compare def and let scope

Target: Compare def and let scope. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; def vs let: scope
(def global-x 10)    ; namespace-wide

(defn scoped []
  (let [local-x 20]  ; function-local
    (+ global-x local-x)))

(println (scoped))   ; 30
;; local-x is invisible outside the function.
```

## Practice Questions

1. What is the key idea behind "Binding and Scope"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Binding and Scope with analogies and real-world examples"
1. "Show me common mistakes beginners make with Binding and Scope"
1. "Provide advanced patterns and performance considerations for Binding and Scope"

## Key Takeaways

- Master the core ideas of Binding and Scope through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
