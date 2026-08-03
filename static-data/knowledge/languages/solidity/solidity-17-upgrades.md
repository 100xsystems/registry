---
{
  "title": "Upgradeable Contracts",
  "description": "Proxy patterns and upgradeability.",
  "type": "lesson",
  "order": 17,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand proxy pattern",
    "Use delegatecall",
    "Deploy with OpenZeppelin",
    "Manage storage layouts"
  ],
  "knowledge_refs": [
    "solidity/solidity-17-upgrades"
  ],
  "prerequisites": [
    "Solidity-16: Libraries and Interfaces"
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

# SOLIDITY-17-UPGRADES: Upgradeable Contracts

## Introduction

Proxy patterns and upgradeability. By the end of this lesson you will be able to: Understand proxy pattern; Use delegatecall; Deploy with OpenZeppelin; Manage storage layouts.

## Key Concepts

### 1. Understand proxy pattern

Target: Understand proxy pattern. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
// Proxy forwards all calls to an implementation
contract Proxy {
    address public implementation;

    fallback() external payable {
        (bool ok, ) = implementation.delegatecall(msg.data);
        require(ok);
    }
}
```
### 2. Use delegatecall

Target: Use delegatecall. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
contract Logic {
    uint256 public value;
    function setValue(uint256 v) public {
        value = v;
    }
}
```
### 3. Deploy with OpenZeppelin

Target: Deploy with OpenZeppelin. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
function upgrade(address newImpl) public onlyOwner {
    implementation = newImpl;
}
```
### 4. Manage storage layouts

Target: Manage storage layouts. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
// Warning: preserve storage layout across upgrades
```

## Practice Questions

1. What is the key idea behind "Upgradeable Contracts"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Upgradeable Contracts with analogies and real-world examples"
1. "Show me common mistakes beginners make with Upgradeable Contracts"
1. "Provide advanced patterns and performance considerations for Upgradeable Contracts"

## Key Takeaways

- Master the core ideas of Upgradeable Contracts through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
