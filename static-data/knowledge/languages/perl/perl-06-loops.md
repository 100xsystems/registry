---
{
  "title": "Loops",
  "description": "for, foreach, while, and loop control keywords.",
  "type": "lesson",
  "order": 6,
  "duration": "25 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Iterate with for and foreach",
    "Loop with while loops",
    "Control loops with next and last"
  ],
  "knowledge_refs": [
    "perl/perl-06-loops"
  ],
  "prerequisites": [
    "perl-05-control-flow"
  ],
  "references": [
    {
      "title": "perldoc — perlsyn (loops)",
      "url": "https://perldoc.perl.org/perlsyn#Compound-Statements"
    },
    {
      "title": "perldoc — perlsyn (Loop Control)",
      "url": "https://perldoc.perl.org/perlsyn#Loop-Control"
    }
  ]
}
---

# PERL-06-LOOPS: Loops

## Introduction

for, foreach, while, and loop control keywords. By the end of this lesson you will be able to: Iterate with for and foreach; Loop with while loops; Control loops with next and last.

## Key Concepts

### 1. Iterate with for and foreach

Target: Iterate with for and foreach. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# for loops
use strict;
use warnings;

for (my $i = 0; $i < 5; $i++) {
    print "$i ";
}
print "\n";

```
### 2. Loop with while loops

Target: Loop with while loops. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# foreach over a list
use strict;
use warnings;

my @fruits = ("apple", "banana", "cherry");
foreach my $fruit (@fruits) {
    print "$fruit ";
}
print "\n";

```
### 3. Control loops with next and last

Target: Control loops with next and last. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# while loops
use strict;
use warnings;

my $n = 0;
while ($n < 5) {
    print "$n ";
    $n++;
}
print "\n";

```
### 4. Iterate with for and foreach

Target: Iterate with for and foreach. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# do-while and loop control
use strict;
use warnings;

my $i = 0;
while ($i < 10) {
    $i++;
    next if $i == 3;       # skip 3
    last if $i == 6;       # stop at 6
    print "$i ";
}
print "\n";                # 1 2 4 5

```

## Practice Questions

1. What is the key idea behind "Loops"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Loops with analogies and real-world examples"
1. "Show me common mistakes beginners make with Loops"
1. "Provide advanced patterns and performance considerations for Loops"

## Key Takeaways

- Master the core ideas of Loops through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
