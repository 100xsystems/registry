---
{
  "title": "Strings and String Functions",
  "description": "String literals, interpolation, and the string function toolbox.",
  "type": "lesson",
  "order": 4,
  "duration": "60 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Write strings with single/double quotes, heredoc, and nowdoc",
    "Interpolate variables safely",
    "Manipulate strings with built-in functions",
    "Work with multibyte strings via mbstring"
  ],
  "knowledge_refs": [
    "php/php-04-strings"
  ],
  "prerequisites": [
    "PHP-02"
  ],
  "references": [
    {
      "title": "PHP Manual — Strings",
      "url": "https://www.php.net/manual/en/language.types.string.php"
    },
    {
      "title": "PHP Manual — String Functions",
      "url": "https://www.php.net/manual/en/ref.strings.php"
    },
    {
      "title": "PHP Manual — mbstring",
      "url": "https://www.php.net/manual/en/book.mbstring.php"
    }
  ]
}
---

# PHP-04-STRINGS: Strings and String Functions

## Introduction

String literals, interpolation, and the string function toolbox. By the end of this lesson you will be able to: Write strings with single/double quotes, heredoc, and nowdoc; Interpolate variables safely; Manipulate strings with built-in functions; Work with multibyte strings via mbstring.

## Key Concepts

### 1. Write strings with single/double quotes, heredoc, and nowdoc

Target: Write strings with single/double quotes, heredoc, and nowdoc. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// string literals
$single = 'It costs $5\n';       // no interpolation, literal \n
$double = "Total: $5\n";          // interpolation attempted
$name = "Alice";
$interp = "Hi $name, welcome!";   // simple interpolation
$braced = "Hi {$name}s, welcome!"; // brace to disambiguate
echo $single . $interp . "\n" . $braced . "\n";
```
### 2. Interpolate variables safely

Target: Interpolate variables safely. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// heredoc (interpolates) and nowdoc (does not)
$name = "Bob";
$heredoc = <<<TXT
Hello $name,
multi-line string here.
TXT;
$nowdoc = <<<'TXT'
Hello $name,
literal $name here.
TXT;
echo $heredoc . "\n" . $nowdoc;
```
### 3. Manipulate strings with built-in functions

Target: Manipulate strings with built-in functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// the string toolbox
$s = "  Hello, World  ";
echo strlen($s) . "\n";            // 16
echo strtoupper(trim($s)) . "\n"; // HELLO, WORLD
echo substr($s, 2, 5) . "\n";     // Hello
echo str_replace("World", "PHP", $s) . "\n";
echo str_contains($s, "World") ? "yes\n" : "no\n";
```
### 4. Work with multibyte strings via mbstring

Target: Work with multibyte strings via mbstring. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// multibyte safety with mbstring
$utf8 = "héllo wörld";
echo strlen($utf8) . " " . mb_strlen($utf8) . "\n";  // 12 11
$emoji = "🚀 rocket";
echo mb_strlen($emoji) . "\n";     // 7 (not 8 bytes)
echo mb_strtoupper($utf8) . "\n";  // HÉLLO WÖRLD
```

## Practice Questions

1. What is the key idea behind "Strings and String Functions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Strings and String Functions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Strings and String Functions"
1. "Provide advanced patterns and performance considerations for Strings and String Functions"

## Key Takeaways

- Master the core ideas of Strings and String Functions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
