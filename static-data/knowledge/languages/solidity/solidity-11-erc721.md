---
{
  "title": "ERC-721 NFTs",
  "description": "Non-fungible tokens and ownership.",
  "type": "lesson",
  "order": 11,
  "duration": "60 min",
  "difficulty": "intermediate",
  "learning_objectives": [
    "Understand NFT uniqueness",
    "Implement minting",
    "Transfer ownership",
    "Handle metadata"
  ],
  "knowledge_refs": [
    "solidity/solidity-11-erc721"
  ],
  "prerequisites": [
    "Solidity-10: ERC-20 Token Standard"
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

# SOLIDITY-11-ERC721: ERC-721 NFTs

## Introduction

Non-fungible tokens and ownership. By the end of this lesson you will be able to: Understand NFT uniqueness; Implement minting; Transfer ownership; Handle metadata.

## Key Concepts

### 1. Understand NFT uniqueness

Target: Understand NFT uniqueness. Start with the foundations — read the runnable example carefully and trace its output before moving on.

```solidity
contract MyNFT {
    mapping(uint256 => address) public ownerOf;
    mapping(address => uint256) public balanceOf;
    uint256 public nextTokenId;
}
```
### 2. Implement minting

Target: Implement minting. Apply the idiomatic pattern — this is how production code expresses this idea, so study the shape of the code.

```solidity
function mint(address to) public returns (uint256) {
    uint256 id = nextTokenId++;
    ownerOf[id] = to;
    balanceOf[to] += 1;
    return id;
}
```
### 3. Transfer ownership

Target: Transfer ownership. Watch for the edge cases — this is where subtle bugs hide, and experienced developers reason about them explicitly.

```solidity
function transfer(address from, address to, uint256 id) public {
    require(ownerOf[id] == msg.sender, "not owner");
    ownerOf[id] = to;
    balanceOf[from] -= 1;
    balanceOf[to] += 1;
}
```
### 4. Handle metadata

Target: Handle metadata. Put it together — extend the example to combine this concept with what you learned in earlier lessons.

```solidity
string public baseURI = "https://api.example.com/nft/";

function tokenURI(uint256 id) public view returns (string memory) {
    return string(abi.encodePacked(baseURI, id));
}
```

## Practice Questions

1. What is the key idea behind "ERC-721 NFTs"?
1. Write a small program that exercises at least two concepts from this lesson.
1. How would you explain this topic to a fellow developer in one paragraph?

## LLM Prompts for Deeper Understanding

1. "Explain ERC-721 NFTs with analogies and real-world examples"
1. "Show me common mistakes beginners make with ERC-721 NFTs"
1. "Provide advanced patterns and performance considerations for ERC-721 NFTs"

## Key Takeaways

- Master the core ideas of ERC-721 NFTs through practice
- Combine this lesson with prior lessons to build real programs
- Explore the linked official documentation for authoritative depth

## Further Reading

Dive deeper into this topic using the reference resources listed in the frontmatter.
