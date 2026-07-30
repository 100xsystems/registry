---
{
  "title": "Optional and Null Safety",
  "description": "Create, check, and unwrap Optional values",
  "type": "lesson",
  "order": 12,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create, check, and unwrap Optional values",
    "Chain Optional with map, flatMap, filter",
    "Use Optional in method return types",
    "Understand Optional anti-patterns"
  ],
  "knowledge_refs": [
    "java/java-12-optional"
  ],
  "prerequisites": [
    "JV-06"
  ],
  "references": [
    {
      "title": "Oracle Docs — Optional",
      "url": "https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Optional.html"
    },
    {
      "title": "Baeldung — Java Optional",
      "url": "https://www.baeldung.com/java-optional"
    },
    {
      "title": "Effective Java — Item 55: Return Optionals Judiciously",
      "url": "https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/"
    }
  ]
}
---

# JAVA-12-OPTIONAL: Optional and Null Safety

## Introduction

Optional<T> (Java 8+) represents a value that may be absent. It forces callers to consider the absent case, reducing NullPointerException. Not for serialization, fields, or collections.

## Key Concepts

### 1. Creating Optional Values

Optional.of(value) throws NPE if null. Optional.ofNullable(value) accepts null. Optional.empty() for absent. orElse returns default. orElseGet lazy default. orElseThrow throws.

```java
// Creation
Optional<String> present = Optional.of("Hello");  // NPE if null
Optional<String> maybeNull = Optional.ofNullable(getName());  // null becomes empty
Optional<String> empty = Optional.empty();

// Unwrapping with defaults
String value1 = present.orElse("Default");          // always evaluates default
String value2 = present.orElseGet(() -> fetchDefault());  // lazy evaluation
String value3 = present.orElseThrow();              // NoSuchElementException
String value4 = present.orElseThrow(() -> new CustomException("missing"));
```

### 2. Chaining with map, flatMap, filter

map transforms value if present. flatMap avoids nested Optional<Optional<T>>. filter keeps value if predicate matches. ifPresent for side effects. All chain returns Optional.empty if any step returns empty.

```java
// Chaining transformations
Optional<String> opt = Optional.of("Hello World");

Optional<Integer> length = opt
    .filter(s -> s.contains("World"))
    .map(String::toUpperCase)
    .map(String::length);

// flatMap — avoid Optional<Optional<T>>
Optional<Double> result = opt
    .flatMap(this::parseAsNumber)  // returns Optional<Double>
    .filter(d -> d > 0);

// ifPresent — side effect
opt.ifPresent(System.out::println);
opt.ifPresentOrElse(
    val -> System.out.println(val),
    () -> System.out.println("empty")
);
```

### 3. Optional in Method Signatures

Return Optional from methods that may not have a result. Inspect IntelliJ/sonar hints. Never return null from an Optional-returning method. Do not use Optional for fields, constructor args, or collections.

```java
// Good: return Optional for potentially absent results
public Optional<User> findById(String id) {
    User user = database.lookup(id);
    return Optional.ofNullable(user);
}

// BAD: returning null Optional
public Optional<User> badFind(String id) {  // may return null!
    return null;  // defeats purpose
}

// BAD: Optional as field type
public class User {
    private Optional<String> middleName;  // not serializable, extra overhead
}
```

### 4. Optional Anti-Patterns

Don't use Optional for collections (empty list is better). Don't use Optional.get() without isPresent() check. Don't use Optional.of() with potentially null args. Don't use Optional for primitive fields.

```java
// BAD: Optional for collections
Optional<List<String>> optList = Optional.ofNullable(getNames());
// BETTER: return empty list instead
List<String> names = getNames();  // never null, empty list for absence

// BAD: Optional.get() without check
Optional<String> opt = getMaybe();
// String s = opt.get();  // throws NoSuchElementException if empty

// GOOD: safe unwrapping
String s = opt.orElse("default");

// BAD: using Optional for primitive fields
OptionalInt optionalInt = OptionalInt.of(42);  // use OptionalInt, OptionalLong, OptionalDouble
// Or just use int with a sentinel value
```

### 5. Optional with Stream API Integration

Optional.stream() (Java 9+) converts to stream for flatMap with streams. Optional.or() (Java 9+) provides alternative Optional. Combine Optional with Stream for powerful queries.

```java
// Optional.stream() — filter out empty optionals
List<Optional<String>> optionals = List.of(
    Optional.of("A"),
    Optional.empty(),
    Optional.of("B")
);

// Java 9+ — convert Optional to Stream
List<String> present = optionals.stream()
    .flatMap(Optional::stream)
    .collect(Collectors.toList());
// ["A", "B"]

// Optional.or() — alternative Optional (Java 9+)
String result = findPrimary()
    .or(() -> findFallback())
    .orElse("default");
```

## Practice Questions

1. How is Optional.of() different from Optional.ofNullable()?
1. What is the difference between orElse and orElseGet?
1. When should you NOT use Optional?
1. What does Optional.stream() do (Java 9+)?

## LLM Prompts for Deeper Understanding

1. "Explain Optional patterns: creation, chaining, unwrapping, anti-patterns"
1. "Show Optional with Stream integration using flatMap and Optional.stream()"
1. "Teach Optional best practices from Effective Java Item 55"

## Key Takeaways

- Optional forces callers to handle absent values explicitly
- orElse eagerly evaluates; orElseGet lazily evaluates
- Never use Optional for fields, method params, or collections