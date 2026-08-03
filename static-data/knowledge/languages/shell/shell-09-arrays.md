---
{
  "title": "Arrays",
  "description": "Indexed and associative arrays for structured data.",
  "type": "lesson",
  "order": 9,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Declare and index arrays",
    "Iterate and slice arrays",
    "Use associative arrays (Bash 4+)",
    "Apply arrays in real scripts"
  ],
  "knowledge_refs": [
    "shell/shell-09-arrays"
  ],
  "prerequisites": [
    "Shell-08: String Manipulation"
  ],
  "references": [
    {
      "title": "GNU Bash Reference Manual",
      "url": "https://www.gnu.org/software/bash/manual/bash.html",
      "description": "The authoritative Bash reference"
    },
    {
      "title": "ShellCheck",
      "url": "https://www.shellcheck.net/",
      "description": "Static analysis for shell scripts"
    },
    {
      "title": "BashGuide (Bash Hackers Wiki)",
      "url": "https://wiki.bash-hackers.org/",
      "description": "Practical Bash wiki"
    },
    {
      "title": "Explain Shell",
      "url": "https://explainshell.com/",
      "description": "Break down any command line"
    }
  ]
}
---

# SHELL-09-ARRAYS: Arrays

## Introduction

Indexed and associative arrays for structured data. By the end of this lesson you will be able to: Declare and index arrays; Iterate and slice arrays; Use associative arrays (Bash 4+); Apply arrays in real scripts.

## Key Concepts

### 1. Declare and index arrays

Target: Declare and index arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
colors=(red green blue)
echo "${colors[1]}"
```
### 2. Iterate and slice arrays

Target: Iterate and slice arrays. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
colors=(red green blue)
for c in "${colors[@]}"; do
  echo "$c"
done
```
### 3. Use associative arrays (Bash 4+)

Target: Use associative arrays (Bash 4+). Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
declare -A caps
caps[us]="Washington"
caps[uk]="London"
echo "${caps[us]}"
```
### 4. Apply arrays in real scripts

Target: Apply arrays in real scripts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
nums=(1 2 3 4 5)
echo "${#nums[@]}"      # length
unset nums[0]         # remove element
```

## Practice Questions

1. What is the key idea behind "Arrays"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Arrays with analogies and real-world examples"
1. "Show me common mistakes beginners make with Arrays"
1. "Provide advanced patterns and performance considerations for Arrays"

## Key Takeaways

- Master the core ideas of Arrays through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
