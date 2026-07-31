---
{
  "title": "Real-World Data Pipelines",
  "description": "Text analysis, map-reduce, grouping, and config as data.",
  "type": "lesson",
  "order": 20,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Analyse text with threads",
    "Compute totals with reduce",
    "Group and count data",
    "Model configuration as data"
  ],
  "knowledge_refs": [
    "clojure/clojure-20-pipelines"
  ],
  "prerequisites": [
    "CLOJURE-19"
  ],
  "references": [
    {
      "title": "ClojureDocs — frequencies",
      "url": "https://clojuredocs.org/clojure.core/frequencies"
    },
    {
      "title": "ClojureDocs — group-by",
      "url": "https://clojuredocs.org/clojure.core/group-by"
    },
    {
      "title": "ClojureDocs — get-in",
      "url": "https://clojuredocs.org/clojure.core/get-in"
    }
  ]
}
---

# CLOJURE-20-PIPELINES: Real-World Data Pipelines

## Introduction

Text analysis, map-reduce, grouping, and config as data. By the end of this lesson you will be able to: Analyse text with threads; Compute totals with reduce; Group and count data; Model configuration as data.

## Key Concepts

### 1. Analyse text with threads

Target: Analyse text with threads. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```clojure
;; A complete data pipeline
(require '[clojure.string :as str])

(defn analyze [text]
  (->> (str/split text #"\s+")
       (map str/lower-case)
       frequencies
       (sort-by val >)
       (take 3)))

(println (analyze "the quick the brown the fox"))
;; (["the" 3] ["quick" 1] ["brown" 1])
```
### 2. Compute totals with reduce

Target: Compute totals with reduce. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```clojure
;; Map-reduce in Clojure
(def orders [{:id 1 :amount 100}
             {:id 2 :amount 50}
             {:id 3 :amount 200}])

(def total
  (->> orders
       (map :amount)
       (reduce +)))

(println total)   ; 350
```
### 3. Group and count data

Target: Group and count data. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```clojure
;; Grouping and counting
(def items [:a :b :a :c :a :b])

(println (frequencies items))
;; {:a 3, :b 2, :c 1}
(println (group-by even? [1 2 3 4]))
;; {false [1 3], true [2 4]}
(println (partition 2 [1 2 3 4 5 6]))
;; ((1 2) (3 4) (5 6))
```
### 4. Model configuration as data

Target: Model configuration as data. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```clojure
;; Data-driven configuration
(def config
  {:server {:port 8080
            :host "0.0.0.0"}
   :db {:url "postgres://localhost/app"
        :pool-size 10}})

(println (get-in config [:server :port]))    ; 8080
(println (get-in config [:db :pool-size]))   ; 10
;; Configuration as plain data — inspect, transform, merge.
```

## Practice Questions

1. What is the key idea behind "Real-World Data Pipelines"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Real-World Data Pipelines with analogies and real-world examples"
1. "Show me common mistakes beginners make with Real-World Data Pipelines"
1. "Provide advanced patterns and performance considerations for Real-World Data Pipelines"

## Key Takeaways

- Master the core ideas of Real-World Data Pipelines through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
