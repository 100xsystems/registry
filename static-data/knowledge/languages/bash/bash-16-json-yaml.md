---
{
  "title": "JSON and Data Parsing",
  "description": "jq for JSON: queries, transforms, building, and validation.",
  "type": "lesson",
  "order": 16,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Query JSON with jq",
    "Filter and transform with jq",
    "Build JSON payloads",
    "Validate JSON in scripts"
  ],
  "knowledge_refs": [
    "bash/bash-16-json-yaml"
  ],
  "prerequisites": [
    "BASH-15"
  ],
  "references": [
    {
      "title": "jq manual",
      "url": "https://jqlang.github.io/jq/manual/"
    },
    {
      "title": "jq Cookbook",
      "url": "https://github.com/stedolan/jq/wiki/Cookbook"
    },
    {
      "title": "yq (YAML)",
      "url": "https://github.com/mikefarah/yq"
    }
  ]
}
---

# BASH-16-JSON-YAML: JSON and Data Parsing

## Introduction

jq for JSON: queries, transforms, building, and validation. By the end of this lesson you will be able to: Query JSON with jq; Filter and transform with jq; Build JSON payloads; Validate JSON in scripts.

## Key Concepts

### 1. Query JSON with jq

Target: Query JSON with jq. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# jq: querying JSON from the shell
echo '{"name":"Alice","age":30}' | jq '.name'
echo '[1,2,3]' | jq '.[] | . * 2'
echo '{"a":1,"b":2}' | jq '.a + .b'
# Pretty-print any JSON:
echo '{"x":1}' | jq .
```
### 2. Filter and transform with jq

Target: Filter and transform with jq. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# jq: filtering and transforming
curl -fsSL https://api.github.com/repos/jqlang/jq 2>/dev/null |
  jq '{name, stars: .stargazers_count, desc: .description}' ||
  echo '{"name":"jq","stars":0}' | jq .
# Selecting array elements:
echo '[{"id":1,"ok":true},{"id":2,"ok":false}]' | jq ".[] | select(.ok)"
```
### 3. Build JSON payloads

Target: Build JSON payloads. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# Building JSON with jq
name="Alice"
age=30
jq -n --arg name "$name" --argjson age "$age" \
  '{name: $name, age: $age, active: true}'
# Array of values:
jq -n '[range(3) | {index: .}]' 
```
### 4. Validate JSON in scripts

Target: Validate JSON in scripts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# yq for YAML (install separately) — pattern shown for JSON only
# Parse CSV via awk into JSON:
printf 'Alice,30\nBob,25\n' | awk -F, '{printf "{\"name\":\"%s\",\"age\":%s}\n", $1, $2}'
# Validate JSON:
if echo '{"ok":true}' | jq -e . >/dev/null 2>&1; then
  echo "valid JSON"
fi
```

## Practice Questions

1. What is the key idea behind "JSON and Data Parsing"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain JSON and Data Parsing with analogies and real-world examples"
1. "Show me common mistakes beginners make with JSON and Data Parsing"
1. "Provide advanced patterns and performance considerations for JSON and Data Parsing"

## Key Takeaways

- Master the core ideas of JSON and Data Parsing through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
