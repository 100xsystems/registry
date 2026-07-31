---
{
  "title": "Files and Streams",
  "description": "Reading and writing files, streams, and JSON.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Read and write files safely",
    "Use stream wrappers",
    "Encode and decode JSON",
    "Handle binary data"
  ],
  "knowledge_refs": [
    "php/php-12-files-streams"
  ],
  "prerequisites": [
    "PHP-07"
  ],
  "references": [
    {
      "title": "PHP Manual — Filesystem",
      "url": "https://www.php.net/manual/en/book.filesystem.php"
    },
    {
      "title": "PHP Manual — Streams",
      "url": "https://www.php.net/manual/en/book.stream.php"
    },
    {
      "title": "PHP Manual — JSON Functions",
      "url": "https://www.php.net/manual/en/ref.json.php"
    }
  ]
}
---

# PHP-12-FILES-STREAMS: Files and Streams

## Introduction

Reading and writing files, streams, and JSON. By the end of this lesson you will be able to: Read and write files safely; Use stream wrappers; Encode and decode JSON; Handle binary data.

## Key Concepts

### 1. Read and write files safely

Target: Read and write files safely. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```php
<?php
// reading and writing
$content = file_get_contents("data.txt");
file_put_contents("out.txt", strtoupper($content));
// line by line
$lines = file("data.txt", FILE_IGNORE_NEW_LINES);
foreach ($lines as $line) { echo "> $line\n"; }
```
### 2. Use stream wrappers

Target: Use stream wrappers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```php
<?php
// JSON round-trip
$data = ["name" => "Alice", "skills" => ["php", "sql"], "active" => true];
$json = json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
echo $json . "\n";
$back = json_decode($json, true);       // associative array
var_dump($back["skills"]);
if (json_last_error() !== JSON_ERROR_NONE) {
    echo "JSON error: " . json_last_error_msg() . "\n";
}
```
### 3. Encode and decode JSON

Target: Encode and decode JSON. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```php
<?php
// stream wrappers
$url = "https://example.com/";
$html = @file_get_contents($url);
// php:// memory stream
$fp = fopen("php://memory", "w+");
fwrite($fp, "buffered");
rewind($fp);
echo stream_get_contents($fp) . "\n";  // buffered
fclose($fp);
```
### 4. Handle binary data

Target: Handle binary data. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```php
<?php
// binary + fgetcsv
$csv = "name,age\nAlice,30\nBob,25\n";
$fp = fopen("php://memory", "r+");
fwrite($fp, $csv);
rewind($fp);
while (($row = fgetcsv($fp)) !== false) {
    echo implode("|", $row) . "\n";
}
fclose($fp);
```

## Practice Questions

1. What is the key idea behind "Files and Streams"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Files and Streams with analogies and real-world examples"
1. "Show me common mistakes beginners make with Files and Streams"
1. "Provide advanced patterns and performance considerations for Files and Streams"

## Key Takeaways

- Master the core ideas of Files and Streams through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
