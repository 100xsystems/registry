---
title: "Control Flow: if, switch, loops"
description: "if/else, switch expressions, for loops, enhanced for-each, while, and loop control."
type: lesson
order: 3
duration: "60 min"
difficulty: beginner
learning_objectives:
  - "Write conditionals with if/else and switch expressions"\n  - "Use for, enhanced for, and while loops"\n  - "Master break, continue, and labeled statements"\n  - "Understand switch expressions (Java 14+)"
knowledge_refs:
  - java/java-03-control-flow
prerequisites:
  - "JAVA-02"
references:
    - title: "Oracle - Control Flow"\n      url: "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/flow.html"\n    - title: "Oracle - Switch Expressions"\n      url: "https://docs.oracle.com/en/java/javase/17/language/switch-expressions.html"
---

# JAVA-03-CONTROL-FLOW: Control Flow: if, switch, loops

## if/else

```java
int score = 85;
String grade;
if (score >= 90) grade = "A";
else if (score >= 80) grade = "B";
else if (score >= 70) grade = "C";
else grade = "F";
```

## Switch Expressions (Java 14+)

Returns a value:

```java
String day = "MONDAY";
int length = switch (day) {
    case "MONDAY", "FRIDAY", "SUNDAY" -> 6;
    case "TUESDAY" -> 7;
    case "THURSDAY", "SATURDAY" -> 8;
    default -> {
        System.out.println("Unknown: " + day);
        yield 0;
    }
};
```

## Loops

```java
// Enhanced for-each (preferred)
for (String name : names) { }

// Traditional for
for (int i = 0; i < 5; i++) { }

// Labeled break
outer:
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (i == 1 && j == 1) break outer;
    }
}
```

