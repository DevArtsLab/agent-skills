---
name: devartslab-org-new
description: Onboard a new partner organization (scaffold org tree, validate, first build)
---

Run this to scaffold a new partner organization into the multi-org system. This creates the org tree from the template, validates it, and runs a first build to verify everything works.

## What this does

1. Validates the org slug (lowercase, filesystem-safe, no reserved words)
2. Scaffolds the org tree from `shared/config/orgs/_template/`:
   - `org-profile.json` (with `{{TOKEN}}` placeholders to fill in)
   - `salesforce/sf-org.json` (org alias, instance URL placeholders)
   - `salesforce/project-scratch-def.json` (scratch org definition)
   - `n8n/default.json` (org-level n8n config placeholders)
   - `n8n/development.json`, `n8n/staging.json`, `n8n/production.json` (env overrides)
   - `n8n/n8n-secrets.json` (credential secrets placeholder)
   - `n8n/tables/manifest.json` (data table manifest placeholder)
   - `n8n/env/.env.{development,staging,production}` (n8n instance URL + API key)
   - `private/` (research notes, access-control docs)
3. Sets the new org as active
4. Prints next-steps checklist

## When to run this

- When onboarding a new partner organization
- When creating a test/demo org for development

## How to run

1. **Scaffold the new org:**

```bash
cd "$(git rev-parse --show-toplevel)"
python3 scripts/org.py new <slug>
```

Replace `<slug>` with the org's filesystem-safe identifier (e.g. `parsi-network`, `isaa-boston`).

**Slug rules:** `^[a-z][a-z0-9-]{1,38}[a-z0-9]$`. No underscores, no uppercase, no dots.
Reserved slugs (cannot be used): `_template`, `default`, `example`, `all`, `orgs`, `private`, `shared`.

2. **Fill in the org profile:**

Edit `shared/config/orgs/<slug>/org-profile.json` — replace every `{{TOKEN}}` with the org's real data. Use `shared/config/org-profile.example.json` as the token schema reference.

3. **Fill in the Salesforce config:**

- `shared/config/orgs/<slug>/salesforce/sf-org.json` — org alias, instance URL, users, consumer key
- Generate the org's JWT key pair (NEVER reuse another org's):
  ```bash
  cd salesforce
  ./scripts/generate-jwt-cert.sh --org <slug>
  ```

4. **Fill in the n8n config:**

- `shared/config/orgs/<slug>/n8n/default.json` — campaigns, elections, occasions, table IDs, workflow IDs, credentials
- `shared/config/orgs/<slug>/n8n/env/.env.{env}` — n8n instance URL + API key per environment

5. **Validate the org:**

```bash
python3 scripts/org.py validate --org <slug>
```

Fix any errors. Warnings are acceptable for a newly scaffolded org (missing optional fields).

6. **Run a first render + build:**

```bash
python3 scripts/render_templates.py --org <slug>
node n8n/development/scripts/build.js --org <slug> --env development
```

Check `dist/<slug>/` for rendered docs and `n8n/development/build/<slug>/development/json/` for built workflows. Verify no unresolved placeholders.

7. **Update REPO_INDEX:**

Run `/update-index` to document the new org tree (only the template and example files are tracked; the org tree itself is gitignored).

## Options

- `--slug <slug>` — the org slug (also accepted as positional argument)
- `--from-template <slug>` — copy from an existing org instead of `_template` (useful for creating similar orgs)

## Output

```
created org tree: shared/config/orgs/<slug>
  + org-profile.json
  + salesforce/sf-org.json
  + salesforce/project-scratch-def.json
  + n8n/n8n-secrets.json
  + n8n/tables/manifest.json
  + n8n/env/.env.development
  + n8n/env/.env.staging
  + n8n/env/.env.production

next steps:
  1. fill in shared/config/orgs/<slug>/org-profile.json (replace every {{TOKEN}})
  2. ensure a consultant profile exists (python3 scripts/org.py consultant list)
     — if none, create one: python3 scripts/org.py consultant new <slug> --name "..."
     — fill in shared/config/consultants/<slug>/consultant-profile.json
     — set active: python3 scripts/org.py consultant use <slug>
  3. python3 scripts/org.py use <slug>
  4. python3 scripts/org.py validate --org <slug>
  5. python3 scripts/render_templates.py --org <slug>
  6. generate this org's own Salesforce JWT pair (never reuse another org's):
     openssl req -x509 -sha256 -nodes -days 1095 -newkey rsa:2048 \
       -keyout shared/config/orgs/<slug>/salesforce/n8n-jwt.key \
       -out shared/config/orgs/<slug>/salesforce/n8n-jwt.crt \
       -subj "/CN=<slug>-n8n-integration"
```

## Security checklist for new orgs

- [ ] JWT key pair generated fresh (never copied from another org)
- [ ] n8n API key unique to this org's instance
- [ ] Salesforce consumer key unique to this org's Connected App
- [ ] No secrets shared across orgs
- [ ] `shared/config/orgs/<slug>/` is gitignored (automatic — entire `orgs/` dir except `_template/` is gitignored)

## Dependencies

- Python 3.x
- `scripts/org.py`
- `shared/config/orgs/_template/` must exist
- `shared/config/org-profile.example.json` must exist (token schema)

## Relationship to other workflows

- After onboarding, use `/org-context` to verify the active org
- Use `/n8n-build` to build workflows for the new org
- Use `/sync-templates` to render docs for the new org
- Use `/salesforce-deploy` to deploy Salesforce metadata to the new org
- See `.dev/contracts/guidelines/multi-org.md` for the full multi-org contract
