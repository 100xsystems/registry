---
{
  "title": "Ecosystem and Next Steps",
  "description": "Mojolicious, DBI, testing, and the road ahead.",
  "type": "lesson",
  "order": 21,
  "duration": "20 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Name key frameworks and modules",
    "Write tests with Test::More",
    "Identify next advanced topics"
  ],
  "knowledge_refs": [
    "perl/perl-21-ecosystem-next-steps"
  ],
  "prerequisites": [
    "perl-19-cpan-tooling"
  ],
  "references": [
    {
      "title": "Mojolicious — Web Framework",
      "url": "https://mojolicious.org/"
    },
    {
      "title": "DBI — Database Interface",
      "url": "https://dbi.perl.org/"
    },
    {
      "title": "Perl Weekly — Newsletter",
      "url": "https://perlweekly.com/"
    },
    {
      "title": "Modern Perl — Free Book",
      "url": "https://modernperlbooks.com/"
    }
  ]
}
---

# PERL-21-ECOSYSTEM-NEXT-STEPS: Ecosystem and Next Steps

## Introduction

Mojolicious, DBI, testing, and the road ahead. By the end of this lesson you will be able to: Name key frameworks and modules; Write tests with Test::More; Identify next advanced topics.

## Key Concepts

### 1. Name key frameworks and modules

Target: Name key frameworks and modules. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```perl
# Web development with Mojolicious
use strict;
use warnings;

# use Mojolicious::Lite;
# get "/" => sub { shift->render(text => "Hello") };
# app->start;
print "Mojolicious is a modern Perl web framework\n";

```
### 2. Write tests with Test::More

Target: Write tests with Test::More. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```perl
# Database access with DBI
use strict;
use warnings;

# use DBI;
# my $dbh = DBI->connect("dbi:SQLite:dbname=test.db", "", "");
# my $sth = $dbh->prepare("SELECT * FROM users");
# $sth->execute();
print "DBI speaks to every major database\n";

```
### 3. Identify next advanced topics

Target: Identify next advanced topics. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```perl
# Testing with Test::More
use strict;
use warnings;
use Test::More;

sub double { $_[0] * 2 }
is(double(2), 4, "doubles 2 to 4");
is(double(0), 0, "doubles 0 to 0");

done_testing();

```
### 4. Name key frameworks and modules

Target: Name key frameworks and modules. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```perl
# Next steps: advanced Perl topics
# 1. Moose/Moo object systems in depth
# 2. Async with AnyEvent / IO::Async
# 3. Functional style with higher-order functions
# 4. Perl 5.40+ features: signatures, native arrays
print "You now have a complete foundation in Perl\n";

```

## Practice Questions

1. What is the key idea behind "Ecosystem and Next Steps"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Ecosystem and Next Steps with analogies and real-world examples"
1. "Show me common mistakes beginners make with Ecosystem and Next Steps"
1. "Provide advanced patterns and performance considerations for Ecosystem and Next Steps"

## Key Takeaways

- Master the core ideas of Ecosystem and Next Steps through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
