---
{
  "title": "Mappings and Structs",
  "description": "Key-value storage and structured data.",
  "type": "lesson",
  "order": 7,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Use mapping types",
    "Define structs",
    "Combine mappings with structs",
    "Iterate with arrays"
  ],
  "knowledge_refs": [
    "solidity/solidity-07-mappings"
  ],
  "prerequisites": [
    "Solidity-06: Errors and Require"
  ],
  "references": [
    {
      "title": "Solidity Documentation",
      "url": "https://docs.soliditylang.org/",
      "description": "Official language docs"
    },
    {
      "title": "Solidity by Example",
      "url": "https://solidity-by-example.org/",
      "description": "Learn by working examples"
    },
    {
      "title": "CryptoZombies",
      "url": "https://cryptozombies.io/",
      "description": "Interactive Solidity tutorial"
    },
    {
      "title": "Ethereum Development Docs",
      "url": "https://ethereum.org/en/developers/docs/",
      "description": "Ethereum developer docs"
    }
  ]
}
---

# SOLIDITY-07-MAPPINGS: Mappings and Structs

## Introduction

Key-value storage and structured data. By the end of this lesson you will be able to: Use mapping types; Define structs; Combine mappings with structs; Iterate with arrays.

## Key Concepts

### 1. Use mapping types

Target: Use mapping types. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
mapping(address => uint256) public balances;
```
### 2. Define structs

Target: Define structs. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
struct User {
    string name;
    uint256 age;
}

mapping(address => User) public users;
```
### 3. Combine mappings with structs

Target: Combine mappings with structs. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
mapping(address => uint256[]) public payments;
```
### 4. Iterate with arrays

Target: Iterate with arrays. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
mapping(address => mapping(address => uint256)) public allowances;
```

## Practice Questions

1. What is the key idea behind "Mappings and Structs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Mappings and Structs with analogies and real-world examples"
1. "Show me common mistakes beginners make with Mappings and Structs"
1. "Provide advanced patterns and performance considerations for Mappings and Structs"

## Key Takeaways

- Master the core ideas of Mappings and Structs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
