---
{
  "title": "Build Tools: Maven and Gradle",
  "description": "Create Maven projects with pom.xml",
  "type": "lesson",
  "order": 15,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create Maven projects with pom.xml",
    "Understand Maven lifecycle phases",
    "Use Gradle for dependency management",
    "Configure plugins and profiles"
  ],
  "knowledge_refs": [
    "java/java-15-build-tools"
  ],
  "prerequisites": [
    "JV-01"
  ],
  "references": [
    {
      "title": "Maven Documentation",
      "url": "https://maven.apache.org/guides/"
    },
    {
      "title": "Gradle Documentation",
      "url": "https://docs.gradle.org/"
    },
    {
      "title": "Baeldung — Maven Guide",
      "url": "https://www.baeldung.com/maven"
    },
    {
      "title": "Baeldung — Gradle Guide",
      "url": "https://www.baeldung.com/gradle"
    }
  ]
}
---

# JAVA-15-BUILD-TOOLS: Build Tools: Maven and Gradle

## Introduction

Maven and Gradle are Java build tools. Maven uses XML (pom.xml) with convention-over-configuration. Gradle uses Groovy/Kotlin DSL with incremental builds. Both handle dependency management, compilation, testing, and packaging.

## Key Concepts

### 1. Maven pom.xml Structure

pom.xml defines project coordinates, dependencies, plugins, and build profiles. groupId:artifactId:version uniquely identify projects. Dependencies declared in <dependencies> section, resolved from Maven Central.

```java
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>my-app</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <dependencies>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.10.0</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
```

### 2. Maven Lifecycle and Plugins

Default lifecycle: validate -> compile -> test -> package -> verify -> install -> deploy. Plugins bind to phases. mvn clean test runs clean + test. Common plugins: compiler, surefire, shade, assembly, failsafe.

```java
# Maven commands
$ mvn clean          # delete target/
$ mvn compile        # compile sources
$ mvn test           # run tests
$ mvn package        # create jar/war
$ mvn install        # install to local repo
$ mvn deploy         # deploy to remote repo

# With phases and profiles
$ mvn clean install -DskipTests
$ mvn verify -P integration
$ mvn dependency:tree  # view dependency tree
```

### 3. Gradle Build Scripts

Gradle uses build.gradle (Groovy) or build.gradle.kts (Kotlin). Tasks are actions. Plugins apply configurations. Incremental builds track inputs/outputs. Gradle Wrapper (gradlew) ensures version consistency.

```java
plugins {
    id 'java'
    id 'application'
}

group = 'com.example'
version = '1.0.0'

repositories {
    mavenCentral()
}

dependencies {
    implementation 'com.google.guava:guava:33.0.0'
    testImplementation 'org.junit.jupiter:junit-jupiter:5.10.0'
}

// Custom task
tasks.register('hello') {
    doLast {
        println 'Hello, Gradle!'
    }
}
```

### 4. Dependency Management (Transitive Dependencies, Conflicts)

Dependencies bring transitive deps. Maven: nearest-wins strategy. Gradle: newest by default. Exclude transitive deps when needed. Bill of Materials (BOM) for version alignment.

```java
// Maven: exclude transitive dependency
<dependency>
    <groupId>com.example</groupId>
    <artifactId>lib</artifactId>
    <exclusions>
        <exclusion>
            <groupId>old.library</groupId>
            <artifactId>conflicting-lib</artifactId>
        </exclusion>
    </exclusions>
</dependency>

// Gradle: force version
configurations.all {
    resolutionStrategy {
        force "com.google.guava:guava:33.0.0"
    }
}
```

### 5. Multi-Module Projects

Multi-module projects organize shared code across submodules. Root POM lists modules. Submodules inherit from parent. Gradle uses settings.gradle to include modules.

```java
// Maven parent pom.xml
<modules>
    <module>core</module>
    <module>api</module>
    <module>app</module>
</modules>

// Core module inherits parent version, dependencies
// api depends on core, app depends on api

// Gradle settings.gradle.kts
rootProject.name = "my-app"
include("core", "api", "app")
```

## Practice Questions

1. What are the main phases of the Maven default lifecycle?
1. How does Maven resolve transitive dependency conflicts?
1. What is the Gradle Wrapper (gradlew)? Why use it?
1. How do you create a multi-module project in Maven?

## LLM Prompts for Deeper Understanding

1. "Explain Maven build lifecycle, plugins, profiles with examples"
1. "Show Gradle vs Maven comparison for dependency management and build speed"
1. "Teach multi-module project patterns for microservices and shared libraries"

## Key Takeaways

- Maven lifecycle: validate -> compile -> test -> package -> verify -> install -> deploy
- Gradle uses Groovy/Kotlin DSL with incremental build support
- Multi-module projects organize shared code across submodules