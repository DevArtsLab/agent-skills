---
name: devartslab-linear-research-refine
description: "Run one bounded refinement pass on a living Linear research ticket. Use for tickets structured with findings, open questions, a decision log, and a refinement protocol (e.g., DEV-47). Verify decaying claims against current sources, update findings in place, and log resolved decisions with evidence."
compatibility: "Requires linear-mcp-server (get_issue, save_issue, save_comment) plus web_search and webfetch for source verification."
license: MIT
---

<!-- author: Amir Olyaei | DevArts Lab | last_updated: 2026-10-04 -->

# Linear Research Refinement

Runs a single daily-quality research pass against a living Linear research ticket. Default target: **DEV-47** (productize job tracker as multi-tenant SaaS on Cloudflare, DevArts Lab workspace). Pass a different issue identifier to reuse for another ticket.

## Pass protocol

1. **Fetch the ticket** via linear-mcp-server (`get_issue` or `list_issues` by identifier). Read the full description and all comments first.

2. **Choose one focus area**: the highest-priority open question with low confidence, or the oldest unverified claim in the findings. Go deep on one area rather than touching everything.

3. **Research with authoritative sources only**: official docs, changelogs, vendor pricing pages, upstream repos/issues. Use `web_search` + `webfetch`. Record each source URL and date checked.

4. **Update the ticket in place** (`save_issue` patch):
   - Mark verified claims with `[verified YYYY-MM-DD: source]`
   - Correct stale or wrong claims
   - Move answered questions into the Decision Log with: date, decision, evidence, confidence, and what would change the decision
   - Add new open questions discovered (why it matters + priority)
   - Update phasing/plans if evidence warrants it

5. **One comment per pass** (`save_comment`): focus area, what changed, what to look at next. Flag product-judgment calls (pricing, scope, privacy trade-offs) for the user instead of deciding them.

6. **Stay bounded**: a focused increment. Daily passes compound.

## Rules

- Research and ticket updates only. Do not modify code or repos.
- Never invent sources or capabilities. Mark unverifiable claims as unverified with the missing evidence.
- Preserve the ticket's structure; edit in place, never rewrite wholesale.
- If every question is resolved: re-verify the oldest verified claims (they decay) or deepen the implementation plan.
- The workspace repo may be read for context but not edited.

## Scheduling

Scheduled copies are generated per-project by the agent-research-kit (`~/projects/devartslab/agent-research-kit/install.sh`), which renders `templates/prompt.md.tmpl` with each project's issue ID. This file is the interactive reference; the kit's prompt template is the scheduled master.
