---
name: devartslab-sync-internal
description: Internal sync - update repo documentation without external pushes
---

Run this to execute internal documentation synchronization workflows. This updates all markdown files, validates references, and regenerates indexes without pushing to external systems (Figma, etc.).

**Org context:** All sub-workflows operate on the active org. Set `ORG_CONTEXT=<slug>` or pass `--org <slug>` to the underlying render/build commands. Template rendering outputs to `dist/<slug>/`.

## What this does

Executes internal-only sync workflows in dependency order:

1. **Template Rendering** (`/sync-templates`) — Renders org-specific docs from templates
2. **Activity Log Update** (`/update-activity-log`) — Records new project activities
3. **Cross-Reference Check** (`/check-references`) — Validates document references
4. **Index Generation** (`/update-index`) — Regenerates INDEX.md
5. **Demo Guide Update** (`/update-demo-guide`) — Updates demo guide with accurate URLs and deployment status

## When to run this

- After making changes to markdown documents
- Before running external sync to ensure internal consistency
- During development when you don't need external systems updated
- When external systems (Figma) are unavailable

## How to run

Ask the AI assistant to run the internal sync:

```
/sync-internal
```

The assistant will:

1. Execute each workflow in order
2. **Proactively identify and update all related documents** when changes are detected
3. Report results for each chain
4. Continue even if one chain fails (with warning)
5. Provide a summary of all changes made

**Critical rule:** When any roadmap document is updated, the AI assistant must identify and update all related documents in the same session. The `/check-references` workflow provides guidance on which documents are related and should be updated together.

## Dependency Order Rationale

1. **Template Rendering first** — Renders `dist/` files that other workflows might reference
2. **Activity Log Update second** — Records new project activities before other validations
3. **Cross-Reference Check third** — Validates that references are correct before indexing
4. **Index Generation fourth** — Captures the final repo structure after all changes
5. **Demo Guide Update last** — Updates demo guide with accurate deployment status after all other changes

**Note:** Memory distillation (`/update-memory`) is removed from automatic sync to keep MEMORY.md focused on distilled facts rather than operational activities. Run `/update-memory` manually only when strategic facts or architectural decisions change.

## Output

For each chain:

- Success/failure status
- Files changed
- Warnings or errors
- Summary of what was updated

Final summary:

- Total chains executed
- Chains succeeded/failed
- Overall sync status

## Error Handling

- If a chain fails, the workflow continues with remaining chains
- Failed chains are reported in the final summary
- You can re-run individual failed chains afterward
- Critical errors (e.g., missing config files) stop execution early

## Dependencies

- All individual workflows must exist in `.devin/skills/`
- Python 3.x (for template rendering)
- Active org context must be resolvable (org tree exists or `--org` is passed)

## Time Estimate

- Template rendering: ~5 seconds
- Cross-reference check: ~10 seconds
- Index generation: ~15 seconds
- Demo guide update: ~30 seconds

Total: ~60 seconds for full internal sync

## Best Practices

- Run this before `/sync-external` to ensure internal consistency
- Review the summary before proceeding to external sync
- Fix failed chains before important deliveries
- Use selective execution for faster feedback during development
