---
{
  "title": "Getting Started with Java",
  "description": "Install JDK and set up development environment",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Install JDK and set up development environment",
    "Understand JVM, JRE, and JDK relationship",
    "Write, compile, and run your first Java program",
    "Use primitive types and basic I/O"
  ],
  "knowledge_refs": [
    "java/java-01-getting-started"
  ],
  "prerequisites": [],
  "references": [
    {
      "title": "Oracle Java Tutorials — Getting Started",
      "url": "https://docs.oracle.com/javase/tutorial/getStarted/index.html"
    },
    {
      "title": "Oracle Java Tutorials — Language Basics",
      "url": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/index.html"
    },
    {
      "title": "Baeldung — Java Tutorial",
      "url": "https://www.baeldung.com/java-tutorial"
    },
    {
      "title": "Java Language Spec",
      "url": "https://docs.oracle.com/javase/specs/jls/se21/html/index.html"
    }
  ]
}
---

# JAVA-01-GETTING-STARTED: Getting Started with Java

## Introduction

Java is a statically-typed, object-oriented language that runs on billions of devices. The JVM (Java Virtual Machine) provides platform independence — write once, run anywhere. Java 21 (LTS) is the latest long-term support release.

## Key Concepts

### 1. JDK, JRE, and JVM

The JDK (Java Development Kit) includes the JRE (Runtime Environment) plus development tools like javac (compiler) and jar. The JVM executes bytecode. Java source (.java) compiles to bytecode (.class).

```java
// Check Java version
$ java -version  # java 21.0.1
$ javac -version # javac 21.0.1

// HelloWorld.java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}

// Compile and run
$ javac HelloWorld.java   # produces HelloWorld.class
$ java HelloWorld         # runs on JVM
```

### 2. Primitive Types and Variables

Java has 8 primitive types: byte (8-bit), short (16), int (32), long (64), float (32), double (64), boolean, char (16-bit Unicode). Variables must be declared before use. Local variables must be initialized.

```java
int age = 30;
long population = 8_000_000_000L;  // L suffix for long
double price = 19.99;
float tax = 0.08f;                 // f suffix for float
boolean isActive = true;
char grade = 'A';
byte b = 127;                      // -128 to 127

// Type inference with var (Java 10+)
var message = "Hello";              // inferred as String
var count = 42;                     // inferred as int
```

### 3. Control Flow: if, for, while, switch

Java control flow is C-style: if/else, for (traditional and enhanced), while, do-while, switch (expressions since Java 14). Braces are required for blocks (optional for single statements).

```java
// if/else
int score = 85;
String grade;
if (score >= 90) {
    grade = "A";
} else if (score >= 80) {
    grade = "B";
} else {
    grade = "F";
}

// Enhanced for loop
String[] names = {"Alice", "Bob", "Charlie"};
for (String name : names) {
    System.out.println(name);
}

// Switch expression (Java 14+)
String result = switch (score / 10) {
    case 9, 10 -> "Excellent";
    case 8 -> "Good";
    default -> "Needs improvement";
};
```

### 4. Arrays

Arrays are fixed-length, zero-indexed containers. Array types are reference types (even for primitives). The length field gives the size. java.util.Arrays provides utility methods.

```java
// Array declaration and initialization
int[] numbers = new int[5];     // [0, 0, 0, 0, 0]
int[] primes = {2, 3, 5, 7, 11};

// Multi-dimensional
int[][] matrix = {
    {1, 2, 3},
    {4, 5, 6}
};
System.out.println(matrix[1][2]);  // 6

// Array utility methods
import java.util.Arrays;
Arrays.sort(primes);
Arrays.toString(primes);           // "[2, 3, 5, 7, 11]"
Arrays.binarySearch(primes, 5);    // 2 (index)

// Copying arrays
int[] copy = Arrays.copyOf(primes, primes.length);
```

### 5. String and StringBuilder

String is immutable in Java. StringBuilder/StringBuffer for mutable strings. String pool caches literals. Use equals() for value comparison, == for reference comparison.

```java
// String basics
String s1 = "Hello";            // string pool
String s2 = new String("Hello"); // heap (avoid this)
System.out.println(s1.equals(s2));   // true (value)
System.out.println(s1 == s2);        // false (reference)

// String methods
String text = "  Java Programming  ";
text.trim().toUpperCase();            // "JAVA PROGRAMMING"
text.replace("a", "o");
String[] parts = "a,b,c".split(",");

// StringBuilder for efficiency
StringBuilder sb = new StringBuilder();
sb.append("Hello").append(" ").append("World");
String result = sb.toString();
```

## Practice Questions

1. What is the difference between JDK, JRE, and JVM?
1. How do var (Java 10+) differ from explicit type declarations?
1. Why should you use StringBuilder for string concatenation in loops?
1. What is the difference between equals() and == for Strings?

## LLM Prompts for Deeper Understanding

1. "Explain JVM architecture: class loader, runtime areas, execution engine"
1. "Show Java primitive types with memory sizes and default values"
1. "Teach String immutability, String pool, StringBuilder vs StringBuffer"

## Key Takeaways

- Java compiles to bytecode (.class) that runs on the JVM
- 8 primitives: byte, short, int, long, float, double, boolean, char
- String is immutable — use StringBuilder for repeated concatenation