---
name: sync-external
description: External sync - push validated docs to external systems (Figma, etc.)
---

Run this to push validated documentation to external systems. This workflow should only be run after `/sync-internal` has completed successfully to ensure all markdown files are consistent and up-to-date before pushing to external systems.

**Org context:** FigJam sync uses the active org's rendered `dist/<slug>/` output. Set `ORG_CONTEXT=<slug>` or pass `--org <slug>` to the render step.

## What this does

Executes external system synchronization workflows:

1. **FigJam Sync** (`/figma-figjam-sync`) — Syncs diagrams to FigJam boards

## When to run this

- After `/sync-internal` has completed successfully
- When you need to update visual diagrams in Figma
- Before a major presentation or demo
- After making diagram changes in markdown

## How to run

Ask the AI assistant to run the external sync:

```
/sync-external
```

The assistant will:

1. Check that internal sync has been run recently (warns if not)
2. Execute FigJam sync for all diagrams with manifests
3. Report results for each diagram
4. Provide a summary of all external updates

**Critical rule:** Always run `/sync-internal` before `/sync-external` to ensure you're pushing consistent, validated documentation to external systems.

## Diagrams synced

The workflow scans for `.figjam.md` manifest files and syncs each:

- `shared/ngo-crm-process-flow-map.figjam.md` — CRM Process Flow Map
- `shared/ngo-automation-map.figjam.md` — Automation Map

Each manifest contains:

- Source `.md` file path
- FigJam board URL and file key
- Figma plan key

## Sync process per diagram

1. Read the source `.md` file
2. Extract the Mermaid diagram from the fenced code block
3. Decide template vs production (see `/figma-figjam-sync` workflow)
4. Clear existing FigJam board nodes
5. Regenerate diagram via Figma MCP (`mcp1_generate_diagram`)
6. Update manifest if URL/file key changed

## Output

For each diagram:

- Success/failure status
- Board URL
- Nodes removed/added
- Warnings or errors

Final summary:

- Total diagrams synced
- Diagrams succeeded/failed
- Overall sync status

## Error Handling

- If a diagram sync fails, the workflow continues with remaining diagrams
- Failed diagrams are reported in the final summary
- You can re-run individual diagram syncs afterward
- Critical errors (e.g., Figma authentication) stop execution early

## Dependencies

- `/sync-internal` must have been run successfully
- Figma access (for FigJam sync)
- All `.figjam.md` manifests must be valid

## Time Estimate

- FigJam sync: ~30 seconds per diagram (if updates needed)

Total: ~1 minute for 2 diagrams

## Best Practices

- Always run `/sync-internal` first
- Review internal sync summary before pushing externally
- Verify Figma board sharing settings after sync
- Use selective execution for specific diagrams if needed
