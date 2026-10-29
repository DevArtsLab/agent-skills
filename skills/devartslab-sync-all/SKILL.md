---
name: devartslab-sync-all
description: Master sync - run all document update chains in order
---

Run this to execute all document synchronization workflows in the correct dependency order. This is the master orchestrator that runs all chains: internal documentation sync (template rendering, activity log update, cross-reference checking, index generation) followed by external system sync (FigJam).

**Org context:** All sub-workflows operate on the active org. Set `ORG_CONTEXT=<slug>` or pass `--org <slug>` to the underlying render/build commands. Template rendering outputs to `dist/<slug>/`; n8n builds to `build/<slug>/<env>/`.

## What this does

Executes all sync workflows in dependency order:

**Internal sync (markdown validation):**

1. **Template Rendering** (`/sync-templates`) — Renders org-specific docs from templates
2. **Activity Log Update** (`/update-activity-log`) — Records new project activities
3. **Cross-Reference Check** (`/check-references`) — Validates document references
4. **Index Generation** (`/update-index`) — Regenerates INDEX.md
5. **Demo Guide Update** (`/update-demo-guide`) — Updates demo guide with accurate URLs and deployment status

**External sync (push to external systems):** 6. **FigJam Sync** (`/figma-figjam-sync`) — Syncs diagrams to FigJam boards

**Alternative: Run separately**

- `/sync-internal` — Only internal documentation sync (chains 1-5)
- `/sync-external` — Only external system sync (chain 6)

## When to run this

- After making changes to multiple document types
- Before a major commit or delivery
- After restructuring the repository
- Weekly maintenance to keep everything in sync
- Before starting a new AI assistant session

## How to run

Ask the AI assistant to run the master sync:

```
/sync-all
```

The assistant will:

1. Execute each workflow in order
2. **Proactively identify and update all related documents** when changes are detected (the `/check-references` workflow identifies which documents need updating together)
3. Report results for each chain
4. Continue even if one chain fails (with warning)
5. Provide a summary of all changes made

**Critical rule:** When any roadmap document is updated (either by user or via MCP operations like n8n workflow creation), the AI assistant must identify and update all related documents in the same session. The `/check-references` workflow provides guidance on which documents are related and should be updated together.

## Dependency Order Rationale

**Internal sync (chains 1-5):**

1. **Template Rendering first** — Renders `dist/` files that other workflows might reference
2. **Activity Log Update second** — Records new project activities before other validations
3. **Cross-Reference Check third** — Validates that references are correct before indexing
4. **Index Generation fourth** — Captures the final repo structure after all changes
5. **Demo Guide Update fifth** — Updates demo guide with accurate deployment status after all other changes

**External sync (chain 6):** 6. **FigJam Sync after internal** — Pushes validated markdown to external systems only after internal consistency is verified

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

## Selective Execution

If you only need specific chains, run them individually:

**Internal sync chains:**

- `/sync-templates` — Only render templates
- `/update-activity-log` — Only update activity log
- `/check-references` — Only check references
- `/update-index` — Only update index
- `/update-demo-guide` — Only update demo guide
- `/update-memory` — Only update memory (manual, not in automatic sync)
- `/sync-internal` — Run all internal chains (1-5)

**External sync chains:**

- `/figma-figjam-sync` — Only sync FigJam
- `/sync-external` — Run all external chains (6)

## Error Handling

- If a chain fails, the workflow continues with remaining chains
- Failed chains are reported in the final summary
- You can re-run individual failed chains afterward
- Critical errors (e.g., missing config files) stop execution early

## Dependencies

- All individual workflows must exist in `.devin/skills/`
- Python 3.x (for template rendering)
- Figma access (for FigJam sync, if applicable)
- Active org context must be resolvable (org tree exists or `--org` is passed)

## Time Estimate

- Template rendering: ~5 seconds
- Cross-reference check: ~10 seconds
- FigJam sync: ~30 seconds (if diagrams need updates)
- Index generation: ~15 seconds
- Demo guide update: ~30 seconds

Total: ~1.5-2 minutes for full sync

## Best Practices

- Run this before committing major changes
- Review the summary before proceeding
- Fix failed chains before important deliveries
- Use selective execution for faster feedback during development
