---
{
  "title": "Builds and Dependencies with sbt",
  "description": "Configure builds, manage dependencies and run tasks with sbt.",
  "type": "lesson",
  "order": 18,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Understand the build.sbt structure and settings",
    "Add library dependencies from Maven Central",
    "Run compile, test and run tasks with the sbt shell",
    "Organize multi-module projects with subprojects"
  ],
  "knowledge_refs": [
    "scala/scala-18-sbt-builds"
  ],
  "prerequisites": [
    "SCALA-17"
  ],
  "references": [
    "https://www.scala-sbt.org/1.x/docs/Basic-Def.html",
    "https://www.scala-sbt.org/1.x/docs/Library-Management.html",
    "https://docs.scala-lang.org/overviews/parallel-collections/overview.html"
  ]
}
---

# SCALA-18-SBT-BUILDS: Builds and Dependencies with sbt

## Introduction

Configure builds, manage dependencies and run tasks with sbt. By the end of this lesson you will be able to: Understand the build.sbt structure and settings; Add library dependencies from Maven Central; Run compile, test and run tasks with the sbt shell; Organize multi-module projects with subprojects.

## Key Concepts

### 1. Understand the build.sbt structure and settings

Target: Understand the build.sbt structure and settings. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```scala
// build.sbt basics
ThisBuild / scalaVersion := "3.3.4"
ThisBuild / organization := "dev.example"
lazy val root = project.in(file("."))
  .settings(name := "myapp")
```
### 2. Add library dependencies from Maven Central

Target: Add library dependencies from Maven Central. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```scala
// library dependencies
ThisBuild / scalaVersion := "3.3.4"
libraryDependencies ++= Seq(
  "org.scalameta" %% "munit" % "1.0.2" % Test,
  "com.lihaoyi" %% "upickle" % "4.0.2"
)
```
### 3. Run compile, test and run tasks with the sbt shell

Target: Run compile, test and run tasks with the sbt shell. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```scala
// multi-module project
lazy val core = project.in(file("core"))
  .settings(name := "core")
lazy val api = project.in(file("api"))
  .dependsOn(core)
  .settings(name := "api")
```
### 4. Organize multi-module projects with subprojects

Target: Organize multi-module projects with subprojects. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```scala
// sbt shell commands
// > compile
// > test
// > run
// > clean
// > reload
// > console
```

## Practice Questions

1. What is the key idea behind "Builds and Dependencies with sbt"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Builds and Dependencies with sbt with analogies and real-world examples"
1. "Show me common mistakes beginners make with Builds and Dependencies with sbt"
1. "Provide advanced patterns and performance considerations for Builds and Dependencies with sbt"

## Key Takeaways

- Master the core ideas of Builds and Dependencies with sbt through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
