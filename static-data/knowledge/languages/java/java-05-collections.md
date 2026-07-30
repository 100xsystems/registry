---
{
  "title": "Collections Framework",
  "description": "Use List, Set, Map, and Queue interfaces",
  "type": "lesson",
  "order": 5,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use List, Set, Map, and Queue interfaces",
    "Choose between implementations: ArrayList, LinkedList, HashMap",
    "Use Stream API for data processing",
    "Understand Comparable vs Comparator"
  ],
  "knowledge_refs": [
    "java/java-05-collections"
  ],
  "prerequisites": [
    "JV-02",
    "JV-04"
  ],
  "references": [
    {
      "title": "Oracle Tutorial — Collections",
      "url": "https://docs.oracle.com/javase/tutorial/collections/index.html"
    },
    {
      "title": "Oracle Tutorial — Streams",
      "url": "https://docs.oracle.com/javase/tutorial/collections/streams/index.html"
    },
    {
      "title": "Baeldung — Java Collections",
      "url": "https://www.baeldung.com/java-collections"
    },
    {
      "title": "Baeldung — Java Streams",
      "url": "https://www.baeldung.com/java-streams"
    }
  ]
}
---

# JAVA-05-COLLECTIONS: Collections Framework

## Introduction

The Collections Framework provides interfaces and implementations for storing and processing groups of objects. Lists (ordered), Sets (unique), Maps (key-value), Queues (FIFO). Stream API (Java 8+) enables functional-style operations.

## Key Concepts

### 1. List: ArrayList vs LinkedList

ArrayList uses a dynamic array — O(1) get, O(n) insert/delete in middle. LinkedList uses doubly-linked list — O(n) get, O(1) insert/delete at ends. ArrayList is the default choice.

```java
List<String> arrayList = new ArrayList<>();  // default choice
arrayList.add("Apple");
arrayList.add(0, "First");  // insert at position
String fruit = arrayList.get(1);  // O(1)

List<Integer> linkedList = new LinkedList<>();
linkedList.addFirst(1);   // O(1) at head
linkedList.addLast(100);  // O(1) at tail

// Common List methods
list.size(); list.isEmpty(); list.contains(x);
list.indexOf(x); list.remove(i);
list.sort(Comparator.naturalOrder());
```

### 2. Set: HashSet, TreeSet, LinkedHashSet

HashSet uses hashCode() — O(1) operations, no ordering. TreeSet uses compareTo() — O(log n), sorted order. LinkedHashSet maintains insertion order. Elements must implement hashCode/equals.

```java
Set<String> hashSet = new HashSet<>();
hashSet.add("Banana");
hashSet.add("Apple");
hashSet.add("Banana");  // ignored — duplicate

Set<String> treeSet = new TreeSet<>();  // sorted
treeSet.add("Charlie");
treeSet.add("Alice");
// treeSet: ["Alice", "Charlie"] (alphabetical)

Set<String> linkedHashSet = new LinkedHashSet<>();  // insertion order
linkedHashSet.add("Z");
linkedHashSet.add("A");
// linkedHashSet: ["Z", "A"] (insertion order preserved)
```

### 3. Map: HashMap, TreeMap, LinkedHashMap

HashMap — O(1) get/put, no ordering. TreeMap — O(log n), sorted by keys. LinkedHashMap — insertion order. computeIfAbsent simplifies lazy initialization.

```java
Map<String, Integer> scores = new HashMap<>();
scores.put("Alice", 95);
scores.put("Bob", 87);
scores.putIfAbsent("Alice", 0);  // doesn't overwrite

// Iteration
for (Map.Entry<String, Integer> entry : scores.entrySet()) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}

// computeIfAbsent (lazy initialization)
Map<String, List<String>> groups = new HashMap<>();
groups.computeIfAbsent("A", k -> new ArrayList<>()).add("Apple");

// HashMap with custom key — requires hashCode() and equals()
Map<Point, String> pointMap = new HashMap<>();
```

### 4. Comparable vs Comparator

Comparable defines natural ordering in the class itself (compareTo). Comparator defines external ordering (compare). Use Comparator.comparing() for chaining. Trees and sorted collections rely on these.

```java
// Comparable — natural ordering
public class Person implements Comparable<Person> {
    private String name;
    private int age;

    @Override
    public int compareTo(Person other) {
        return this.name.compareTo(other.name);
    }
}

// Comparator — external ordering
Comparator<Person> byAge = Comparator.comparingInt(Person::getAge);
Comparator<Person> byNameThenAge = Comparator
    .comparing(Person::getName)
    .thenComparingInt(Person::getAge);
```

### 5. Stream API Basics

Streams process collections functionally. Pipeline: source -> intermediate ops (filter, map, sorted) -> terminal op (collect, reduce, forEach). Streams are lazy, single-use, parallelizable.

```java
List<String> names = Arrays.asList("Alice", "Bob", "Charlie", "David");

// Stream pipeline
List<String> result = names.stream()
    .filter(name -> name.startsWith("A") || name.startsWith("C"))
    .map(String::toUpperCase)
    .sorted()
    .collect(Collectors.toList());

// Common operations
long count = names.stream().filter(s -> s.length() > 3).count();
Optional<String> first = names.stream().findFirst();
boolean allMatch = names.stream().allMatch(s -> s.length() > 1);

// Parallel stream
names.parallelStream()
    .map(String::toLowerCase)
    .forEach(System.out::println);
```

## Practice Questions

1. When would you choose ArrayList vs LinkedList?
1. What is the difference between HashSet and TreeSet?
1. What does computeIfAbsent do on a Map?
1. What is the difference between Comparable and Comparator?

## LLM Prompts for Deeper Understanding

1. "Explain Java Collections Framework with time complexity comparisons"
1. "Show Stream API: filter, map, reduce, collect with parallel streams"
1. "Teach HashMap internals: buckets, hashCode, equals, load factor"

## Key Takeaways

- ArrayList for most cases; LinkedList for frequent head/tail operations
- HashMap O(1) get/put; TreeMap O(log n) sorted; LinkedHashSet insertion order
- Stream API enables functional-style pipelines with lazy evaluation