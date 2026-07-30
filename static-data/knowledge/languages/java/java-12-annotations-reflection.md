---
title: "Annotations and Reflection"
description: "Built-in annotations, custom annotations, Reflection API, annotation processing."
type: lesson
order: 12
duration: "75 min"
difficulty: advanced
learning_objectives:
  - "Use built-in annotations"\n  - "Create custom annotations"\n  - "Inspect classes at runtime with Reflection"\n  - "Implement annotation processors"
knowledge_refs:
  - java/java-12-annotations-reflection
prerequisites:
  - "JAVA-08"
references:
    - title: "Oracle - Annotations"\n      url: "https://docs.oracle.com/javase/tutorial/java/annotations/index.html"\n    - title: "Oracle - Reflection"\n      url: "https://docs.oracle.com/javase/tutorial/reflect/index.html"
---

# JAVA-12-ANNOTATIONS-REFLECTION: Annotations and Reflection

## Custom Annotations

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
        json.append("\"").append(name).append("\": ")
            .append(value).append(", ");
    }
    json.setLength(json.length() - 2);
    json.append("}");
    return json.toString();
}
```

