---
{
  "title": "Nested Data Structures",
  "description": "Arrays of arrays, hashes of hashes, and traversal.",
  "type": "lesson",
  "order": 13,
  "duration": "35 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Build 2D structures with references",
    "Pass references to functions",
    "Traverse nested hashes"
  ],
  "knowledge_refs": [
    "perl/perl-13-data-structures"
  ],
  "prerequisites": [
    "perl-12-references"
  ],
  "references": [
    {
      "title": "perldoc — perldsc",
      "url": "https://perldoc.perl.org/perldsc"
    },
    {
      "title": "perldoc — perllol",
      "url": "https://perldoc.perl.org/perllol"
    }
  ]
}
---

# PERL-13-DATA-STRUCTURES: Nested Data Structures

## Introduction

Arrays of arrays, hashes of hashes, and traversal. By the end of this lesson you will be able to: Build 2D structures with references; Pass references to functions; Traverse nested hashes.

## Key Concepts

### 1. Build 2D structures with references

Target: Build 2D structures with references. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# Building nested structures
use strict;
use warnings;

my @rows = ();
for my $i (0..2) {
    my @row = ();
    for my $j (0..2) {
        push @row, $i * 10 + $j;
    }
    push @rows, \@row;
}
print $rows[2][2], "\n";          # 22

```
### 2. Pass references to functions

Target: Pass references to functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# Passing references to functions
use strict;
use warnings;

sub total {
    my ($arr_ref) = @_;
    my $sum = 0;
    $sum += $_ for @$arr_ref;
    return $sum;
}

my @nums = (1, 2, 3, 4, 5);
print total(\@nums), "\n";        # 15

```
### 3. Traverse nested hashes

Target: Traverse nested hashes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# Deep copies vs shallow references
use strict;
use warnings;

my @orig = (1, 2, 3);
my $alias = \@orig;
my @copy = @orig;                  # shallow copy of values

$alias->[0] = 99;                  # mutates @orig
print "@orig\n";                   # 99 2 3
print "@copy\n";                   # 1 2 3

```
### 4. Build 2D structures with references

Target: Build 2D structures with references. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# Walking a nested hash
use strict;
use warnings;

my $config = {
    db => {host => "localhost", pool => 10},
    cache => {ttl => 300},
};
for my $section (keys %$config) {
    my $opts = $config->{$section};
    print "$section: ", join(",", keys %$opts), "\n";
}

```

## Practice Questions

1. What is the key idea behind "Nested Data Structures"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Nested Data Structures with analogies and real-world examples"
1. "Show me common mistakes beginners make with Nested Data Structures"
1. "Provide advanced patterns and performance considerations for Nested Data Structures"

## Key Takeaways

- Master the core ideas of Nested Data Structures through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
