---
title: "Interfaces and Abstract Classes"
description: "Interface definitions, default methods, static methods, functional interfaces."
type: lesson
order: 7
duration: "60 min"
difficulty: intermediate
learning_objectives:
  - "Define interfaces with abstract and default methods"\n  - "Implement multiple interfaces"\n  - "Use functional interfaces with lambdas"\n  - "Choose between abstract classes and interfaces"
knowledge_refs:
  - java/java-07-interfaces
prerequisites:
  - "JAVA-06"
references:
    - title: "Oracle - Interfaces"\n      url: "https://docs.oracle.com/javase/tutorial/java/IandI/createinterface.html"\n    - title: "Oracle - Default Methods"\n      url: "https://docs.oracle.com/javase/tutorial/java/IandI/defaultmethods.html"
---

# JAVA-07-INTERFACES: Interfaces and Abstract Classes

## Interface Definition

```java
public interface Flyable {
    void fly();
    default void takeOff() {
        System.out.println("Taking off...");
        fly();
    }
    static boolean isFlyingObject(Object o) {
        return o instanceof Flyable;
    }
}
```

## Multiple Implementation

```java
public class Bird implements Flyable, Singable {
    @Override public void fly() { System.out.println("Flying"); }
    @Override public void sing() { System.out.println("Chirp"); }
}
```

## Functional Interfaces

Exactly ONE abstract method - allows lambda usage:

```java
@FunctionalInterface
interface Comparator<T> {
    int compare(T o1, T o2);
}

Comparator<Person> byAge = (p1, p2) ->
    Integer.compare(p1.getAge(), p2.getAge());
```

