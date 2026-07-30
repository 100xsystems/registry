---
{
  "title": "Stream API Deep Dive",
  "description": "Build stream pipelines with intermediate/terminal ops",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Build stream pipelines with intermediate/terminal ops",
    "Collect results with Collectors groupingBy, partitioningBy",
    "Use reduce for custom aggregation",
    "Understand stream laziness and parallel streams"
  ],
  "knowledge_refs": [
    "java/java-11-streams-deep"
  ],
  "prerequisites": [
    "JV-05",
    "JV-06"
  ],
  "references": [
    {
      "title": "Oracle Tutorial — Streams",
      "url": "https://docs.oracle.com/javase/tutorial/collections/streams/index.html"
    },
    {
      "title": "Oracle Docs — Collectors",
      "url": "https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/stream/Collectors.html"
    },
    {
      "title": "Baeldung — Streams Guide",
      "url": "https://www.baeldung.com/java-streams"
    },
    {
      "title": "Baeldung — Stream API",
      "url": "https://www.baeldung.com/java-8-streams"
    }
  ]
}
---

# JAVA-11-STREAMS-DEEP: Stream API Deep Dive

## Introduction

The Stream API enables functional-style data processing. Pipelines consist of a source, zero or more intermediate operations (lazy), and a terminal operation (eager). Streams are single-use, parallelizable, and optimized.

## Key Concepts

### 1. Stream Pipeline: Source -> Intermediate -> Terminal

Streams from collections (.stream()), arrays (Arrays.stream()), or generators (Stream.of, iterate). Intermediate ops: filter, map, sorted, distinct, limit, skip. Terminal ops: collect, forEach, reduce, count, anyMatch.

```java
List<String> names = List.of("Alice", "Bob", "Charlie", "David", "Eve");

// Complete pipeline
List<String> result = names.stream()
    .filter(s -> s.length() > 3)       // intermediate
    .map(String::toUpperCase)           // intermediate
    .sorted(Comparator.reverseOrder())  // intermediate
    .limit(3)                           // intermediate
    .collect(Collectors.toList());      // terminal

// Short-circuit operations
boolean anyMatch = names.stream().anyMatch(s -> s.startsWith("A"));
Optional<String> first = names.stream().findFirst();
long count = names.stream().filter(s -> s.length() > 3).count();
```

### 2. Collectors: groupingBy, partitioningBy, toMap

Collectors.groupingBy classifies by classifier function. partitioningBy for boolean predicates. toMap for custom key-value mapping. downstream collectors: counting, summingInt, mapping, reducing.

```java
List<Person> people = getPeople();

// Group by city
Map<String, List<Person>> byCity = people.stream()
    .collect(Collectors.groupingBy(Person::getCity));

// Group with downstream (count per city)
Map<String, Long> countByCity = people.stream()
    .collect(Collectors.groupingBy(Person::getCity, Collectors.counting()));

// Partition by age (adult/minor)
Map<Boolean, List<Person>> byAdult = people.stream()
    .collect(Collectors.partitioningBy(p -> p.getAge() >= 18));

// toMap with duplicate key handling
Map<String, Person> nameToPerson = people.stream()
    .collect(Collectors.toMap(
        Person::getName,
        Function.identity(),
        (existing, replacement) -> existing  // keep first
    ));
```

### 3. Custom Reduction with reduce

reduce performs custom aggregation: identity, accumulator, combiner (for parallel). Three forms: reduce(BinaryOperator) (no identity, returns Optional), reduce(T, BinaryOperator), reduce(T, BiFunction, BinaryOperator).

```java
// Sum with reduce
List<Integer> numbers = List.of(1, 2, 3, 4, 5);
int sum = numbers.stream()
    .reduce(0, Integer::sum);  // identity: 0

// Max with reduce (no identity)
Optional<Integer> max = numbers.stream()
    .reduce(Integer::max);

// Custom reduction: concatenate strings
List<String> words = List.of("Hello", "World", "Java", "Stream");
String sentence = words.stream()
    .reduce("", (a, b) -> a + " " + b)
    .trim();

// Reduce with combiner (parallel)
int parallelSum = numbers.parallelStream()
    .reduce(0, Integer::sum, Integer::sum);
```

### 4. Stream Laziness and Optimization

Intermediate ops are lazy — they don't execute until a terminal op is called. Operations can be fused. filter and map are stateless; sorted and distinct are stateful. limit/anyMatch support short-circuit.

```java
// Lazy execution — nothing happens until terminal op
Stream<String> stream = names.stream()
    .peek(s -> System.out.println("Filter: " + s))
    .filter(s -> s.length() > 3)
    .peek(s -> System.out.println("Map: " + s))
    .map(String::toUpperCase);
// Nothing printed yet!

// Terminal op triggers execution
List<String> result = stream.collect(Collectors.toList());

// Short-circuit with findFirst
// Only processes enough elements to find first match
Optional<String> found = names.stream()
    .filter(s -> s.startsWith("C"))
    .findFirst();
```

### 5. Parallel Streams Considerations

parallelStream() or stream().parallel() splits data across threads. Use for CPU-intensive operations on large datasets. Sequential may be faster for small data or high overhead. Use with thread-safe, stateless functions.

```java
// Parallel stream — fork-join pool
long count = largeList.parallelStream()
    .filter(ExpensivePredicate::check)
    .count();

// When to use parallel:
// - Large dataset (10k+ elements)
// - CPU-intensive operations
// - Independent elements (no shared mutable state)

// When NOT to use parallel:
// - Small datasets (overhead exceeds benefit)
// - I/O-bound operations (use async instead)
// - Operations with ordering constraints

// Ordered vs unordered parallel
// If order matters, use sequential or pay overhead for ordering
```

## Practice Questions

1. What does the pipeline: source -> intermediate -> terminal mean?
1. What is the difference between groupingBy and partitioningBy?
1. What are the three reduce forms? When would you use each?
1. When should you use parallel streams? When should you avoid them?

## LLM Prompts for Deeper Understanding

1. "Explain Stream pipeline with lazy evaluation and operation fusion"
1. "Show advanced Collectors: groupingBy, mapping, filtering, flatMapping"
1. "Teach parallel stream internals: fork-join, spliterator, thread safety"

## Key Takeaways

- Stream pipeline: source -> intermediate ops (lazy) -> terminal op (eager)
- Collectors.groupingBy/partitioningBy for classification
- Parallel streams for large, CPU-intensive, stateless operations