---
{
  "title": "Functional PHP",
  "description": "Closures, arrow functions, and higher-order helpers.",
  "type": "lesson",
  "order": 15,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create closures and bind state with use",
    "Write concise arrow functions",
    "Use array_map, array_filter, array_reduce",
    "Leverage first-class callable syntax"
  ],
  "knowledge_refs": [
    "php/php-15-functional"
  ],
  "prerequisites": [
    "PHP-07"
  ],
  "references": [
    {
      "title": "PHP Manual — Anonymous Functions",
      "url": "https://www.php.net/manual/en/functions.anonymous.php"
    },
    {
      "title": "PHP Manual — Arrow Functions",
      "url": "https://www.php.net/manual/en/functions.arrow.php"
    },
    {
      "title": "PHP Manual — array_map",
      "url": "https://www.php.net/manual/en/function.array-map.php"
    }
  ]
}
---

# PHP-15-FUNCTIONAL: Functional PHP

## Introduction

Closures, arrow functions, and higher-order helpers. By the end of this lesson you will be able to: Create closures and bind state with use; Write concise arrow functions; Use array_map, array_filter, array_reduce; Leverage first-class callable syntax.

## Key Concepts

### 1. Create closures and bind state with use

Target: Create closures and bind state with use. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// closures capture state with use
$factor = 2;
$multiply = function (int $n) use ($factor): int {
    return $n * $factor;
};
echo $multiply(21) . "\n";  // 42
// closures are objects: can bind
$greet = function (): string { return "Hi " . $this->name; };
$bound = $greet->bindTo((object) ["name" => "Alice"]);
echo $bound() . "\n";
```
### 2. Write concise arrow functions

Target: Write concise arrow functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// arrow functions are compact and capture automatically
$tax = 0.2;
$prices = [10, 20, 30];
$withTax = array_map(fn(int $p): float => $p * (1 + $tax), $prices);
var_dump($withTax);
```
### 3. Use array_map, array_filter, array_reduce

Target: Use array_map, array_filter, array_reduce. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// higher-order helpers
$people = [
    ["name" => "Alice", "age" => 30],
    ["name" => "Bob", "age" => 17],
    ["name" => "Cal", "age" => 25],
];
$adults = array_filter($people, fn($p) => $p["age"] >= 18);
$names = array_map(fn($p) => $p["name"], $adults);
sort($names);
var_dump($names);  // Alice Cal
```
### 4. Leverage first-class callable syntax

Target: Leverage first-class callable syntax. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// first-class callable syntax (PHP 8.1+)
$toUpper = strtoupper(...);
$words = ["php", "100x"];
var_dump(array_map($toUpper, $words));
// invoke any callable
echo is_callable($toUpper) ? "callable\n" : "no\n";
```

## Practice Questions

1. What is the key idea behind "Functional PHP"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Functional PHP with analogies and real-world examples"
1. "Show me common mistakes beginners make with Functional PHP"
1. "Provide advanced patterns and performance considerations for Functional PHP"

## Key Takeaways

- Master the core ideas of Functional PHP through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
