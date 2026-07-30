---
title: "Methods and Parameters"
description: "Method declarations, overloading, varargs, and pass-by-value."
type: lesson
order: 4
duration: "60 min"
difficulty: beginner
learning_objectives:
  - "Declare methods with parameters and return types"\n  - "Overload methods"\n  - "Use varargs for flexible parameters"\n  - "Understand pass-by-value"
knowledge_refs:
  - java/java-04-methods
prerequisites:
  - "JAVA-03"
references:
    - title: "Oracle - Methods"\n      url: "https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html"\n    - title: "Oracle - Arguments"\n      url: "https://docs.oracle.com/javase/tutorial/java/javaOO/arguments.html"
---

# JAVA-04-METHODS: Methods and Parameters

## Method Declaration

```java
public int add(int a, int b) {
    return a + b;
}
```

## Overloading

Same name, different parameters:

```java
public int add(int a, int b) { return a + b; }
public double add(double a, double b) { return a + b; }
public int add(int a, int b, int c) { return a + b + c; }
```

## Varargs

```java
public int sum(int... numbers) {
    int total = 0;
    for (int n : numbers) total += n;
    return total;
}
sum(1, 2); sum(1, 2, 3, 4, 5); sum();  // all valid
```

## Pass-by-Value

Java is always pass-by-value:

```java
public void mutate(int x, StringBuilder sb) {
    x = 99;
    sb.append(" world");
}
// x unchanged outside, sb is mutated
```

