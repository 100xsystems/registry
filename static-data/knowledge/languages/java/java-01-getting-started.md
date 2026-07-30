---
title: "Getting Started with Java"
description: "Install JDK, understand JVM/JRE/JDK, compile and run programs, set up your IDE."
type: lesson
order: 1
duration: "45 min"
difficulty: beginner
learning_objectives:
  - "Install JDK 21+ and configure JAVA_HOME"\n  - "Understand JVM, JRE, and JDK architecture"\n  - "Compile and run Java from the command line"\n  - "Use an IDE for efficient development"
knowledge_refs:
  - java/java-01-getting-started
prerequisites:
  - "None - entry point"
references:
    - title: "Oracle Tutorials - Getting Started"\n      url: "https://docs.oracle.com/javase/tutorial/getStarted/index.html"\n    - title: "Oracle - Hello World"\n      url: "https://docs.oracle.com/javase/tutorial/getStarted/application/index.html"
---

# JAVA-01-GETTING-STARTED: Getting Started with Java

## Introduction

The Java Virtual Machine (JVM) is the cornerstone of Java's "write once, run anywhere" promise.

## JDK, JRE, JVM

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, Java!");
    }
}
```

Compile and run:
```bash
javac HelloWorld.java     # Produces HelloWorld.class (bytecode)
java HelloWorld            # JVM executes the bytecode
```

## Setting Up

Download JDK 21+ from Oracle or use SDKMAN:
```bash
sdk install java 21-open
java --version
# openjdk 21.0.2 2024-01-16
```

## Practice Questions
1. What's the difference between JVM, JRE, and JDK?
2. Why does main need to be public static void?
3. What is bytecode and how is it executed?

