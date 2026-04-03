---
name: architecture
description: Audit and improve system architecture
---

Review the current system architecture.

Goals:
- ensure clear separation of concerns
- validate layer boundaries:
  API → services → router → gateway → models
- detect missing abstractions or contracts
- identify scalability issues

Then:

1. Propose improvements to architecture
2. Define or refine core contracts (if missing):
   - LLMRequest
   - LLMResponse
   - RoutingDecision
3. Ensure router is isolated and replaceable
4. Ensure gateway is the only LLM entry point
5. Ensure observability is applied across all layers

Rules:
- be concise
- avoid overengineering
- prefer simple and modular design

Git workflow:
- create branch: architecture/improvements
- commit per change
- no co-authored-by

Output:
- only code and file changes
- no explanations