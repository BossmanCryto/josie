---
name: token_compression
description: Protocols and techniques for extreme token efficiency, context pruning, and zero-waste agent execution on Android/Termux.
---

# Token Compression & Zero-Waste Protocol

## Objective
Maximize reasoning output while cutting input token burn by 70%+. Protect cloud quota and maintain high execution velocity on mobile.

## Key Rules
1. **Direct Payload Framing**: Strip boilerplate greetings, preamble, and meta-commentary ("I will now do X", "Here is your solution:").
2. **Context Window Pruning**: When passing past conversation history to subagents or local models, summarize and distill state rather than forwarding raw JSON transcripts.
3. **Local Filter First**: Use local offline models (`smollm2:135m`, `qwen2.5:0.5b`) for syntax checks, classification, formatting, or filtering before routing complex logic to cloud Gemini models.
4. **Targeted Diffs**: Utilize precision line replacement tools instead of rewriting entire multikilobyte source files.
5. **Silent Subagent Execution**: Subagents must return dense, structured status payloads without conversational padding.
