---
{
  "title": "Lists and Arrays",
  "description": "Indexing, slicing, stack ops, and array functions.",
  "type": "lesson",
  "order": 7,
  "duration": "30 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Index and slice arrays",
    "Use push, pop, shift, unshift",
    "Sort, reverse, and count arrays"
  ],
  "knowledge_refs": [
    "perl/perl-07-arrays"
  ],
  "prerequisites": [
    "perl-03-variables"
  ],
  "references": [
    {
      "title": "perldoc — perldata (arrays)",
      "url": "https://perldoc.perl.org/perldata#List-value-constructors"
    },
    {
      "title": "perldoc — perlfunc (push/pop)",
      "url": "https://perldoc.perl.org/perlfunc"
    }
  ]
}
---

# PERL-07-ARRAYS: Lists and Arrays

## Introduction

Indexing, slicing, stack ops, and array functions. By the end of this lesson you will be able to: Index and slice arrays; Use push, pop, shift, unshift; Sort, reverse, and count arrays.

## Key Concepts

### 1. Index and slice arrays

Target: Index and slice arrays. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# Arrays: indexing and assignment
use strict;
use warnings;

my @nums = (10, 20, 30);
print $nums[0], "\n";      # 10
print $nums[-1], "\n";     # 30 — negative index
$nums[1] = 99;
print "@nums\n";           # 10 99 30

```
### 2. Use push, pop, shift, unshift

Target: Use push, pop, shift, unshift. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# Slicing arrays
use strict;
use warnings;

my @nums = (1, 2, 3, 4, 5);
my @slice = @nums[1..3];
print "@slice\n";          # 2 3 4
my @every_other = @nums[0, 2, 4];
print "@every_other\n";    # 1 3 5

```
### 3. Sort, reverse, and count arrays

Target: Sort, reverse, and count arrays. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# push, pop, shift, unshift
use strict;
use warnings;

my @stack = ();
push @stack, 1, 2, 3;
my $top = pop @stack;      # 3
unshift @stack, 0;
my $first = shift @stack;  # 0
print "@stack\n";          # 1 2

```
### 4. Index and slice arrays

Target: Index and slice arrays. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# Array functions: sort, reverse, scalar
use strict;
use warnings;

my @nums = (5, 2, 8, 1);
my @sorted = sort { $a <=> $b } @nums;
my @reversed = reverse @sorted;
print "@sorted\n";         # 1 2 5 8
print "@reversed\n";       # 8 5 2 1
print scalar @nums, "\n";  # 4 — count

```

## Practice Questions

1. What is the key idea behind "Lists and Arrays"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Lists and Arrays with analogies and real-world examples"
1. "Show me common mistakes beginners make with Lists and Arrays"
1. "Provide advanced patterns and performance considerations for Lists and Arrays"

## Key Takeaways

- Master the core ideas of Lists and Arrays through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
