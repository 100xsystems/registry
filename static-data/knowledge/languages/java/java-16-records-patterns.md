---
{
  "title": "Records, Pattern Matching, and Modern Features (Java 16+)",
  "description": "Create data carriers with records",
  "type": "lesson",
  "order": 16,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create data carriers with records",
    "Use pattern matching for instanceof",
    "Use switch expressions and pattern matching",
    "Write sealed hierarchies with exhaustive matching"
  ],
  "knowledge_refs": [
    "java/java-16-records-patterns"
  ],
  "prerequisites": [
    "JV-02",
    "JV-04"
  ],
  "references": [
    {
      "title": "Oracle Docs — Records",
      "url": "https://docs.oracle.com/en/java/javase/21/language/records.html"
    },
    {
      "title": "Oracle Docs — Pattern Matching",
      "url": "https://docs.oracle.com/en/java/javase/21/language/pattern-matching.html"
    },
    {
      "title": "Oracle Docs — Sealed Classes",
      "url": "https://docs.oracle.com/en/java/javase/21/language/sealed-classes-and-interfaces.html"
    },
    {
      "title": "Baeldung — Java Records",
      "url": "https://www.baeldung.com/java-record-keyword"
    }
  ]
}
---

# JAVA-16-RECORDS-PATTERNS: Records, Pattern Matching, and Modern Features (Java 16+)

## Introduction

Modern Java (16+) introduces records, pattern matching for instanceof (16+), switch expressions (14+), and sealed classes (17+). These features reduce boilerplate and enable more expressive, safer code.

## Key Concepts

### 1. Records — Transparent Data Carriers

Records auto-generate constructor, accessors, equals, hashCode, toString. All components are private final. Compact constructor for validation. Local records allowed. Can implement interfaces but not extend classes.

```java
// Simple record
public record Point(int x, int y) { }

// Record with compact constructor (validation)
public record Person(String name, int age) {
    public Person {
        if (age < 0) throw new IllegalArgumentException();
        if (name == null || name.isBlank())
            throw new IllegalArgumentException();
    }

    // Custom method
    public boolean isAdult() { return age >= 18; }

    // Static factory
    public static Person of(String name, int age) {
        return new Person(name, age);
    }
}
```

### 2. Pattern Matching for instanceof (Java 16+)

Pattern matching combines instanceof check with variable declaration. No more separate cast. Nested patterns with record patterns (Java 21+). Guarded patterns with &&.

```java
// Before Java 16
if (obj instanceof String) {
    String s = (String) obj;  // explicit cast needed
    System.out.println(s.length());
}

// Java 16+ — pattern matching
if (obj instanceof String s) {
    System.out.println(s.length());  // no cast needed
}

// With logical conditions
if (obj instanceof String s && s.length() > 5) {
    System.out.println("Long string: " + s);
}
```

### 3. Switch Expressions (Java 14+)

Switch expressions return values, use -> syntax, eliminate fall-through. Exhaustiveness required (default or all cases covered). yield returns values in block expressions.

```java
// Traditional switch (statement)
String result;
switch (day) {
    case MONDAY:
    case FRIDAY:
        result = "Work day";
        break;
    default:
        result = "Other";
}

// Switch expression with ->
String result = switch (day) {
    case MONDAY, FRIDAY -> "Work day";
    case SATURDAY, SUNDAY -> "Weekend";
    default -> "Other";
};

// Switch expression with blocks
int val = switch (obj) {
    case String s -> s.length();
    case Integer i -> i;
    default -> {
        System.out.println("Unknown");
        yield 0;
    }
};
```

### 4. Pattern Matching for switch (Java 17+, 21+)

Dominate patterns in switch case labels. Works with any type. Sealed classes enable exhaustive checking without default. Guarded patterns with when clause.

```java
public String describe(Object obj) {
    return switch (obj) {
        case Integer i -> "Integer: " + i;
        case String s -> "String: " + s;
        case null -> "null";
        case int[] arr -> "Array of size " + arr.length;
        default -> "Unknown type";
    };
}

// With sealed classes — exhaustive matching
public double calculate(Vehicle v) {
    return switch (v) {
        case Car c -> c.fuelCost();
        case Truck t -> t.fuelCost() + t.maintenanceCost();
        // no default needed — covered all permitted types
    };
}
```

### 5. Text Blocks (Java 15+) and New String Methods

Text blocks use triple quotes for multi-line strings. Strip indent, formatted for template substitution. New String methods: isBlank(), lines(), strip(), repeat(), formatted().

```java
// Text block (Java 15+)
String json = """
    {
        "name": "Alice",
        "age": 30
    }
    """.stripIndent();

// Template with formatted()
String html = """
    <div>
        <h1>%s</h1>
        <p>%s</p>
    </div>
    """.formatted(title, body);

// New String methods
"   ".isBlank();        // true
"a\nb\nc".lines().count();  // 3
"  hi  ".strip();       // "hi"
"ha".repeat(3);        // "hahaha"
```

## Practice Questions

1. What methods does a record auto-generate?
1. How does pattern matching for instanceof work?
1. What is the difference between a switch statement and switch expression?
1. What are text blocks? What method removes leading whitespace?

## LLM Prompts for Deeper Understanding

1. "Explain records with compact constructors, static factories, and local records"
1. "Show pattern matching evolution: instanceof -> switch -> sealed class integration"
1. "Teach text blocks and new String methods (isBlank, lines, strip, repeat)"

## Key Takeaways

- Records auto-generate constructor, accessors, equals, hashCode, toString
- Switch expressions return values and eliminate fall-through bugs
- Pattern matching combines type check + variable declaration in one step