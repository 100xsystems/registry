---
{
  "title": "Classes and Objects",
  "description": "Properties, methods, constructors, and object semantics.",
  "type": "lesson",
  "order": 8,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Define classes with typed properties and methods",
    "Use constructors, promotion, and readonly properties",
    "Understand objects as references",
    "Use visibility, static, and const members"
  ],
  "knowledge_refs": [
    "php/php-08-oop-classes"
  ],
  "prerequisites": [
    "PHP-07"
  ],
  "references": [
    {
      "title": "PHP Manual — Classes and Objects",
      "url": "https://www.php.net/manual/en/language.oop5.php"
    },
    {
      "title": "PHP Manual — Properties",
      "url": "https://www.php.net/manual/en/language.oop5.properties.php"
    },
    {
      "title": "PHP 8.2 Readonly Classes",
      "url": "https://www.php.net/manual/en/language.oop5.properties.php"
    }
  ]
}
---

# PHP-08-OOP-CLASSES: Classes and Objects

## Introduction

Properties, methods, constructors, and object semantics. By the end of this lesson you will be able to: Define classes with typed properties and methods; Use constructors, promotion, and readonly properties; Understand objects as references; Use visibility, static, and const members.

## Key Concepts

### 1. Define classes with typed properties and methods

Target: Define classes with typed properties and methods. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// basic class with typed properties
class Product {
    public function __construct(
        public readonly string $name,
        public readonly float $price,
        public int $stock = 0,
    ) {}
    public function summary(): string {
        return "{$this->name} — \${$this->price} (stock: {$this->stock})";
    }
}
$p = new Product("Keyboard", 49.99, 12);
echo $p->summary() . "\n";
```
### 2. Use constructors, promotion, and readonly properties

Target: Use constructors, promotion, and readonly properties. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// objects are references
class Counter { public int $n = 0; }
$a = new Counter();
$b = $a;              // $b points to the SAME object
$b->n = 5;
echo $a->n . "\n";   // 5
echo ($a === $b ? "same instance\n" : "different\n");
```
### 3. Understand objects as references

Target: Understand objects as references. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// visibility
class Bank {
    private int $balance = 0;
    protected string $owner;
    public function __construct(string $owner) { $this->owner = $owner; }
    public function deposit(int $amount): void { $this->balance += $amount; }
    public function balance(): int { return $this->balance; }
}
$acc = new Bank("Alice");
$acc->deposit(100);
// $acc->balance = 999;  // Fatal: cannot access private
// use the accessor instead
echo $acc->balance() . "\n";
```
### 4. Use visibility, static, and const members

Target: Use visibility, static, and const members. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// static members
class MathHelper {
    public const PI = 3.14159;
    private static int $calls = 0;
    public static function square(int $n): int {
        self::$calls++;
        return $n * $n;
    }
    public static function calls(): int { return self::$calls; }
}
echo MathHelper::PI . "\n";
echo MathHelper::square(9) . "\n";
echo MathHelper::calls() . "\n";
```

## Practice Questions

1. What is the key idea behind "Classes and Objects"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Classes and Objects with analogies and real-world examples"
1. "Show me common mistakes beginners make with Classes and Objects"
1. "Provide advanced patterns and performance considerations for Classes and Objects"

## Key Takeaways

- Master the core ideas of Classes and Objects through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
