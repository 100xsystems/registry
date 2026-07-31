---
{
  "title": "Documentation and Metadata",
  "description": "Docstrings, metadata, comments, and debugging.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write docstrings",
    "Attach metadata",
    "Comment and document",
    "Debug with prints"
  ],
  "knowledge_refs": [
    "clojure/clojure-18-docs-meta"
  ],
  "prerequisites": [
    "CLOJURE-17"
  ],
  "references": [
    {
      "title": "Clojure — Metadata",
      "url": "https://clojure.org/reference/metadata"
    },
    {
      "title": "ClojureDocs — meta",
      "url": "https://clojuredocs.org/clojure.core/meta"
    },
    {
      "title": "Clojure — Documentation conventions",
      "url": "https://clojure.org/guides/contributing"
    }
  ]
}
---

# CLOJURE-18-DOCS-META: Documentation and Metadata

## Introduction

Docstrings, metadata, comments, and debugging. By the end of this lesson you will be able to: Write docstrings; Attach metadata; Comment and document; Debug with prints.

## Key Concepts

### 1. Write docstrings

Target: Write docstrings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; Clojure docs and docstrings
(defn square
  "Returns the square of a number."
  [x]
  (* x x))

(println (square 5))   ; 25
;; (doc square) in the REPL shows the docstring.
;; (source square) shows the source.
```
### 2. Attach metadata

Target: Attach metadata. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; Metadata: data about data
(def ^{:author "Alice" :added "1.0"} version "1.0.0")
(println (meta #'version))
;; {:author "Alice", :added "1.0"}
;; ^{:k v} attaches metadata to the following form.
```
### 3. Comment and document

Target: Comment and document. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; Comments and documentation conventions
;; ; single-line comment
;; #_ whole-form comment: #_(println "skipped")
(println "active line")
#_(println "never runs")
;; docstrings live above defn; cljdoc/autodoc build docs
(println "Comments use ; and #_")
```
### 4. Debug with prints

Target: Debug with prints. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; Debugging tools
(defn debug-demo [x]
  (println "x is:" x)      ; quick print
  (let [y (* x 2)]
    (println "y is:" y)
    (+ x y)))

(println (debug-demo 5))
;; x is: 5
;; y is: 10
;; 15
;; Libraries like clojure.tools.trace add deeper tracing.
```

## Practice Questions

1. What is the key idea behind "Documentation and Metadata"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Documentation and Metadata with analogies and real-world examples"
1. "Show me common mistakes beginners make with Documentation and Metadata"
1. "Provide advanced patterns and performance considerations for Documentation and Metadata"

## Key Takeaways

- Master the core ideas of Documentation and Metadata through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
