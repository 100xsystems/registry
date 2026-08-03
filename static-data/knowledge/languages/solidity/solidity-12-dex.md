---
{
  "title": "DeFi and DEX Patterns",
  "description": "Liquidity pools and swap mechanics.",
  "type": "lesson",
  "order": 12,
  "duration": "60 min",
  "difficulty": "advanced",
  "learning_objectives": [
    "Understand automated market makers",
    "Implement a liquidity pool",
    "Compute swap amounts",
    "Handle fees"
  ],
  "knowledge_refs": [
    "solidity/solidity-12-dex"
  ],
  "prerequisites": [
    "Solidity-11: ERC-721 NFTs"
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

# SOLIDITY-12-DEX: DeFi and DEX Patterns

## Introduction

Liquidity pools and swap mechanics. By the end of this lesson you will be able to: Understand automated market makers; Implement a liquidity pool; Compute swap amounts; Handle fees.

## Key Concepts

### 1. Understand automated market makers

Target: Understand automated market makers. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
contract Pool {
    uint256 public reserveA;
    uint256 public reserveB;

    function addLiquidity(uint a, uint b) public {
        reserveA += a;
        reserveB += b;
    }
}
```
### 2. Implement a liquidity pool

Target: Implement a liquidity pool. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
function swapAtoB(uint amountA) public returns (uint) {
    uint amountB = (reserveB * amountA) / (reserveA + amountA);
    reserveA += amountA;
    reserveB -= amountB;
    return amountB;
}
```
### 3. Compute swap amounts

Target: Compute swap amounts. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
uint256 public constant FEE = 997;  // 0.3%

function swapWithFee(uint amountIn) public view returns (uint) {
    uint amountInWithFee = amountIn * FEE;
    return (amountInWithFee) / (reserveA * 1000 + amountInWithFee) * reserveB;
}
```
### 4. Handle fees

Target: Handle fees. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
function getAmountOut(uint amountIn, uint reserveIn, uint reserveOut) public pure returns (uint) {
    uint amountInWithFee = amountIn * 997;
    uint numerator = amountInWithFee * reserveOut;
    uint denominator = reserveIn * 1000 + amountInWithFee;
    return numerator / denominator;
}
```

## Practice Questions

1. What is the key idea behind "DeFi and DEX Patterns"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain DeFi and DEX Patterns with analogies and real-world examples"
1. "Show me common mistakes beginners make with DeFi and DEX Patterns"
1. "Provide advanced patterns and performance considerations for DeFi and DEX Patterns"

## Key Takeaways

- Master the core ideas of DeFi and DEX Patterns through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
