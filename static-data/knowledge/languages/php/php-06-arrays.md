---
{
  "title": "Arrays",
  "description": "Indexed and associative arrays, array functions, and sorting.",
  "type": "lesson",
  "order": 6,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Build indexed and associative arrays",
    "Add, remove, and look up elements",
    "Use array_* functions for transformation",
    "Sort arrays with stable comparators"
  ],
  "knowledge_refs": [
    "php/php-06-arrays"
  ],
  "prerequisites": [
    "PHP-05"
  ],
  "references": [
    {
      "title": "PHP Manual — Arrays",
      "url": "https://www.php.net/manual/en/language.types.array.php"
    },
    {
      "title": "PHP Manual — Array Functions",
      "url": "https://www.php.net/manual/en/ref.array.php"
    },
    {
      "title": "PHP Manual — Sorting Arrays",
      "url": "https://www.php.net/manual/en/array.sorting.php"
    }
  ]
}
---

# PHP-06-ARRAYS: Arrays

## Introduction

Indexed and associative arrays, array functions, and sorting. By the end of this lesson you will be able to: Build indexed and associative arrays; Add, remove, and look up elements; Use array_* functions for transformation; Sort arrays with stable comparators.

## Key Concepts

### 1. Build indexed and associative arrays

Target: Build indexed and associative arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// indexed and associative arrays
$fruits = ["apple", "banana", "cherry"];
$user = [
    "name" => "Alice",
    "age" => 30,
    "admin" => true,
];
$fruits[] = "date";            // append
unset($user["age"]);           // remove
echo count($fruits) . "\n";    // 4
echo $user["name"] . "\n";
```
### 2. Add, remove, and look up elements

Target: Add, remove, and look up elements. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// array key/array functions
$nums = [3, 1, 4, 1, 5];
var_dump(in_array(4, $nums, true));  // bool(true) strict
echo array_search(5, $nums) . "\n"; // index 4
echo max($nums) . " " . min($nums) . "\n";
echo array_sum($nums) . "\n";       // 14
```
### 3. Use array_* functions for transformation

Target: Use array_* functions for transformation. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// transform and filter
$nums = [1, 2, 3, 4, 5];
$doubled = array_map(fn($n) => $n * 2, $nums);
$evens   = array_filter($nums, fn($n) => $n % 2 === 0);
$sum     = array_reduce($nums, fn($c, $n) => $c + $n, 0);
var_dump($doubled, array_values($evens), $sum);
```
### 4. Sort arrays with stable comparators

Target: Sort arrays with stable comparators. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// sorting
$words = ["pear", "apple", "Mango", "banana"];
sort($words);                    // in-place, case-sensitive
var_dump($words);
$users = [["name" => "Bob", "age" => 40], ["name" => "Amy", "age" => 25]];
usort($users, fn($a, $b) => $a["age"] <=> $b["age"]);
var_dump(array_column($users, "name"));  // Amy Bob
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
