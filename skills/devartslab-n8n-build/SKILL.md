---
name: devartslab-n8n-build
description: Build n8n workflows for a target org and environment
---

Run this to render the n8n development source into a deployable `build/<slug>/<env>/` directory.

## What this does

1. Resolves the active org context (via `--org`, `ORG_CONTEXT` env, or active-org file).
2. Resolves the active consultant context (via `--consultant`, `CONSULTANT_CONTEXT` env, or active-consultant file). The consultant profile merges UNDER the org profile automatically inside `loadProfile()`.
3. Builds all workflow JSON files from the editable source.
4. Layers config in order (later layers win). All `config/` paths are relative to `n8n/development/`:
   - `n8n/development/config/default.json` (tracked, org-agnostic)
   - `n8n/development/config/default.local.json` (machine-local, gitignored)
   - `<org tree>/org-profile.json` with consultant profile merged in (normalized to `organization.*`)
   - `<org tree>/n8n/default.json` (org-level values: campaigns, elections, occasions)
   - `n8n/development/config/<env>.json` (tracked env defaults)
   - `<org tree>/n8n/<env>.json` (org + env values)
   - `n8n/development/config/<env>.local.json` (machine-local env overrides, gitignored)
   - `<org tree>/n8n/n8n-secrets.json` (org secrets — highest precedence)
5. Recursively resolves `{{...}}` placeholders and applies `text_substitutions` (single-pass, longest-key-first) in Code nodes and other string fields.
6. Replaces webhook paths and `errorWorkflow` references with the configured values.
7. Writes the output to `build/<slug>/<env>/json/` and copies the org's table manifest to `build/<slug>/<env>/tables/`.

## When to run this

- After editing `n8n/development/src/workflows/`, `n8n/development/config/*.json`, or any org's `org-profile.json` / `n8n/*.json`.
- Before running `deploy.js` to import/activate on the target n8n instance.
- To verify that the current source still renders cleanly with the latest config values.

## How to run

1. **Build the n8n workflows for a specific org:**

```bash
cd "$(git rev-parse --show-toplevel)/n8n/development"
node scripts/build.js --org iaboston --env development
```

Replace `iaboston` with the target org slug and `development` with `staging` or `production` as needed.

If `--org` is omitted, the resolver tries `ORG_CONTEXT` env, then `active-org.json`, then auto-selects if only one org exists. The active consultant's profile (from `--consultant`, `CONSULTANT_CONTEXT`, or `active-consultant.json`) merges automatically into the org profile during rendering.

2. **Build for all orgs:**

```bash
node scripts/build.js --all-orgs --env development
```

3. **Update `REPO_INDEX.md`:**

Run `/update-index` to reflect any tracked source changes. Generated `build/<slug>/<env>/` files are gitignored and will not appear in the index.

4. **Update demo guide with workflow URLs:**

Run `/update-demo-guide` to update the demo guide with accurate n8n workflow URLs and deployment status after the build.

## Options

- `--org <slug>` — target organization (overrides auto-resolution)
- `--all-orgs` — build for every org in `shared/config/orgs/`
- `--env {env}` — target environment; controls which `config/<env>.json` overlay is loaded
- `--strict` — fail the build if any placeholders remain unresolved
- `--dry-run` — resolve config and report, but write nothing

## Output

- `build/<slug>/<env>/json/*.json` — rendered, org- and environment-specific workflow JSON
- `build/<slug>/<env>/tables/manifest.json` — data table schemas + seed rows for the target instance

## Verification

- Inspect `build/<slug>/<env>/json/` for any `{{unresolved}}` placeholders or obvious errors.
- Check the final `Done. N workflow(s) built...` message.
- Run `python3 scripts/org.py validate --org <slug>` to check config completeness.

## Relationship to other workflows

- `/update-index` is run as part of this workflow so `REPO_INDEX.md` stays in sync with tracked source changes.
- `build/<slug>/<env>/` is a generated directory and already gitignored, so it will not appear in `REPO_INDEX.md`.
- For a full local round-trip: edit `src/workflows/` → `build.js --org <slug> --env development` → `/update-index` → (optionally) `deploy.js --org <slug> --env development`.

## Dependencies

- Node.js 20+
- `n8n/development/config/default.json` (tracked, org-agnostic)
- `shared/config/orgs/<slug>/org-profile.json` (gitignored)
- `shared/config/orgs/<slug>/n8n/default.json` (gitignored, org-level values)
- `shared/config/orgs/<slug>/n8n/<env>.json` (gitignored, per-env org overrides)
- `src/workflows/`
