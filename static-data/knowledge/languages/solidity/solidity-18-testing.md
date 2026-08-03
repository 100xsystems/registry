---
{
  "title": "Testing Smart Contracts",
  "description": "Write tests with Foundry and Hardhat.",
  "type": "lesson",
  "order": 18,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Write Foundry tests",
    "Use test modifiers",
    "Test with cheats",
    "Measure coverage"
  ],
  "knowledge_refs": [
    "solidity/solidity-18-testing"
  ],
  "prerequisites": [
    "Solidity-17: Upgradeable Contracts"
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

# SOLIDITY-18-TESTING: Testing Smart Contracts

## Introduction

Write tests with Foundry and Hardhat. By the end of this lesson you will be able to: Write Foundry tests; Use test modifiers; Test with cheats; Measure coverage.

## Key Concepts

### 1. Write Foundry tests

Target: Write Foundry tests. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {Test} from "forge-std/Test.sol";

contract CounterTest is Test {
    function testIncrement() public {
        // arrange, act, assert
    }
}
```
### 2. Use test modifiers

Target: Use test modifiers. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
function testCounter() public {
    Counter c = new Counter();
    c.increment();
    assertEq(c.count(), 1);
}
```
### 3. Test with cheats

Target: Test with cheats. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
function testFuzz(uint256 n) public {
    vm.assume(n < 100);
    assertTrue(n > 0 || n < 100);
}
```
### 4. Measure coverage

Target: Measure coverage. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
function testRevert() public {
    vm.expectRevert("insufficient");
    c.withdraw(1 ether);
}
```

## Practice Questions

1. What is the key idea behind "Testing Smart Contracts"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Testing Smart Contracts with analogies and real-world examples"
1. "Show me common mistakes beginners make with Testing Smart Contracts"
1. "Provide advanced patterns and performance considerations for Testing Smart Contracts"

## Key Takeaways

- Master the core ideas of Testing Smart Contracts through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
