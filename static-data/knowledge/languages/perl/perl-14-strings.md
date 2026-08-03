---
{
  "title": "String Manipulation",
  "description": "chomp, case, substr, index, and sprintf.",
  "type": "lesson",
  "order": 14,
  "duration": "25 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Trim newlines with chomp",
    "Transform case and substrings",
    "Format output with sprintf"
  ],
  "knowledge_refs": [
    "perl/perl-14-strings"
  ],
  "prerequisites": [
    "perl-10-regular-expressions"
  ],
  "references": [
    {
      "title": "perldoc — perlfunc (chomp/substr)",
      "url": "https://perldoc.perl.org/perlfunc"
    },
    {
      "title": "perldoc — perlsyn (quotes)",
      "url": "https://perldoc.perl.org/perlsyn"
    }
  ]
}
---

# PERL-14-STRINGS: String Manipulation

## Introduction

chomp, case, substr, index, and sprintf. By the end of this lesson you will be able to: Trim newlines with chomp; Transform case and substrings; Format output with sprintf.

## Key Concepts

### 1. Trim newlines with chomp

Target: Trim newlines with chomp. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# chomp removes trailing newline
use strict;
use warnings;

my $line = "hello\n";
chomp $line;
print "[$line]\n";         # [hello]

```
### 2. Transform case and substrings

Target: Transform case and substrings. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# Case conversion and substring functions
use strict;
use warnings;

my $s = "Hello World";
print uc $s, "\n";         # HELLO WORLD
print lc $s, "\n";         # hello world
print substr($s, 0, 5), "\n";  # Hello
print index($s, "World"), "\n";  # 6

```
### 3. Format output with sprintf

Target: Format output with sprintf. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# sprintf for formatted output
use strict;
use warnings;

my $name = "Ada";
my $age = 36;
printf "%s is %d years old\n", $name, $age;
my $formatted = sprintf("%04d", 42);
print "$formatted\n";      # 0042

```
### 4. Trim newlines with chomp

Target: Trim newlines with chomp. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# length and regex-based string work
use strict;
use warnings;

my $word = "perl";
print length $word, "\n";  # 4
my $upper = ucfirst $word;
print "$upper\n";          # Perl
my $count = () = "a1b2c3" =~ /[0-9]/g;
print "$count digits\n";   # 3

```

## Practice Questions

1. What is the key idea behind "String Manipulation"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain String Manipulation with analogies and real-world examples"
1. "Show me common mistakes beginners make with String Manipulation"
1. "Provide advanced patterns and performance considerations for String Manipulation"

## Key Takeaways

- Master the core ideas of String Manipulation through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
