---
{
  "title": "Functions",
  "description": "Declarations, parameters, variadics, and return types.",
  "type": "lesson",
  "order": 7,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Define functions with typed parameters and returns",
    "Use default values and named arguments",
    "Collect extra args with variadics",
    "Pass by reference and by value correctly"
  ],
  "knowledge_refs": [
    "php/php-07-functions"
  ],
  "prerequisites": [
    "PHP-05"
  ],
  "references": [
    {
      "title": "PHP Manual — User-Defined Functions",
      "url": "https://www.php.net/manual/en/functions.user-defined.php"
    },
    {
      "title": "PHP Manual — Function Arguments",
      "url": "https://www.php.net/manual/en/functions.arguments.php"
    },
    {
      "title": "PHP Manual — Returning Values",
      "url": "https://www.php.net/manual/en/functions.returning-values.php"
    }
  ]
}
---

# PHP-07-FUNCTIONS: Functions

## Introduction

Declarations, parameters, variadics, and return types. By the end of this lesson you will be able to: Define functions with typed parameters and returns; Use default values and named arguments; Collect extra args with variadics; Pass by reference and by value correctly.

## Key Concepts

### 1. Define functions with typed parameters and returns

Target: Define functions with typed parameters and returns. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// typed functions
declare(strict_types=1);
function greet(string $name, int $times = 1): string {
    return str_repeat("Hi $name! ", $times);
}
echo greet("Alice") . "\n";          // Hi Alice!
echo greet("Bob", 2) . "\n";         // Hi Bob! Hi Bob!
// named arguments (PHP 8+)
echo greet(times: 3, name: "Cal") . "\n";
```
### 2. Use default values and named arguments

Target: Use default values and named arguments. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// variadics collect extra args
function sum(...$nums): int {
    return array_sum($nums);
}
echo sum(1, 2, 3, 4) . "\n";   // 10
// spread to unpack
$args = [5, 6];
echo sum(...$args) . "\n";     // 11
```
### 3. Collect extra args with variadics

Target: Collect extra args with variadics. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// union types and nullable
function parse(mixed $value): int|float {
    return is_numeric($value) ? $value + 0 : 0;
}
function maybe(?string $s): string {
    return $s ?? "empty";
}
var_dump(parse("3.5"), parse(7), maybe(null));
```
### 4. Pass by reference and by value correctly

Target: Pass by reference and by value correctly. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// by-reference and by-value
function byValue(int $n): int { $n++; return $n; }
function byRef(int &$n): void { $n++; }
$x = 10;
echo byValue($x) . "\n";  // 11
byRef($x);
echo $x . "\n";           // 11
```

## Practice Questions

1. What is the key idea behind "Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functions"
1. "Provide advanced patterns and performance considerations for Functions"

## Key Takeaways

- Master the core ideas of Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
