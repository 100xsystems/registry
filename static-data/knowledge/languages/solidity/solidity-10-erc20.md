---
{
  "title": "ERC-20 Token Standard",
  "description": "Build a standard fungible token.",
  "type": "lesson",
  "order": 10,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Implement totalSupply and balances",
    "Implement transfer and approve",
    "Implement transferFrom",
    "Deploy a real token"
  ],
  "knowledge_refs": [
    "solidity/solidity-10-erc20"
  ],
  "prerequisites": [
    "Solidity-09: Ether and Payable Functions"
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

# SOLIDITY-10-ERC20: ERC-20 Token Standard

## Introduction

Build a standard fungible token. By the end of this lesson you will be able to: Implement totalSupply and balances; Implement transfer and approve; Implement transferFrom; Deploy a real token.

## Key Concepts

### 1. Implement totalSupply and balances

Target: Implement totalSupply and balances. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
contract MyToken {
    string public name = "MyToken";
    string public symbol = "MTK";
    uint8 public decimals = 18;
    uint256 public totalSupply;
    mapping(address => uint256) public balanceOf;
}
```
### 2. Implement transfer and approve

Target: Implement transfer and approve. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
function transfer(address to, uint256 value) public returns (bool) {
    require(balanceOf[msg.sender] >= value, "insufficient");
    balanceOf[msg.sender] -= value;
    balanceOf[to] += value;
    return true;
}
```
### 3. Implement transferFrom

Target: Implement transferFrom. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
mapping(address => mapping(address => uint256)) public allowance;

function approve(address spender, uint256 value) public returns (bool) {
    allowance[msg.sender][spender] = value;
    return true;
}
```
### 4. Deploy a real token

Target: Deploy a real token. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
function transferFrom(address from, address to, uint256 value) public returns (bool) {
    require(allowance[from][msg.sender] >= value, "not allowed");
    allowance[from][msg.sender] -= value;
    balanceOf[from] -= value;
    balanceOf[to] += value;
    return true;
}
```

## Practice Questions

1. What is the key idea behind "ERC-20 Token Standard"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain ERC-20 Token Standard with analogies and real-world examples"
1. "Show me common mistakes beginners make with ERC-20 Token Standard"
1. "Provide advanced patterns and performance considerations for ERC-20 Token Standard"

## Key Takeaways

- Master the core ideas of ERC-20 Token Standard through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
