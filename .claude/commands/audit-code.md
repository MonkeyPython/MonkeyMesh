---
name: audit-code
description: Perform code quality and structure audit
---

Review the entire codebase.

Goals:
- detect bad practices
- find duplicated or unnecessary code
- identify missing typing
- detect violations of project rules

Check:

1. Architecture violations:
   - direct LLM calls
   - logic inside endpoints
   - missing routing layer

2. Code quality:
   - large functions
   - unclear naming
   - missing type hints

3. Consistency:
   - naming conventions
   - folder structure
   - imports

4. Observability:
   - missing traces
   - missing metadata

Then:

- refactor code where needed
- remove dead or redundant code
- improve clarity

Rules:
- keep behavior unchanged
- prefer small, safe changes
- be concise

Git workflow:
- create branch: code/audit
- commit per topic
- no co-authored-by

Output:
- only code changes
- no explanations