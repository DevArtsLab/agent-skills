---
name: devartslab-project-new
description: Scaffold a new project from the project-blueprint copier template and wire it into the workspace config store. Use whenever the user wants to create, start, bootstrap, or set up a new project or repo in the workspace, even if they just say "new project", "start a project", or name a slug without mentioning the blueprint.
---

<!-- author: Amir Olyaei | DevArts Lab | created: 2026-11-01 -->

Scaffold a new project: renders `project-blueprint` via copier (identity manifest as answers file), creates the workspace store dirs, renders a gitignored `.env.local` skeleton, registers declared secret ids, runs `git init`.

Contracts implemented: D12 (identity manifest, brand-neutral template) and D14 (workspace store, `.workspace.json` marker), per `foundation/reference/store-layout.md`.

## Architecture

- `project-blueprint/copier.yml` — the field contract.
- `project-blueprint/template/` — scaffold rendered into children; root files are the repo's own docs. `_exclude` cannot separate same-named meta/scaffold files (matches output paths), hence the subdirectory.
- `config/identity/identity.schema.json` — the identity contract (D12): grouped sections (legal, brand, contact, github, workspace), `x-copier-var` annotations are the only name map. New fields go through the schema, never ad hoc.
- `config/identity/<brand>.json` — manifest per brand; the wrapper flattens it via the schema into copier answers.
- This script — wrapper: root/marker resolution, store dirs, env render, registry, git init.
- `.copier-answers.yml` in each generated repo — replay record; enables `copier update` once the template is committed.

## Workflow

1. Collect inputs: `slug` (required), `--identity` (required when multiple manifests), secret ids `<platform>/<env>/<NAME>` (optional).
2. Dry-run first, always:

```bash
python3 ~/.agents/skills/devartslab-project-new/scripts/project_new.py --slug <slug> --identity <brand> --secrets a,b,c
```

3. **Checkpoint.** Show the printed plan and ask once: proceed? Do not ask per-file questions.
4. On approval, rerun the same command with `--apply`.
5. Report the printed next steps. Do not stage, commit, or push anything.

Blueprint source resolution: `--blueprint` path/URL > `gh:<github_org>/<blueprint_repo>` from manifest > sibling `project-blueprint/` dir.

## Update path

Generated repos carry `.copier-answers.yml`. After blueprint changes are committed:

```bash
copier update <project-dir> --defaults
```

Requires the template to be at a committed ref; copier cannot diff a dirty working tree.

## Retire

Inverse of scaffold, same gate. `--slug <slug> --retire` prints the footprint; `--retire --apply` removes `<store>/projects/<slug>/`, `<env>/projects/<slug>/`, and `owner=projects/<slug>` registry entries. Repo dir, `LAB_INDEX.md` rows, and the Linear issue are listed, never deleted — those stay human.

## What stays human

- Choosing the slug, identity, and secret id list
- Supplying real credential values into `<store>/projects/<slug>/secrets/` and `.env.local`
- All git staging/committing and the first push
- Regenerating `REPO_INDEX.md` / `LAB_INDEX.md` (run the update-index skill after files exist)

## Failure behavior

Resolution failure, existing destination, invalid slug, bad secret id format, and copier errors are hard errors with a remediation message. No silent fallback.
