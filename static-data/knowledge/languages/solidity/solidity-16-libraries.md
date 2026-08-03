---
{
  "title": "Libraries and Interfaces",
  "description": "Reusable library code and contract interfaces.",
  "type": "lesson",
  "order": 16,
  "duration": "45 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write libraries",
    "Use library functions",
    "Define interfaces",
    "Interact with external contracts"
  ],
  "knowledge_refs": [
    "solidity/solidity-16-libraries"
  ],
  "prerequisites": [
    "Solidity-15: Gas Optimization"
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

# SOLIDITY-16-LIBRARIES: Libraries and Interfaces

## Introduction

Reusable library code and contract interfaces. By the end of this lesson you will be able to: Write libraries; Use library functions; Define interfaces; Interact with external contracts.

## Key Concepts

### 1. Write libraries

Target: Write libraries. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
library Math {
    function sqrt(uint256 x) internal pure returns (uint256) {
        return x ** 0.5;
    }
}
```
### 2. Use library functions

Target: Use library functions. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
library SafeMath {
    function add(uint a, uint b) internal pure returns (uint) {
        require(a + b >= a, "overflow");
        return a + b;
    }
}
```
### 3. Define interfaces

Target: Define interfaces. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
}
```
### 4. Interact with external contracts

Target: Interact with external contracts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
function payWithToken(IERC20 token, address to, uint256 amount) public {
    token.transfer(to, amount);
}
```

## Practice Questions

1. What is the key idea behind "Libraries and Interfaces"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Libraries and Interfaces with analogies and real-world examples"
1. "Show me common mistakes beginners make with Libraries and Interfaces"
1. "Provide advanced patterns and performance considerations for Libraries and Interfaces"

## Key Takeaways

- Master the core ideas of Libraries and Interfaces through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
