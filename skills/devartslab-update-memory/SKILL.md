---
name: devartslab-update-memory
description: Update MEMORY.md with distilled facts from source documents
---

Run this when source documents change significantly to suggest updates to MEMORY.md. This workflow analyzes changed source documents and proposes additions or updates to the distilled facts in MEMORY.md.

## What this does

1. Identifies recently changed source documents
2. Extracts key facts, decisions, and patterns from changed documents
3. Compares against existing MEMORY.md content
4. Suggests additions, updates, or deprecations for MEMORY.md sections

## When to run this

- After major updates to program documentation (RTS*Program*\*.md)
- After significant changes to project roadmaps
- After adding new capabilities or phases to the NGO project
- After updating contact information or key dates
- Before a new AI assistant session to ensure context is fresh

## How to run

Ask the AI assistant to update memory:

```
/update-memory
```

The assistant will:

1. Review source documents that have been modified
2. Read changed files to extract new facts
3. Compare with current MEMORY.md content
4. Propose specific updates (additions, modifications, removals)
5. Ask for approval before applying changes

## What gets tracked in MEMORY.md

**Program Overview:**

- Program dates, cohort info, instructor/coordinator contacts
- Operating tools (Moodle, Slack, Outline Wiki)
- Assignment deadlines

**Program Structure:**

- Phase breakdown (Foundations, Specialization, Capstone)
- Weekly themes and topics
- Signature habits and frameworks

**Technology Stack:**

- Core platforms (HubSpot, Salesforce, etc.)
- Productivity tools (Google Workspace, Slack, etc.)
- Specialized tools (n8n, Zapier, Clay, etc.)

**Certifications:**

- Certification targets and due dates

**Capstone Project:**

- Project selection, organization info, milestones
- Core capabilities and technology stack
- Project principles and structure
- Current system state (high-level, not operational details)
- Key architectural decisions (not implementation details)

**Repository Structure:**

- Key files and folders
- Where to find what

**Career Resources:**

- Employer lists, interview targets, LinkedIn checklist

**Key Contacts:**

- Program staff and their contact info

## What does NOT get tracked in MEMORY.md

**Operational activities:**

- Routine sync executions (internal/external syncs)
- Daily development tasks and bug fixes
- File edits and minor documentation updates
- Workflow execution logs
- Credential updates and maintenance

**Chronological entries:**

- Daily progress updates
- Activity log entries (use ngo-activity-log.md instead)
- Meeting notes and discussions
- Task completion records

**Implementation details:**

- Specific workflow configurations
- Code-level changes and refactoring
- Build and deployment logs
- Testing and validation results

**Reasoning:** MEMORY.md is for distilled facts and strategic knowledge, not operational logs. Routine operational content belongs in ngo-activity-log.md to keep MEMORY.md concise and focused on high-level context that AI agents need for quick understanding.

## Output

- Suggested additions to MEMORY.md (new facts discovered)
- Suggested updates (changed values, outdated info)
- Suggested removals (deprecated information)
- Each suggestion includes the source document and rationale

## Manual update process

If you prefer manual updates:

1. Read the changed source document
2. Identify new facts or changed information
3. Find the relevant section in MEMORY.md
4. Add or update the fact with proper formatting
5. Update the "Last updated" date at the top
6. Commit the change

## Dependencies

- Source documents must be readable
- MEMORY.md must exist

## Best practices

- Keep facts concise and factual (no opinions)
- Use consistent formatting (bullet points, tables)
- Update the "Last updated" date with every change (format: "YYYY-MM-DD at H:MM AM/PM EDT" per terminology guidelines)
- Avoid duplicating information across sections
- Remove outdated facts rather than commenting them out
