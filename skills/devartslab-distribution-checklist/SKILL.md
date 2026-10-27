---
name: devartslab-distribution-checklist
description: Evaluate a finished tool/app for distribution formats (package, binary, MCP, skill, extension, etc.) and open-source readiness. Run whenever a repo or tool is complete and the question is "what's next for distribution/scaling/reuse?"
---

<!-- author: Amir Olyaei | DevArts Lab | last_updated: 2026-10-10 -->

Use this after any tool, app, or repo is finished (or merged/released) to produce a
concrete distribution and open-source recommendation instead of re-deriving the
options each time. Works for CLI tools, libraries, web apps, agents, and scripts.

## Step 1: Profile the artifact

Answer these first — they decide which formats even apply:

- **Type**: CLI tool / library / web app / agent script / one-file script?
- **Language + runtime**: Python, Node, Go, shell? Single file or multi-module?
- **External requirements**: needs a CLI (`gh`, `aws`, `docker`), a token, a
  service, a display, a browser? Anything that can't ship inside a package
  limits "standalone" claims.
- **Interaction model**: interactive TUI/prompts vs. batch/flag-driven vs.
  API-callable? Interactive flows do NOT port to MCP/GitHub Apps/agents cleanly.
- **Auth model**: user-supplied credentials (gh auth, env vars) vs. needing its
  own OAuth/app identity? The latter is what actually justifies a GitHub App.
- **Mutation surface**: read-only vs. writes/deletes? Writes raise the bar for
  agent-facing formats (MCP, skills) — keep a human-confirmation path.
- **Audience**: our org only, or general public? Internal tools may only need a
  skill + private package.

## Step 2: Distribution format checklist

For EACH option, mark it: **Build** / **Maybe later** / **Poor fit** — with a
one-line reason and rough effort. Do not recommend every option; kill the poor
fits explicitly.

| Format | Build it when | Skip when | Effort |
|---|---|---|---|
| **Remote-run one-liner** (`uv run <raw-url>`, `curl \| sh`, `npx`) | Script has inline deps or a fetchable installer; zero-install matters | Requires build step or secrets baked in | S |
| **Package registry** (PyPI/npm/brew/crates) | CLI or library others will run repeatedly; want `uvx`/`pipx`/`brew install` | Internal-only, or needs non-packageable services | M |
| **Standalone binary** (PyInstaller, pkg, goreleaser) | Users may lack the runtime AND deps are self-contained | It still needs external CLIs/tokens (only half-standalone) | M |
| **Agent skill** (`.agents/skills/*/SKILL.md`) | Org uses AI agents; want agent sessions to invoke it | Tool is trivial or purely interactive | S |
| **MCP server** | Read-mostly ops agents should call programmatically; returns structured data | Core UX is an interactive prompt flow; or heavy mutation needs human-in-loop UI | M-L |
| **GitHub App / OAuth app** | Needs its own identity, webhooks, or acts on users' behalf unattended | It's a local CLI using the user's existing auth | L |
| **IDE extension** | Value is editor-context-aware (linting, inline actions) | It wraps a terminal command — thin wrapper, low value | L |
| **CI Action / reusable workflow** | Runs per-repo or per-PR inside pipelines; token scope fits the job | Scope is account/org-level (GITHUB_TOKEN sees only its repo) | M |
| **Browser extension / plugin** | Extends a host app users already live in | Standalone usage is the norm | L |
| **Docker image** | Reproducible env with many system deps, or server component | Single-script tools — image adds overhead | M |
| **Library/SDK** (importable) | Other code should call its logic, not just its CLI | Logic is thin CLI glue; not worth an API surface | M |
| **Dockerized agent / cloud agent** | Should run unattended on a schedule | Needs interactive confirmation for mutations | M-L |

Effort legend: S < 1 hour, M = hours, L = days.

## Step 3: Open-source readiness checklist

Run only if the repo is or should be public. Check and report gaps:

- [ ] LICENSE file present (pick one — MIT/Apache-2.0 for tools)
- [ ] README: what it does, requirements, install, quickstart, safety model
- [ ] Repo About section: description + topics set (`gh repo edit`)
- [ ] No PII/credentials/local paths hardcoded — grep for secrets, emails, `/Users/`
- [ ] Tagged release with changelog (`gh release create`)
- [ ] Security issues triaged (Dependabot/code-scanning/issue reports addressed)
- [ ] Contribution path: CONTRIBUTING.md, issue templates (optional for small tools)
- [ ] Tests exist and run command is documented
- [ ] Compatible lint/format commands documented (e.g. `isort --profile black`)

## Step 4: Output format

Produce a short report, then let the user pick what to build:

```
## Distribution assessment: <tool>

Profile: <type, runtime, external reqs, interaction model, auth, audience>

Build now:
- <format> — <why> (~effort)

Maybe later:
- <format> — <what would make it worthwhile>

Poor fit:
- <format> — <why not>

Open-source gaps: <list or "none">

Recommended order: 1) ... 2) ...
```

## Rules

- Always recommend the CHEAPEST high-value option first; kill poor fits with reasons.
- A PEP 723 single-file Python script already supports `uv run <raw-url>` — verify and
  document before building real packaging.
- Never recommend formats that silently drop the tool's safety properties
  (e.g. don't expose a mutating operation through MCP without a confirmation path).
- Don't build anything until the user picks from the checklist output.
