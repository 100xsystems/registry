---
{
  "title": "References",
  "description": "Scalar, array, hash references, and dereferencing.",
  "type": "lesson",
  "order": 12,
  "duration": "35 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create references with backslash",
    "Dereference with arrow and $$",
    "Build anonymous structures"
  ],
  "knowledge_refs": [
    "perl/perl-12-references"
  ],
  "prerequisites": [
    "perl-08-hashes"
  ],
  "references": [
    {
      "title": "perldoc — perlreftut",
      "url": "https://perldoc.perl.org/perlreftut"
    },
    {
      "title": "perldoc — perlref",
      "url": "https://perldoc.perl.org/perlref"
    }
  ]
}
---

# PERL-12-REFERENCES: References

## Introduction

Scalar, array, hash references, and dereferencing. By the end of this lesson you will be able to: Create references with backslash; Dereference with arrow and $$; Build anonymous structures.

## Key Concepts

### 1. Create references with backslash

Target: Create references with backslash. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# References: scalars, arrays, and hashes
use strict;
use warnings;

my $scalar_ref = \"value";
my @array = (1, 2, 3);
my $array_ref = \@array;
my %hash = (a => 1);
my $hash_ref = \%hash;

print $$scalar_ref, "\n";        # value
print $array_ref->[0], "\n";     # 1
print $hash_ref->{a}, "\n";      # 1

```
### 2. Dereference with arrow and $$

Target: Dereference with arrow and $$. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# Anonymous references
use strict;
use warnings;

my $arr = [1, 2, 3];
my $hash = {name => "Ada", age => 36};
print $arr->[2], "\n";           # 3
print $hash->{name}, "\n";       # Ada

```
### 3. Build anonymous structures

Target: Build anonymous structures. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# Array of arrays (2D structures)
use strict;
use warnings;

my $matrix = [
    [1, 2],
    [3, 4],
];
print $matrix->[1][0], "\n";     # 3
$matrix->[0][1] = 99;
print $matrix->[0][1], "\n";     # 99

```
### 4. Create references with backslash

Target: Create references with backslash. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# Hash of hashes
use strict;
use warnings;

my $people = {
    Ada => {age => 36, lang => "Ada"},
    Grace => {age => 85, lang => "COBOL"},
};
print $people->{Grace}{lang}, "\n";   # COBOL

```

## Practice Questions

1. What is the key idea behind "References"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain References with analogies and real-world examples"
1. "Show me common mistakes beginners make with References"
1. "Provide advanced patterns and performance considerations for References"

## Key Takeaways

- Master the core ideas of References through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
