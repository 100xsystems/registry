---
{
  "title": "Macros and the Ecosystem",
  "description": "Macros, quote/unquote, Ring/Compojure, and the community.",
  "type": "lesson",
  "order": 21,
  "duration": "75 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Write macros",
    "Use quote and unquote",
    "Build web apps",
    "Navigate the ecosystem"
  ],
  "knowledge_refs": [
    "clojure/clojure-21-macros"
  ],
  "prerequisites": [
    "CLOJURE-20"
  ],
  "references": [
    {
      "title": "Clojure — Macros",
      "url": "https://clojure.org/reference/macros"
    },
    {
      "title": "Ring — GitHub",
      "url": "https://github.com/ring-clojure/ring"
    },
    {
      "title": "Clojure — Libraries",
      "url": "https://clojure.org/community/libraries"
    }
  ]
}
---

# CLOJURE-21-MACROS: Macros and the Ecosystem

## Introduction

Macros, quote/unquote, Ring/Compojure, and the community. By the end of this lesson you will be able to: Write macros; Use quote and unquote; Build web apps; Navigate the ecosystem.

## Key Concepts

### 1. Write macros

Target: Write macros. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; Macros: code that writes code
(defmacro unless [test & body]
  `(if (not ~test)
     (do ~@body)))

(unless false
  (println "unless runs when false"))
;; Macros receive unevaluated forms and return code.
```
### 2. Use quote and unquote

Target: Use quote and unquote. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; quote, syntax-quote, unquote
(println '(+ 1 2))          ; (+ 1 2) — quoted, not evaluated
(println `(1 2 3))          ; (1 2 3) — syntax-quoted, namespaced
(let [x 42]
  (println `(value ~x)))    ; (user/value 42) — unquoted in
;; ~ injects a value; ~@ splices a list into a form.
```
### 3. Build web apps

Target: Build web apps. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; Web apps with Ring and Compojure
;; Ring: the HTTP abstraction (request map -> response map)
;; (defn handler [request]
;;   {:status 200
;;    :headers {"Content-Type" "text/html"}
;;    :body "<h1>Hello</h1>"})
;; Compojure adds routing on top of Ring.
(println "Ring + Compojure = web apps")
```
### 4. Navigate the ecosystem

Target: Navigate the ecosystem. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; The ecosystem at a glance
;; - Ring/Compojure: HTTP and routing
;; - Reitit: modern data-driven routing
;; - ClojureScript + Reagent: frontend on React
;; - next.jdbc: database access
;; - core.async: CSP-style channels
;; - clj-kondo: linter; clojure-lsp: editor tooling
(println "A rich, pragmatic ecosystem around the JVM")
```

## Practice Questions

1. What is the key idea behind "Macros and the Ecosystem"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Macros and the Ecosystem with analogies and real-world examples"
1. "Show me common mistakes beginners make with Macros and the Ecosystem"
1. "Provide advanced patterns and performance considerations for Macros and the Ecosystem"

## Key Takeaways

- Master the core ideas of Macros and the Ecosystem through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
