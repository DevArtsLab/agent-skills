---
name: update-activity-log
description: Update NGO activity log with new project activities
---

Run this whenever significant project activities occur that should be recorded in the activity log. This workflow ensures the activity log stays current as a chronological record of project progress.

## What this does

1. Reviews recent project activities (from completed tasks, current context, or user input)
2. Adds new entries to the appropriate phase section in `shared/ngo-activity-log.md`
3. Updates phase headers if the project has moved to a new phase
4. Ensures all entries use `{{TOKEN}}` placeholders for org-specific data
5. Updates workflow references if new workflows are created

## When to run this

- After completing a major project milestone
- After finishing a significant task or deliverable
- After making key project decisions
- After starting a new project phase
- After adding or modifying n8n workflows
- After sending or receiving important communications with the partner org
- Weekly as part of project maintenance

## How to run

Ask the AI assistant to update the activity log:

```
/update-activity-log
```

The assistant will:

1. Ask for a summary of recent activities
2. Determine the appropriate phase section for each activity
3. Format entries consistently with existing log style
4. Add entries to the activity log file
5. Update phase headers if needed

## Entry format

The activity log is organized by project phases, with each phase divided into:

**Strategic Milestones & Decisions:**

- Major project milestones and deliverables
- Key architectural and strategic decisions
- Project direction changes
- Phase transitions
- Communications with partner org leadership

**Operational Activities:**

- Technical implementations and deployments
- Workflow creation and modifications
- Document creation and updates
- Infrastructure changes
- Routine maintenance tasks

Each entry should follow this format:

- **[Action completed]**: Brief description of what was done. Include relevant dates, references, and outcomes.
- Use `{{TOKEN}}` placeholders for any org-specific information (org name, contacts, URLs, etc.)
- Include workflow references when applicable: `Workflow reference: {{N8N_WORKFLOW_URL}}`
- Keep entries concise but informative

## Phase structure

The log is organized by project phases:

- Phase 1 — Discovery & Assessment
- Phase 2 — Planning & Design
- Phase 3 — Implementation
- Phase 4 — Testing & Validation
- Phase 5 — Deployment & Handoff

Add new phase sections as the project progresses.

## What gets recorded

**Strategic Milestones & Decisions:**

- Proposal drafts and submissions
- Roadmap creation and updates
- Communications with partner org leadership
- Milestone completions and deliverable submissions
- Phase transitions
- Key architectural and strategic decisions
- Project direction changes

**Operational Activities:**

- Technical implementations (Salesforce, n8n, HubSpot, etc.)
- Workflow creation and modifications
- Document creation and major updates
- Infrastructure changes
- Routine maintenance tasks
- Sync workflow executions
- Credential updates and access changes

**What NOT to log:**

- Minor code edits or routine file changes
- Personal notes or opinions
- Duplicate information already in other docs
- Trivial operational details that don't impact project state

## Dependencies

- `shared/ngo-activity-log.md` must exist
- `shared/config/orgs/<slug>/org-profile.json` for token reference (if checking token validity)

## Integration with parent workflows

This workflow is part of the `/sync-all` chain and runs after template rendering:

1. `/sync-templates` — renders templates with org values
2. `/update-activity-log` — records new activities (this workflow)
3. `/check-references` — validates document references
4. `/update-index` — regenerates REPO_INDEX.md
5. `/update-demo-guide` — updates demo guide with accurate deployment status

**Note:** Memory distillation (`/update-memory`) is not part of automatic sync to keep MEMORY.md focused on distilled facts rather than operational activities.

## Manual update process

If you prefer manual updates:

1. Open `shared/ngo-activity-log.md`
2. Find the appropriate phase section
3. Determine if the entry is a Strategic Milestone & Decision or Operational Activity
4. Add new entries at the top of the appropriate subsection (most recent first)
5. Use consistent formatting with existing entries
6. Ensure org-specific data uses `{{TOKEN}}` placeholders
7. Update the phase header if moving to a new phase
8. Save the file

## Best practices

- Keep entries factual and concise
- Use past tense for completed actions
- Include dates for time-sensitive activities
- Reference related documents or workflows when applicable
- Update the log regularly rather than batching many entries
- Use the same placeholder tokens as other template files
