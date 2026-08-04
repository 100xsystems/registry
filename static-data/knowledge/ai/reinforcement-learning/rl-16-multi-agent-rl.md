---
slug: rl-16-multi-agent-rl
title: "Multi-Agent Reinforcement Learning"
description: "Agents interacting with each other — cooperative, competitive, and communication in multi-agent systems."
order: 16
tags:
  - reinforcement-learning
  - multi-agent
  - marl
  - self-play
  - cooperative
  - competitive
prerequisites:
  - rl-11-actor-critic
knowledge_refs:
  - rl-11-actor-critic
    title: "Actor-Critic Methods"
  - rl-17-rl-in-games
    title: "RL in Games"
  - rl-02-markov-decision-processes
    title: "Markov Decision Processes"
references:
  - title: "Multi-Agent RL Survey — Zhang et al."
    url: "https://arxiv.org/abs/1810.11735"
  - title: "MARL with Self-Play — OpenAI"
    url: "https://openai.com/research/"
  - title: "QMIX — Value Decomposition Methods"
    url: "https://arxiv.org/abs/1803.11485"
  - title: "CommNet — Learning to Communicate"
    url: "https://arxiv.org/abs/1705.10868"
  - title: "Multi-Agent Actor-Critic (MADDPG)"
    url: "https://arxiv.org/abs/1706.02275"
---

## Multi-Agent Reinforcement Learning

MARL extends RL to settings with multiple interacting agents. The environment is non-stationary from each agent's perspective because other agents are simultaneously learning and changing behavior.

### Types of Multi-Agent Settings

**Cooperative:** All agents share a common goal (team sports, multi-robot coordination). The challenge is coordinating behavior without centralized control.

**Competitive:** Agents have opposing goals (chess, poker). The challenge is modeling opponent behavior and adapting strategy.

**Mixed:** Some agents cooperate, others compete (self-driving with other cars). The most realistic and complex setting.

### Key Challenges

**Non-stationarity:** From each agent's perspective, the environment changes as other agents learn. Standard RL algorithms assume a stationary environment.

**Credit assignment:** In cooperative settings, how do you attribute team success to individual agent actions?

**Scalability:** The joint action space grows exponentially with the number of agents.

### Approaches

**Centralized training, decentralized execution (CTDE):** Train with access to all agents' information, but each agent acts independently at test time. Examples: MADDPG, QMIX.

**Self-play:** Agents train against copies of themselves, developing increasingly sophisticated strategies. Used in AlphaGo, OpenAI Five.

**Communication:** Agents learn to share information through learned communication protocols. Examples: CommNet, TarMAC.

**Value decomposition:** Factorize the joint value function into individual agent contributions. Examples: QMIX, VDN.

### Common Mistakes

- **Ignoring non-stationarity:** Standard single-agent RL fails in multi-agent settings.
- **Assuming cooperation:** In mixed settings, agents may need to model opponent behavior.
- **Scalability:** Naive approaches don't scale beyond a few agents.

---

*Continue to learn about RL in games — from board games to complex video games.*
