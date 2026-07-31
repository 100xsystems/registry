---
{
  "title": "Inheritance and Traits",
  "description": "extends, abstract classes, interfaces, and trait composition.",
  "type": "lesson",
  "order": 10,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Extend classes and override methods",
    "Design with abstract classes and interfaces",
    "Compose behavior with traits",
    "Use final and prevent misuse"
  ],
  "knowledge_refs": [
    "php/php-10-inheritance-traits"
  ],
  "prerequisites": [
    "PHP-08"
  ],
  "references": [
    {
      "title": "PHP Manual — Inheritance",
      "url": "https://www.php.net/manual/en/language.oop5.inheritance.php"
    },
    {
      "title": "PHP Manual — Interfaces",
      "url": "https://www.php.net/manual/en/language.oop5.interfaces.php"
    },
    {
      "title": "PHP Manual — Traits",
      "url": "https://www.php.net/manual/en/language.oop5.traits.php"
    }
  ]
}
---

# PHP-10-INHERITANCE-TRAITS: Inheritance and Traits

## Introduction

extends, abstract classes, interfaces, and trait composition. By the end of this lesson you will be able to: Extend classes and override methods; Design with abstract classes and interfaces; Compose behavior with traits; Use final and prevent misuse.

## Key Concepts

### 1. Extend classes and override methods

Target: Extend classes and override methods. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// inheritance
class Animal {
    public function __construct(protected string $name) {}
    public function speak(): string { return "..."; }
}
class Dog extends Animal {
    public function speak(): string { return "Woof!"; }
}
$d = new Dog("Rex");
echo $d->speak() . "\n";  // Woof!
```
### 2. Design with abstract classes and interfaces

Target: Design with abstract classes and interfaces. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// abstract class
abstract class Shape {
    abstract public function area(): float;
    public function describe(): string {
        return "Area: " . $this->area();
    }
}
class Circle extends Shape {
    public function __construct(private float $r) {}
    public function area(): float { return pi() * $this->r ** 2; }
}
echo (new Circle(2))->describe() . "\n";
```
### 3. Compose behavior with traits

Target: Compose behavior with traits. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// interface + multiple via composition
interface Loggable {
    public function toLog(): string;
}
class Order implements Loggable {
    public function __construct(private int $id) {}
    public function toLog(): string { return "order:$this->id"; }
}
foreach ([new Order(1), new Order(2)] as $o) {
    echo $o->toLog() . "\n";
}
```
### 4. Use final and prevent misuse

Target: Use final and prevent misuse. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// traits compose behavior without inheritance
trait Timestampable {
    private \DateTimeImmutable $createdAt;
    public function touch(): void {
        $this->createdAt = new \DateTimeImmutable();
    }
    public function createdAt(): string {
        return $this->createdAt->format("Y-m-d H:i:s");
    }
}
class Post { use Timestampable; }
$post = new Post();
$post->touch();
echo $post->createdAt() . "\n";
```

## Practice Questions

1. What is the key idea behind "Inheritance and Traits"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Inheritance and Traits with analogies and real-world examples"
1. "Show me common mistakes beginners make with Inheritance and Traits"
1. "Provide advanced patterns and performance considerations for Inheritance and Traits"

## Key Takeaways

- Master the core ideas of Inheritance and Traits through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
