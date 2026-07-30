---
title: "Records, Sealed Classes, and Pattern Matching"
description: "Records, sealed classes, pattern matching for instanceof and switch, text blocks."
type: lesson
order: 14
duration: "60 min"
difficulty: advanced
learning_objectives:
  - "Create immutable data carriers with records"\n  - "Define sealed hierarchies"\n  - "Use pattern matching for instanceof"\n  - "Write text blocks"
knowledge_refs:
  - java/java-19-modern-features
prerequisites:
  - "JAVA-08"\n  - "JAVA-06"
references:
    - title: "Baeldung - Records"\n      url: "https://www.baeldung.com/java-record-keyword"\n    - title: "Baeldung - Sealed Classes"\n      url: "https://www.baeldung.com/java-sealed-classes-interfaces"\n    - title: "Baeldung - Pattern Matching"\n      url: "https://www.baeldung.com/java-pattern-matching-instanceof"
---

# JAVA-19-MODERN-FEATURES: Records, Sealed Classes, and Pattern Matching

## Records (Java 16+)

Transparent, immutable data carriers:

```java
public record Point(int x, int y) { }

Point p = new Point(3, 4);
System.out.println(p.x());    // auto-accessor
System.out.println(p);        // auto-toString()

// With validation
public record Range(int min, int max) {
    public Range {
        if (min > max) throw new IllegalArgumentException();
    }
    public boolean contains(int v) {
        return v >= min && v <= max;
    }
}
```

## Sealed Classes (Java 17+)

Fixed set of permitted subclasses:

```java
public sealed class Shape permits Circle, Rectangle { }
public final class Circle extends Shape { }
public final class Rectangle extends Shape { }
```

## Pattern Matching for instanceof (Java 16+)

```java
// Old: cast required
if (obj instanceof String) {
    String s = (String) obj;
}

// New: pattern variable
if (obj instanceof String s) {
    System.out.println(s.length());  // No cast!
}
```

## Text Blocks (Java 13+)

```java
String html = """
    <html>
        <body>
            <p>Hello, World!</p>
        </body>
    </html>
    """;
```

