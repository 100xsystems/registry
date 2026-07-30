---
{
  "title": "Annotations and Reflection",
  "description": "Define and use custom annotations",
  "type": "lesson",
  "order": 17,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Define and use custom annotations",
    "Use reflection for runtime analysis",
    "Access fields, methods, constructors reflectively",
    "Understand retention policies and annotation processing"
  ],
  "knowledge_refs": [
    "java/java-17-annotations-reflection"
  ],
  "prerequisites": [
    "JV-02"
  ],
  "references": [
    {
      "title": "Oracle Tutorial — Annotations",
      "url": "https://docs.oracle.com/javase/tutorial/java/annotations/index.html"
    },
    {
      "title": "Oracle Tutorial — Reflection",
      "url": "https://docs.oracle.com/javase/tutorial/reflect/index.html"
    },
    {
      "title": "Baeldung — Java Annotations",
      "url": "https://www.baeldung.com/java-annotations"
    },
    {
      "title": "Baeldung — Java Reflection",
      "url": "https://www.baeldung.com/java-reflection"
    }
  ]
}
---

# JAVA-17-ANNOTATIONS-REFLECTION: Annotations and Reflection

## Introduction

Annotations provide metadata about code. Reflection inspects classes at runtime. These power frameworks: Spring, Hibernate, JUnit. Retention determines lifecycle: SOURCE (compile), CLASS (binary), RUNTIME (reflection).

## Key Concepts

### 1. Custom Annotations and Meta-Annotations

@interface declares annotation. Target specifies where it applies (method, field, class). Retention specifies lifecycle. Repeatable for multiple instances. Inherited propagates to subclasses.

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface LogExecution {
    String value() default "info";
    boolean showArgs() default false;
}

// Usage
public class Service {
    @LogExecution(value = "debug", showArgs = true)
    public void process(String data) {
        System.out.println("Processing: " + data);
    }
}
```

### 2. Reflection: Class Object and Constructors

Every object has a Class<?> from .getClass() or MyClass.class. newInstance() (deprecated), use Constructor<T>.newInstance(). ForName() loads classes dynamically from fully-qualified name.

```java
// Getting Class object
Class<?> strClass = String.class;
Class<?> runtimeClass = "hello".getClass();
Class<?> forName = Class.forName("java.util.ArrayList");

// Create instance reflectively
Constructor<StringBuilder> constructor =
    StringBuilder.class.getConstructor(int.class);
StringBuilder sb = constructor.newInstance(100);

// Inspect class info
String name = strClass.getName();  // java.lang.String
Package pkg = strClass.getPackage();
int modifiers = strClass.getModifiers();  // Modifier.isPublic()
```

### 3. Reflection: Fields and Methods

Access fields via getDeclaredField, setAccessible(true) for private fields. Invoke methods via Method.invoke(). Get annotations on methods, fields, classes.

```java
public class InspectService {
    public Object getFieldValue(Object obj, String fieldName)
            throws Exception {
        Field field = obj.getClass().getDeclaredField(fieldName);
        field.setAccessible(true);  // access private fields
        return field.get(obj);
    }

    public Object invokeMethod(Object obj, String methodName,
            Object... args) throws Exception {
        Class<?>[] paramTypes = Arrays.stream(args)
            .map(Object::getClass).toArray(Class[]::new);
        Method method = obj.getClass().getMethod(methodName, paramTypes);
        return method.invoke(obj, args);
    }
}
```

### 4. Annotation Processing at Runtime

Reflectively read annotations to drive behavior. Common pattern: scan annotated classes, process them. Spring uses this for @Service, @Autowired. JUnit uses @Test annotations.

```java
// Process @LogExecution annotation
public class AnnotationProcessor {
    public static void process(Object obj) throws Exception {
        for (Method method : obj.getClass().getMethods()) {
            LogExecution log = method.getAnnotation(LogExecution.class);
            if (log != null) {
                System.out.println("Log level: " + log.value());
                // Wrap method with logging
            }
        }
    }
}

// Classpath scanning (Spring-style)
// Reflections library: Set<Class<?>> = new Reflections("com.example")
//     .getTypesAnnotatedWith(MyAnnotation.class);
```

### 5. Annotation Processors (Compile-Time)

javax.annotation.processing.Processor process annotations during compilation. Generates source files, validates usage, creates documentation. Lombok uses annotation processing for code generation.

```java
// AbstractProcessor for compile-time processing
@SupportedAnnotationTypes("com.example.GenerateBuilder")
@SupportedSourceVersion(SourceVersion.RELEASE_21)
public class BuilderProcessor extends AbstractProcessor {
    @Override
    public boolean process(Set<? extends TypeElement> annotations,
            RoundEnvironment roundEnv) {
        for (Element elem : roundEnv.getElementsAnnotatedWith(
                GenerateBuilder.class)) {
            // Generate builder class source
            String source = generateBuilder((TypeElement) elem);
            try {
                JavaFileObject file = processingEnv.getFiler()
                    .createSourceFile("com.example.ExampleBuilder");
                try (Writer w = file.openWriter()) {
                    w.write(source);
                }
            } catch (IOException e) {
                processingEnv.getMessager().printMessage(
                    Diagnostic.Kind.ERROR, e.getMessage());
            }
        }
        return true;
    }
}
```

## Practice Questions

1. What does @Retention(RUNTIME) mean? What other options exist?
1. Why call setAccessible(true) on a private Field?
1. What is the difference between getField and getDeclaredField?
1. How do annotation processors differ from runtime reflection?

## LLM Prompts for Deeper Understanding

1. "Explain annotation retention policies and @Target element types"
1. "Show reflection API: Class, Constructor, Field, Method, Annotation"
1. "Teach annotation processing for compile-time code generation (Lombok-style)"

## Key Takeaways

- @Retention(RUNTIME) keeps annotations available for runtime reflection
- Class.forName() dynamically loads classes by fully-qualified name
- Annotation processors generate source code at compile time