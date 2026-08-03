---
{
  "title": "Errors and Require",
  "description": "require, revert, assert, and custom errors.",
  "type": "lesson",
  "order": 6,
  "duration": "45 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Validate with require",
    "Revert with custom errors",
    "Use assert for invariants",
    "Save gas with error strings"
  ],
  "knowledge_refs": [
    "solidity/solidity-06-errors"
  ],
  "prerequisites": [
    "Solidity-05: Events and Logging"
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

# SOLIDITY-06-ERRORS: Errors and Require

## Introduction

require, revert, assert, and custom errors. By the end of this lesson you will be able to: Validate with require; Revert with custom errors; Use assert for invariants; Save gas with error strings.

## Key Concepts

### 1. Validate with require

Target: Validate with require. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
function withdraw(uint amount) public {
    require(balances[msg.sender] >= amount, "insufficient balance");
    balances[msg.sender] -= amount;
}
```
### 2. Revert with custom errors

Target: Revert with custom errors. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
error InsufficientBalance(uint available, uint required);

function withdraw(uint amount) public {
    if (balances[msg.sender] < amount) {
        revert InsufficientBalance(balances[msg.sender], amount);
    }
}
```
### 3. Use assert for invariants

Target: Use assert for invariants. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
assert(totalSupply >= 0);   // internal invariant
```
### 4. Save gas with error strings

Target: Save gas with error strings. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
function safeDiv(uint a, uint b) public pure returns (uint) {
    require(b > 0, "division by zero");
    return a / b;
}
```

## Practice Questions

1. What is the key idea behind "Errors and Require"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain Errors and Require with analogies and real-world examples"
1. "Show me common mistakes beginners make with Errors and Require"
1. "Provide advanced patterns and performance considerations for Errors and Require"

## Key Takeaways

- Master the core ideas of Errors and Require through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
