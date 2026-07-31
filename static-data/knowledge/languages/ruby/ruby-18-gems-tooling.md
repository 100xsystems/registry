---
{
  "title": "Gems, Bundler, and Standard Library",
  "description": "Gems, JSON, dates, Net::HTTP, and the standard library.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Understand gems and Bundler",
    "Parse and generate JSON",
    "Work with dates and times",
    "Make HTTP requests"
  ],
  "knowledge_refs": [
    "ruby/ruby-18-gems-tooling"
  ],
  "prerequisites": [
    "RUBY-17"
  ],
  "references": [
    {
      "title": "RubyGems Guides",
      "url": "https://guides.rubygems.org/"
    },
    {
      "title": "Ruby — JSON",
      "url": "https://docs.ruby-lang.org/en/master/JSON.html"
    },
    {
      "title": "Ruby — Net::HTTP",
      "url": "https://docs.ruby-lang.org/en/master/Net/HTTP.html"
    }
  ]
}
---

# RUBY-18-GEMS-TOOLING: Gems, Bundler, and Standard Library

## Introduction

Gems, JSON, dates, Net::HTTP, and the standard library. By the end of this lesson you will be able to: Understand gems and Bundler; Parse and generate JSON; Work with dates and times; Make HTTP requests.

## Key Concepts

### 1. Understand gems and Bundler

Target: Understand gems and Bundler. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```ruby
# gems + Bundler
# Gemfile:
#   source "https://rubygems.org"
#   gem "rails"
#   gem "json"
#   bundle install
p Gem::Specification.find_all_by_name("json").any?
```
### 2. Parse and generate JSON

Target: Parse and generate JSON. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```ruby
require "json"
data = { name: "Alice", tags: [1, 2] }
json = JSON.generate(data)
p json
p JSON.parse(json)
```
### 3. Work with dates and times

Target: Work with dates and times. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```ruby
require "date"
d = Date.today
p d.year
p (d + 7).to_s
require "time"
p Time.now.strftime("%Y-%m-%d")
```
### 4. Make HTTP requests

Target: Make HTTP requests. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```ruby
require "net/http"
require "uri"
uri = URI("https://example.com")
res = Net::HTTP.get_response(uri)
p res.code    # "200"
p res.body.length
```

## Practice Questions

1. What is the key idea behind "Gems, Bundler, and Standard Library"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Gems, Bundler, and Standard Library with analogies and real-world examples"
1. "Show me common mistakes beginners make with Gems, Bundler, and Standard Library"
1. "Provide advanced patterns and performance considerations for Gems, Bundler, and Standard Library"

## Key Takeaways

- Master the core ideas of Gems, Bundler, and Standard Library through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
