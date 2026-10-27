---
name: check-references
description: Check cross-references and semantic consistency between roadmap documents
---

Run this to validate that cross-references between roadmap documents are consistent and up-to-date. This workflow checks that referenced documents exist, validates semantic consistency, and flags documents that should be updated together.

## What this does

1. Scans roadmap documents for cross-references (markdown links, file references)
2. Validates that referenced files exist in the expected locations
3. Checks for circular references
4. Validates semantic consistency across related documents
5. Identifies documents that should be updated together when changes are made
6. Reports broken references and inconsistent information

## When to run this

- After updating any roadmap document
- After adding or modifying n8n workflows
- After making changes to the CRM process flow
- Before committing changes to roadmap files
- After restructuring the project hierarchy
- As part of `/sync-all` to ensure all docs are consistent

## How to run

Ask the AI assistant to check cross-references:

```
/check-references
```

The assistant will:

1. Read all roadmap documents in `shared/`
2. Extract all markdown-style links: `[text](path/to/file.md)`
3. Validate each referenced file exists
4. Check semantic consistency across related documents
5. Report any broken references or inconsistencies
6. Provide guidance on which documents need updating

## Key relationships to validate

**Main roadmap references:**

- `ngo-project-roadmap.md` → `ngo-salesforce-roadmap.md`
- `ngo-project-roadmap.md` → `ngo-n8n-roadmap.md`
- `ngo-project-roadmap.md` → `ngo-crm-process-flow-map.md`

**FigJam sync references:**

- `ngo-crm-process-flow-map.md` → `ngo-crm-process-flow-map.figjam.md`

**Semantic consistency checks:**

- When `ngo-project-roadmap.md` is updated, check if `ngo-n8n-roadmap.md` and `ngo-salesforce-roadmap.md` reflect the same changes
- When `ngo-n8n-roadmap.md` is updated, check if `ngo-crm-process-flow-map.md` reflects the new workflows
- When workflows are added/modified via n8n MCP, check if all roadmaps are updated
- When approval channels change, check if all documents reflect the change

## What gets checked

- File existence (does the referenced file exist?)
- File path accuracy (is the path correct relative to the repo root?)
- Link format (is the markdown link syntax valid?)
- Semantic consistency (do related documents describe the same state?)
- Workflow consistency (do all roadmaps list the same workflows?)
- Approval channel consistency (do all documents use the same approval mechanisms?)

## Output

- List of valid references (green)
- List of broken references (red) with suggested fixes
- List of semantic inconsistencies (yellow) with required updates
- Guidance on which documents need updating when changes are made

## Dependencies

- All roadmap documents must be readable
- Repo structure must be stable during check

## Manual validation

For complex restructures, manually verify:

1. Open each roadmap document
2. Ctrl+F for `](./` to find all relative links
3. Click each link to verify it opens the correct file
4. Update any broken links
5. Compare workflow lists across all roadmaps
6. Compare approval channel descriptions across all documents
