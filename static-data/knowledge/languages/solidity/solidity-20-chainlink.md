---
{
  "title": "Oracles and Real-World Data",
  "description": "Bring off-chain data on-chain.",
  "type": "lesson",
  "order": 20,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand oracle problem",
    "Use Chainlink price feeds",
    "Get randomness with VRF",
    "Call external APIs"
  ],
  "knowledge_refs": [
    "solidity/solidity-20-chainlink"
  ],
  "prerequisites": [
    "Solidity-19: Hardhat Development Workflow"
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

# SOLIDITY-20-CHAINLINK: Oracles and Real-World Data

## Introduction

Bring off-chain data on-chain. By the end of this lesson you will be able to: Understand oracle problem; Use Chainlink price feeds; Get randomness with VRF; Call external APIs.

## Key Concepts

### 1. Understand oracle problem

Target: Understand oracle problem. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
import {AggregatorV3Interface} from "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract PriceFeed {
    AggregatorV3Interface internal feed;
    constructor() {
        feed = AggregatorV3Interface(0x694AA1769357215DE4FAC081bf1f309aDC325306);
    }
}
```
### 2. Use Chainlink price feeds

Target: Use Chainlink price feeds. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
function latestPrice() public view returns (int256) {
    (, int256 price, , , ) = feed.latestRoundData();
    return price;
}
```
### 3. Get randomness with VRF

Target: Get randomness with VRF. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
function requestRandom() public returns (uint256 requestId) {
    requestId = vrfCoordinator.requestRandomWords(
        keyHash, s_subscriptionId, 3, 1, 1
    );
}
```
### 4. Call external APIs

Target: Call external APIs. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
require(timestamp > lastUpdate + interval, "too soon");
lastUpdate = timestamp;
```

## Practice Questions

1. What is the key idea behind "Oracles and Real-World Data"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Oracles and Real-World Data with analogies and real-world examples"
1. "Show me common mistakes beginners make with Oracles and Real-World Data"
1. "Provide advanced patterns and performance considerations for Oracles and Real-World Data"

## Key Takeaways

- Master the core ideas of Oracles and Real-World Data through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
