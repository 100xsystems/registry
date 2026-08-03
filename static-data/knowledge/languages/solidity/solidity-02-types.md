---
{
  "title": "Value Types",
  "description": "uint, int, address, bool, and bytes.",
  "type": "lesson",
  "order": 2,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Use unsigned and signed integers",
    "Work with addresses",
    "Use bool and bytes",
    "Understand type conversion"
  ],
  "knowledge_refs": [
    "solidity/solidity-02-types"
  ],
  "prerequisites": [
    "Solidity-01: Getting Started with Solidity"
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

# SOLIDITY-02-TYPES: Value Types

## Introduction

uint, int, address, bool, and bytes. By the end of this lesson you will be able to: Use unsigned and signed integers; Work with addresses; Use bool and bytes; Understand type conversion.

## Key Concepts

### 1. Use unsigned and signed integers

Target: Use unsigned and signed integers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
uint256 public big = 1e18;
uint8 public small = 255;
```
### 2. Work with addresses

Target: Work with addresses. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
address public wallet = 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4;
```
### 3. Use bool and bytes

Target: Use bool and bytes. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
bool public active = true;
bytes32 public hash = keccak256(abi.encodePacked("data"));
```
### 4. Understand type conversion

Target: Understand type conversion. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
uint8 a = 200;
uint16 b = uint16(a) * 2;   // explicit widening
```

## Practice Questions

1. What is the key idea behind "Value Types"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Value Types with analogies and real-world examples"
1. "Show me common mistakes beginners make with Value Types"
1. "Provide advanced patterns and performance considerations for Value Types"

## Key Takeaways

- Master the core ideas of Value Types through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
