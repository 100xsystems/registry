---
title: "Variables, Types, and Operators"
description: "Primitive types, object references, var, operators, and type conversion."
type: lesson
order: 2
duration: "60 min"
difficulty: beginner
learning_objectives:
  - "Use all primitive types: int, double, boolean, char"\n  - "Understand reference vs value types"\n  - "Use var for local variable type inference"\n  - "Perform type conversions safely"
knowledge_refs:
  - java/java-02-variables-types
prerequisites:
  - "JAVA-01"
references:
    - title: "Oracle Tutorials - Primitive Types"\n      url: "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html"\n    - title: "Oracle Tutorials - Operators"\n      url: "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/operators.html"
---

# JAVA-02-VARIABLES-TYPES: Variables, Types, and Operators

## Primitive Types

Java has 8 primitive types - stored directly on the stack:

```java
byte b = 127;            // 8-bit
short s = 32_767;        // 16-bit
int i = 2_147_483_647;   // 32-bit (most common)
long l = 9_223_372_036_854_775_807L; // 64-bit
float f = 3.14f;         // 32-bit, needs 'f' suffix
double d = 3.14159;      // 64-bit (default for decimals)
boolean flag = true;     // true or false
char c = 'A';          // 16-bit Unicode
```

## Type Conversion

```java
// Widening (implicit) - safe
int i = 100;
long l = i;         // int to long (OK)

// Narrowing (explicit) - needs cast
double pi = 3.14159;
int truncated = (int) pi;  // 3 - fractional part lost!

// Autoboxing
Integer wrapper = 42;     // int to Integer
int value = wrapper;      // Integer to int
```

## var (Java 10+)

```java
var message = "Hello!";            // infers String
var count = 42;                    // infers int
var list = new ArrayList<String>(); // infers ArrayList
```

