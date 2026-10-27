---
name: devartslab-figma-figjam-sync
description: Sync a source diagram in the IDE to an editable FigJam board via the Figma MCP
---

# Source of truth

The `.md` file in the repo is the single source of truth. The `.figjam.md` file next to it is only a sync manifest (board URL + `fileKey`).

# Diagrams with sync manifests

The workflow scans for `.figjam.md` manifest files and syncs each:

- `shared/ngo-crm-process-flow-map.figjam.md` — CRM Process Flow Map (technical data architecture)
- `shared/ngo-automation-map.figjam.md` — Automation Map (business workflow summary)

# Push: source -> FigJam

1. Open the source `.md` and the matching `.figjam.md` manifest.
2. Extract the diagram source from the fenced code block in the `.md` file.
   **Note:** This process always uses the _current local state_ of the source `.md` file, regardless of its git commit status, to ensure the FigJam board reflects the latest changes in the IDE.
3. Decide whether this board should show **template placeholders** or **org-specific real values**:
   - **Template / public board (default):** use the unrendered `shared/*.md` source. The board will display `{{TOKEN}}` placeholders and generic labels — this is the safe choice when the board is shared or the data is not yet approved for production.
   - **Production / org-specific board:** render first with the target org:
     ```
     python3 scripts/render_templates.py --org <slug>
     ```
     Then extract the diagram source from the rendered `dist/<slug>/*.md` output. This injects real org values from `shared/config/orgs/<slug>/org-profile.json`.
4. To keep the same board URL, clear the existing board:
   - Run `mcp1_use_figma` on the `figjam_file_key` and remove all top-level nodes:
     ```js
     const children = [...figma.currentPage.children];
     for (const node of children) {
       node.remove();
     }
     return { removed: children.length };
     ```
5. Run `mcp1_generate_diagram`:
   - `fileKey`: the `figjam_file_key` from the manifest
   - `name`: the `diagram_name` from the manifest
   - `mermaidSyntax`: the diagram source extracted in step 2
   - `planKey`: the Figma plan key from the manifest or your account
6. The returned link is the same board. Update `figjam_url` and `figjam_file_key` in the manifest if they change.

> **Identifiable information in FigJam:** prefer placeholders for any org-specific or personally identifiable information. Real values (e.g., names, emails, URLs, IDs) should only be injected when generating a production board from `dist/`.

# Pull: FigJam -> source markdown (manual)

1. Run `mcp1_get_figjam` with `fileKey` and `nodeId: 0:1`.
2. Review the returned node text, comments, and any sticky notes added to the board.
3. Manually edit the source `.md` diagram block to match the board. This is the only reverse path — the Figma MCP does not export shapes back to the source format.
4. If you edited a template, also update the corresponding values in `shared/config/orgs/<slug>/org-profile.json` so re-rendering does not overwrite your changes.
5. Regenerate the board using the push steps above.

# Constraints for the Figma diagram generator

- No HTML tags (e.g. `<br/>`) inside labels.
- No emoji characters.
- Wrap labels containing special characters (`:`, `,`, `;`, `/`, `→`, `—`, etc.) in double quotes.
- Multi-line labels are allowed; use actual line breaks inside quoted text, not `\n` escape sequences.
- Reserved words (`end`, `subgraph`, `graph`) cannot be used as node IDs.

# First-time setup

If no `figjam_file_key` exists yet, run `mcp1_generate_diagram` without `fileKey` to create a new board. Record the returned `fileKey` and `figjam_url` in the matching manifest (or in `shared/config/orgs/<slug>/org-profile.json` if the manifest is a template).

# Record — legacy export options

The same diagram source can be pasted into Lucidchart (Insert → Diagram-as-code) or Miro to generate a PNG. Those are legacy alternatives; the active IDE → FigJam flow uses the Figma MCP.
