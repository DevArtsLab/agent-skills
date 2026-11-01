---
name: devartslab-forensic-report
description: "Produce a forensic verification report: check claims against primary sources (git state, APIs, CLIs, configs, deployed URLs) and emit a telegraphic verdict with evidence refs. Use whenever the user asks to verify, audit, or confirm that work actually shipped; before writing Linear Outcome/Impact/Evidence blocks or completion comments; before recording facts in persistent docs; when stale claims need re-verification; or any time documented state must be checked against real state."
license: MIT
---

<!-- author: Amir Olyaei | DevArts Lab | created: 2026-10-31 | last_updated: 2026-10-31 -->

# Forensic Report

Verify claims against primary sources. Emit telegraphic verdict with evidence refs. Chat assertions, session memory, and prior docs are leads, not proof.

## Protocol

1. **Extract claims**: pull the specific assertions under test from the scope (issue description, doc, chat claim, commit message, deploy note). Each claim gets an ID: C1, C2, ...

2. **Pick the source of truth per claim**:
   - Code shipped | `git log`, `git diff`, branch state vs remote
   - Commit exists | `git log --oneline`, `git show <sha>`
   - Deployed | live URL fetch, `wrangler deployments list`, platform CLI
   - Config applied | read the config file or API object, not the doc describing it
   - Linear state | MCP `get_issue`, never session recall
   - Numbers (tests, endpoints, records) | rerun the count command, do not copy prior figures

3. **Verify each claim**: run the check. Record tool, command, and result. Classify:
   - `verified` | primary source confirms
   - `contradicted` | primary source disproves; record actual state
   - `unverifiable` | source unreachable or claim untestable; name the missing evidence

4. **Report telegraphic**: verdict first, evidence after. Every line cites a ref (SHA, URL, file:line, command output). No commentary, no hedging.

## Output format

```
## Forensic report: <scope> | <date>

VERDICT: <pass | partial | fail> | <n>/<m> claims verified

| ID | Claim | Status | Evidence |
| C1 | <claim, compressed> | verified | <sha / url / file:line> |
| C2 | <claim> | contradicted | actual: <real state> |
| C3 | <claim> | unverifiable | missing: <what would prove it> |

## Stale / drift
<facts that verified once but decayed: age, last verified date, rescan needed>

## Actions
<only if user asked for remediation: minimal fixes, each tied to a failed claim>
```

Compress claims to the shortest form that keeps the assertion testable. Skip table rows that carry no information (e.g. restating the claim in the evidence column).

## Rules

- Verify before writing. Never mark Linear done, post completion comments, or record facts in persistent docs from session work alone; a local commit counts, staged-only does not.
- Contradicted beats unverifiable: if the check fails, report the real state found, not just "could not confirm".
- Numbers only in Impact-style lines: counts, SHAs, URLs. No adjectives.
- Scope reads, no writes: this skill produces a report; it does not fix findings unless the user asked.
- Distinguish verified state from decisions and plans. Label anything not applied: `planned`, `proposed`.
- ASCII punctuation only. No em dashes.

## Triggers

- "verify", "audit", "did it actually ship", "forensic", "confirm it's live"
- Before appending `## Outcome / ## Impact / ## Evidence` to a Linear issue
- Before flagging or quoting stale MARKET-SIGNALS.md facts as current
- Post-sync checks: rendered doc vs source template
- Fleet audits: pnpm compliance, skill symlink integrity, automation drift
