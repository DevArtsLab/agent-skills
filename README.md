# agent-skills

**DevArts Lab's agent skill library. One repo, every agent, always current.**

Agent skills for AI coding assistants (Claude, Cursor, Copilot, Devin,
Windsurf, and any tool that reads `SKILL.md`). Source of truth for the
DevArts Lab skill set - local skill dirs are installed copies, not working
copies.

## Install

```bash
npx skills add DevArtsLab/agent-skills
```

Installs into `~/.agents/skills/`. From there,
[universal-ai-config](https://github.com/DevArtsLab/tool-universal-ai-config)
(`ai-config sync`) distributes to provider skill dirs
(`~/.claude/skills`, `~/.cursor/skills`, `~/.copilot/skills`,
`~/.config/devin/skills`, `~/.windsurf/skills`) and tracks content hashes,
origins, and drift in `~/.agents/.ai-config-lock.json`.

## Edit loop

1. Edit skills **in this repo**, not in `~/.agents/skills` (installed copies
   are overwritten on reinstall).
2. Commit + push.
3. `npx skills add DevArtsLab/agent-skills` on each machine refreshes the
   installed copies.
4. `ai-config sync` pushes them to provider dirs; `ai-config status` shows
   per-provider sync state and flags locally edited copies as drifted.

## Skills

| Skill | What it does |
| ----- | ------------ |
| `career-knowledge-bank` | Convert historical career information from multiple sources into a single interconnected career knowledge bank |
| `check-references` | Check cross-references and semantic consistency between roadmap documents |
| `code-review` | Pre-push code review and security gate. Run before every git push, pull request, or commit |
| `cv-compiler` | Convert historical career information into a single interconnected career content bank |
| `distribution-checklist` | Evaluate a finished tool/app for distribution formats and open-source readiness |
| `figma-figjam-sync` | Sync a source diagram in the IDE to an editable FigJam board via the Figma MCP |
| `linear` | Work with Linear via the linear-mcp-server MCP tools |
| `linear-research-refine` | Run one bounded refinement pass on a living Linear research ticket |
| `n8n-build` | Build n8n workflows for a target org and environment |
| `org-context` | Resolve and display the active organization and consultant context |
| `org-new` | Onboard a new partner organization (scaffold org tree, validate, first build) |
| `pnpm-fleet` | Enforce DevArts Lab pnpm fleet policy across repos via tool-pnpm-fleet |
| `readme-badges` | Catalog of README badges for GitHub repositories |
| `salesforce-deploy` | Deploy Salesforce metadata to a target org with certificate restoration |
| `scrapy-resources` | Building, refactoring, or debugging Scrapy spiders for city-scrapers projects |
| `sync-all` | Master sync - run all document update chains in order |
| `sync-external` | Push validated docs to external systems (Figma, etc.) |
| `sync-internal` | Update repo documentation without external pushes |
| `sync-templates` | Render org-specific docs from templates |
| `update-activity-log` | Update NGO activity log with new project activities |
| `update-demo-guide` | Update demo guide with accurate access links and deployment status |
| `update-index` | Regenerate REPO_INDEX.md after adding/removing/changing repo content |
| `update-memory` | Update MEMORY.md with distilled facts from source documents |
| `upgrade-stripe` | Guide for upgrading Stripe API versions and SDKs |
| `review` | Alias for code-review |

## Layout

```text
skills/
  <skill-name>/
    SKILL.md          # frontmatter (name, description) + instructions
    references/       # optional companion docs loaded on demand
    scripts/          # optional helper scripts
```

The folder name must match the `name:` field in `SKILL.md` frontmatter -
mismatched names do not load.

## License

MIT - see [LICENSE](LICENSE).
