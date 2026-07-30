#!/usr/bin/env python3
"""Generate deep Java lessons — avoids triple-quote collisions by using single-quote delimiters."""
import json, os
BASE = os.path.join(os.path.dirname(__file__), '..', 'static-data', 'knowledge', 'languages', 'java')

lessons = []

def add(slug, title, desc, order, dur, diff, objs, prereqs, refs, content):
    lessons.append({
        "slug": slug, "title": title, "description": desc, "order": order,
        "duration": dur, "difficulty": diff, "objectives": objs,
        "prereqs": prereqs, "refs": refs, "content": content
    })

# Use single-quote delimited strings (triple single-quotes) to avoid collision with Java triple double-quotes
add('java-01-getting-started', 'Getting Started with Java',
    'Install JDK, understand JVM/JRE/JDK, compile and run programs, set up your IDE.', 1, '45 min', 'beginner',
    ['Install JDK 21+ and configure JAVA_HOME','Understand JVM, JRE, and JDK architecture',
     'Compile and run Java from the command line','Use an IDE for efficient development'],
    ['None - entry point'],
    [('Oracle Tutorials - Getting Started','https://docs.oracle.com/javase/tutorial/getStarted/index.html'),
     ('Oracle - Hello World','https://docs.oracle.com/javase/tutorial/getStarted/application/index.html')],
'''## Introduction

The Java Virtual Machine (JVM) is the cornerstone of Java\'s "write once, run anywhere" promise.

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
1. What\'s the difference between JVM, JRE, and JDK?
2. Why does main need to be public static void?
3. What is bytecode and how is it executed?
''')

add('java-02-variables-types', 'Variables, Types, and Operators',
    'Primitive types, object references, var, operators, and type conversion.', 2, '60 min', 'beginner',
    ['Use all primitive types: int, double, boolean, char','Understand reference vs value types',
     'Use var for local variable type inference','Perform type conversions safely'],
    ['JAVA-01'],
    [('Oracle Tutorials - Primitive Types','https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html'),
     ('Oracle Tutorials - Operators','https://docs.oracle.com/javase/tutorial/java/nutsandbolts/operators.html')],
'''## Primitive Types

Java has 8 primitive types - stored directly on the stack:

```java
byte b = 127;            // 8-bit
short s = 32_767;        // 16-bit
int i = 2_147_483_647;   // 32-bit (most common)
long l = 9_223_372_036_854_775_807L; // 64-bit
float f = 3.14f;         // 32-bit, needs \'f\' suffix
double d = 3.14159;      // 64-bit (default for decimals)
boolean flag = true;     // true or false
char c = \'A\';          // 16-bit Unicode
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
''')

add('java-03-control-flow', 'Control Flow: if, switch, loops',
    'if/else, switch expressions, for loops, enhanced for-each, while, and loop control.', 3, '60 min', 'beginner',
    ['Write conditionals with if/else and switch expressions','Use for, enhanced for, and while loops',
     'Master break, continue, and labeled statements','Understand switch expressions (Java 14+)'],
    ['JAVA-02'],
    [('Oracle - Control Flow','https://docs.oracle.com/javase/tutorial/java/nutsandbolts/flow.html'),
     ('Oracle - Switch Expressions','https://docs.oracle.com/en/java/javase/17/language/switch-expressions.html')],
'''## if/else

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
''')

add('java-04-methods', 'Methods and Parameters',
    'Method declarations, overloading, varargs, and pass-by-value.', 4, '60 min', 'beginner',
    ['Declare methods with parameters and return types','Overload methods',
     'Use varargs for flexible parameters','Understand pass-by-value'],
    ['JAVA-03'],
    [('Oracle - Methods','https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html'),
     ('Oracle - Arguments','https://docs.oracle.com/javase/tutorial/java/javaOO/arguments.html')],
'''## Method Declaration

```java
public int add(int a, int b) {
    return a + b;
}
```

## Overloading

Same name, different parameters:

```java
public int add(int a, int b) { return a + b; }
public double add(double a, double b) { return a + b; }
public int add(int a, int b, int c) { return a + b + c; }
```

## Varargs

```java
public int sum(int... numbers) {
    int total = 0;
    for (int n : numbers) total += n;
    return total;
}
sum(1, 2); sum(1, 2, 3, 4, 5); sum();  // all valid
```

## Pass-by-Value

Java is always pass-by-value:

```java
public void mutate(int x, StringBuilder sb) {
    x = 99;
    sb.append(" world");
}
// x unchanged outside, sb is mutated
```
''')

add('java-05-classes-objects', 'Objects and Classes',
    'Class definitions, constructors, instance vs static, this, Object methods.', 5, '75 min', 'beginner',
    ['Define classes with fields, constructors, methods','Create objects',
     'Distinguish static from instance members','Override equals, hashCode, toString'],
    ['JAVA-04'],
    [('Oracle - Classes','https://docs.oracle.com/javase/tutorial/java/javaOO/classes.html'),
     ('Oracle - Objects','https://docs.oracle.com/javase/tutorial/java/javaOO/objects.html')],
'''## Class Definition

```java
public class Person {
    private String name;
    private int age;
    private static int population = 0;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
        population++;
    }

    public void introduce() {
        System.out.println("Hi, I\'m " + name);
    }
}
```

## Overriding Object Methods

```java
@Override
public String toString() {
    return "Person{name=\'" + name + "\', age=" + age + "}";
}

@Override
public boolean equals(Object o) {
    if (this == o) return true;
    if (!(o instanceof Person)) return false;
    Person p = (Person) o;
    return age == p.age && Objects.equals(name, p.name);
}

@Override
public int hashCode() {
    return Objects.hash(name, age);
}
```

## Records (Java 16+)

```java
public record Point(int x, int y) {}
// Auto-generates: constructor, accessors, equals, hashCode, toString
```
''')

add('java-06-inheritance', 'Inheritance and Polymorphism',
    'Extending classes, super, method overriding, polymorphism, abstract classes.', 6, '75 min', 'beginner',
    ['Extend classes with extends and super','Override methods polymorphically',
     'Create abstract classes and final members','Understand Liskov Substitution Principle'],
    ['JAVA-05'],
    [('Oracle - Inheritance','https://docs.oracle.com/javase/tutorial/java/IandI/subclasses.html'),
     ('Oracle - Polymorphism','https://docs.oracle.com/javase/tutorial/java/IandI/polymorphism.html')],
'''## Inheritance

```java
public class Animal {
    protected String name;
    public Animal(String name) { this.name = name; }
    public void speak() { System.out.println("Some sound"); }
}

public class Dog extends Animal {
    public Dog(String name) { super(name); }
    @Override
    public void speak() { System.out.println(name + " says Woof!"); }
}

// Polymorphism
Animal myPet = new Dog("Rex");
myPet.speak();  // "Rex says Woof!"
```

## Abstract Classes

```java
public abstract class Shape {
    protected String color;
    public Shape(String color) { this.color = color; }
    public abstract double area();
    public String getColor() { return color; }
}

public class Circle extends Shape {
    private double radius;
    public Circle(String color, double r) { super(color); this.radius = r; }
    @Override
    public double area() { return Math.PI * radius * radius; }
}
```

## Final

```java
public final class Constants {  // Cannot be extended
    public static final double PI = 3.14159;  // Cannot be reassigned
    public final void utility() { }  // Cannot be overridden
}
```
''')

add('java-07-interfaces', 'Interfaces and Abstract Classes',
    'Interface definitions, default methods, static methods, functional interfaces.', 7, '60 min', 'intermediate',
    ['Define interfaces with abstract and default methods','Implement multiple interfaces',
     'Use functional interfaces with lambdas','Choose between abstract classes and interfaces'],
    ['JAVA-06'],
    [('Oracle - Interfaces','https://docs.oracle.com/javase/tutorial/java/IandI/createinterface.html'),
     ('Oracle - Default Methods','https://docs.oracle.com/javase/tutorial/java/IandI/defaultmethods.html')],
'''## Interface Definition

```java
public interface Flyable {
    void fly();
    default void takeOff() {
        System.out.println("Taking off...");
        fly();
    }
    static boolean isFlyingObject(Object o) {
        return o instanceof Flyable;
    }
}
```

## Multiple Implementation

```java
public class Bird implements Flyable, Singable {
    @Override public void fly() { System.out.println("Flying"); }
    @Override public void sing() { System.out.println("Chirp"); }
}
```

## Functional Interfaces

Exactly ONE abstract method - allows lambda usage:

```java
@FunctionalInterface
interface Comparator<T> {
    int compare(T o1, T o2);
}

Comparator<Person> byAge = (p1, p2) ->
    Integer.compare(p1.getAge(), p2.getAge());
```
''')

add('java-08-generics-collections', 'Generics and Collections',
    'Generic classes, type bounds, wildcards, Collections Framework.', 8, '75 min', 'intermediate',
    ['Write generic classes with type parameters','Use wildcards for flexible generics',
     'Master List, Set, Map, Queue','Choose the right collection'],
    ['JAVA-06'],
    [('Oracle - Generics','https://docs.oracle.com/javase/tutorial/java/generics/index.html'),
     ('Oracle - Collections','https://docs.oracle.com/javase/tutorial/collections/index.html')],
'''## Generic Methods

```java
public static <T> T getMiddle(T... args) {
    return args[args.length / 2];
}

// Multiple type parameters
public static <K, V> Map<K, V> singletonMap(K key, V value) {
    return Collections.singletonMap(key, value);
}
```

## Bounded Type Parameters

```java
public static <T extends Number> double sumOf(T[] array) {
    double sum = 0;
    for (T elem : array) sum += elem.doubleValue();
    return sum;
}
```

## Wildcards

```java
// Upper-bounded - read only
public double sum(List<? extends Number> nums) {
    double total = 0;
    for (Number n : nums) total += n.doubleValue();
    return total;
}

// Lower-bounded - write only
public void addNums(List<? super Integer> list) {
    list.add(1); list.add(2);
}
```

## Collections Guide

```java
List<String> names = new ArrayList<>();    // Ordered, indexed
Set<Integer> unique = new HashSet<>();      // Unique, fast membership
Map<String, Integer> scores = new HashMap<>(); // Key-value
```
''')

add('java-09-lambdas-streams', 'Lambda Expressions and Streams',
    'Lambda syntax, functional interfaces, method references, stream pipelines, collectors.', 9, '75 min', 'intermediate',
    ['Write lambda expressions','Use method references',
     'Build stream pipelines','Collect results with Collectors'],
    ['JAVA-07', 'JAVA-08'],
    [('Oracle - Lambda Expressions','https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html'),
     ('Oracle - Streams','https://docs.oracle.com/javase/tutorial/collections/streams/index.html'),
     ('Baeldung - Java Streams','https://www.baeldung.com/java-streams')],
'''## Lambda Expressions

```java
// Anonymous class (old way)
button.setOnAction(new EventHandler<ActionEvent>() {
    @Override public void handle(ActionEvent e) { }
});

// Lambda (Java 8+)
button.setOnAction(e -> System.out.println("Clicked!"));

// Multiple params
Comparator<Person> byAge = (p1, p2) ->
    Integer.compare(p1.getAge(), p2.getAge());
```

## Method References

```java
Stream.of("a", "b").map(String::toUpperCase)  // Static method
Stream.of("a").forEach(System.out::println)    // Instance method
Stream.of("A").map(Person::new).toList()       // Constructor
```

## Stream Pipeline

```java
List<String> result = transactions.stream()
    .filter(t -> t.getYear() == 2024)
    .sorted(Comparator.comparing(Transaction::getAmount).reversed())
    .map(Transaction::getDescription)
    .limit(10)
    .collect(Collectors.toList());
```

## Collectors

```java
Map<String, List<Person>> byCity = people.stream()
    .collect(Collectors.groupingBy(Person::getCity));

Map<Boolean, List<Person>> adults = people.stream()
    .collect(Collectors.partitioningBy(p -> p.getAge() >= 18));
```
''')

add('java-10-exceptions', 'Exception Handling',
    'Try/catch/finally, checked vs unchecked, try-with-resources, custom exceptions.', 10, '60 min', 'intermediate',
    ['Handle exceptions with try/catch/finally','Distinguish checked from unchecked',
     'Use try-with-resources','Create custom exceptions'],
    ['JAVA-04'],
    [('Oracle - Exceptions','https://docs.oracle.com/javase/tutorial/essential/exceptions/index.html'),
     ('Oracle - Try-with-resources','https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html')],
'''## Exception Hierarchy

Throwable -> Error (don\'t catch) and Exception -> RuntimeException (unchecked)

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
''')

add('java-11-io-nio', 'File I/O and NIO',
    'java.io basics, java.nio.file, reading/writing files, file system operations.', 11, '60 min', 'intermediate',
    ['Read and write files with java.io and java.nio','Use Paths and Files',
     'Read/write text files efficiently','Work with directories'],
    ['JAVA-10'],
    [('Oracle - I/O','https://docs.oracle.com/javase/tutorial/essential/io/streams.html'),
     ('Oracle - NIO','https://docs.oracle.com/javase/tutorial/essential/io/fileio.html')],
'''## Reading Files (NIO)

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
Files.write(Paths.get("log.txt"), "entry\\n".getBytes(),
    StandardOpenOption.APPEND);
```

## Directory Operations

```java
Files.walk(Paths.get("/home/projects"))
    .filter(p -> p.toString().endsWith(".java"))
    .forEach(System.out::println);

Files.createDirectories(Paths.get("a/b/c"));
```
''')

add('java-12-annotations-reflection', 'Annotations and Reflection',
    'Built-in annotations, custom annotations, Reflection API, annotation processing.', 12, '75 min', 'advanced',
    ['Use built-in annotations','Create custom annotations',
     'Inspect classes at runtime with Reflection','Implement annotation processors'],
    ['JAVA-08'],
    [('Oracle - Annotations','https://docs.oracle.com/javase/tutorial/java/annotations/index.html'),
     ('Oracle - Reflection','https://docs.oracle.com/javase/tutorial/reflect/index.html')],
'''## Custom Annotations

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
public @interface JsonField {
    String name() default "";
    boolean required() default true;
}
```

## Using Reflection

```java
public String toJson(Object obj) throws Exception {
    var json = new StringBuilder("{");
    for (Field field : obj.getClass().getDeclaredFields()) {
        field.setAccessible(true);
        String name = field.getName();
        Object value = field.get(obj);
        json.append("\\"").append(name).append("\\": ")
            .append(value).append(", ");
    }
    json.setLength(json.length() - 2);
    json.append("}");
    return json.toString();
}
```
''')

add('java-13-concurrency', 'Concurrency: Threads and Executors',
    'Thread class, Runnable, synchronized, locks, ExecutorService, CompletableFuture.', 13, '75 min', 'advanced',
    ['Create threads with Thread and Runnable','Synchronize with synchronized and Lock',
     'Use ExecutorService for thread pools','Write async code with CompletableFuture'],
    ['JAVA-08'],
    [('Oracle - Concurrency','https://docs.oracle.com/javase/tutorial/essential/concurrency/index.html'),
     ('Oracle - Executors','https://docs.oracle.com/javase/tutorial/essential/concurrency/executors.html')],
'''## Threads

```java
// Via Runnable
Thread thread = new Thread(() ->
    System.out.println("In: " + Thread.currentThread().getName()));
thread.start();
```

## Synchronization

```java
public class Counter {
    private int count = 0;
    public synchronized void increment() {
        count++;  // Thread-safe
    }
}
```

## ExecutorService

```java
ExecutorService exec = Executors.newFixedThreadPool(4);
Future<Integer> future = exec.submit(() -> {
    Thread.sleep(1000);
    return 42;
});
Integer result = future.get();  // Blocks until done
exec.shutdown();
```

## CompletableFuture

```java
CompletableFuture.supplyAsync(() -> fetchUser(123))
    .thenApply(user -> user.withLastLogin(LocalDateTime.now()))
    .thenAccept(user -> cache(user))
    .exceptionally(ex -> { log.error("Failed", ex); return null; });
```
''')

add('java-19-modern-features', 'Records, Sealed Classes, and Pattern Matching',
    'Records, sealed classes, pattern matching for instanceof and switch, text blocks.', 14, '60 min', 'advanced',
    ['Create immutable data carriers with records','Define sealed hierarchies',
     'Use pattern matching for instanceof','Write text blocks'],
    ['JAVA-08', 'JAVA-06'],
    [('Baeldung - Records','https://www.baeldung.com/java-record-keyword'),
     ('Baeldung - Sealed Classes','https://www.baeldung.com/java-sealed-classes-interfaces'),
     ('Baeldung - Pattern Matching','https://www.baeldung.com/java-pattern-matching-instanceof')],
'''## Records (Java 16+)

Transparent, immutable data carriers:

```java
public record Point(int x, int y) { }

Point p = new Point(3, 4);
System.out.println(p.x());    // auto-accessor
System.out.println(p);        // auto-toString()

// With validation
public record Range(int min, int max) {
    public Range {
        if (min > max) throw new IllegalArgumentException();
    }
    public boolean contains(int v) {
        return v >= min && v <= max;
    }
}
```

## Sealed Classes (Java 17+)

Fixed set of permitted subclasses:

```java
public sealed class Shape permits Circle, Rectangle { }
public final class Circle extends Shape { }
public final class Rectangle extends Shape { }
```

## Pattern Matching for instanceof (Java 16+)

```java
// Old: cast required
if (obj instanceof String) {
    String s = (String) obj;
}

// New: pattern variable
if (obj instanceof String s) {
    System.out.println(s.length());  // No cast!
}
```

## Text Blocks (Java 13+)

```java
String html = \"\"\"
    <html>
        <body>
            <p>Hello, World!</p>
        </body>
    </html>
    \"\"\";
```
''')

def generate_md(lesson):
    objs = "\\n".join(f'  - "{o}"' for o in lesson["objectives"])
    pre = "\\n".join(f'  - "{p}"' for p in lesson["prereqs"])
    refs = "\\n".join(f'    - title: "{t}"\\n      url: "{u}"' for t, u in lesson["refs"])
    return f"""---
title: "{lesson['title']}"
description: "{lesson['description']}"
type: lesson
order: {lesson['order']}
duration: "{lesson['duration']}"
difficulty: {lesson['difficulty']}
learning_objectives:
{objs}
knowledge_refs:
  - java/{lesson['slug']}
prerequisites:
{pre}
references:
{refs}
---

# {lesson['slug'].upper()}: {lesson['title']}

{lesson['content']}
"""

def main():
    for fname in os.listdir(BASE):
        if fname.endswith('.md') and fname != 'index.json':
            os.remove(os.path.join(BASE, fname))
    for lesson in lessons:
        with open(os.path.join(BASE, f"{lesson['slug']}.md"), 'w') as f:
            f.write(generate_md(lesson))
    idx = os.path.join(BASE, 'index.json')
    data = json.load(open(idx))
    data['lessons'] = [{
        "slug": l['slug'], "title": l['title'], "description": l['description'],
        "type": "lesson", "order": l['order'], "duration": l['duration'],
        "difficulty": l['difficulty'], "knowledge_refs": [f"java/{l['slug']}"],
    } for l in lessons]
    json.dump(data, open(idx, 'w'), indent=2, ensure_ascii=False)
    total = sum(len(l['content']) for l in lessons)
    print(f"Java: {len(lessons)} lessons ({total} chars)")

main()
