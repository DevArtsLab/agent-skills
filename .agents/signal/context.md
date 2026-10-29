# Project context

- Updated: 2026-10-28
- Repository or folder: DevArtsLab/agent-skills
- Visibility: public
- Context confidence: verified

## Purpose

DevArts Lab's shared source library of agent skills for coding assistants and
automation tools. The repository is the maintained source; provider-specific
skill directories are installed or synchronized copies.

## Current state

The repository contains 25 `SKILL.md` files across the `skills/` library.
The README documents installation with `npx skills add DevArtsLab/agent-skills`
and subsequent distribution through the universal-ai-config sync workflow.

## Technology and architecture

- Markdown skill packages organized by skill directory.
- Each skill directory contains a `SKILL.md` with frontmatter and instructions;
  folder name and frontmatter `name` must match.
- Optional `references/` and `scripts/` directories hold supporting material.
- Licensed under MIT.

## Key locations

- `skills/`: maintained skill definitions and references.
- `README.md`: installation, editing, synchronization, and catalog overview.
- `LICENSE`: MIT terms.

## Verified work and outcomes

- The library covers career knowledge, code review, reference checks, Linear,
  integrations, synchronization, publishing, and other DevArts Lab workflows.
- The documented edit loop updates this repository first, then reinstalls and
  synchronizes skills to local assistant providers.

## Open work and constraints

- Installed provider copies can drift; use the documented synchronization
  workflow to compare or refresh them.
- Do not edit installed copies as the durable source because reinstalling can
  overwrite those changes.

## Sources

- https://github.com/DevArtsLab/agent-skills
- `README.md`
- `LICENSE`
- `skills/`
