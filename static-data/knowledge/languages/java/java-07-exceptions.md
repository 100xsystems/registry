---
{
  "title": "Exception Handling and Best Practices",
  "description": "Use try-catch-finally blocks effectively",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use try-catch-finally blocks effectively",
    "Understand checked vs unchecked exceptions",
    "Create custom exception classes",
    "Use try-with-resources for resource cleanup"
  ],
  "knowledge_refs": [
    "java/java-07-exceptions"
  ],
  "prerequisites": [
    "JV-01"
  ],
  "references": [
    {
      "title": "Oracle Tutorial — Exceptions",
      "url": "https://docs.oracle.com/javase/tutorial/essential/exceptions/index.html"
    },
    {
      "title": "Oracle Tutorial — Try-with-Resources",
      "url": "https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html"
    },
    {
      "title": "Effective Java — Ch 10: Exceptions Items 69-77",
      "url": "https://www.oreilly.com/library/view/effective-java-3rd/9780134686097/"
    },
    {
      "title": "Baeldung — Java Exceptions",
      "url": "https://www.baeldung.com/java-exceptions"
    }
  ]
}
---

# JAVA-07-EXCEPTIONS: Exception Handling and Best Practices

## Introduction

Java exceptions provide structured error handling. Checked exceptions (must catch or declare) vs unchecked exceptions (runtime, may ignore). Try-with-resources (Java 7+) auto-closes resources. Best practice: throw early, catch late.

## Key Concepts

### 1. Checked vs Unchecked Exceptions

Checked exceptions (extends Exception but not RuntimeException) must be caught or declared with throws. Unchecked exceptions (extends RuntimeException) like NullPointerException, IllegalArgumentException do not need handling.

```java
// Checked exception — must handle
try {
    FileReader reader = new FileReader("file.txt");
} catch (FileNotFoundException e) {
    System.err.println("File not found: " + e.getMessage());
}

// Or declare with throws
public void readFile(String path) throws IOException {
    // method body
}

// Unchecked exception — no handling required
public void setAge(int age) {
    if (age < 0) {
        throw new IllegalArgumentException("Age must be positive");
    }
}
```

### 2. try-catch-finally Blocks

try block contains risky code. catch blocks handle specific exception types (most specific first). finally block always executes (cleanup). Java 7+ multi-catch: catch (IOE | SQLException e).

```java
public void processFile(String path) {
    BufferedReader reader = null;
    try {
        reader = new BufferedReader(new FileReader(path));
        String line = reader.readLine();
        System.out.println(line);
    } catch (FileNotFoundException e) {
        System.err.println("File not found");
    } catch (IOException e) {
        System.err.println("IO error: " + e.getMessage());
    } finally {
        if (reader != null) {
            try { reader.close(); } catch (IOException e) { }
        }
    }
}
```

### 3. Try-with-Resources (Java 7+)

try-with-resources automatically closes AutoCloseable resources. Multiple resources separated by semicolons. Resources are closed in reverse order. Much cleaner than finally blocks for resource management.

```java
// Single resource
try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
    String line = reader.readLine();
    System.out.println(line);
} catch (IOException e) {
    System.err.println("Error: " + e.getMessage());
}  // reader auto-closed

// Multiple resources
try (FileInputStream in = new FileInputStream("input.txt");
     FileOutputStream out = new FileOutputStream("output.txt")) {
    out.write(in.readAllBytes());
}
```

### 4. Custom Exception Classes

Extend Exception (checked) or RuntimeException (unchecked). Include constructors that match Exception base. Add custom fields for error context. Use exception chaining with cause.

```java
// Custom checked exception
public class UserNotFoundException extends Exception {
    private final String userId;

    public UserNotFoundException(String userId) {
        super("User not found: " + userId);
        this.userId = userId;
    }

    public UserNotFoundException(String userId, Throwable cause) {
        super("User not found: " + userId, cause);
        this.userId = userId;
    }

    public String getUserId() { return userId; }
}

// Usage with chaining
try {
    userRepository.findById(id);
} catch (DataAccessException e) {
    throw new UserNotFoundException(id, e);
}
```

### 5. Best Practices: Throw Early, Catch Late

Validate inputs at method start (throw early). Let checked exceptions propagate to the appropriate handling layer (catch late). Use unchecked exceptions for programming errors. Log or wrap at boundaries.

```java
// Throw early — validate inputs immediately
public void deposit(double amount) {
    if (amount <= 0) {
        throw new IllegalArgumentException("Amount must be positive");
    }
    balance += amount;
}

// Catch late — handle at the right level
// BAD: catch everywhere
// GOOD: let propagate to caller that knows how to handle

// Wrap at boundaries (translation)
try {
    db.query(sql);
} catch (SQLException e) {
    throw new DataAccessException("Query failed", e);
}
```

## Practice Questions

1. What is the difference between checked and unchecked exceptions?
1. How does try-with-resources work? What interface must resources implement?
1. What is exception chaining? How do you preserve the original cause?
1. What does throw early, catch late mean?

## LLM Prompts for Deeper Understanding

1. "Explain checked vs unchecked exceptions with examples and best practices"
1. "Show try-with-resources and AutoCloseable vs Closeable differences"
1. "Teach custom exceptions with chaining, context fields, and factory methods"

## Key Takeaways

- Checked exceptions must be caught/declared; unchecked extend RuntimeException
- Try-with-resources auto-closes AutoCloseable resources
- Best practice: throw early (validate), catch late (handle at right level)