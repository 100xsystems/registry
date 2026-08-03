---
{
  "title": "Object-Oriented Perl",
  "description": "bless, methods, inheritance, and modern OO.",
  "type": "lesson",
  "order": 17,
  "duration": "35 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Create objects with bless",
    "Write methods and accessors",
    "Use inheritance with parent"
  ],
  "knowledge_refs": [
    "perl/perl-17-oop"
  ],
  "prerequisites": [
    "perl-12-references"
  ],
  "references": [
    {
      "title": "perldoc — perlobj",
      "url": "https://perldoc.perl.org/perlobj"
    },
    {
      "title": "perldoc — perlootut (OO tutorial)",
      "url": "https://perldoc.perl.org/perlootut"
    },
    {
      "title": "Moo — Modern OO on CPAN",
      "url": "https://metacpan.org/pod/Moo"
    }
  ]
}
---

# PERL-17-OOP: Object-Oriented Perl

## Introduction

bless, methods, inheritance, and modern OO. By the end of this lesson you will be able to: Create objects with bless; Write methods and accessors; Use inheritance with parent.

## Key Concepts

### 1. Create objects with bless

Target: Create objects with bless. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# Object-oriented Perl with bless
use strict;
use warnings;

package Point;
sub new {
    my ($class, $x, $y) = @_;
    my $self = {x => $x, y => $y};
    bless $self, $class;
    return $self;
}
sub show {
    my ($self) = @_;
    return "($self->{x}, $self->{y})";
}

my $p = Point->new(1, 2);
print $p->show, "\n";      # (1, 2)

```
### 2. Write methods and accessors

Target: Write methods and accessors. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# Methods and accessors
use strict;
use warnings;

package Counter;
sub new { bless {value => 0}, shift }
sub increment { $_[0]->{value}++ }
sub value { $_[0]->{value} }

my $c = Counter->new;
$c->increment;
$c->increment;
print $c->value, "\n";     # 2

```
### 3. Use inheritance with parent

Target: Use inheritance with parent. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# Inheritance with @ISA or parent
use strict;
use warnings;

package Animal;
sub speak { "generic animal sound" }

package Dog;
use parent -norequire, "Animal";
sub speak { "Woof!" }

print Dog->speak, "\n";    # Woof!
print Animal->speak, "\n"; # generic animal sound

```
### 4. Create objects with bless

Target: Create objects with bless. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# Modern OO with Moo/Moose
use strict;
use warnings;

# package Person;
# use Moo;
# has name => (is => "ro");
# has age  => (is => "rw");
# sub greeting { "Hi, I am " . $_[0]->name }
# 1;
print "Moo and Moose provide modern OO on CPAN\n";

```

## Practice Questions

1. What is the key idea behind "Object-Oriented Perl"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Object-Oriented Perl with analogies and real-world examples"
1. "Show me common mistakes beginners make with Object-Oriented Perl"
1. "Provide advanced patterns and performance considerations for Object-Oriented Perl"

## Key Takeaways

- Master the core ideas of Object-Oriented Perl through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
