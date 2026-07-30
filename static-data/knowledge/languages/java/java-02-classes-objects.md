---
{
  "title": "Classes and Objects",
  "description": "Define classes with fields, constructors, and methods",
  "type": "lesson",
  "order": 2,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define classes with fields, constructors, and methods",
    "Understand constructors, this, and overloading",
    "Use access modifiers: public, private, protected",
    "Apply encapsulation with getters/setters"
  ],
  "knowledge_refs": [
    "java/java-02-classes-objects"
  ],
  "prerequisites": [
    "JV-01"
  ],
  "references": [
    {
      "title": "Oracle Tutorial — Classes",
      "url": "https://docs.oracle.com/javase/tutorial/java/javaOO/classes.html"
    },
    {
      "title": "Oracle Tutorial — Objects",
      "url": "https://docs.oracle.com/javase/tutorial/java/javaOO/objects.html"
    },
    {
      "title": "Oracle Tutorial — Nested Classes",
      "url": "https://docs.oracle.com/javase/tutorial/java/javaOO/nested.html"
    },
    {
      "title": "Baeldung — Java Classes",
      "url": "https://www.baeldung.com/java-classes"
    }
  ]
}
---

# JAVA-02-CLASSES-OBJECTS: Classes and Objects

## Introduction

Classes are the blueprint for objects in Java. They define state (fields) and behavior (methods). Java enforces single-file-per-top-level-class (public class must match filename).

## Key Concepts

### 1. Class Declaration and Fields

A class declaration includes fields (state), constructors (initialization), and methods (behavior). Fields can be instance (per-object) or static (per-class). Initialization order: static fields, instance fields, constructor.

```java
public class User {
    // Instance fields (one per object)
    private String name;
    private int age;
    private final String id;  // must be set in constructor

    // Static field (shared across all instances)
    private static int count = 0;

    // Constructor
    public User(String name, int age) {
        this.name = name;
        this.age = age;
        this.id = UUID.randomUUID().toString();
        count++;
    }

    // Static method
    public static int getCount() { return count; }
}
```

### 2. Constructor Chaining and Overloading

Constructors can be overloaded (different parameter lists). Use this() to call another constructor in the same class. Use super() to call parent constructor. If no constructor defined, Java provides a default no-arg constructor.

```java
public class Rectangle {
    private double width;
    private double height;

    // No-arg constructor
    public Rectangle() {
        this(1.0, 1.0);  // calls parameterized constructor
    }

    // Parameterized constructor
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    // Copy constructor
    public Rectangle(Rectangle other) {
        this(other.width, other.height);
    }
}
```

### 3. Encapsulation with Access Modifiers

Access modifiers control visibility: public (anywhere), protected (package + subclasses), default/package-private (same package), private (class only). Getters/setters encapsulate field access.

```java
public class BankAccount {
    private String accountNumber;  // only accessible within class
    private double balance;

    // Getter (read access)
    public double getBalance() {
        return balance;
    }

    // Setter with validation (write access)
    public void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Amount must be positive");
        }
        this.balance += amount;
    }

    // Package-private method (no modifier)
    void generateStatement() {
        System.out.println("Statement for " + accountNumber);
    }
}
```

### 4. Static Members and Constants

Static fields/methods belong to the class, not instances. Access them via class name (e.g., Math.PI). Constants use static final. Static initialization blocks run when the class is first loaded.

```java
public class MathUtils {
    // Constants
    public static final double PI = 3.14159;
    private static final String VERSION = "1.0";

    // Static initialization block
    static {
        System.out.println("MathUtils loaded");
    }

    // Static method
    public static int max(int a, int b) {
        return a > b ? a : b;
    }
}

// Usage
double area = MathUtils.PI * r * r;
int max = MathUtils.max(10, 20);
```

### 5. Records (Java 16+)

Records are transparent data carriers. They auto-generate constructor, getters, equals, hashCode, toString. Components are private final fields. Perfect for DTOs, value objects, and API responses.

```java
// Traditional class
public class Point {
    private final int x;
    private final int y;
    // constructor, getters, equals, hashCode, toString...
}

// Record (Java 16+) — all boilerplate auto-generated
public record Point(int x, int y) { }

// Records can have compact constructors
public record Person(String name, int age) {
    public Person {  // compact constructor
        if (age < 0) throw new IllegalArgumentException();
    }

    // Custom methods
    public boolean isAdult() { return age >= 18; }
}
```

## Practice Questions

1. What is the difference between instance fields and static fields?
1. What does this() do in a constructor? What does super() do?
1. What are the four access modifiers in Java? Describe each.
1. What is a record? What methods does it auto-generate?

## LLM Prompts for Deeper Understanding

1. "Explain encapsulation with access modifiers and getter/setter patterns"
1. "Show constructor chaining with this() and super() examples"
1. "Teach records (Java 16+) vs traditional POJOs with comparisons"

## Key Takeaways

- Classes define state (fields) and behavior (methods)
- Access modifiers: public, protected, (default), private
- Records (16+) auto-generate constructors, getters, equals, hashCode