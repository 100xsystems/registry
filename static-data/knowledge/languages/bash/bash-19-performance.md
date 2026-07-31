---
{
  "title": "Performance",
  "description": "Builtins over forks, timing, profiling, and caching.",
  "type": "lesson",
  "order": 19,
  "duration": "75 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Avoid external process forks",
    "Time and profile scripts",
    "Batch work into single passes",
    "Cache expensive results"
  ],
  "knowledge_refs": [
    "bash/bash-19-performance"
  ],
  "prerequisites": [
    "BASH-18"
  ],
  "references": [
    {
      "title": "Bash — Why builtins are faster",
      "url": "https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins"
    },
    {
      "title": "Bash pitfalls (BashPitfalls)",
      "url": "https://mywiki.wooledge.org/BashPitfalls"
    },
    {
      "title": "time — GNU manual",
      "url": "https://www.gnu.org/software/time/"
    }
  ]
}
---

# BASH-19-PERFORMANCE: Performance

## Introduction

Builtins over forks, timing, profiling, and caching. By the end of this lesson you will be able to: Avoid external process forks; Time and profile scripts; Batch work into single passes; Cache expensive results.

## Key Concepts

### 1. Avoid external process forks

Target: Avoid external process forks. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```bash
#!/usr/bin/env bash
# Avoiding external processes: builtins win
# BAD:  for f in $(cat list.txt)
# GOOD: while read -r f <&3; do ... done 3< list.txt
# printf is a builtin; echo with -e is not portable:
printf 'value=%s\n' "$x"
# Arithmetic in the shell, not awk:
sum=$(( 3 + 4 * 2 ))
echo "sum=$sum"
```
### 2. Time and profile scripts

Target: Time and profile scripts. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```bash
#!/usr/bin/env bash
# Timing and profiling a script
start=$(date +%s%N)
sleep 0.1
end=$(date +%s%N)
echo "elapsed: $(( (end - start) / 1000000 ))ms"
# Or use the `time` keyword:
time ( sleep 0.1 )
```
### 3. Batch work into single passes

Target: Batch work into single passes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```bash
#!/usr/bin/env bash
# Reduce forking: group work into one awk/one sed pass
# BAD: 3 forks per line
# GOOD: single awk pass
awk '{s+=$1} END {print s}' numbers.txt
# Bash pattern matching instead of external grep:
if [[ "$str" == *error* ]]; then
  echo "contains error"
fi
# $RANDOM is a builtin:
echo "random: $RANDOM"
```
### 4. Cache expensive results

Target: Cache expensive results. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```bash
#!/usr/bin/env bash
# Memoization and caching in a loop
cached=""
for url in $(cat urls.txt); do
  key=$(echo "$url" | md5 -q 2>/dev/null || echo "$url")
  if [ -f "/tmp/cache/$key" ]; then
    echo "cached: $url"
    continue
  fi
  sleep 0.2   # simulate fetch
  mkdir -p /tmp/cache
  echo "$url" > "/tmp/cache/$key"
  echo "fetched: $url"
done
```

## Practice Questions

1. What is the key idea behind "Performance"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Performance with analogies and real-world examples"
1. "Show me common mistakes beginners make with Performance"
1. "Provide advanced patterns and performance considerations for Performance"

## Key Takeaways

- Master the core ideas of Performance through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
