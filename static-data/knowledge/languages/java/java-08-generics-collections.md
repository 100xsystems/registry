---
title: "Generics and Collections"
description: "Generic classes, type bounds, wildcards, Collections Framework."
type: lesson
order: 8
duration: "75 min"
difficulty: intermediate
learning_objectives:
  - "Write generic classes with type parameters"\n  - "Use wildcards for flexible generics"\n  - "Master List, Set, Map, Queue"\n  - "Choose the right collection"
knowledge_refs:
  - java/java-08-generics-collections
prerequisites:
  - "JAVA-06"
references:
    - title: "Oracle - Generics"\n      url: "https://docs.oracle.com/javase/tutorial/java/generics/index.html"\n    - title: "Oracle - Collections"\n      url: "https://docs.oracle.com/javase/tutorial/collections/index.html"
---

# JAVA-08-GENERICS-COLLECTIONS: Generics and Collections

## Generic Methods

```java
public static <T> T getMiddle(T... args) {
    return args[args.length / 2];
}

// Multiple type parameters
public static <K, V> Map<K, V> singletonMap(K key, V value) {
    return Collections.singletonMap(key, value);
}
```

## Bounded Type Parameters

```java
public static <T extends Number> double sumOf(T[] array) {
    double sum = 0;
    for (T elem : array) sum += elem.doubleValue();
    return sum;
}
```

## Wildcards

```java
// Upper-bounded - read only
public double sum(List<? extends Number> nums) {
    double total = 0;
    for (Number n : nums) total += n.doubleValue();
    return total;
}

// Lower-bounded - write only
public void addNums(List<? super Integer> list) {
    list.add(1); list.add(2);
}
```

## Collections Guide

```java
List<String> names = new ArrayList<>();    // Ordered, indexed
Set<Integer> unique = new HashSet<>();      // Unique, fast membership
Map<String, Integer> scores = new HashMap<>(); // Key-value
```

