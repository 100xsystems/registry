---
{
  "title": "Arrays and Associative Arrays",
  "description": "Indexed arrays, associative arrays, slicing, and safe copying.",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Build and index arrays",
    "Use associative arrays",
    "Slice and append arrays",
    "Read files into arrays with mapfile"
  ],
  "knowledge_refs": [
    "bash/bash-07-arrays"
  ],
  "prerequisites": [
    "BASH-06"
  ],
  "references": [
    {
      "title": "Bash — Arrays",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Arrays"
    },
    {
      "title": "BashGuide — Arrays",
      "url": "https://mywiki.wooledge.org/BashGuide/Arrays"
    },
    {
      "title": "mapfile builtin",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#index-mapfile"
    }
  ]
}
---

# BASH-07-ARRAYS: Arrays and Associative Arrays

## Introduction

Indexed arrays, associative arrays, slicing, and safe copying. By the end of this lesson you will be able to: Build and index arrays; Use associative arrays; Slice and append arrays; Read files into arrays with mapfile.

## Key Concepts

### 1. Build and index arrays

Target: Build and index arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# Indexed arrays
colors=(red green blue)
colors[3]="yellow"
echo "first: ${colors[0]}"
echo "all: ${colors[*]}"
echo "count: ${#colors[@]}"
for c in "${colors[@]}"; do
  echo "color $c"
done
```
### 2. Use associative arrays

Target: Use associative arrays. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# Associative arrays (Bash 4+)
declare -A cities
cities[IN]="Mumbai"
cities[US]="New York"
cities[JP]="Tokyo"
echo "US -> ${cities[US]}"
for country in "${!cities[@]}"; do
  echo "$country -> ${cities[$country]}"
done
```
### 3. Slice and append arrays

Target: Slice and append arrays. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# Slicing and appending to arrays
nums=(1 2 3 4 5)
echo "slice 1..3: ${nums[@]:1:3}"
nums+=(6 7)
echo "appended: ${nums[*]}"
# Copy an array safely
copy=("${nums[@]}")
echo "copy count: ${#copy[@]}"
```
### 4. Read files into arrays with mapfile

Target: Read files into arrays with mapfile. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# Reading lines into an array
mapfile -t lines < /etc/hostname
echo "lines read: ${#lines[@]}"
# Or read stdin into array:
mapfile -t words <<< "one two three"
echo "words: ${words[*]}"
# mapfile is efficient — avoid while-read loops when possible
```

## Practice Questions

1. What is the key idea behind "Arrays and Associative Arrays"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays and Associative Arrays with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays and Associative Arrays"
1. "Provide advanced patterns and performance considerations for Arrays and Associative Arrays"

## Key Takeaways

- Master the core ideas of Arrays and Associative Arrays through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
