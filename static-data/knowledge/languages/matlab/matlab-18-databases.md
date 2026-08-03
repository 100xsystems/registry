---
{
  "title": "Working with Tables",
  "description": "Tabular data analysis.",
  "type": "lesson",
  "order": 18,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Create tables",
    "Filter rows",
    "Group and summarize",
    "Merge tables"
  ],
  "knowledge_refs": [
    "matlab/matlab-18-databases"
  ],
  "prerequisites": [
    "Matlab-17: App Designer"
  ],
  "references": [
    {
      "title": "MATLAB Documentation",
      "url": "https://www.mathworks.com/help/matlab/",
      "description": "Official docs"
    },
    {
      "title": "MATLAB Onramp",
      "url": "https://www.mathworks.com/learn/tutorials/matlab-onramp.html",
      "description": "Official intro course"
    },
    {
      "title": "MATLAB Central",
      "url": "https://www.mathworks.com/matlabcentral/",
      "description": "Community Q&A"
    }
  ]
}
---

# MATLAB-18-DATABASES: Working with Tables

## Introduction

Tabular data analysis. By the end of this lesson you will be able to: Create tables; Filter rows; Group and summarize; Merge tables.

## Key Concepts

### 1. Create tables

Target: Create tables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```matlab
T = table([1;2;3], ["a";"b";"c"], "VariableNames", ["ID", "Name"]);
```
### 2. Filter rows

Target: Filter rows. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```matlab
T(T.ID > 1, :)
```
### 3. Group and summarize

Target: Group and summarize. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```matlab
groupsummary(T, "Name")
```
### 4. Merge tables

Target: Merge tables. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```matlab
join(T1, T2)
```

## Practice Questions

1. What is the key idea behind "Working with Tables"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Working with Tables with analogies and real-world examples"
1. "Show me common mistakes beginners make with Working with Tables"
1. "Provide advanced patterns and performance considerations for Working with Tables"

## Key Takeaways

- Master the core ideas of Working with Tables through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
