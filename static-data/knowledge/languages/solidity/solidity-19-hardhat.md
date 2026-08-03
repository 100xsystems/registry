---
{
  "title": "Hardhat Development Workflow",
  "description": "Deploy, verify, and interact from scripts.",
  "type": "lesson",
  "order": 19,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Set up a Hardhat project",
    "Write deploy scripts",
    "Verify contracts",
    "Interact via console"
  ],
  "knowledge_refs": [
    "solidity/solidity-19-hardhat"
  ],
  "prerequisites": [
    "Solidity-18: Testing Smart Contracts"
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

# SOLIDITY-19-HARDHAT: Hardhat Development Workflow

## Introduction

Deploy, verify, and interact from scripts. By the end of this lesson you will be able to: Set up a Hardhat project; Write deploy scripts; Verify contracts; Interact via console.

## Key Concepts

### 1. Set up a Hardhat project

Target: Set up a Hardhat project. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
npx hardhat init
npx hardhat compile
```
### 2. Write deploy scripts

Target: Write deploy scripts. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
const { ethers } = require("hardhat");
async function main() {
  const Token = await ethers.getContractFactory("MyToken");
  const token = await Token.deploy();
  await token.waitForDeployment();
  console.log("Deployed:", await token.getAddress());
}
```
### 3. Verify contracts

Target: Verify contracts. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
npx hardhat run scripts/deploy.js --network sepolia
```
### 4. Interact via console

Target: Interact via console. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
npx hardhat verify --network sepolia DEPLOYED_ADDRESS
```

## Practice Questions

1. What is the key idea behind "Hardhat Development Workflow"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Hardhat Development Workflow with analogies and real-world examples"
1. "Show me common mistakes beginners make with Hardhat Development Workflow"
1. "Provide advanced patterns and performance considerations for Hardhat Development Workflow"

## Key Takeaways

- Master the core ideas of Hardhat Development Workflow through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
