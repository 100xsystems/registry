---
{
  "title": "State Variables and Storage",
  "description": "Storage, memory, and calldata.",
  "type": "lesson",
  "order": 3,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Declare state variables",
    "Understand storage locations",
    "Use memory in functions",
    "Distinguish calldata"
  ],
  "knowledge_refs": [
    "solidity/solidity-03-state-variables"
  ],
  "prerequisites": [
    "Solidity-02: Value Types"
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

# SOLIDITY-03-STATE-VARIABLES: State Variables and Storage

## Introduction

Storage, memory, and calldata. By the end of this lesson you will be able to: Declare state variables; Understand storage locations; Use memory in functions; Distinguish calldata.

## Key Concepts

### 1. Declare state variables

Target: Declare state variables. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
contract Storage {
    uint256 public storedData;  // persisted on-chain

    function set(uint256 x) public {
        storedData = x;
    }
}
```
### 2. Understand storage locations

Target: Understand storage locations. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
function f(uint[] memory arr) public pure returns (uint) {
    return arr.length;
}
```
### 3. Use memory in functions

Target: Use memory in functions. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
function g(string calldata s) external pure returns (uint) {
    return bytes(s).length;
}
```
### 4. Distinguish calldata

Target: Distinguish calldata. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
uint256 public constant MAX = 1000;
address public immutable owner;
```

## Practice Questions

1. What is the key idea behind "State Variables and Storage"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain State Variables and Storage with analogies and real-world examples"
1. "Show me common mistakes beginners make with State Variables and Storage"
1. "Provide advanced patterns and performance considerations for State Variables and Storage"

## Key Takeaways

- Master the core ideas of State Variables and Storage through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
