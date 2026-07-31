---
{
  "title": "Numbers and Math",
  "description": "Integers, floats, integer overflow, and math functions.",
  "type": "lesson",
  "order": 3,
  "duration": "50 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use int and float with their limits",
    "Handle precision loss and overflow",
    "Use bcmath for exact decimal arithmetic",
    "Generate random numbers safely"
  ],
  "knowledge_refs": [
    "php/php-03-numbers-math"
  ],
  "prerequisites": [
    "PHP-02"
  ],
  "references": [
    {
      "title": "PHP Manual — Integers",
      "url": "https://www.php.net/manual/en/language.types.integer.php"
    },
    {
      "title": "PHP Manual — Floating Point",
      "url": "https://www.php.net/manual/en/language.types.float.php"
    },
    {
      "title": "PHP Manual — Math Functions",
      "url": "https://www.php.net/manual/en/ref.math.php"
    }
  ]
}
---

# PHP-03-NUMBERS-MATH: Numbers and Math

## Introduction

Integers, floats, integer overflow, and math functions. By the end of this lesson you will be able to: Use int and float with their limits; Handle precision loss and overflow; Use bcmath for exact decimal arithmetic; Generate random numbers safely.

## Key Concepts

### 1. Use int and float with their limits

Target: Use int and float with their limits. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// integer limits
$max = PHP_INT_MAX;      // 9223372036854775807 (64-bit)
$min = PHP_INT_MIN;
$big = $max + 1;         // becomes float (silent overflow)
var_dump($max, $min, $big);
echo PHP_INT_SIZE . " bytes\n";
```
### 2. Handle precision loss and overflow

Target: Handle precision loss and overflow. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// float precision pitfall
$a = 0.1;
$b = 0.2;
var_dump($a + $b);           // float(0.30000000000000004)
var_dump($a + $b === 0.3);    // bool(false)
// use an epsilon comparison
echo abs(($a + $b) - 0.3) < 1e-9 ? "close enough\n" : "not close\n";
```
### 3. Use bcmath for exact decimal arithmetic

Target: Use bcmath for exact decimal arithmetic. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// bcmath: arbitrary precision for money
$a = "0.1";
$b = "0.2";
$sum = bcadd($a, $b, 2);      // "0.30"
echo $sum . "\n";
echo bcmul("12.50", "3", 2) . "\n";  // "37.50"
```
### 4. Generate random numbers safely

Target: Generate random numbers safely. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// safe random numbers (CSPRNG)
$roll = random_int(1, 6);          // unbiased int
echo "d6: $roll\n";
echo bin2hex(random_bytes(8)) . "\n";  // 16 hex chars
// deterministic pseudo-random for games
mt_srand(42);
echo mt_rand(1, 10) . "\n";
```

## Practice Questions

1. What is the key idea behind "Numbers and Math"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Numbers and Math with analogies and real-world examples"
1. "Show me common mistakes beginners make with Numbers and Math"
1. "Provide advanced patterns and performance considerations for Numbers and Math"

## Key Takeaways

- Master the core ideas of Numbers and Math through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
