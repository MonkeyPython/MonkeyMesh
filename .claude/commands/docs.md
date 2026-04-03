---
name: docs
description: Audit and organize documentation
---

Review all project documentation.

Goals:
- remove outdated or redundant content
- add missing essential documentation
- improve clarity and consistency
- keep everything concise

Then:

1. Create /docs directory if it does not exist
2. Organize documentation into topics:
   - architecture.md
   - backend.md
   - routing.md
   - observability.md
   - setup.md

3. Move or rewrite existing content into these files
4. Ensure no duplicated information across files

Rules:
- be concise
- avoid unnecessary text
- prefer bullet points over paragraphs
- keep each file focused on one topic

Git workflow:
- create a new branch: docs/restructure
- commit per file/topic
- no co-authored-by

Output:
- no explanations
- only file changess

If documentation is unclear or missing, infer best practices based on the project architecture.