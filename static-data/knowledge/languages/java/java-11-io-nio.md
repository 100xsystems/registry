---
title: "File I/O and NIO"
description: "java.io basics, java.nio.file, reading/writing files, file system operations."
type: lesson
order: 11
duration: "60 min"
difficulty: intermediate
learning_objectives:
  - "Read and write files with java.io and java.nio"\n  - "Use Paths and Files"\n  - "Read/write text files efficiently"\n  - "Work with directories"
knowledge_refs:
  - java/java-11-io-nio
prerequisites:
  - "JAVA-10"
references:
    - title: "Oracle - I/O"\n      url: "https://docs.oracle.com/javase/tutorial/essential/io/streams.html"\n    - title: "Oracle - NIO"\n      url: "https://docs.oracle.com/javase/tutorial/essential/io/fileio.html"
---

# JAVA-11-IO-NIO: File I/O and NIO

## Reading Files (NIO)

```java
Path path = Paths.get("data.txt");
List<String> lines = Files.readAllLines(path);  // Small files
String content = Files.readString(path);         // Java 11+

// Streaming for large files
try (Stream<String> stream = Files.lines(path)) {
    stream.filter(l -> l.contains("ERROR"))
          .forEach(System.out::println);
}
```

## Writing Files

```java
Files.writeString(Paths.get("out.txt"), "Hello!");
Files.write(Paths.get("out.txt"), List.of("Line1", "Line2"));
Files.write(Paths.get("log.txt"), "entry\n".getBytes(),
    StandardOpenOption.APPEND);
```

## Directory Operations

```java
Files.walk(Paths.get("/home/projects"))
    .filter(p -> p.toString().endsWith(".java"))
    .forEach(System.out::println);

Files.createDirectories(Paths.get("a/b/c"));
```

