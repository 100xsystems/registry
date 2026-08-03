---
{
  "title": "Unicode and Encoding",
  "description": "utf8, Encode, file layers, and character properties.",
  "type": "lesson",
  "order": 20,
  "duration": "30 min",
  "difficulty": "expert",
  "learning_objectives": [
    "Enable utf8 in scripts",
    "Encode and decode strings",
    "Use Unicode properties in regex"
  ],
  "knowledge_refs": [
    "perl/perl-20-unicode"
  ],
  "prerequisites": [
    "perl-10-regular-expressions"
  ],
  "references": [
    {
      "title": "perldoc — perlunicode",
      "url": "https://perldoc.perl.org/perlunicode"
    },
    {
      "title": "perldoc — Encode module",
      "url": "https://perldoc.perl.org/Encode"
    }
  ]
}
---

# PERL-20-UNICODE: Unicode and Encoding

## Introduction

utf8, Encode, file layers, and character properties. By the end of this lesson you will be able to: Enable utf8 in scripts; Encode and decode strings; Use Unicode properties in regex.

## Key Concepts

### 1. Enable utf8 in scripts

Target: Enable utf8 in scripts. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# Unicode handling with utf8
use strict;
use warnings;
use utf8;
use Encode;

my $text = "héllo wörld";
print "char count: ", length($text), "\n";
my $bytes = encode("UTF-8", $text);
print "byte count: ", length($bytes), "\n";

```
### 2. Encode and decode strings

Target: Encode and decode strings. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# Reading UTF-8 from files
use strict;
use warnings;
use utf8;
use open ':std', ':encoding(UTF-8)';

# open my $fh, "<:encoding(UTF-8)", "file.txt" or die $!;
print "open with :encoding(UTF-8) layer\n";

```
### 3. Use Unicode properties in regex

Target: Use Unicode properties in regex. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# Decoding external input
use strict;
use warnings;
use Encode qw(decode encode is_utf8);

my $bytes = "\xc3\xa9";      # é (U+00E9) encoded as UTF-8 bytes
my $decoded = decode("UTF-8", $bytes);
print "decoded: $decoded\n";

```
### 4. Enable utf8 in scripts

Target: Enable utf8 in scripts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# Unicode properties in regex
use strict;
use warnings;
use utf8;

my $greek = "αβγ";
print "greek letters\n" if $greek =~ /[\p{Greek}]/;
print "matched letter\n" if $greek =~ /\p{L}+/;

```

## Practice Questions

1. What is the key idea behind "Unicode and Encoding"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Unicode and Encoding with analogies and real-world examples"
1. "Show me common mistakes beginners make with Unicode and Encoding"
1. "Provide advanced patterns and performance considerations for Unicode and Encoding"

## Key Takeaways

- Master the core ideas of Unicode and Encoding through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
