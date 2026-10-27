---
name: devartslab-review
description: Review changes and run pre-push security checks. Alias for devartslab-code-review; run before every git push or when the user asks for a review.
allowed-tools:
  - read
  - grep
  - glob
  - exec
---

<!-- author: Amir Olyaei | DevArts Lab | last_updated: 2026-10-16 -->

Invoke the `devartslab-code-review` skill and follow its full flow: diff
review, secret scan, dependency/Dependabot check, repo hygiene, verdict.
