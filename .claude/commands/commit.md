---
name: commit
description: Create clean commits from uncommitted changes
---

Review all uncommitted changes.

Goals:
- group changes by topic
- create clean, atomic commits
- ensure logical separation

Steps:

1. Inspect git status and diffs
2. Identify change groups (by purpose):
   - feature
   - refactor
   - fix
   - docs
   - config

3. Stage and commit changes per group

Commit rules:
- one topic per commit
- small and focused commits
- do not mix unrelated changes

Commit message format:
<type>: <short description>

Examples:
- feat: add routing decision model
- refactor: simplify router logic
- fix: handle null response in gateway
- docs: update architecture docs

Constraints:
- do NOT include co-authored-by
- do NOT create a single large commit
- skip empty or irrelevant changes

Git workflow:
- stay on current branch (do NOT create new one)

Output:
- no explanations
- only git actions

Group changes based on intent, not files.