---
title: "Sidecar: A Helper Next to Your App"
order: 1
difficulty: "Beginner"
duration: "45 min"
learning_objectives:
  - "Explain the sidecar model"
  - "Co-locate without coupling"
  - "Describe the communication"
  - "Know the deployment"
prerequisites:
  - "patterns/ambassador"
  - "patterns/proxy"
knowledge_refs:
  - "patterns/sidecar"
---

# Sidecar: A Helper Next to Your App

## The Model

A sidecar is a separate process deployed alongside the main app — same host, same lifecycle — that provides a supporting capability: logging, proxying, config reload, TLS. The app talks to the sidecar over localhost; the sidecar talks to the world. The main app stays small and language-agnostic.

```yaml
# Kubernetes pod: app + sidecar sharing a volume and localhost
apiVersion: v1
kind: Pod
metadata:
  name: web-app
spec:
  containers:
    - name: app
      image: web-app:1.2
      volumeMounts:
        - name: logs
          mountPath: /var/log/app
    - name: log-shipper      # sidecar: supporting capability
      image: log-shipper:2.1
      volumeMounts:
        - name: logs
          mountPath: /var/log/app   # reads the app's logs
      args: ["tail", "/var/log/app/*.log"]
  volumes:
    - name: logs
      emptyDir: {}
# The app does not know the sidecar exists; the sidecar does
# not change the app's code.
```

## Why a Process

A separate process isolates failures, languages, and versions: the sidecar can crash and restart without touching the app, can be written in any language, and upgrades independently. The cost: another process to deploy and monitor, and the localhost hop adds a little latency.

## Practice: Add the Log Sidecar

A Python app writes logs; the team wants shipping, rotation, and buffering without changing the app.

**Task 1:** Design the sidecar that reads, rotates, and ships the logs.

**Task 2:** Define the localhost contract and the shared volume.

**Task 3:** Test: the sidecar crashes and restarts; the app is unaffected.

## Guided LLM Prompts

**Prompt 1 — Socratic Tutor:**
> Ask me one question at a time about why co-location without code coupling is the sidecar win. Start with the language barrier.

**Prompt 2 — Compare & Contrast:**
> Compare sidecar with ambassador, proxy, and an in-process library. When does a process win over a library?

**Prompt 3 — Boundary Testing:**
> The sidecar dies and the app must keep serving. Design the degraded mode and the alert.

## Key Takeaways

- Sidecars co-locate supporting logic without coupling
- They isolate failures, languages, and versions
- Communication is localhost + shared volumes
- Another process means another thing to monitor

## Further Reading

- [Sidecar pattern — Microsoft](https://learn.microsoft.com/en-us/azure/architecture/patterns/sidecar)
- [Kubernetes — multi-container pods](https://kubernetes.io/docs/concepts/workloads/pods/)
