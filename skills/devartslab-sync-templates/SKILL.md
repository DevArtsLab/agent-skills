---
name: devartslab-sync-templates
description: Sync template rendering - render org-specific docs from templates
---

Run this whenever an org's `org-profile.json` changes or when template files in `shared/*.md` are updated. This workflow renders the templated markdown files into org-specific documents in `dist/<slug>/`.

## What this does

1. Resolves the active org context (via `--org`, `ORG_CONTEXT` env, or active-org file).
2. Resolves the active consultant context (via `--consultant`, `CONSULTANT_CONTEXT` env, or active-consultant file). The consultant profile merges UNDER the org profile, providing `consultant.*`, `repository.url`, and `figma.plan_key` values.
3. Checks that `shared/config/orgs/<slug>/org-profile.json` exists (gitignored, contains real org data).
4. Runs `scripts/render_templates.py` to replace `{{TOKEN}}` placeholders with real values from the merged profile.
5. Outputs rendered files to `dist/<slug>/` (gitignored, production copy for this org).
6. Reports any unresolved tokens that need to be added to the org or consultant profile.

## When to run this

- After updating `shared/config/orgs/<slug>/org-profile.json` with new org data
- After adding new `{{TOKEN}}` placeholders to template files
- After modifying any template in `shared/*.md`
- Before delivering org-specific documents to a partner

## How to run

```bash
cd "$(git rev-parse --show-toplevel)"
python3 scripts/render_templates.py --org iaboston
```

Replace `iaboston` with the target org slug. If `--org` is omitted, the resolver tries `ORG_CONTEXT` env, then `active-org.json`, then auto-selects if only one org exists. The active consultant's profile merges automatically into the org profile during rendering.

To render for all orgs:

```bash
python3 scripts/render_templates.py --all-orgs
```

## Options

- `--org <slug>` — target organization (overrides auto-resolution)
- `--all-orgs` — render for every org in `shared/config/orgs/`
- `--out /path` — custom output directory (default: `dist/<slug>/`)
- `--check` — validate tokens without writing files (useful for pre-commit checks)

## What gets rendered

All `shared/*.md` files except:

- `ngo-ux-research-documentation.md` (hand-filled skeleton, skipped by renderer)

## Output

- Rendered files appear in `dist/<slug>/` with `{{TOKEN}}` replaced by real values
- Unresolved tokens are reported to stderr
- The `dist/<slug>/` directory is gitignored — never commit rendered files with real PII

## Dependencies

- `shared/config/orgs/<slug>/org-profile.json` must exist and be valid JSON
- `shared/config/org-profile.example.json` must match the token structure
- Python 3.x required
