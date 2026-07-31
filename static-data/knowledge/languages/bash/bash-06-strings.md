---
{
  "title": "String Manipulation",
  "description": "Length, substring, pattern removal, replacement, and defaults.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Compute length and concatenate",
    "Extract substrings",
    "Replace and transform patterns",
    "Apply parameter expansion defaults"
  ],
  "knowledge_refs": [
    "bash/bash-06-strings"
  ],
  "prerequisites": [
    "BASH-05"
  ],
  "references": [
    {
      "title": "Bash — Parameter Expansion",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Shell-Parameter-Expansion"
    },
    {
      "title": "BashGuide — Parameter Expansion",
      "url": "https://mywiki.wooledge.org/BashGuide/Parameters"
    },
    {
      "title": "Parameter Expansion Cheat Sheet",
      "url": "https://devhints.io/bash"
    }
  ]
}
---

# BASH-06-STRINGS: String Manipulation

## Introduction

Length, substring, pattern removal, replacement, and defaults. By the end of this lesson you will be able to: Compute length and concatenate; Extract substrings; Replace and transform patterns; Apply parameter expansion defaults.

## Key Concepts

### 1. Compute length and concatenate

Target: Compute length and concatenate. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# String basics: length, concatenation, uppercase
name="bash"
echo "length: ${#name}"
full="${name} scripting"
echo "$full"
upper="${name^^}"
lower="${upper,,}"
echo "upper: $upper, lower: $lower"
```
### 2. Extract substrings

Target: Extract substrings. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# Substring extraction
text="Hello, World!"
echo "${text:0:5}"      # Hello
echo "${text:7}"        # World!
echo "${text: -6}"      # World! (space before -6 needed)
# Pattern removal
path="/usr/local/bin/bash"
echo "${path#*/}"       # remove shortest prefix to first /
echo "${path##*/}"      # remove longest prefix -> bash
echo "${path%.*}"       # nothing (no dot at end)
echo "${path%/*}"       # /usr/local/bin
```
### 3. Replace and transform patterns

Target: Replace and transform patterns. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# Replacement in strings
msg="the quick brown fox"
echo "${msg/fox/dog}"           # replace first match
echo "${msg//o/0}"              # replace ALL matches
echo "${msg/#the/ThE}"          # replace at start
echo "${msg/%fox/dog}"          # replace at end
```
### 4. Apply parameter expansion defaults

Target: Apply parameter expansion defaults. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# Default values and error on unset
unset MAYBE
echo "${MAYBE:-fallback}"      # fallback if unset/empty
echo "${MAYBE:=assigned}"      # assign if unset/empty
echo "$MAYBE"                  # now assigned
echo "${REQUIRED:?must be set}"  # errors if unset (with message)
# Note: ${var?} exits the script with the message
```

## Practice Questions

1. What is the key idea behind "String Manipulation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain String Manipulation with analogies and real-world examples"
1. "Show me common mistakes beginners make with String Manipulation"
1. "Provide advanced patterns and performance considerations for String Manipulation"

## Key Takeaways

- Master the core ideas of String Manipulation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
