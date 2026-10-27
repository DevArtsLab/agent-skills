---
name: devartslab-salesforce-deploy
description: Deploy Salesforce metadata to a target org with certificate restoration
---

Run this to deploy Salesforce metadata to a target org with proper certificate handling. All org-specific Salesforce config (JWT keys, org alias, scratch def) lives in the org tree at `shared/config/orgs/<slug>/salesforce/`.

## What this does

1. Resolves the active org context (via `--org`, `ORG_CONTEXT` env, or active-org file).
2. Restores the Connected App certificate from the example template
3. Loads the org's JWT key pair from `shared/config/orgs/<slug>/salesforce/n8n-jwt.{key,crt}`
4. Validates certificate format before deployment
5. Deploys Salesforce metadata to the target org (alias from `shared/config/orgs/<slug>/salesforce/sf-org.json`)
6. Handles Connected App consumer key retrieval and storage
7. Cleans up sensitive data from source files after deployment

## When to run this

- When deploying to a new Salesforce org for a partner
- After regenerating certificates for security reasons
- When setting up the n8n integration for the first time for an org
- After updating Connected App metadata
- When deploying custom field, layout, or Apex metadata changes to an existing org

## Source-backed metadata deployment (field/layout/Apex only)

For deploying custom fields, layouts, duplicate rules, or Apex classes/triggers **without** touching the Connected App certificate, use the source-deploy path directly:

```bash
cd "$(git rev-parse --show-toplevel)/salesforce"

# Deploy all metadata from source
sf project deploy start --source-dir force-app --target-org "$SF_ORG_ALIAS"

# Or deploy a specific component
sf project deploy start --source-dir force-app/main/default/objects/Contact/fields --target-org "$SF_ORG_ALIAS"

# Validate without deploying (dry run)
sf project deploy validate --source-dir force-app --target-org "$SF_ORG_ALIAS"
```

### What's in the source tree

```
force-app/main/default/
├── classes/
│   ├── Contact_Duplicate_Email_Test.cls          # Apex test class (6 tests, 100% pass)
│   └── Contact_Duplicate_Email_Test.cls-meta.xml
├── triggers/
│   ├── Contact_Duplicate_Email.trigger            # Before-insert/update email dedup
│   └── Contact_Duplicate_Email.trigger-meta.xml
├── objects/Contact/fields/
│   ├── At_Risk__c.field-meta.xml                  # 15 custom fields, all source-backed
│   ├── Engagement_Score__c.field-meta.xml
│   ├── Membership_Tier__c.field-meta.xml
│   ├── ... (12 more)
├── layouts/
│   └── Contact-Contact Layout.layout-meta.xml     # Layout with all 15 custom fields
├── duplicateRules/
│   └── Contact.Contact_Email_Duplicate_Rule.duplicateRule-meta.xml
└── connectedApps/                                 # gitignored — see certificate workflow below
```

### Why source-backed deployment matters

Deploying via `sf project deploy start` from `field-meta.xml` files **updates fields in place** — no delete/re-create cycle. This avoids the `_del`/`_del1`/`_del2` DeveloperName suffix problem that occurs when fields are created via the UI wizard or Tooling API insert and then deleted/recreated. The DeveloperName stays stable across deploys.

### package.xml

The `salesforce/package.xml` lists all deployable metadata types (CustomField, Layout, DuplicateRule, ApexTrigger, ApexClass). It's used for retrieve/deploy operations that reference the package manifest.

### destructiveChanges.xml

`salesforce/destructiveChanges.xml` lists fields to delete when a clean removal is needed. Use with:

```bash
sf project deploy start --metadata-manifest destructiveChanges.xml --target-org "$SF_ORG_ALIAS"
```

## How to run

1. **Resolve the org context and restore the Connected App certificate:**

```bash
cd "$(git rev-parse --show-toplevel)/salesforce"
# Source the org context to get SF_ORG_ALIAS, SF_CONFIG_DIR, etc.
eval "$(python3 ../scripts/org.py env --org iaboston)"
./scripts/restore-connected-app-cert.sh --org iaboston
```

Replace `iaboston` with the target org slug.

2. **Generate or obtain the org's certificate (NEVER reuse across orgs):**

```bash
# Each org gets its own JWT key pair in its org tree
openssl req -x509 -sha256 -nodes -days 1095 -newkey rsa:2048 \
  -keyout "$SF_CONFIG_DIR/n8n-jwt.key" \
  -out "$SF_CONFIG_DIR/n8n-jwt.crt" \
  -subj "/CN=<slug>-n8n-integration"

# Convert to base64 for the Connected App metadata
cat "$SF_CONFIG_DIR/n8n-jwt.crt" | base64 | tr -d '\n'
```

Or use the helper script:

```bash
./scripts/generate-jwt-cert.sh --org iaboston
```

3. **Update the Connected App metadata:**

Edit `force-app/main/default/connectedApps/NGO_n8n_Integration.connectedApp-meta.xml`:

- Replace `{{CERTIFICATE_BASE64}}` with the base64 certificate from step 2
- Replace `{{CONTACT_EMAIL}}` with the org's contact email

4. **Deploy to target org:**

```bash
sf project deploy start --source-dir force-app --target-org "$SF_ORG_ALIAS"
```

Or use the helper script:

```bash
./scripts/deploy.sh --org iaboston
```

5. **Retrieve and store the consumer key:**

```bash
sf project retrieve start --metadata ConnectedApp:NGO_n8n_Integration --target-org "$SF_ORG_ALIAS"
grep -o "<consumerKey>[^<]*" force-app/main/default/connectedApps/NGO_n8n_Integration.connectedApp-meta.xml
# Record the key in shared/config/orgs/<slug>/salesforce/sf-org.json
```

6. **Clean up sensitive data:**

```bash
# Remove consumer key from source file (git will track the cleaned version)
# The example file will be used as the template for future deployments
```

7. **Update demo guide with Salesforce URLs:**

Run `/update-demo-guide` to update the demo guide with accurate Salesforce component URLs and deployment status after the deployment.

## Security considerations

- **Never reuse certificates or JWT keys across orgs** — each org has its own key pair in `shared/config/orgs/<slug>/salesforce/`
- **Never commit real certificates** to git — the org tree is gitignored
- **Always rotate certificates** if they're ever exposed
- **Store the private key** (`n8n-jwt.key`) securely in the org tree, never commit it
- **The Connected App source file** is gitignored to prevent accidental commits

## Org context environment variables

The `org-context.sh` script exports:

- `SF_ORG_ALIAS` — Salesforce org alias from `sf-org.json`
- `SF_CONFIG_DIR` — path to the org's Salesforce config directory
- `ORG_SLUG` — the resolved org slug

## Dependencies

- Salesforce CLI (`sf`) installed and authenticated
- OpenSSL for certificate generation
- Valid org alias configured in `shared/config/orgs/<slug>/salesforce/sf-org.json`
- Example Connected App template: `force-app/main/default/connectedApps/NGO_n8n_Integration.connectedApp-meta.xml.example`

## Relationship to other workflows

- This skill complements the manual procedure in `salesforce/procedures/salesforce-n8n-connected-app.md`
- Certificate restoration script: `salesforce/scripts/restore-connected-app-cert.sh`
- Org context script: `salesforce/scripts/org-context.sh`
- Deploy script: `salesforce/scripts/deploy.sh`
- After deployment, use `/update-index` to document any changes

## Troubleshooting

- **Certificate format errors**: Ensure the base64 string has no line breaks
- **Deployment failures**: Check that the Connected App metadata is valid XML
- **Consumer key retrieval**: Ensure you have admin permissions on the target org
- **Auth failures**: Verify the integration user exists and has the correct permission sets
- **Wrong org**: Always pass `--org <slug>` or set `ORG_CONTEXT` to avoid deploying to the wrong org
