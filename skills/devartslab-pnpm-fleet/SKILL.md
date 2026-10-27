---
name: devartslab-pnpm-fleet
description: Enforce DevArts Lab pnpm fleet policy across repos via tool-pnpm-fleet. Use when migrating a repo to pnpm, auditing pnpm compliance or vulnerabilities, bumping the pinned pnpm version fleet-wide, managing exceptions, or questions about the lab's package-manager governance rules.
---

<!-- author: Amir Olyaei | DevArts Lab | last_updated: 2026-10-26 -->

# pnpm fleet policy

Tool: `~/projects/devartslab/tool-pnpm-fleet` (repo: DevArtsLab/tool-pnpm-fleet).
CLI: `bin/pnpm-fleet`. Config: `fleet.conf` (pinned version), `exceptions.list`, `policy/npmrc`.

## Enforced

- One pnpm version fleet-wide: `packageManager` pin + `manage-package-manager-versions`.
- Single dep version per repo: `pnpm dedupe --check`; force via `pnpm.overrides` if needed.
- No `package-lock.json`/`yarn.lock`; `minimum-release-age=1440`; `engine-strict`.
- `pnpm audit --audit-level=high` on routine runs and CI gate (`ci/pnpm-gate.yml`).

## Commands

```bash
bin/pnpm-fleet check [DIR]  # fleet audit, exit 1 on violations (default: siblings)
bin/pnpm-fleet apply REPO   # .npmrc + packageManager pin into one repo
bin/pnpm-fleet pin VERSION  # re-pin every repo + fleet.conf
bin/pnpm-fleet audit [DIR]  # vulnerability sweep
bin/pnpm-fleet dupes REPO   # duplicate-version check
```

## Adopt npm repo

```bash
bin/pnpm-fleet apply <repo>
cd <repo> && pnpm import && rm package-lock.json && rm -rf node_modules && pnpm install
```

## Rules

- Cross-repo version uniformity is a drift report, not enforcement; never
  force-bump a deployed repo because another repo upgraded.
- Majors merge only after green build; no blind automerge.
- Edge cases go in `exceptions.list` (dir name or relative path + reason),
  never ad-hoc. Re-review quarterly.
- Security releases: `pin` immediately. Routine pnpm bumps: on minor releases.
