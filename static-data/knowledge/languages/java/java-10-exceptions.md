---
title: "Exception Handling"
description: "Try/catch/finally, checked vs unchecked, try-with-resources, custom exceptions."
type: lesson
order: 10
duration: "60 min"
difficulty: intermediate
learning_objectives:
  - "Handle exceptions with try/catch/finally"\n  - "Distinguish checked from unchecked"\n  - "Use try-with-resources"\n  - "Create custom exceptions"
knowledge_refs:
  - java/java-10-exceptions
prerequisites:
  - "JAVA-04"
references:
    - title: "Oracle - Exceptions"\n      url: "https://docs.oracle.com/javase/tutorial/essential/exceptions/index.html"\n    - title: "Oracle - Try-with-resources"\n      url: "https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html"
---

# JAVA-10-EXCEPTIONS: Exception Handling

## Exception Hierarchy

Throwable -> Error (don't catch) and Exception -> RuntimeException (unchecked)

## Try/Catch/Finally

```java
try {
    FileReader file = new FileReader("data.txt");
    BufferedReader reader = new BufferedReader(file);
} catch (FileNotFoundException e) {
    System.err.println("Not found: " + e.getMessage());
} catch (IOException e) {
    System.err.println("IO error: " + e);
} finally {
    System.out.println("Cleanup");  // Always runs
}
```

## Try-with-Resources (Java 7+)

```java
try (BufferedReader reader =
         new BufferedReader(new FileReader("data.txt"))) {
    System.out.println(reader.readLine());
} // Auto-closed!
```

## Custom Exceptions

```java
public class InsufficientFundsException extends RuntimeException {
    public InsufficientFundsException(double balance, double amount) {
        super(String.format("Need $%.2f, have $%.2f", amount, balance));
    }
}
```

