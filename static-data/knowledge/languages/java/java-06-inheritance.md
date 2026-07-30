---
title: "Inheritance and Polymorphism"
description: "Extending classes, super, method overriding, polymorphism, abstract classes."
type: lesson
order: 6
duration: "75 min"
difficulty: beginner
learning_objectives:
  - "Extend classes with extends and super"\n  - "Override methods polymorphically"\n  - "Create abstract classes and final members"\n  - "Understand Liskov Substitution Principle"
knowledge_refs:
  - java/java-06-inheritance
prerequisites:
  - "JAVA-05"
references:
    - title: "Oracle - Inheritance"\n      url: "https://docs.oracle.com/javase/tutorial/java/IandI/subclasses.html"\n    - title: "Oracle - Polymorphism"\n      url: "https://docs.oracle.com/javase/tutorial/java/IandI/polymorphism.html"
---

# JAVA-06-INHERITANCE: Inheritance and Polymorphism

## Inheritance

```java
public class Animal {
    protected String name;
    public Animal(String name) { this.name = name; }
    public void speak() { System.out.println("Some sound"); }
}

public class Dog extends Animal {
    public Dog(String name) { super(name); }
    @Override
    public void speak() { System.out.println(name + " says Woof!"); }
}

// Polymorphism
Animal myPet = new Dog("Rex");
myPet.speak();  // "Rex says Woof!"
```

## Abstract Classes

```java
public abstract class Shape {
    protected String color;
    public Shape(String color) { this.color = color; }
    public abstract double area();
    public String getColor() { return color; }
}

public class Circle extends Shape {
    private double radius;
    public Circle(String color, double r) { super(color); this.radius = r; }
    @Override
    public double area() { return Math.PI * radius * radius; }
}
```

## Final

```java
public final class Constants {  // Cannot be extended
    public static final double PI = 3.14159;  // Cannot be reassigned
    public final void utility() { }  // Cannot be overridden
}
```

