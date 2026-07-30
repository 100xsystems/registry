---
{
  "title": "Inheritance and Polymorphism",
  "description": "Use extends for class inheritance",
  "type": "lesson",
  "order": 3,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use extends for class inheritance",
    "Override methods with @Override",
    "Understand polymorphism and dynamic dispatch",
    "Work with abstract classes and interfaces"
  ],
  "knowledge_refs": [
    "java/java-03-inheritance"
  ],
  "prerequisites": [
    "JV-02"
  ],
  "references": [
    {
      "title": "Oracle Tutorial — Inheritance",
      "url": "https://docs.oracle.com/javase/tutorial/java/IandI/index.html"
    },
    {
      "title": "Oracle Tutorial — Polymorphism",
      "url": "https://docs.oracle.com/javase/tutorial/java/IandI/polymorphism.html"
    },
    {
      "title": "Oracle Tutorial — Abstract/Interfaces",
      "url": "https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html"
    },
    {
      "title": "Baeldung — Inheritance",
      "url": "https://www.baeldung.com/java-inheritance"
    }
  ]
}
---

# JAVA-03-INHERITANCE: Inheritance and Polymorphism

## Introduction

Inheritance enables code reuse through an is-a relationship. Java uses single inheritance for classes (extends) and multiple inheritance of type (implements interfaces). Polymorphism lets objects take many forms.

## Key Concepts

### 1. extends and Method Overriding

A subclass extends a superclass, inheriting all non-private members. Methods can be overridden with @Override (annotation, not required but best practice). final methods cannot be overridden.

```java
public class Animal {
    protected String name;

    public Animal(String name) {
        this.name = name;
    }

    public void speak() {
        System.out.println("Some sound");
    }

    public final void eat() {  // cannot be overridden
        System.out.println("Eating...");
    }
}

public class Dog extends Animal {
    public Dog(String name) {
        super(name);  // must call super constructor
    }

    @Override  // verifies override at compile time
    public void speak() {
        System.out.println("Woof!");
    }
}
```

### 2. Polymorphism and Dynamic Dispatch

Polymorphism means a superclass reference can point to a subclass object. Method calls are resolved at runtime (dynamic dispatch) based on the actual object type, not the reference type.

```java
public static void main(String[] args) {
    Animal myAnimal = new Dog("Buddy");  // upcasting
    myAnimal.speak();  // "Woof!" (dynamic dispatch)

    // instanceof check before downcasting
    if (myAnimal instanceof Dog) {
        Dog dog = (Dog) myAnimal;  // downcasting
        dog.fetch();
    }
}

// Polymorphic collections
List<Animal> animals = Arrays.asList(
    new Dog("Rex"),
    new Cat("Whiskers")
);
for (Animal a : animals) {
    a.speak();  // calls the correct overridden method
}
```

### 3. Abstract Classes

Abstract classes cannot be instantiated. They can have both abstract (no body) and concrete methods. Subclasses must implement all abstract methods. Use for base functionality with mandatory overrides.

```java
public abstract class Shape {
    protected String color;

    public Shape(String color) {
        this.color = color;
    }

    // Abstract method — must be implemented
    public abstract double area();
    public abstract double perimeter();

    // Concrete method — shared implementation
    public String getColor() { return color; }
}

public class Circle extends Shape {
    private double radius;

    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    @Override public double area() {
        return Math.PI * radius * radius;
    }
}
```

### 4. Interfaces and Default Methods

Interfaces define contracts (what to do, not how). Classes can implement multiple interfaces (multiple inheritance of type). Java 8+ supports default methods (with body) and static methods in interfaces.

```java
public interface Flyable {
    void fly();  // abstract method

    // Default method (Java 8+)
    default void takeOff() {
        System.out.println("Taking off...");
        fly();
    }

    // Static method (Java 8+)
    static boolean isFlyingObject(Object obj) {
        return obj instanceof Flyable;
    }
}

public class Bird implements Flyable {
    @Override public void fly() {
        System.out.println("Flapping wings");
    }
}

// Multiple interface implementation
public class Duck implements Flyable, Swimmable {
    @Override public void fly() { /* ... */ }
    @Override public void swim() { /* ... */ }
}
```

### 5. Sealed Classes (Java 17+)

Sealed classes restrict which subclasses can extend them. All permitted subclasses must be explicitly listed. This enables exhaustive pattern matching. sealed -> permits -> final/sealed/non-sealed.

```java
// Base class permits only two subclasses
public sealed class Vehicle permits Car, Truck {
    protected String licensePlate;
}

// Permitted subclass must be final, sealed, or non-sealed
public final class Car extends Vehicle {
    private int doors;
}

public non-sealed class Truck extends Vehicle {
    private double loadCapacity;
}

// Exhaustive switch with sealed classes
double load = switch (vehicle) {
    case Car c -> 0;
    case Truck t -> t.getLoadCapacity();
};
```

## Practice Questions

1. What is the difference between method overloading and overriding?
1. How does Java support multiple inheritance?
1. What is the sealed keyword? When would you use it?
1. What does instanceof do? Why use pattern matching (Java 16+)?

## LLM Prompts for Deeper Understanding

1. "Explain polymorphism with dynamic dispatch and virtual method tables"
1. "Show abstract classes vs interfaces with Java 8+ default methods"
1. "Teach sealed classes (Java 17+) with exhaustive pattern matching"

## Key Takeaways

- extends for single-class inheritance; implements for multiple interfaces
- @Override ensures correct override at compile time
- Sealed classes (17+) restrict subclasses for exhaustive pattern matching