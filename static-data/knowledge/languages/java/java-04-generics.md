---
{
  "title": "Generics: Type Parameterization",
  "description": "Write generic classes, methods, and interfaces",
  "type": "lesson",
  "order": 4,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write generic classes, methods, and interfaces",
    "Use bounded type parameters (extends, super)",
    "Understand type erasure and bridge methods",
    "Use wildcards: ? extends T, ? super T"
  ],
  "knowledge_refs": [
    "java/java-04-generics"
  ],
  "prerequisites": [
    "JV-02"
  ],
  "references": [
    {
      "title": "Oracle Tutorial — Generics",
      "url": "https://docs.oracle.com/javase/tutorial/java/generics/index.html"
    },
    {
      "title": "Oracle Tutorial — Wildcards",
      "url": "https://docs.oracle.com/javase/tutorial/java/generics/wildcards.html"
    },
    {
      "title": "Effective Java — Ch 5: Generics Items 26-33",
      "url": "https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/"
    },
    {
      "title": "Baeldung — Java Generics",
      "url": "https://www.baeldung.com/java-generics"
    }
  ]
}
---

# JAVA-04-GENERICS: Generics: Type Parameterization

## Introduction

Generics provide compile-time type safety by parameterizing types. They eliminate casts and enable reusable code (e.g., List<String>, Optional<T>). The compiler erases generic type information at runtime (type erasure).

## Key Concepts

### 1. Generic Classes

A generic class has one or more type parameters in angle brackets <T>. The type parameter can be used for fields, method params, and return types. Convention: E (element), K (key), V (value), T (type), R (return).

```java
public class Box<T> {
    private T contents;

    public void put(T item) {
        this.contents = item;
    }

    public T get() {
        return contents;
    }
}

// Usage
Box<String> stringBox = new Box<>();  // diamond operator <>
stringBox.put("Hello");
String value = stringBox.get();  // no cast needed

// Multiple type parameters
public class Pair<K, V> {
    private K key;
    private V value;
    // constructor, getters...
}
```

### 2. Generic Methods

Generic methods introduce type parameters independently of the class. The type parameter goes before the return type. Inference determines T from arguments — cast not needed on call.

```java
public class Utils {
    // Generic method
    public static <T> T identity(T value) {
        return value;
    }

    // Generic method with type bound
    public static <T extends Comparable<T>> T max(T a, T b) {
        return a.compareTo(b) > 0 ? a : b;
    }
}

// Type inference
String s = Utils.identity("hello");  // T inferred as String
int max = Utils.max(42, 100);         // T inferred as Integer
```

### 3. Bounded Type Parameters

extends bounds restrict T to subclasses of a type. This enables calling methods from the bound type. Multiple bounds use & (e.g., T extends Comparable & Serializable). Use super for lower bounds.

```java
// Upper bound: T must be Number or subclass
public class Stats<T extends Number> {
    private T[] numbers;

    public double average() {
        double sum = 0.0;
        for (T n : numbers) {
            sum += n.doubleValue();  // Number method
        }
        return sum / numbers.length;
    }
}

Stats<Integer> intStats = new Stats<>();     // OK
Stats<Double> doubleStats = new Stats<>();   // OK
// Stats<String> stringStats;  // Compile error
```

### 4. Wildcards: ? extends and ? super

? extends T (covariant): producer — read items but cannot add. ? super T (contravariant): consumer — add items but only read as Object. Unbounded ? for simple presence checks. PECS: Producer Extends, Consumer Super.

```java
import java.util.List;

// Covariant (? extends) — read, but cannot write
public double sum(List<? extends Number> list) {
    double total = 0;
    for (Number n : list) {
        total += n.doubleValue();
    }
    // list.add(42);  // compile error
    return total;
}

// Contravariant (? super) — write, read as Object
public void addNumbers(List<? super Integer> list) {
    for (int i = 1; i <= 10; i++) {
        list.add(i);  // OK to add Integer
    }
    // Integer x = list.get(0);  // compile error
    Object o = list.get(0);  // only Object
}
```

### 5. Type Erasure and Bridge Methods

The compiler replaces type parameters with their bounds (or Object) — type erasure. Bridge methods handle polymorphism with erased types. Generics are compile-time only; runtime uses raw types.

```java
// Before erasure: Box<T>
// After erasure: Box (T -> Object) or Box (T -> Number with bound)

public class ErasedBox {
    private Object contents;  // T erased to Object
    public Object get() { return contents; }
    public void put(Object item) { this.contents = item; }
}

// Bridge method example
// Subclass: MyList extends ArrayList<String>
// Compiler adds bridge: public Object get(int i) { return (String)get(i); }

// Cannot create instances of type parameters
// T item = new T();     // compile error
// T[] arr = new T[10]; // compile error
```

## Practice Questions

1. What is the diamond operator <>? Why is it useful?
1. What does T extends Comparable<T> mean?
1. What is PECS? When would you use ? extends vs ? super?
1. What is type erasure? What gets erased at compile time?

## LLM Prompts for Deeper Understanding

1. "Explain Java generics: type parameters, bounds, and wildcards with examples"
1. "Show PECS (Producer Extends, Consumer Super) with Collection examples"
1. "Teach type erasure, bridge methods, and generics restrictions"

## Key Takeaways

- Generics provide compile-time type safety without runtime overhead
- Use extends for upper bounds (producer), super for lower bounds (consumer)
- Type erasure replaces T with Object (or bound) at compile time