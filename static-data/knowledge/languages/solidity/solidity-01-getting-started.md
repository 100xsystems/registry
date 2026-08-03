---
{
  "title": "Getting Started with Solidity",
  "description": "Remix IDE, contracts, and first deploy.",
  "type": "lesson",
  "order": 1,
  "duration": "45 min",
  "difficulty": "beginner",
  "learning_objectives": [
    "Understand what smart contracts are",
    "Use Remix IDE",
    "Write a first contract",
    "Compile and deploy to a testnet"
  ],
  "knowledge_refs": [
    "solidity/solidity-01-getting-started"
  ],
  "prerequisites": [
    "None — this is the entry point"
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

# SOLIDITY-01-GETTING-STARTED: Getting Started with Solidity

## Introduction

Remix IDE, contracts, and first deploy. By the end of this lesson you will be able to: Understand what smart contracts are; Use Remix IDE; Write a first contract; Compile and deploy to a testnet.

## Key Concepts

### 1. Understand what smart contracts are

Target: Understand what smart contracts are. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Hello {
    string public greeting = "Hello, World!";
}
```
### 2. Use Remix IDE

Target: Use Remix IDE. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Counter {
    uint256 public count;

    function increment() public {
        count += 1;
    }
}
```
### 3. Write a first contract

Target: Write a first contract. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Owner {
    address public owner;

    constructor() {
        owner = msg.sender;
    }
}
```
### 4. Compile and deploy to a testnet

Target: Compile and deploy to a testnet. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Greeting {
    string private message = "hi";

    function setMessage(string calldata m) public {
        message = m;
    }

    function getMessage() public view returns (string memory) {
        return message;
    }
}
```

## Practice Questions

1. What is the key idea behind "Getting Started with Solidity"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Getting Started with Solidity with analogies and real-world examples"
1. "Show me common mistakes beginners make with Getting Started with Solidity"
1. "Provide advanced patterns and performance considerations for Getting Started with Solidity"

## Key Takeaways

- Master the core ideas of Getting Started with Solidity through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
