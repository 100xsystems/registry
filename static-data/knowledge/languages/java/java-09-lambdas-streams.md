---
title: "Lambda Expressions and Streams"
description: "Lambda syntax, functional interfaces, method references, stream pipelines, collectors."
type: lesson
order: 9
duration: "75 min"
difficulty: intermediate
learning_objectives:
  - "Write lambda expressions"\n  - "Use method references"\n  - "Build stream pipelines"\n  - "Collect results with Collectors"
knowledge_refs:
  - java/java-09-lambdas-streams
prerequisites:
  - "JAVA-07"\n  - "JAVA-08"
references:
    - title: "Oracle - Lambda Expressions"\n      url: "https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html"\n    - title: "Oracle - Streams"\n      url: "https://docs.oracle.com/javase/tutorial/collections/streams/index.html"\n    - title: "Baeldung - Java Streams"\n      url: "https://www.baeldung.com/java-streams"
---

# JAVA-09-LAMBDAS-STREAMS: Lambda Expressions and Streams

## Lambda Expressions

```java
// Anonymous class (old way)
button.setOnAction(new EventHandler<ActionEvent>() {
    @Override public void handle(ActionEvent e) { }
});

// Lambda (Java 8+)
button.setOnAction(e -> System.out.println("Clicked!"));

// Multiple params
Comparator<Person> byAge = (p1, p2) ->
    Integer.compare(p1.getAge(), p2.getAge());
```

## Method References

```java
Stream.of("a", "b").map(String::toUpperCase)  // Static method
Stream.of("a").forEach(System.out::println)    // Instance method
Stream.of("A").map(Person::new).toList()       // Constructor
```

## Stream Pipeline

```java
List<String> result = transactions.stream()
    .filter(t -> t.getYear() == 2024)
    .sorted(Comparator.comparing(Transaction::getAmount).reversed())
    .map(Transaction::getDescription)
    .limit(10)
    .collect(Collectors.toList());
```

## Collectors

```java
Map<String, List<Person>> byCity = people.stream()
    .collect(Collectors.groupingBy(Person::getCity));

Map<Boolean, List<Person>> adults = people.stream()
    .collect(Collectors.partitioningBy(p -> p.getAge() >= 18));
```

