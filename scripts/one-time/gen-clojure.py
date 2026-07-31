#!/usr/bin/env python3
"""Generate the 21-lesson Clojure curriculum at Python/JS/Java depth.
Uses the shared gen_lib template. Exact refs from clojure.org docs.
Each lesson has 4 sub-topics, each with its OWN distinct code sample.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from gen_lib import main as run_gen  # noqa: E402

LANGUAGE = 'clojure'

BASE = os.path.join(os.path.dirname(__file__), '..', '..', 'static-data', 'knowledge', 'languages', 'clojure')

CODE = {
    1: [
        ''';; Your first Clojure program
(println "Hello, 100X Systems!")
;; run: clojure -M hello.clj   ->   Hello, 100X Systems!
;; or with Leiningen: lein run''',
        ''';; The REPL: interactive exploration
;; user=> (+ 1 2)
;; 3
;; user=> (str "Hello" " " "Clojure")
;; "Hello Clojure"
(println (* 6 7))   ; 42 — everything is a prefix expression''',
        ''';; Forms: code is data (homoiconic)
(println (+ 1 2 3))        ; 6 — function call
(println '(1 2 3))         ; (1 2 3) — quoted list, NOT a call
(println :keyword)         ; :keyword — a keyword literal
(println {:a 1 :b 2})      ; {:a 1, :b 2} — a map literal
;; Clojure code IS Clojure data.''',
        ''';; Namespaces and the dot syntax for Java interop
(ns hello.core)

(defn greet [name]
  (str "Hello, " name "!"))

(println (greet "World"))
(println (.toUpperCase "clojure"))  ; CLOJURE — Java method call
(println (Math/sqrt 16))             ; 4.0 — Java static method''',
    ],
    2: [
        ''';; Immutable data structures
(def v [1 2 3])
(def v2 (conj v 4))        ; v2 = [1 2 3 4]
(println v)                ; [1 2 3] — original untouched
(println v2)
;; Every "modification" returns a NEW structure.''',
        ''';; Numbers, arithmetic, and division
(println (+ 1 2 3))    ; 6
(println (- 10 3))     ; 7
(println (* 2 3 4))    ; 24
(println (/ 10 2))     ; 5 — ratio preserved when exact
(println (/ 1 3))      ; 1/3 — Clojure keeps exact ratios
(println (quot 10 3))  ; 3 — integer division
(println (rem 10 3))   ; 1 — remainder
(println (inc 41))     ; 42
(println (dec 43))     ; 42''',
        ''';; Strings and keywords
(println (str "con" "cat"))      ; "concat"
(println (count "hello"))        ; 5
(println (subs "hello" 1 3))     ; "el"
(println (clojure.string/upper-case "hi"))  ; "HI"
(println (clojure.string/join ", " [1 2 3])) ; "1, 2, 3"
;; Keywords are fast, self-evaluating identifiers:
(println (keyword "user"))       ; :user
(println (name :user))           ; "user"''',
        ''';; Booleans, nil, and truthiness
(println true)     ; true
(println false)    ; false
(println nil)      ; nil
(println (if nil :truthy :falsy))  ; :falsy — nil is falsey
(println (if 0 :truthy :falsy))    ; :truthy — 0 IS truthy!
(println (if "" :truthy :falsy))   ; :truthy — empty string too
;; Only nil and false are falsey in Clojure.''',
    ],
    3: [
        ''';; if, if-not, when
(println (if (> 3 2) "yes" "no"))        ; yes
(println (if-not (> 3 2) "yes" "no"))    ; no
(when true
  (println "when runs")
  (println "multiple forms"))
;; when returns nil if the condition is false.''',
        ''';; cond: the else-if chain
(defn grade [score]
  (cond
    (>= score 90) "A"
    (>= score 75) "B"
    (>= score 50) "C"
    :else "D"))

(println (grade 85))   ; B
;; :else is just a truthy keyword — the catch-all.''',
        ''';; case: dispatch on constant values
(defn fruit-type [fruit]
  (case fruit
    :apple  "tree fruit"
    :banana "tropical"
    "unknown"))

(println (fruit-type :apple))    ; tree fruit
(println (fruit-type :mango))    ; unknown''',
        ''';; condp and predicate dispatch
(defn classify [n]
  (condp > n
    10 "small"
    100 "medium"
    "large"))

(println (classify 5))     ; small
(println (classify 50))    ; medium
(println (classify 500))   ; large
;; condp compares each value against the test expression.''',
    ],
    4: [
        ''';; Vectors: fast indexed access
(def v [10 20 30])
(println (nth v 1))          ; 20
(println (get v 2))          ; 30
(println (conj v 40))        ; [10 20 30 40] — appends to vector
(println (count v))          ; 3
(println (first v))          ; 10
(println (last v))           ; 30''',
        ''';; Lists: linked lists, fast prepend
(def lst '(1 2 3))
(println (first lst))        ; 1
(println (rest lst))         ; (2 3)
(println (conj lst 0))       ; (0 1 2 3) — PREPENDS to list
(println (count lst))        ; 3
;; Vectors conj at the end; lists conj at the front.''',
        ''';; Maps: key-value lookup
(def m {:name "Alice" :age 30})
(println (get m :name))        ; Alice
(println (m :age))             ; 30 — map as function!
(println (:name m))            ; Alice — keyword as function!
(println (assoc m :city "NYC"))
;; {:name "Alice", :age 30, :city "NYC"}
(println (dissoc m :age))      ; {:name "Alice"}
(println (contains? m :name))  ; true''',
        ''';; Sets: uniqueness and membership
(def s #{1 2 3})
(println (contains? s 2))      ; true
(println (conj s 4))           ; #{1 4 3 2}
(println (conj s 2))           ; #{1 3 2} — already there, no dup
(println (clojure.set/union #{1 2} #{2 3}))  ; #{1 3 2}
(println (clojure.set/intersection #{1 2 3} #{2 3 4})) ; #{3 2}''',
    ],
    5: [
        ''';; Anonymous functions
(println ((fn [x] (* x x)) 6))       ; 36
(println (#(* % %) 7))               ; 49 — #() reader shorthand
(println (map #(* % 2) [1 2 3]))     ; (2 4 6)
;; % is the first arg, %2 the second, %& the rest.''',
        ''';; Named functions with defn
(defn square [x]
  (* x x))

(defn add [a b]
  (+ a b))

(println (square 5))        ; 25
(println (add 3 4))         ; 7
;; Last expression is the return value — no return keyword.''',
        ''';; Multi-arity functions
(defn greet
  ([name] (str "Hello, " name "!"))
  ([greeting name] (str greeting ", " name "!")))

(println (greet "Alice"))        ; Hello, Alice!
(println (greet "Hey" "Bob"))    ; Hey, Bob!
;; Each arity is its own clause with its own params.''',
        ''';; Destructuring: pull values out of collections
(defn describe [[a b c]]
  (str a " + " b " + " c))

(println (describe [1 2 3]))     ; 1 + 2 + 3

(defn person-info [{:keys [name age]}]
  (str name " is " age))

(println (person-info {:name "Alice" :age 30}))
;; Alice is 30''',
    ],
    6: [
        ''';; Map, filter, reduce — the holy trinity
(println (map #(* % 2) [1 2 3]))        ; (2 4 6)
(println (filter even? [1 2 3 4]))      ; (2 4)
(println (reduce + [1 2 3 4]))          ; 10
(println (reduce #(str %1 %2) "" ["a" "b" "c"])) ; "abc"''',
        ''';; More sequence functions
(println (reduce + 100 [1 2 3]))    ; 106 — initial value
(println (map + [1 2] [10 20]))     ; (11 22) — multi-collection
(println (remove even? [1 2 3 4]))  ; (1 3)
(println (take 2 [1 2 3 4]))        ; (1 2)
(println (drop 2 [1 2 3 4]))        ; (3 4)
(println (sort [3 1 2]))            ; (1 2 3)
(println (reverse [1 2 3]))         ; (3 2 1)''',
        ''';; Threading macros: -> and ->>
(println (-> 5
            (* 2)
            (+ 1)))            ; 11 — threads as FIRST arg

(println (->> [3 1 2]
             (map inc)
             (filter even?)
             (reduce +)))      ; 6 — threads as LAST arg
;; ->> shines for sequence pipelines.''',
        ''';; reduce with an accumulator pattern
(defn word-count [words]
  (reduce (fn [acc w]
            (update acc w (fnil inc 0)))
          {}
          words))

(println (word-count ["a" "b" "a" "c" "a"]))
;; {"a" 3, "b" 1, "c" 1}''',
    ],
    7: [
        ''';; Recursion with loop/recur — tail-call optimized
(defn count-down [n]
  (loop [i n]
    (when (pos? i)
      (println i)
      (recur (dec i)))))

(count-down 3)
;; 3 2 1 — recur jumps to the loop, never grows the stack.''',
        ''';; Recursive functions with recur
(defn sum-to [n]
  (if (zero? n)
    0
    (+ n (sum-to (dec n)))))

(println (sum-to 100))   ; 5050
;; This version is NOT tail-recursive (the + wraps the call).''',
        ''';; Tail-recursive sum with an accumulator
(defn sum-acc [n]
  (loop [i n acc 0]
    (if (zero? i)
      acc
      (recur (dec i) (+ acc i)))))

(println (sum-acc 100))   ; 5050 — tail call optimized
;; recur must be in tail position.''',
        ''';; Building results with recur
(defn evens [coll]
  (loop [xs coll acc []]
    (if (empty? xs)
      acc
      (let [x (first xs)]
        (if (even? x)
          (recur (rest xs) (conj acc x))
          (recur (rest xs) acc))))))

(println (evens [1 2 3 4 5 6]))   ; [2 4 6]''',
    ],
    8: [
        ''';; Lazy sequences: compute on demand
(def naturals (iterate inc 1))
(println (take 5 naturals))        ; (1 2 3 4 5)
(println (take 5 (map #(* % %) naturals)))
;; (1 4 9 16 25) — infinite source, finite consumption''',
        ''';; Fibonacci as a lazy sequence
(def fibs
  (lazy-seq
    (cons 0
          (lazy-seq
            (cons 1
                  (map + fibs (rest fibs)))))))

(println (take 10 fibs))
;; (0 1 1 2 3 5 8 13 21 34)''',
        ''';; range, repeat, repeatedly
(println (range 5))          ; (0 1 2 3 4)
(println (take 3 (repeat :x)))   ; (:x :x :x)
(println (take 3 (repeatedly rand)))
;; three random doubles between 0 and 1''',
        ''';; Laziness in pipelines
(defn process [coll]
  (->> coll
       (map #(do (println "mapping" %) (* % %)))
       (filter even?)
       (take 2)))

;; process realizes ONLY as much as needed:
(println (process (range 10)))
;; prints "mapping" for 0, 1, 2 only — stops after 2 evens.''',
    ],
    9: [
        ''';; Keywords as functions for map lookup
(def m {:name "Alice" :age 30})
(println (:name m))             ; Alice
(println (:age m))              ; 30
(println (:city m :unknown))    ; :unknown — default value
(println (map :name [{:name "A"} {:name "B"}]))
;; ("A" "B") — pull a key from each map''',
        ''';; Update and merge maps
(def m {:count 0})
(println (update m :count inc))       ; {:count 1}
(println (update m :count + 5))       ; {:count 5}
(println (merge {:a 1} {:b 2}))       ; {:a 1, :b 2}
(println (merge-with + {:a 1} {:a 2})) ; {:a 3}
;; update applies a function to an existing key''',
        ''';; Nested map access and update
(def config {:db {:host "localhost" :port 5432}})
(println (get-in config [:db :host]))     ; localhost
(println (assoc-in config [:db :port] 5433))
;; {:db {:host "localhost", :port 5433}}
(println (update-in config [:db :port] inc))
;; {:db {:host "localhost", :port 5433}}
;; get-in/assoc-in/update-in navigate nested structures.''',
        ''';; Records: maps with a type
(defrecord Person [name age])

(def alice (->Person "Alice" 30))
(println (:name alice))        ; Alice
(println (assoc alice :age 31))
;; #user.Person{:name "Alice", :age 31}
(println (map? alice))         ; true — records ARE maps
;; defrecord gives you maps plus a type and protocols.''',
    ],
    10: [
        ''';; Error handling: the simple way
(defn safe-divide [a b]
  (if (zero? b)
    {:error "division by zero"}
    {:ok (/ a b)}))

(println (safe-divide 10 2))   ; {:ok 5}
(println (safe-divide 1 0))    ; {:error "division by zero"}''',
        ''';; Exceptions with try/catch
(defn risky []
  (try
    (/ 1 0)
    (catch ArithmeticException e
      (str "caught: " (.getMessage e)))))

(println (risky))
;; caught: Divide by zero''',
        ''';; The either pattern with nil
(defn parse-int [s]
  (try
    (Integer/parseInt s)
    (catch NumberFormatException _ nil)))

(println (parse-int "42"))    ; 42
(println (parse-int "abc"))   ; nil
;; nil signals failure; callers check with when-let/if-let.''',
        ''';; if-let and when-let: bind then branch
(defn maybe-name [m]
  (if-let [n (get m :name)]
    (str "Hello, " n)
    "anonymous"))

(println (maybe-name {:name "Alice"}))  ; Hello, Alice
(println (maybe-name {}))               ; anonymous
;; if-let binds once, tests truthiness, and shares the binding.''',
    ],
    11: [
        ''';; Atoms: thread-safe mutable references
(def counter (atom 0))
(swap! counter inc)
(swap! counter inc)
(println @counter)   ; 2 — deref with @
;; swap! applies a function atomically.''',
        ''';; Atoms: more operations
(def state (atom {:count 0}))
(swap! state update :count inc)
(swap! state update :count + 10)
(println @state)          ; {:count 11}
(reset! state {:count 0})
(println @state)          ; {:count 0}
(println (compare-and-set! state {:count 0} {:count 100}))
;; true — CAS-style update''',
        ''';; Refs: coordinated changes (STM)
(def account-a (ref 100))
(def account-b (ref 50))

(dosync
  (alter account-a - 30)
  (alter account-b + 30))

(println @account-a)   ; 70
(println @account-b)   ; 80
;; dosync retries until the whole transaction commits.''',
        ''';; Agents: asynchronous state updates
(def log-agent (agent []))
(send log-agent conj :started)
(send log-agent conj :finished)
(await log-agent)
(println @log-agent)   ; [:started :finished]
;; send queues actions; await blocks until they run.''',
    ],
    12: [
        ''';; Futures: parallel computation
(def f (future
         (Thread/sleep 100)
         (* 6 7)))

(println "computing in the background...")
(println @f)   ; 42 — deref blocks until the future completes''',
        ''';; Promises: deliver values manually
(def p (promise))
(future (Thread/sleep 100) (deliver p :done))
(println "waiting...")
(println @p)   ; :done — blocks until someone delivers''',
        ''';; pmap: parallel map
(defn slow-double [x]
  (Thread/sleep 50)
  (* x 2))

;; pmap runs the function across threads:
(time (doall (pmap slow-double (range 4))))
;; ~50ms for 4 items (serial would be ~200ms)''',
        ''';; Agents + futures for background work
(def results (agent []))
(future
  (send results conj :task-a)
  (send results conj :task-b))
(await results)
(println @results)
;; [:task-b :task-a] — order depends on scheduling''',
    ],
    13: [
        ''';; def: top-level values
(def pi 3.14159)
(def greeting "Hello")

(println pi)         ; 3.14159
(println greeting)   ; Hello
;; def binds a value to a global name in the namespace.''',
        ''';; let: local bindings
(let [x 10
      y 20]
  (println (+ x y)))   ; 30
;; bindings are sequential; later ones see earlier ones.
(let [a 1 b 2] (println a b))  ; 1 2''',
        ''';; let with destructuring
(let [[a b] [1 2]
      {:keys [name age]} {:name "Alice" :age 30}]
  (println a b name age))
;; 1 2 Alice 30
;; let is the workhorse for local scope.''',
        ''';; def vs let: scope
(def global-x 10)    ; namespace-wide

(defn scoped []
  (let [local-x 20]  ; function-local
    (+ global-x local-x)))

(println (scoped))   ; 30
;; local-x is invisible outside the function.''',
    ],
    14: [
        ''';; Higher-order functions: pass functions around
(defn apply-twice [f x]
  (f (f x)))

(println (apply-twice inc 5))        ; 7
(println (apply-twice #(* % 2) 3))   ; 12
;; Functions are first-class values.''',
        ''';; Function composition
(def add1 (comp inc))
(def double-then-add (comp inc #(* % 2)))

(println (double-then-add 5))   ; 11 — inc applied LAST
;; comp composes right-to-left: (inc (* 5 2)).
(println ((comp str inc) 41))   ; "42"''',
        ''';; Partial application
(def add-100 (partial + 100))
(println (add-100 1))        ; 101
(println (add-100 50))       ; 150

(def multiply (partial * 3))
(println (multiply 4))       ; 12
;; partial fixes the first args, returns a waiting function.''',
        ''';; Calling functions as data with apply
(println (apply + [1 2 3]))        ; 6
(println (apply max [3 9 4]))      ; 9
(println (apply str ["a" "b" "c"])) ; "abc"
;; apply spreads a collection across a function's args.''',
    ],
    15: [
        ''';; Namespaces: organising code
;; (ns my-app.core (:require [clojure.string :as str]))
(require '[clojure.string :as str])
(println (str/join "-" [2026 7 31]))   ; "2026-7-31"
(println (str/upper-case "hello"))     ; HELLO
;; Aliasing keeps namespaces concise.''',
        ''';; refer and refer-clojure
;; (use 'clojure.string) — avoid; use require instead.
(require '[clojure.set :refer [union intersection]])
(println (union #{1 2} #{3}))         ; #{1 3 2}
(println (intersection #{1 2 3} #{3})) ; #{3}
;; refer pulls specific symbols into scope.''',
        ''';; The classpath and project structure
;; src/my_app/core.clj       -> namespace my-app.core
;; test/my_app/core_test.clj -> tests
;; deps.edn lists dependencies:
;; {:deps {org.clojure/clojure {:mvn/version "1.11.1"}}}
(println "deps.edn manages dependencies and paths")''',
        ''';; Java interop: calling into the JVM
(println (System/currentTimeMillis))  ; epoch millis
(println (.length "hello"))           ; 5 — instance method
(println (Math/floor 3.7))            ; 3.0 — static method
(println (java.util.UUID/randomUUID))
;; a random UUID — full Java ecosystem available''',
    ],
    16: [
        ''';; Protocols: polymorphism on types
(defprotocol Shape
  (area [s])
  (perimeter [s]))

(defrecord Square [side]
  Shape
  (area [s] (* side side))
  (perimeter [s] (* 4 side)))

(println (area (->Square 4)))       ; 16
(println (perimeter (->Square 4)))  ; 16
;; defrecord implements the protocol for the new type.''',
        ''';; extend-type and extend-protocol
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
;; Extend protocols to existing types without modifying them.''',
        ''';; Core protocols in action
(println (seq [1 2 3]))      ; (1 2 3) — Seqable
(println (count {:a 1}))     ; 1 — Counted
(println (assoc {} :a 1))    ; {:a 1} — Associative
(println (conj #{} 1))       ; #{1} — Conjable
;; The core sequence functions all go through protocols.''',
        ''';; Multimethods: dispatch on anything
(defmulti area :shape)

(defmethod area :square [{:keys [side]}]
  (* side side))

(defmethod area :circle [{:keys [radius]}]
  (* Math/PI radius radius))

(println (area {:shape :square :side 4}))   ; 16
(println (area {:shape :circle :radius 2}))
;; 12.566370614359172 — dispatch on any value''',
    ],
    17: [
        ''';; lein and deps.edn tooling
;; lein new app my-app     -> project scaffold
;; lein repl               -> REPL with the project loaded
;; lein test               -> run tests
;; lein run                -> run the app
;; clojure -M:test         -> run tests via deps.edn aliases
(println "Leiningen and tools.deps manage Clojure projects")''',
        ''';; clojure.test: the built-in test library
(ns my-app.core-test
  (:require [clojure.test :refer [deftest is testing run-tests]]))

(deftest addition-test
  (testing "addition"
    (is (= 4 (+ 2 2)))
    (is (= 5 (+ 2 3)))))

(run-tests)
;; Ran 1 tests containing 2 assertions. 0 failures.''',
        ''';; Property-based and rich assertions
(deftest data-test
  (is (= {:a 1} {:a 1}))
  (is (even? 4))
  (is (thrown? ArithmeticException (/ 1 0))))

(run-tests)
;; is supports =, predicates, and thrown? — no special API.''',
        ''';; The REPL-driven workflow
;; Start a REPL, evaluate forms incrementally:
;;   (require 'my-app.core)
;;   (my-app.core/greet "REPL")
;;   (def x 42)  ; redefine as you explore
;; The REPL becomes the development environment itself.
(println "REPL-driven development is the Clojure workflow")''',
    ],
    18: [
        ''';; Clojure docs and docstrings
(defn square
  "Returns the square of a number."
  [x]
  (* x x))

(println (square 5))   ; 25
;; (doc square) in the REPL shows the docstring.
;; (source square) shows the source.''',
        ''';; Metadata: data about data
(def ^{:author "Alice" :added "1.0"} version "1.0.0")
(println (meta #'version))
;; {:author "Alice", :added "1.0"}
;; ^{:k v} attaches metadata to the following form.''',
        ''';; Comments and documentation conventions
;; ; single-line comment
;; #_ whole-form comment: #_(println "skipped")
(println "active line")
#_(println "never runs")
;; docstrings live above defn; cljdoc/autodoc build docs
(println "Comments use ; and #_")''',
        ''';; Debugging tools
(defn debug-demo [x]
  (println "x is:" x)      ; quick print
  (let [y (* x 2)]
    (println "y is:" y)
    (+ x y)))

(println (debug-demo 5))
;; x is: 5
;; y is: 10
;; 15
;; Libraries like clojure.tools.trace add deeper tracing.''',
    ],
    19: [
        ''';; Concurrency model overview
;; - Atoms: uncoordinated synchronous updates
;; - Refs: coordinated transactional updates (STM)
;; - Agents: asynchronous updates
;; - Futures/Promises: parallel computation and handoff
;; - Vars: dynamic, thread-local state
(println "Clojure's concurrency is built on immutable state")''',
        ''';; Dynamic vars: thread-local bindings
(def ^:dynamic *debug* false)

(defn log [msg]
  (when *debug*
    (println "DEBUG:" msg)))

(binding [*debug* true]
  (log "visible"))       ; DEBUG: visible
(log "hidden")           ; nothing — back to default''',
        ''';; The STM transaction
(def cart (ref []))
(dosync
  (alter cart conj :item-1)
  (alter cart conj :item-2))
(println @cart)   ; [:item-1 :item-2]
;; refs + dosync give multi-ref atomic updates.''',
        ''';; State vs identity: the Clojure philosophy
;; - Identity: a stable name (an atom, a ref)
;; - Value: the immutable snapshot at a moment (@atom)
;; - Change: swap! to a NEW value, never mutation
(def n (atom 0))
(swap! n + 1)
(swap! n + 1)
(println @n)   ; 2
;; n always refers to the atom; its VALUE changed twice.''',
    ],
    20: [
        ''';; A complete data pipeline
(require '[clojure.string :as str])

(defn analyze [text]
  (->> (str/split text #"\\s+")
       (map str/lower-case)
       frequencies
       (sort-by val >)
       (take 3)))

(println (analyze "the quick the brown the fox"))
;; (["the" 3] ["quick" 1] ["brown" 1])''',
        ''';; Map-reduce in Clojure
(def orders [{:id 1 :amount 100}
             {:id 2 :amount 50}
             {:id 3 :amount 200}])

(def total
  (->> orders
       (map :amount)
       (reduce +)))

(println total)   ; 350''',
        ''';; Grouping and counting
(def items [:a :b :a :c :a :b])

(println (frequencies items))
;; {:a 3, :b 2, :c 1}
(println (group-by even? [1 2 3 4]))
;; {false [1 3], true [2 4]}
(println (partition 2 [1 2 3 4 5 6]))
;; ((1 2) (3 4) (5 6))''',
        ''';; Data-driven configuration
(def config
  {:server {:port 8080
            :host "0.0.0.0"}
   :db {:url "postgres://localhost/app"
        :pool-size 10}})

(println (get-in config [:server :port]))    ; 8080
(println (get-in config [:db :pool-size]))   ; 10
;; Configuration as plain data — inspect, transform, merge.''',
    ],
    21: [
        ''';; Macros: code that writes code
(defmacro unless [test & body]
  `(if (not ~test)
     (do ~@body)))

(unless false
  (println "unless runs when false"))
;; Macros receive unevaluated forms and return code.''',
        ''';; quote, syntax-quote, unquote
(println '(+ 1 2))          ; (+ 1 2) — quoted, not evaluated
(println `(1 2 3))          ; (1 2 3) — syntax-quoted, namespaced
(let [x 42]
  (println `(value ~x)))    ; (user/value 42) — unquoted in
;; ~ injects a value; ~@ splices a list into a form.''',
        ''';; Web apps with Ring and Compojure
;; Ring: the HTTP abstraction (request map -> response map)
;; (defn handler [request]
;;   {:status 200
;;    :headers {"Content-Type" "text/html"}
;;    :body "<h1>Hello</h1>"})
;; Compojure adds routing on top of Ring.
(println "Ring + Compojure = web apps")''',
        ''';; The ecosystem at a glance
;; - Ring/Compojure: HTTP and routing
;; - Reitit: modern data-driven routing
;; - ClojureScript + Reagent: frontend on React
;; - next.jdbc: database access
;; - core.async: CSP-style channels
;; - clj-kondo: linter; clojure-lsp: editor tooling
(println "A rich, pragmatic ecosystem around the JVM")''',
    ],
}

LESSONS = [
    dict(slug='clojure-01-getting-started', title='Getting Started with Clojure',
         desc='Installation, the REPL, forms, namespaces, and Java interop.',
         dur='45 min', diff='beginner', prereq=[],
         objs=['Write and run a Clojure program',
               'Explore with the REPL',
               'Understand forms as data',
               'Use namespaces and Java interop'],
         refs=[dict(title='Clojure — Getting Started', url='https://clojure.org/guides/getting_started'),
               dict(title='Clojure — Reference', url='https://clojure.org/reference'),
               dict(title='Clojure — REPL and Main', url='https://clojure.org/guides/repl/basics')]),
    dict(slug='clojure-02-values-types', title='Values, Types, and Immutability',
         desc='Immutable data, numbers, strings, keywords, and truthiness.',
         dur='45 min', diff='beginner', prereq=['CLOJURE-01'],
         objs=['Use immutable data structures',
               'Do arithmetic with ratios',
               'Manipulate strings and keywords',
               'Understand truthiness'],
         refs=[dict(title='Clojure — Data Structures', url='https://clojure.org/reference/data_structures'),
               dict(title='Clojure — Special Forms (if)', url='https://clojure.org/reference/special_forms'),
               dict(title='ClojureDocs — str', url='https://clojuredocs.org/clojure.core/str')]),
    dict(slug='clojure-03-control-flow', title='Control Flow',
         desc='if, when, cond, case, and condp.',
         dur='45 min', diff='beginner', prereq=['CLOJURE-02'],
         objs=['Branch with if and when',
               'Chain with cond',
               'Dispatch with case',
               'Compare with condp'],
         refs=[dict(title='Clojure — Control Flow', url='https://clojure.org/guides/learn/flow'),
               dict(title='ClojureDocs — cond', url='https://clojuredocs.org/clojure.core/cond'),
               dict(title='ClojureDocs — case', url='https://clojuredocs.org/clojure.core/case')]),
    dict(slug='clojure-04-collections', title='Collections',
         desc='Vectors, lists, maps, and sets — the four core structures.',
         dur='60 min', diff='intermediate', prereq=['CLOJURE-03'],
         objs=['Use vectors for indexed access',
               'Use lists for linked sequences',
               'Look up and update maps',
               'Test set membership'],
         refs=[dict(title='Clojure — Collections', url='https://clojure.org/reference/data_structures#Collections'),
               dict(title='ClojureDocs — assoc', url='https://clojuredocs.org/clojure.core/assoc'),
               dict(title='ClojureDocs — conj', url='https://clojuredocs.org/clojure.core/conj')]),
    dict(slug='clojure-05-functions', title='Functions',
         desc='Anonymous functions, defn, arities, and destructuring.',
         dur='60 min', diff='intermediate', prereq=['CLOJURE-04'],
         objs=['Write anonymous functions',
               'Define named functions',
               'Use multiple arities',
               'Destructure collections'],
         refs=[dict(title='Clojure — Functions', url='https://clojure.org/guides/learn/functions'),
               dict(title='ClojureDocs — defn', url='https://clojuredocs.org/clojure.core/defn'),
               dict(title='Clojure — Destructuring', url='https://clojure.org/guides/destructuring')]),
    dict(slug='clojure-06-sequences', title='Sequences and Transforms',
         desc='map, filter, reduce, threading macros, and the seq abstraction.',
         dur='60 min', diff='intermediate', prereq=['CLOJURE-05'],
         objs=['Transform with map/filter/reduce',
               'Use more sequence functions',
               'Thread with -> and ->>',
               'Accumulate with reduce'],
         refs=[dict(title='Clojure — Sequences', url='https://clojure.org/reference/sequences'),
               dict(title='ClojureDocs — reduce', url='https://clojuredocs.org/clojure.core/reduce'),
               dict(title='ClojureDocs — ->>', url='https://clojuredocs.org/clojure.core/-%3E%3E')]),
    dict(slug='clojure-07-recursion', title='Recursion',
         desc='loop/recur, tail calls, and building results.',
         dur='60 min', diff='intermediate', prereq=['CLOJURE-06'],
         objs=['Loop with loop/recur',
               'Write recursive functions',
               'Use tail-call optimization',
               'Build results with recur'],
         refs=[dict(title='Clojure — loop/recur', url='https://clojure.org/reference/special_forms#recur'),
               dict(title='ClojureDocs — recur', url='https://clojuredocs.org/clojure.core/recur'),
               dict(title='ClojureDocs — loop', url='https://clojuredocs.org/clojure.core/loop')]),
    dict(slug='clojure-08-lazy-seq', title='Lazy Sequences',
         desc='Laziness, infinite sequences, and on-demand computation.',
         dur='75 min', diff='advanced', prereq=['CLOJURE-07'],
         objs=['Build lazy sequences',
               'Create Fibonacci lazily',
               'Use range/repeat/repeatedly',
               'Control realization'],
         refs=[dict(title='Clojure — Laziness', url='https://clojure.org/reference/lazy'),
               dict(title='ClojureDocs — lazy-seq', url='https://clojuredocs.org/clojure.core/lazy-seq'),
               dict(title='ClojureDocs — repeatedly', url='https://clojuredocs.org/clojure.core/repeatedly')]),
    dict(slug='clojure-09-maps', title='Maps in Depth',
         desc='Keywords as functions, update/merge, nested access, records.',
         dur='60 min', diff='intermediate', prereq=['CLOJURE-08'],
         objs=['Use keywords as functions',
               'Update and merge maps',
               'Navigate nested maps',
               'Define records'],
         refs=[dict(title='Clojure — Maps', url='https://clojure.org/reference/data_structures#Maps'),
               dict(title='ClojureDocs — update', url='https://clojuredocs.org/clojure.core/update'),
               dict(title='ClojureDocs — get-in', url='https://clojuredocs.org/clojure.core/get-in')]),
    dict(slug='clojure-10-error-handling', title='Error Handling',
         desc='Result maps, try/catch, nil, and if-let patterns.',
         dur='60 min', diff='intermediate', prereq=['CLOJURE-09'],
         objs=['Return error values',
               'Catch exceptions',
               'Use the nil either pattern',
               'Bind with if-let/when-let'],
         refs=[dict(title='Clojure — Exceptions', url='https://clojure.org/reference/special_forms#try'),
               dict(title='ClojureDocs — if-let', url='https://clojuredocs.org/clojure.core/if-let'),
               dict(title='ClojureDocs — when-let', url='https://clojuredocs.org/clojure.core/when-let')]),
    dict(slug='clojure-11-atoms-refs-agents', title='Atoms, Refs, and Agents',
         desc='Synchronous atoms, coordinated refs, and async agents.',
         dur='75 min', diff='advanced', prereq=['CLOJURE-10'],
         objs=['Mutate with atoms',
               'Coordinate with refs and dosync',
               'Update asynchronously with agents',
               'Choose the right reference type'],
         refs=[dict(title='Clojure — Atoms', url='https://clojure.org/reference/atoms'),
               dict(title='Clojure — Refs and Transactions', url='https://clojure.org/reference/refs'),
               dict(title='Clojure — Agents', url='https://clojure.org/reference/agents')]),
    dict(slug='clojure-12-futures-promises', title='Futures, Promises, and Parallelism',
         desc='Future, promise, pmap, and background tasks.',
         dur='75 min', diff='advanced', prereq=['CLOJURE-11'],
         objs=['Compute with futures',
               'Deliver with promises',
               'Parallelize with pmap',
               'Orchestrate background work'],
         refs=[dict(title='ClojureDocs — future', url='https://clojuredocs.org/clojure.core/future'),
               dict(title='ClojureDocs — promise', url='https://clojuredocs.org/clojure.core/promise'),
               dict(title='ClojureDocs — pmap', url='https://clojuredocs.org/clojure.core/pmap')]),
    dict(slug='clojure-13-scope', title='Binding and Scope',
         desc='def, let, destructuring, and scope rules.',
         dur='60 min', diff='intermediate', prereq=['CLOJURE-12'],
         objs=['Define with def',
               'Bind locally with let',
               'Destructure in let',
               'Compare def and let scope'],
         refs=[dict(title='Clojure — let', url='https://clojure.org/reference/special_forms#let'),
               dict(title='ClojureDocs — let', url='https://clojuredocs.org/clojure.core/let'),
               dict(title='Clojure — Special Forms', url='https://clojure.org/reference/special_forms')]),
    dict(slug='clojure-14-higher-order', title='Higher-Order Functions',
         desc='First-class functions, composition, partial, apply.',
         dur='60 min', diff='intermediate', prereq=['CLOJURE-13'],
         objs=['Pass functions as values',
               'Compose functions',
               'Partially apply functions',
               'Spread with apply'],
         refs=[dict(title='ClojureDocs — comp', url='https://clojuredocs.org/clojure.core/comp'),
               dict(title='ClojureDocs — partial', url='https://clojuredocs.org/clojure.core/partial'),
               dict(title='ClojureDocs — apply', url='https://clojuredocs.org/clojure.core/apply')]),
    dict(slug='clojure-15-namespaces', title='Namespaces and Interop',
         desc='require, refer, project layout, and Java interop.',
         dur='60 min', diff='intermediate', prereq=['CLOJURE-14'],
         objs=['Require and alias namespaces',
               'Refer specific symbols',
               'Structure the classpath',
               'Call into the JVM'],
         refs=[dict(title='Clojure — Namespaces', url='https://clojure.org/reference/namespaces'),
               dict(title='Clojure — Java Interop', url='https://clojure.org/reference/java_interop'),
               dict(title='Clojure — deps.edn', url='https://clojure.org/guides/deps_and_cli')]),
    dict(slug='clojure-16-protocols', title='Protocols and Multimethods',
         desc='Protocols, extend-type, records, and multimethods.',
         dur='75 min', diff='advanced', prereq=['CLOJURE-15'],
         objs=['Define protocols',
               'Extend existing types',
               'Use core protocols',
               'Dispatch with multimethods'],
         refs=[dict(title='Clojure — Protocols', url='https://clojure.org/reference/protocols'),
               dict(title='Clojure — Multimethods', url='https://clojure.org/reference/multimethods'),
               dict(title='ClojureDocs — defrecord', url='https://clojuredocs.org/clojure.core/defrecord')]),
    dict(slug='clojure-17-tooling', title='Tooling and Testing',
         desc='Leiningen, deps.edn, clojure.test, and the REPL workflow.',
         dur='60 min', diff='intermediate', prereq=['CLOJURE-16'],
         objs=['Manage projects with Leiningen',
               'Write clojure.test tests',
               'Assert with is',
               'Develop REPL-driven'],
         refs=[dict(title='Leiningen — Getting Started', url='https://leiningen.org/'),
               dict(title='Clojure — clojure.test', url='https://clojure.github.io/clojure/clojure.test-api.html'),
               dict(title='Clojure — REPL workflow', url='https://clojure.org/guides/repl/guidelines')]),
    dict(slug='clojure-18-docs-meta', title='Documentation and Metadata',
         desc='Docstrings, metadata, comments, and debugging.',
         dur='60 min', diff='intermediate', prereq=['CLOJURE-17'],
         objs=['Write docstrings',
               'Attach metadata',
               'Comment and document',
               'Debug with prints'],
         refs=[dict(title='Clojure — Metadata', url='https://clojure.org/reference/metadata'),
               dict(title='ClojureDocs — meta', url='https://clojuredocs.org/clojure.core/meta'),
               dict(title='Clojure — Documentation conventions', url='https://clojure.org/guides/contributing')]),
    dict(slug='clojure-19-concurrency', title='Concurrency in Depth',
         desc='The concurrency model, dynamic vars, STM, and identity.',
         dur='75 min', diff='advanced', prereq=['CLOJURE-18'],
         objs=['Compare reference types',
               'Use dynamic vars',
               'Run STM transactions',
               'Reason about identity vs value'],
         refs=[dict(title='Clojure — Concurrency', url='https://clojure.org/reference/concurrency_and_parallelism'),
               dict(title='ClojureDocs — binding', url='https://clojuredocs.org/clojure.core/binding'),
               dict(title='ClojureDocs — dosync', url='https://clojuredocs.org/clojure.core/dosync')]),
    dict(slug='clojure-20-pipelines', title='Real-World Data Pipelines',
         desc='Text analysis, map-reduce, grouping, and config as data.',
         dur='75 min', diff='advanced', prereq=['CLOJURE-19'],
         objs=['Analyse text with threads',
               'Compute totals with reduce',
               'Group and count data',
               'Model configuration as data'],
         refs=[dict(title='ClojureDocs — frequencies', url='https://clojuredocs.org/clojure.core/frequencies'),
               dict(title='ClojureDocs — group-by', url='https://clojuredocs.org/clojure.core/group-by'),
               dict(title='ClojureDocs — get-in', url='https://clojuredocs.org/clojure.core/get-in')]),
    dict(slug='clojure-21-macros', title='Macros and the Ecosystem',
         desc='Macros, quote/unquote, Ring/Compojure, and the community.',
         dur='75 min', diff='expert', prereq=['CLOJURE-20'],
         objs=['Write macros',
               'Use quote and unquote',
               'Build web apps',
               'Navigate the ecosystem'],
         refs=[dict(title='Clojure — Macros', url='https://clojure.org/reference/macros'),
               dict(title='Ring — GitHub', url='https://github.com/ring-clojure/ring'),
               dict(title='Clojure — Libraries', url='https://clojure.org/community/libraries')]),
]


if __name__ == '__main__':
    run_gen(LANGUAGE, 'clojure', LESSONS, CODE, BASE)
