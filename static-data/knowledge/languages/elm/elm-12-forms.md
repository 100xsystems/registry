---
{
  "title": "Forms and User Input",
  "description": "Text fields, checkboxes, and validation.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Handle text input",
    "Use checkbox events",
    "Validate form data",
    "Show field errors"
  ],
  "knowledge_refs": [
    "elm/elm-12-forms"
  ],
  "prerequisites": [
    "Elm-11: JSON Decoding"
  ],
  "references": [
    {
      "title": "Elm Guide",
      "url": "https://guide.elm-lang.org/",
      "description": "Official guide — the best way to start"
    },
    {
      "title": "Elm Packages",
      "url": "https://package.elm-lang.org/",
      "description": "Package registry"
    },
    {
      "title": "Elm Syntax",
      "url": "https://elm-lang.org/docs/syntax",
      "description": "Language syntax reference"
    },
    {
      "title": "Elm Discourse",
      "url": "https://discourse.elm-lang.org/",
      "description": "Community forum"
    }
  ]
}
---

# ELM-12-FORMS: Forms and User Input

## Introduction

Text fields, checkboxes, and validation. By the end of this lesson you will be able to: Handle text input; Use checkbox events; Validate form data; Show field errors.

## Key Concepts

### 1. Handle text input

Target: Handle text input. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```elm
input [ type_ "text", value model.name, onInput NameChanged ] []
```
### 2. Use checkbox events

Target: Use checkbox events. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```elm
input [ type_ "checkbox", checked model.agree, onCheck AgreeChanged ] []
```
### 3. Validate form data

Target: Validate form data. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```elm
type Msg = NameChanged String

update (NameChanged name) model =
    { model | name = name }
```
### 4. Show field errors

Target: Show field errors. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```elm
validate : Model -> Result String Model
validate m =
    if String.length m.name < 2 then
        Err "name too short"
    else
        Ok m
```

## Practice Questions

1. What is the key idea behind "Forms and User Input"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Forms and User Input with analogies and real-world examples"
1. "Show me common mistakes beginners make with Forms and User Input"
1. "Provide advanced patterns and performance considerations for Forms and User Input"

## Key Takeaways

- Master the core ideas of Forms and User Input through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
