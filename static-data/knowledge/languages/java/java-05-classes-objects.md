---
title: "Objects and Classes"
description: "Class definitions, constructors, instance vs static, this, Object methods."
type: lesson
order: 5
duration: "75 min"
difficulty: beginner
learning_objectives:
  - "Define classes with fields, constructors, methods"\n  - "Create objects"\n  - "Distinguish static from instance members"\n  - "Override equals, hashCode, toString"
knowledge_refs:
  - java/java-05-classes-objects
prerequisites:
  - "JAVA-04"
references:
    - title: "Oracle - Classes"\n      url: "https://docs.oracle.com/javase/tutorial/java/javaOO/classes.html"\n    - title: "Oracle - Objects"\n      url: "https://docs.oracle.com/javase/tutorial/java/javaOO/objects.html"
---

# JAVA-05-CLASSES-OBJECTS: Objects and Classes

## Class Definition

```java
public class Person {
    private String name;
    private int age;
    private static int population = 0;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
        population++;
    }

    public void introduce() {
        System.out.println("Hi, I'm " + name);
    }
}
```

## Overriding Object Methods

```java
@Override
public String toString() {
    return "Person{name='" + name + "', age=" + age + "}";
}

@Override
public boolean equals(Object o) {
    if (this == o) return true;
    if (!(o instanceof Person)) return false;
    Person p = (Person) o;
    return age == p.age && Objects.equals(name, p.name);
}

@Override
public int hashCode() {
    return Objects.hash(name, age);
}
```

## Records (Java 16+)

```java
public record Point(int x, int y) {}
// Auto-generates: constructor, accessors, equals, hashCode, toString
```

