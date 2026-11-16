---
name: devartslab-session-closeout
description: "End-of-session checklist: run lab-check drift scan, then walk the judgment items (published-URL verification, session-context containment, pushed-vs-committed honesty, Linear evidence, index registration) before declaring work done. Use at the end of any session that touched repos, remotes, deployed services, or durable docs; before merging index or config branches; before publishing docs."
license: MIT
---

<!-- author: Amir Olyaei | DevArts Lab | created: 2026-11-16 | last_updated: 2026-11-16 -->

# Session Closeout

Two layers: mechanical drift detection, then judgment checks. Do not declare work done until both pass or every failure is surfaced to the user.

## 1. Mechanical: lab-check

From workspace root:

```
scripts/lab lab-check
```

Read-only scan: git state per repo (dirty, unpushed, no upstream), LAB_INDEX vs live GitHub org, skills-lock freshness vs `agent-skills` source, stray provider skill dirs (`./.claude/skills`, `./.devin/skills`), registered domain reachability. Exit 1 on any FAIL.

Each FAIL: fix it, or report it to the user as known drift with the cause. Sections run independently: `scripts/lab lab-check skills` scans only that section.

## 2. Judgment checklist

Items the script cannot decide. Walk each; every violation found gets fixed or reported.

- **Published URLs verified live**: every URL written into a durable doc this session was fetched (curl, gh api) before or immediately after writing. Unverifiable URL -> replace with path reference or drop it. Never ship a link checked only from session output.
- **Session-context containment**: durable docs contain no session framing, conversational phrasing, or process narration (who decided what, when, why the discussion happened). Scan new/edited docs for chat-shaped content: audience invitations, "as discussed", meta-sections about the writing process itself. Repo docs describe the instance; generic patterns live in foundation; nothing else.
- **State honesty**: records distinguish committed from pushed from remotely visible. Nothing documented as shipped while it is local-only. Unpushed commits and unmerged branches named as such in any status claim.
- **Linear evidence**: issues touched this session carry current status; completed work has `## Outcome`, `## Impact` (numbers only), `## Evidence` (commit SHAs, URLs that resolve). Comments posted for user-visible changes.
- **Index registration**: new or renamed repos/dirs have a LAB_INDEX row, updated counts, and a Domains entry when a hostname exists. New foundation docs registered in `INDEX.md`.
- **Skill changes**: skills edited in `agent-skills/skills/` only; installed copies refreshed via `npx skills add ./agent-skills -s <name> -a universal -y`; `skills-lock.json` regenerated and committed with the change.

## Output

```
## Closeout

lab-check: <n> FAIL(s) -> <fixed | carried: list>
Judgment: <n> findings -> <fixed | carried: list>
Pending user action: <exact commands or decisions needed, or "none">
```

Carried items are reported, not hidden. A closeout with unresolved FAILs ends in a report, not a declaration of done.

## Triggers

- End of session with repo, remote, deploy, or doc changes
- Before merging index/config branches (LAB_INDEX, .workspace.json, skills-lock)
- Before pushing docs that add URLs to public repos
