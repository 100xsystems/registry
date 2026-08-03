---
{
  "title": "Regular Expressions",
  "description": "Matching, capturing, substitution, split, and join.",
  "type": "lesson",
  "order": 10,
  "duration": "35 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Match patterns with =~",
    "Capture groups with $1, $2",
    "Substitute with s///"
  ],
  "knowledge_refs": [
    "perl/perl-10-regular-expressions"
  ],
  "prerequisites": [
    "perl-06-loops"
  ],
  "references": [
    {
      "title": "perldoc — perlre",
      "url": "https://perldoc.perl.org/perlre"
    },
    {
      "title": "perldoc — perlretut (tutorial)",
      "url": "https://perldoc.perl.org/perlretut"
    }
  ]
}
---

# PERL-10-REGULAR-EXPRESSIONS: Regular Expressions

## Introduction

Matching, capturing, substitution, split, and join. By the end of this lesson you will be able to: Match patterns with =~; Capture groups with $1, $2; Substitute with s///.

## Key Concepts

### 1. Match patterns with =~

Target: Match patterns with =~. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# Matching with =~
use strict;
use warnings;

my $text = "The quick brown fox";
print "has fox\n" if $text =~ /fox/;
print "has cat\n" if $text =~ /cat/;

```
### 2. Capture groups with $1, $2

Target: Capture groups with $1, $2. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# Capturing groups
use strict;
use warnings;

my $email = "ada@example.com";
if ($email =~ /^(.+)@(.+)$/) {
    print "user: $1\n";
    print "domain: $2\n";
}

```
### 3. Substitute with s///

Target: Substitute with s///. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# Substitution with s///
use strict;
use warnings;

my $msg = "Hello World";
$msg =~ s/World/Perl/;
print "$msg\n";            # Hello Perl
$msg =~ s/Perl/Perl!/;
print "$msg\n";            # Hello Perl!

```
### 4. Match patterns with =~

Target: Match patterns with =~. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# split and join
use strict;
use warnings;

my $csv = "a,b,c";
my @parts = split /,/, $csv;
print "@parts\n";          # a b c
my $rejoined = join "-", @parts;
print "$rejoined\n";       # a-b-c

```

## Practice Questions

1. What is the key idea behind "Regular Expressions"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Regular Expressions with analogies and real-world examples"
1. "Show me common mistakes beginners make with Regular Expressions"
1. "Provide advanced patterns and performance considerations for Regular Expressions"

## Key Takeaways

- Master the core ideas of Regular Expressions through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
