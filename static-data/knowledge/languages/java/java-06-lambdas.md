---
{
  "title": "Lambda Expressions and Functional Interfaces",
  "description": "Write lambda expressions and method references",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Write lambda expressions and method references",
    "Use built-in functional interfaces (Predicate, Function, Consumer)",
    "Build function composition with andThen, compose",
    "Understand effectively final and variable capture"
  ],
  "knowledge_refs": [
    "java/java-06-lambdas"
  ],
  "prerequisites": [
    "JV-02",
    "JV-05"
  ],
  "references": [
    {
      "title": "Oracle Tutorial — Lambda Expressions",
      "url": "https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html"
    },
    {
      "title": "Oracle Tutorial — Method References",
      "url": "https://docs.oracle.com/javase/tutorial/java/javaOO/methodreferences.html"
    },
    {
      "title": "Oracle Docs — Function Package",
      "url": "https://docs.oracle.com/javase/8/docs/api/java/util/function/package-summary.html"
    },
    {
      "title": "Baeldung — Java Lambdas",
      "url": "https://www.baeldung.com/java-lambda-expressions"
    }
  ]
}
---

# JAVA-06-LAMBDAS: Lambda Expressions and Functional Interfaces

## Introduction

Lambdas (Java 8+) enable functional programming by treating functions as method arguments. A lambda implements a functional interface (single abstract method). Method references provide concise syntax for existing methods.

## Key Concepts

### 1. Lambda Syntax

Lambda syntax: (parameters) -> expression or (params) -> { statements }. Parameter types can be inferred. Single parameter: p -> expr. No parameters: () -> expr. The lambda is compiled into a functional interface implementation.

```java
// Lambda forms
Runnable r1 = () -> System.out.println("Hello");
Consumer<String> c1 = s -> System.out.println(s);
BinaryOperator<Integer> add = (a, b) -> a + b;

// With type declarations (optional)
Comparator<Person> byName = (Person p1, Person p2) ->
    p1.getName().compareTo(p2.getName());

// Block body
Function<String, Integer> countVowels = s -> {
    int count = 0;
    for (char c : s.toCharArray()) {
        if ("aeiou".indexOf(c) >= 0) count++;
    }
    return count;
};
```

### 2. Functional Interfaces: Predicate, Function, Consumer, Supplier

java.util.function contains 43 functional interfaces. Key ones: Predicate<T> (test), Function<T,R> (apply), Consumer<T> (accept), Supplier<T> (get). Each has primitive variants for performance.

```java
// Predicate — test a condition
Predicate<String> isEmpty = String::isEmpty;
Predicate<String> isLong = s -> s.length() > 10;
Predicate<String> isEmptyOrLong = isEmpty.or(isLong);

// Function — transform input to output
Function<String, Integer> length = String::length;
Function<String, String> toUpper = String::toUpperCase;
Function<String, String> upperThenTrim = toUpper.andThen(String::trim);

// Consumer — accept input, no output
Consumer<String> printer = System.out::println;
Consumer<String> logger = s -> log.info("Value: {}", s);
printer.andThen(logger).accept("Hello");

// Supplier — produce value (lazy)
Supplier<Double> random = Math::random;
Supplier<String> config = () -> System.getProperty("app.name");
```

### 3. Method References

Method references provide cleaner lambda syntax for simple method calls. Four types: Class::staticMethod, instance::instanceMethod, Class::instanceMethod (first arg becomes target), Class::new (constructor).

```java
// Static method reference
Function<String, Integer> parser = Integer::parseInt;
// Same as: s -> Integer.parseInt(s)

// Instance method reference on specific object
String prefix = "Item: ";
Function<String, String> prepend = prefix::concat;

// Instance method reference on arbitrary object
Function<String, String> toLower = String::toLowerCase;
// Same as: s -> s.toLowerCase()

// Constructor reference
Supplier<List<String>> listMaker = ArrayList::new;
Function<String, File> fileMaker = File::new;
```

### 4. Variable Capture and Effectively Final

Lambdas can access local variables from the enclosing scope if they are effectively final (assigned once). Cannot modify captured variables — they are copied, not referenced. Instance variables can be modified.

```java
// Effectively final — OK
String prefix = "User: ";  // never reassigned
Function<String, String> addPrefix = name -> prefix + name;

// NOT effectively final — compile error
String msg = "Hello";
// msg = "World";  // if uncommented, lambda fails
Runnable r = () -> System.out.println(msg);

// Instance variable — can be modified
public class Counter {
    private int count = 0;
    public Supplier<Integer> increment() {
        return () -> ++count;  // OK — modifies field
    }
}
```

### 5. Optional — Null Handling

Optional<T> (Java 8+) represents a value that may be absent. Avoids null checks and NullPointerException. Use map, filter, flatMap for chaining. orElse/orElseGet for defaults.

```java
Optional<String> opt = Optional.ofNullable(getName());

// Safe chaining
String result = opt
    .filter(name -> name.length() > 3)
    .map(String::toUpperCase)
    .orElse("DEFAULT");

// orElse vs orElseGet
// orElse: always evaluates default (even if value present)
// orElseGet: lazy evaluation (lambda called only if absent)
String name = opt.orElseGet(() -> fetchDefaultName());

// Throw if absent
String value = opt.orElseThrow(() -> new NoSuchElementException());
```

## Practice Questions

1. What is a functional interface? Name four from java.util.function.
1. What is the difference between andThen() and compose() on Function?
1. What does effectively final mean for lambda variable capture?
1. What is the difference between orElse and orElseGet in Optional?

## LLM Prompts for Deeper Understanding

1. "Explain lambda syntax, functional interfaces, and method references"
1. "Show Optional chaining with map, flatMap, filter, orElse patterns"
1. "Teach function composition with andThen, compose, and primitive variants"

## Key Takeaways

- Lambdas implement functional interfaces (single abstract method)
- Method references (::) provide concise syntax for simple lambda calls
- Optional eliminates null checks with monadic chaining