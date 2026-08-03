---
{
  "title": "Hashes",
  "description": "Key-value pairs, exists, delete, and iteration.",
  "type": "lesson",
  "order": 8,
  "duration": "30 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Create and update hashes",
    "Check keys with exists",
    "Iterate with each and keys"
  ],
  "knowledge_refs": [
    "perl/perl-08-hashes"
  ],
  "prerequisites": [
    "perl-03-variables"
  ],
  "references": [
    {
      "title": "perldoc — perldata (hashes)",
      "url": "https://perldoc.perl.org/perldata#Hash-variables"
    },
    {
      "title": "perldoc — perlfunc (keys/each)",
      "url": "https://perldoc.perl.org/perlfunc"
    }
  ]
}
---

# PERL-08-HASHES: Hashes

## Introduction

Key-value pairs, exists, delete, and iteration. By the end of this lesson you will be able to: Create and update hashes; Check keys with exists; Iterate with each and keys.

## Key Concepts

### 1. Create and update hashes

Target: Create and update hashes. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# Hashes: key-value pairs
use strict;
use warnings;

my %ages = (Ada => 36, Grace => 85);
print "$ages{Ada}\n";      # 36
$ages{Linus} = 55;
print "$ages{Linus}\n";    # 55

```
### 2. Check keys with exists

Target: Check keys with exists. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# Accessing and checking hash keys
use strict;
use warnings;

my %config = (host => "localhost", port => 8080);
print "has host\n" if exists $config{host};
delete $config{port};
print "port gone\n" unless exists $config{port};

```
### 3. Iterate with each and keys

Target: Iterate with each and keys. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# keys, values, and each
use strict;
use warnings;

my %score = (a => 90, b => 80, c => 70);
my @names = keys %score;
my @vals = values %score;
print scalar @names, " keys\n";
print "total: ", $score{a} + $score{b} + $score{c}, "\n";

```
### 4. Create and update hashes

Target: Create and update hashes. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# Iterating hashes
use strict;
use warnings;

my %fruit_color = (apple => "red", banana => "yellow");
while (my ($fruit, $color) = each %fruit_color) {
    print "$fruit is $color\n";
}

```

## Practice Questions

1. What is the key idea behind "Hashes"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Hashes with analogies and real-world examples"
1. "Show me common mistakes beginners make with Hashes"
1. "Provide advanced patterns and performance considerations for Hashes"

## Key Takeaways

- Master the core ideas of Hashes through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
