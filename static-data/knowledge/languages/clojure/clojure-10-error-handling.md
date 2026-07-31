---
{
  "title": "Error Handling",
  "description": "Result maps, try/catch, nil, and if-let patterns.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Return error values",
    "Catch exceptions",
    "Use the nil either pattern",
    "Bind with if-let/when-let"
  ],
  "knowledge_refs": [
    "clojure/clojure-10-error-handling"
  ],
  "prerequisites": [
    "CLOJURE-09"
  ],
  "references": [
    {
      "title": "Clojure — Exceptions",
      "url": "https://clojure.org/reference/special_forms#try"
    },
    {
      "title": "ClojureDocs — if-let",
      "url": "https://clojuredocs.org/clojure.core/if-let"
    },
    {
      "title": "ClojureDocs — when-let",
      "url": "https://clojuredocs.org/clojure.core/when-let"
    }
  ]
}
---

# CLOJURE-10-ERROR-HANDLING: Error Handling

## Introduction

Result maps, try/catch, nil, and if-let patterns. By the end of this lesson you will be able to: Return error values; Catch exceptions; Use the nil either pattern; Bind with if-let/when-let.

## Key Concepts

### 1. Return error values

Target: Return error values. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; Error handling: the simple way
(defn safe-divide [a b]
  (if (zero? b)
    {:error "division by zero"}
    {:ok (/ a b)}))

(println (safe-divide 10 2))   ; {:ok 5}
(println (safe-divide 1 0))    ; {:error "division by zero"}
```
### 2. Catch exceptions

Target: Catch exceptions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; Exceptions with try/catch
(defn risky []
  (try
    (/ 1 0)
    (catch ArithmeticException e
      (str "caught: " (.getMessage e)))))

(println (risky))
;; caught: Divide by zero
```
### 3. Use the nil either pattern

Target: Use the nil either pattern. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; The either pattern with nil
(defn parse-int [s]
  (try
    (Integer/parseInt s)
    (catch NumberFormatException _ nil)))

(println (parse-int "42"))    ; 42
(println (parse-int "abc"))   ; nil
;; nil signals failure; callers check with when-let/if-let.
```
### 4. Bind with if-let/when-let

Target: Bind with if-let/when-let. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; if-let and when-let: bind then branch
(defn maybe-name [m]
  (if-let [n (get m :name)]
    (str "Hello, " n)
    "anonymous"))

(println (maybe-name {:name "Alice"}))  ; Hello, Alice
(println (maybe-name {}))               ; anonymous
;; if-let binds once, tests truthiness, and shares the binding.
```

## Practice Questions

1. What is the key idea behind "Error Handling"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Error Handling with analogies and real-world examples"
1. "Show me common mistakes beginners make with Error Handling"
1. "Provide advanced patterns and performance considerations for Error Handling"

## Key Takeaways

- Master the core ideas of Error Handling through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
