---
{
  "title": "Control Flow",
  "description": "Conditionals, match expressions, and loops.",
  "type": "lesson",
  "order": 5,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use if/elseif/else and ternary conditions",
    "Replace switch with the match expression",
    "Iterate with for, foreach, while, and do-while",
    "Break, continue, and goto responsibly"
  ],
  "knowledge_refs": [
    "php/php-05-control-flow"
  ],
  "prerequisites": [
    "PHP-02"
  ],
  "references": [
    {
      "title": "PHP Manual — Control Structures",
      "url": "https://www.php.net/manual/en/language.control-structures.php"
    },
    {
      "title": "PHP Manual — match",
      "url": "https://www.php.net/manual/en/control-structures.match.php"
    },
    {
      "title": "PHP Manual — foreach",
      "url": "https://www.php.net/manual/en/control-structures.foreach.php"
    }
  ]
}
---

# PHP-05-CONTROL-FLOW: Control Flow

## Introduction

Conditionals, match expressions, and loops. By the end of this lesson you will be able to: Use if/elseif/else and ternary conditions; Replace switch with the match expression; Iterate with for, foreach, while, and do-while; Break, continue, and goto responsibly.

## Key Concepts

### 1. Use if/elseif/else and ternary conditions

Target: Use if/elseif/else and ternary conditions. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
$score = 85;
if ($score >= 90) {
    echo "A\n";
} elseif ($score >= 80) {
    echo "B\n";
} else {
    echo "C\n";
}
// ternary + null coalescing
$grade = $score >= 50 ? "pass" : "fail";
echo $grade . "\n";
```
### 2. Replace switch with the match expression

Target: Replace switch with the match expression. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// match is an expression: returns a value, strict ===
$status = 404;
$message = match ($status) {
    200, 204 => "ok",
    404     => "not found",
    500     => "server error",
    default => "unknown",
};
echo $message . "\n";  // not found
```
### 3. Iterate with for, foreach, while, and do-while

Target: Iterate with for, foreach, while, and do-while. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// loops
for ($i = 0; $i < 5; $i++) { echo $i; }       // 01234
echo "\n";
$items = ["a", "b", "c"];
foreach ($items as $k => $v) { echo "$k:$v "; } // 0:a 1:b 2:c
echo "\n";
$n = 0;
while ($n < 3) { echo $n++; }                  // 012
echo "\n";
```
### 4. Break, continue, and goto responsibly

Target: Break, continue, and goto responsibly. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// break/continue
for ($i = 1; $i <= 10; $i++) {
    if ($i % 3 === 0) continue;   // skip multiples of 3
    if ($i === 8) break;
    echo $i;
}
echo "\n";  // 12457
```

## Practice Questions

1. What is the key idea behind "Control Flow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Control Flow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Control Flow"
1. "Provide advanced patterns and performance considerations for Control Flow"

## Key Takeaways

- Master the core ideas of Control Flow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
