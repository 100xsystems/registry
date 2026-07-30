---
{
  "title": "Java Module System (Project Jigsaw, Java 9+)",
  "description": "Create module-info.java declarations",
  "type": "lesson",
  "order": 19,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create module-info.java declarations",
    "Export packages and require modules",
    "Understand open modules and reflection",
    "Migrate classpath to module path"
  ],
  "knowledge_refs": [
    "java/java-19-module-system"
  ],
  "prerequisites": [
    "JV-01"
  ],
  "references": [
    {
      "title": "Oracle Tutorial — Modules",
      "url": "https://docs.oracle.com/javase/tutorial/java/modules/modules.html"
    },
    {
      "title": "JPMS Documentation",
      "url": "https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java.base-summary.html"
    },
    {
      "title": "Baeldung — Java 9 Modules",
      "url": "https://www.baeldung.com/java-9-modularity"
    },
    {
      "title": "Baeldung — Migration Classpath Modulepath",
      "url": "https://www.baeldung.com/java-modules-migration"
    }
  ]
}
---

# JAVA-19-MODULE-SYSTEM: Java Module System (Project Jigsaw, Java 9+)

## Introduction

The Java Module System (JPMS, Java 9+) provides strong encapsulation, reliable configuration, and scalable dependencies. module-info.java declares module name, exports, requires, opens, and services.

## Key Concepts

### 1. Module Declaration: module-info.java

module-info.java is the module descriptor. module keyword declares the module. exports makes packages accessible. requires declares dependencies. open opens a module for reflection.

```java
module com.example.myapp {
    // Required modules
    requires java.base;  // always implicitly required
    requires java.sql;
    requires transitive com.example.utils;

    // Export packages (make them accessible)
    exports com.example.myapp.api;
    exports com.example.myapp.model;

    // Opens for reflection (e.g., Hibernate, Jackson)
    opens com.example.myapp.model to org.hibernate, com.fasterxml.jackson.databind;
}
```

### 2. Exports and Opens — Controlling Access

exports makes public types accessible. exports ... to restricts access to specific modules. opens exposes packages for reflection (without opens, reflection cannot access private members).

```java
module com.example.library {
    // Export to all
    exports com.example.library.api;

    // Export only to specific modules
    exports com.example.library.internal
        to com.example.app, com.example.tools;

    // Open entire module for reflection
    open com.example.orm {
        exports com.example.orm.model;
    }

    // Open specific package
    opens com.example.library.config
        to com.fasterxml.jackson.databind;
}
```

### 3. Services: provides and uses

ServiceLoader enables plugin architecture. provides declares an implementation. uses declares a dependency. ServiceLoader.load() discovers implementations at runtime. Loose coupling via interfaces.

```java
// Service interface
public interface GreetingService {
    String greet(String name);
}

// Module providing the service
module com.example.greeting {
    exports com.example.greeting.api;
    provides com.example.greeting.api.GreetingService
        with com.example.greeting.impl.EnglishGreeting;
}

// Module consuming the service
module com.example.app {
    requires com.example.greeting;
    uses com.example.greeting.api.GreetingService;
}

// At runtime
ServiceLoader<GreetingService> loader =
    ServiceLoader.load(GreetingService.class);
for (GreetingService service : loader) {
    System.out.println(service.greet("World"));
}
```

### 4. Module Path vs Classpath

Modular jars go on module path (--module-path). Regular jars on classpath. Module path enforces module boundaries. Automatic modules (jar on module path without module-info) exports all packages.

```java
// Compile with modules
$ javac -d out --module-source-path src
    --module com.example.myapp

// Run with modules
$ java --module-path out --module com.example.myapp/com.example.myapp.Main

// Add modules with -add-modules
$ java --add-modules java.xml.bind -jar app.jar

// Open module for reflection
$ java --add-opens java.base/java.lang=com.example.app

// Read module for access
$ java --add-reads com.example.app=com.example.lib
```

### 5. Migration Strategy

Start by adding module-info to leaf modules. Use --add-reads, --add-exports for migration. Automatic modules bridge classpath and module path. Unnamed module (classpath) reads all named modules.

```java
// Migration steps
// 1. Ensure all dependencies are modular or have Automatic-Module-Name
// 2. Add module-info.java to leaf modules first
// 3. Use --add-reads and --add-exports as temporary flags
// 4. Add module-info to upstream modules

// Identify package conflicts
$ jdeps -summary -jdkinternals target/myapp.jar

// Create module-info for existing jar
// Add Automatic-Module-Name in MANIFEST.MF:
// Automatic-Module-Name: com.example.library
```

## Practice Questions

1. What is the difference between exports and opens in module-info?
1. How does ServiceLoader work in JPMS?
1. What is an automatic module? When is it created?
1. What is the unnamed module? What does it contain?

## LLM Prompts for Deeper Understanding

1. "Explain JPMS module descriptors with exports, opens, requires, provides/uses"
1. "Show ServiceLoader plugin pattern with module declarations"
1. "Teach migration strategy from classpath to module path with jdeps"

## Key Takeaways

- module-info.java declares module name, exports, requires, opens
- exports makes public types accessible; opens enables reflection
- ServiceLoader discovers implementations via provides/uses declarations