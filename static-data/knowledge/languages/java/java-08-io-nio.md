---
{
  "title": "I/O: Streams, Readers, and NIO",
  "description": "Read/write files with InputStream/OutputStream",
  "type": "lesson",
  "order": 8,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read/write files with InputStream/OutputStream",
    "Use Reader/Writer for text I/O",
    "Use NIO Files and Path for modern file ops",
    "Serialize objects with ObjectOutputStream"
  ],
  "knowledge_refs": [
    "java/java-08-io-nio"
  ],
  "prerequisites": [
    "JV-07"
  ],
  "references": [
    {
      "title": "Oracle Tutorial — I/O",
      "url": "https://docs.oracle.com/javase/tutorial/essential/io/index.html"
    },
    {
      "title": "Oracle Tutorial — File I/O (NIO)",
      "url": "https://docs.oracle.com/javase/tutorial/essential/io/fileio.html"
    },
    {
      "title": "Baeldung — Java I/O",
      "url": "https://www.baeldung.com/java-io"
    },
    {
      "title": "Baeldung — Java NIO",
      "url": "https://www.baeldung.com/java-nio-2-file-api"
    }
  ]
}
---

# JAVA-08-IO-NIO: I/O: Streams, Readers, and NIO

## Introduction

Java I/O uses streams (byte-oriented: InputStream/OutputStream) and readers (text-oriented: Reader/Writer). NIO (Java 7+) provides modern file operations via Files and Path classes with better error handling.

## Key Concepts

### 1. Byte Streams: InputStream and OutputStream

Byte streams handle raw binary data. FileInputStream/FileOutputStream for files. BufferedInputStream adds buffering. read() returns int (-1 for EOF). Always close in finally or use try-with-resources.

```java
// Reading bytes
try (FileInputStream fis = new FileInputStream("image.jpg");
     BufferedInputStream bis = new BufferedInputStream(fis)) {
    byte[] buffer = new byte[4096];
    int bytesRead;
    while ((bytesRead = bis.read(buffer)) != -1) {
        process(buffer, bytesRead);
    }
}

// Writing bytes
try (FileOutputStream fos = new FileOutputStream("output.bin")) {
    fos.write(new byte[]{0x48, 0x65, 0x6C, 0x6C, 0x6F});
}
```

### 2. Character Streams: Reader and Writer

Reader/Writer handle text, handling charset encoding. FileReader/FileWriter for files. BufferedReader readLine() for line-by-line. PrintWriter for formatted output.

```java
// Reading text
try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
    String line;
    while ((line = reader.readLine()) != null) {
        System.out.println(line);
    }
}

// Writing text with PrintWriter
try (PrintWriter writer = new PrintWriter(new FileWriter("output.txt"))) {
    writer.println("Hello, World!");
    writer.printf("Count: %d%n", 42);
}

// Specify encoding
new BufferedReader(new InputStreamReader(new FileInputStream("f.txt"), "UTF-8"))
```

### 3. NIO Path and Files (Java 7+)

java.nio.file.Path represents file paths. Files utility class provides static methods: readAllLines, write, copy, move, delete, walk, find. Much cleaner than legacy File API.

```java
Path path = Paths.get("docs", "report.txt");  // platform-independent
Path absolute = Paths.get("/home/user/docs");

// Reading and writing
List<String> lines = Files.readAllLines(path);
Files.write(path, "Hello".getBytes());
Files.write(path, lines);  // overwrite
Files.write(path, lines, StandardOpenOption.APPEND);

// File operations
Files.copy(source, target, StandardCopyOption.REPLACE_EXISTING);
Files.move(source, target, StandardCopyOption.ATOMIC_MOVE);
Files.deleteIfExists(path);
Files.createDirectories(Paths.get("a/b/c"));  // creates all parents
```

### 4. Object Serialization

ObjectOutputStream/ObjectInputStream serialize/deserialize objects. Class must implement Serializable. transient fields are skipped. serialVersionUID ensures version compatibility.

```java
@Serial private static final long serialVersionUID = 1L;

public record User(String name, int age) implements Serializable { }

// Serialize
try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("user.ser"))) {
    oos.writeObject(new User("Alice", 30));
}

// Deserialize
try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream("user.ser"))) {
    User user = (User) ois.readObject();
    System.out.println(user.name());
} catch (ClassNotFoundException e) {
    System.err.println("Class not found: " + e.getMessage());
}
```

### 5. Files.walk and Directory Traversal

Files.walk recursively traverses directories. Files.find with BiPredicate for filtered search. DirectoryStream for simple directory listing. NIO handles symbolic links and file attributes.

```java
// Walk directory tree
try (Stream<Path> stream = Files.walk(Paths.get("src"))) {
    stream.filter(Files::isRegularFile)
          .filter(p -> p.toString().endsWith(".java"))
          .forEach(System.out::println);
}

// File attributes
BasicFileAttributes attrs = Files.readAttributes(path, BasicFileAttributes.class);
attrs.creationTime();
attrs.lastModifiedTime();
attrs.size();

// Check file type
Files.isDirectory(path);
Files.isRegularFile(path);
Files.isSymbolicLink(path);
```

## Practice Questions

1. What is the difference between byte streams and character streams?
1. How does try-with-resources work for multiple I/O streams?
1. What is the advantage of NIO Files over legacy File?
1. What does transient mean in serialization?

## LLM Prompts for Deeper Understanding

1. "Explain Java I/O stream hierarchy: InputStream, Reader, and decorator pattern"
1. "Show NIO Files API with walk, find, readAttributes examples"
1. "Teach serialization with serialVersionUID, transient, Externalizable"

## Key Takeaways

- Byte streams for binary; Reader/Writer for text with charset encoding
- NIO Files/Path provides modern file operations (Java 7+)
- Serializable marks objects for binary serialization; transient skips fields