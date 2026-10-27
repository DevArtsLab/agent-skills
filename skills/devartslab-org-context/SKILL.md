---
name: devartslab-org-context
description: Resolve and display the active organization and consultant context (slug, paths, profile)
---

Run this to check which org and consultant are currently active and see all derived paths. Every tool in this repo resolves an org context (and a consultant context) before touching org-specific data — this skill shows you what that resolution produces.

## What this does

1. Resolves the active org using the standard precedence:
   - `--org <slug>` CLI flag (highest)
   - `ORG_CONTEXT` environment variable
   - `shared/config/private/active-org.json` → `{"active_org": "<slug>"}`
   - Single org tree under `shared/config/orgs/` (ignoring `_` prefixed dirs)
   - Fail loudly if none of the above resolve
2. Resolves the active consultant using the same precedence pattern:
   - `--consultant <slug>` CLI flag (highest)
   - `CONSULTANT_CONTEXT` environment variable
   - `shared/config/private/active-consultant.json` → `{"active_consultant": "<slug>"}`
   - Single consultant tree under `shared/config/consultants/` (ignoring `_` prefixed dirs)
   - Fail loudly if none of the above resolve
3. Prints the resolved slug, source, and all derived paths:
   - Org tree: `shared/config/orgs/<slug>/`
   - Profile: `shared/config/orgs/<slug>/org-profile.json`
   - Salesforce dir: `shared/config/orgs/<slug>/salesforce/`
   - n8n dir: `shared/config/orgs/<slug>/n8n/`
   - Private dir: `shared/config/orgs/<slug>/private/`
   - Render output: `dist/<slug>/`
   - n8n build output: `n8n/development/build/<slug>/<env>/`
   - Consultant tree: `shared/config/consultants/<slug>/`
   - Consultant profile: `shared/config/consultants/<slug>/consultant-profile.json`
4. Exports environment variables for shell use (via `org.py env`).

## When to run this

- Before running any org-specific build, render, or deploy command
- When unsure which org is active
- After switching orgs with `org.py use <slug>`
- When debugging "wrong org" issues

## How to run

**Display the active org context:**

```bash
cd "$(git rev-parse --show-toplevel)"
python3 scripts/org.py show
```

**Display a specific org:**

```bash
python3 scripts/org.py show --org iaboston
```

**Export env vars for shell scripts:**

```bash
eval "$(python3 scripts/org.py env --org iaboston)"
echo $ORG_SLUG        # iaboston
echo $ORG_TREE        # shared/config/orgs/iaboston
echo $SF_ORG_ALIAS    # from sf-org.json
echo $SF_CONFIG_DIR   # shared/config/orgs/iaboston/salesforce
```

**List all available orgs:**

```bash
python3 scripts/org.py list
```

**Switch the active org:**

```bash
python3 scripts/org.py use iaboston
```

**List all consultants:**

```bash
python3 scripts/org.py consultant list
```

**Show the active consultant:**

```bash
python3 scripts/org.py consultant show
```

**Switch the active consultant:**

```bash
python3 scripts/org.py consultant use amir-olyaei
```

**Scaffold a new consultant:**

```bash
python3 scripts/org.py consultant new lane-doe --name "Lane Doe"
```

## Node.js equivalent

For Node.js scripts (n8n build, deploy):

```bash
node -e "import('./scripts/org-context.mjs').then(m => m.printContext())" -- --org iaboston
```

## Output

```
  SLUG      ORGANIZATION
* iaboston  Iranian Association of Boston

active org: iaboston
org tree:   shared/config/orgs/iaboston
profile:    shared/config/orgs/iaboston/org-profile.json
salesforce: shared/config/orgs/iaboston/salesforce
n8n:        shared/config/orgs/iaboston/n8n
private:    shared/config/orgs/iaboston/private
dist:       dist/iaboston
n8n build:  n8n/development/build/iaboston/<env>
```

## Dependencies

- Python 3.x
- `scripts/org_context.py` (Python resolver)
- `scripts/org-context.mjs` (Node resolver)
- `scripts/org.py` (CLI wrapper)

## Relationship to other workflows

- Every org-specific skill (`/n8n-build`, `/sync-templates`, `/salesforce-deploy`) calls this resolver internally
- Use `/org-new` to create a new org tree
- See `.dev/contracts/guidelines/multi-org.md` for the full contract
