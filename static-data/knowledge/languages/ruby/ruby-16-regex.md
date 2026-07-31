---
{
  "title": "Regular Expressions",
  "description": "=~, match, scan, gsub, anchors, captures.",
  "type": "lesson",
  "order": 16,
  "duration": "75 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Match with =~ and Regexp",
    "Extract captures",
    "Scan and substitute text",
    "Write anchored and character-class patterns"
  ],
  "knowledge_refs": [
    "ruby/ruby-16-regex"
  ],
  "prerequisites": [
    "RUBY-15"
  ],
  "references": [
    {
      "title": "Ruby — Regexp",
      "url": "https://docs.ruby-lang.org/en/master/Regexp.html"
    },
    {
      "title": "Ruby — Regexp Literals",
      "url": "https://docs.ruby-lang.org/en/master/syntax/literals_rdoc.html"
    },
    {
      "title": "Ruby — String#scan",
      "url": "https://docs.ruby-lang.org/en/master/String.html#method-i-scan"
    }
  ]
}
---

# RUBY-16-REGEX: Regular Expressions

## Introduction

=~, match, scan, gsub, anchors, captures. By the end of this lesson you will be able to: Match with =~ and Regexp; Extract captures; Scan and substitute text; Write anchored and character-class patterns.

## Key Concepts

### 1. Match with =~ and Regexp

Target: Match with =~ and Regexp. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
text = "The quick brown fox"
p text =~ /quick/            # 4 (index)
p /quick/.match?(text)       # true
p text =~ /xyz/              # nil
```
### 2. Extract captures

Target: Extract captures. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
m = /(\d{2})-(\d{2})/.match("date 12-34")
p m[0]    # "12-34"
p m[1]    # "12"
p m[2]    # "34"
```
### 3. Scan and substitute text

Target: Scan and substitute text. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
p "hello 42 world".scan(/\d+/)     # ["42"]
p "a1b2".gsub(/\d/) { |d| d.to_i * 2 }   # a2b4
p "hello".sub("l", "L")            # heLlo
```
### 4. Write anchored and character-class patterns

Target: Write anchored and character-class patterns. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
p /\Astart/ === "start here"
p /end\z/ === "the end"
p /[a-z]{3}/ === "abc"
email = "a@b.com"
p email =~ /\A[^@]+@[^@]+\.[^@]+\z/   # 0 (valid)
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
