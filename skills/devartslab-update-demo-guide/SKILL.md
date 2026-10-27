---
name: update-demo-guide
description: Update demo guide with accurate access links and deployment status
---

Run this after Salesforce deployments, n8n builds, or before demo preparation to ensure
`shared/demo-guide.md` reflects the actual system state with accurate URLs and component status.

**Org context:** This skill operates on the active org. Pass `--org <slug>` to the underlying build/deploy commands, or set `ORG_CONTEXT=<slug>`. The org profile is read from `shared/config/orgs/<slug>/org-profile.json`.

## When to Run

- After Salesforce deployments (via `salesforce-deploy` skill)
- After n8n workflow builds (via `n8n-build` skill)
- As part of `sync-internal` workflow
- Manually before demo preparation
- After significant system changes

## What It Does

1. **Queries Salesforce deployment status**
   - Checks org access and base URL
   - Retrieves deployed components (custom fields, permission sets, reports, dashboards)
   - Gets component IDs and access URLs
   - Verifies Connected App and user setup

2. **Queries n8n instance status**
   - Checks n8n instance access and base URL
   - Retrieves active workflows and their IDs
   - Gets workflow URLs and status
   - Verifies data tables and their schemas

3. **Updates demo guide with accurate data**
   - Replaces tokenized URLs with actual values
   - Updates component counts and deployment status
   - Marks demo sections as READY/IN PROGRESS/NOT STARTED
   - Generates screenshot checklist based on deployed items

4. **Maintains tokenization**
   - Updates token values in `shared/config/orgs/<slug>/org-profile.json`
   - Preserves template structure for reusability
   - Updates status tokens for demo readiness

## Steps

1. **Check Salesforce deployment status**

   ```bash
   sf org display --json
   sf sobject describe --sobject Contact --json
   sf sobject describe --sobject Opportunity --json
   ```

2. **Get Salesforce component details**
   - Custom fields: Count and key field names
   - Permission sets: Names and access scopes
   - Reports: Names and folder locations
   - Dashboards: Names and component IDs
   - Connected App: Name and OAuth type
   - Users: Count and roles

3. **Check n8n instance status**

   ```bash
   # Use migration tools to query instance
   node n8n/migration-tools/client.js --list-workflows
   node n8n/migration-tools/client.js --list-tables
   ```

4. **Get n8n workflow details**
   - Active workflows: Count and names
   - Workflow IDs and access URLs
   - Data tables: Count and schemas
   - Credential status

5. **Update the org's org-profile.json with actual values**
   - `{{SALESFORCE_BASE_URL}}`: Actual Salesforce org URL
   - `{{N8N_WORKFLOW_URL}}`: Actual n8n instance URL
   - `{{SALESFORCE_STATUS}}`: Current deployment status
   - `{{N8N_STATUS}}`: Current instance status

   The org profile is at `shared/config/orgs/<slug>/org-profile.json` (gitignored).

6. **Update demo-guide.md with deployment data**
   - Replace Salesforce URLs with actual component URLs
   - Update component counts (fields, permission sets, reports, dashboards)
   - Mark sections as READY based on actual deployments
   - Generate screenshot checklist for deployed components

7. **Generate screenshot requirements**
   - Create checklist of URLs to screenshot
   - Mark items as READY FOR SCREENSHOT vs NOT YET DEPLOYED
   - Include workflow screenshots for n8n components
   - Include Salesforce page screenshots for deployed components

## Salesforce URL Patterns

- **Dashboard**: `{{SALESFORCE_BASE_URL}}/lightning/r/Dashboard/{dashboardId}/view`
- **Reports Folder**: `{{SALESFORCE_BASE_URL}}/lightning/o/Report/home?queryScope=everything`
- **Custom Fields**: `{{SALESFORCE_BASE_URL}}/lightning/setup/CustomFields/home?setupId={object}`
- **Permission Sets**: `{{SALESFORCE_BASE_URL}}/lightning/setup/PermSets/page?address={permSetId}`
- **Connected Apps**: `{{SALESFORCE_BASE_URL}}/lightning/setup/ConnectedApps/home`
- **Users**: `{{SALESFORCE_BASE_URL}}/lightning/setup/ManageUsers/page?address={userId}`

## n8n URL Patterns

- **Workflow**: `{{N8N_WORKFLOW_URL}}/workflow/{workflowId}`
- **Workflows List**: `{{N8N_WORKFLOW_URL}}/workflows`
- **Data Tables**: `{{N8N_WORKFLOW_URL}}/data-tables`

## Status Markers

Use these status tokens in demo guide:

- **READY**: Component deployed and tested, ready for demo
- **IN PROGRESS**: Component partially deployed, needs completion
- **NOT STARTED**: Component not yet deployed
- **BLOCKED**: Component blocked by dependency or issue

## Integration with Other Skills

### Add to `sync-internal` workflow

Run `update-demo-guide` after other sync operations to keep demo guide current.

### Add to `salesforce-deploy` skill

Run `update-demo-guide` after Salesforce deployments to update Salesforce URLs.

### Add to `n8n-build` skill

Run `update-demo-guide` after n8n builds to update workflow URLs.

### Standalone invocation

Run manually before demo preparation to ensure all links are accurate.

## Example Output

Updates demo guide sections like:

**Before:**

```
**Base URL**: `{{SALESFORCE_BASE_URL}}`
**Status**: {{SALESFORCE_STATUS}}
- **Custom fields**: 15 Contact + 1 Opportunity
- **Permission sets**: 5
```

**After:**

```
**Base URL**: `https://orgfarm-b7f2ea89fb-dev-ed.develop.lightning.force.com`
**Status**: Salesforce Dev org setup complete with AI Agent + n8n Integration users
- **Custom fields**: 15 Contact + 1 Opportunity (READY)
- **Permission sets**: 5 (READY)
```

## Error Handling

- If Salesforce CLI not authenticated, prompt user to run `sf org login`
- If n8n instance not accessible, prompt user to check credentials
- If component queries fail, mark status as UNKNOWN and continue
- If demo guide update fails, report error and preserve original file

## Best Practices

- Always verify URLs are accessible before marking as READY
- Test screenshot URLs in browser before adding to checklist
- Keep backup of demo guide before major updates
- Update activity log after successful demo guide update
- Commit updated demo guide and org-profile.json after changes (note: org profiles are gitignored — never commit real org data)
