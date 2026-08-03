---
{
  "title": "Gas Optimization",
  "description": "Reduce deployment and execution costs.",
  "type": "lesson",
  "order": 15,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Optimize storage usage",
    "Use calldata over memory",
    "Pack variables tightly",
    "Avoid expensive operations"
  ],
  "knowledge_refs": [
    "solidity/solidity-15-gas"
  ],
  "prerequisites": [
    "Solidity-14: Security: Overflows and Front-running"
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

# SOLIDITY-15-GAS: Gas Optimization

## Introduction

Reduce deployment and execution costs. By the end of this lesson you will be able to: Optimize storage usage; Use calldata over memory; Pack variables tightly; Avoid expensive operations.

## Key Concepts

### 1. Optimize storage usage

Target: Optimize storage usage. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
// Packed: 1 slot
struct Packed {
    uint128 a;
    uint128 b;
}
// Unpacked: 2 slots
struct Unpacked {
    uint256 a;
    uint256 b;
}
```
### 2. Use calldata over memory

Target: Use calldata over memory. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
function read(string calldata s) external pure returns (uint) {
    return bytes(s).length;
}
```
### 3. Pack variables tightly

Target: Pack variables tightly. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
uint256 private immutable deployedAt;
constructor() {
    deployedAt = block.timestamp;
}
```
### 4. Avoid expensive operations

Target: Avoid expensive operations. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
require(gasleft() > 2300, "not enough gas");
```

## Practice Questions

1. What is the key idea behind "Gas Optimization"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Gas Optimization with analogies and real-world examples"
1. "Show me common mistakes beginners make with Gas Optimization"
1. "Provide advanced patterns and performance considerations for Gas Optimization"

## Key Takeaways

- Master the core ideas of Gas Optimization through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
