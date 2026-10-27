---
name: devartslab-readme-badges
description: Catalog of README badges (shields.io, CI, coverage, registry, social) for GitHub repositories. Use whenever the user asks what badges to add to a repo, wants to polish a README, mentions shields.io, or asks for license, language, build, version, or status badges, even if they only say "add badges" without naming a type.
---

Help the user pick and insert README badges that are true for their repo. The full badge catalog lives in `references/badges.md` - read it when you need snippet options beyond the common set below.

## Workflow

1. **Detect repo facts before suggesting badges.** Never suggest a badge that claims something untrue. Check for:
   - `LICENSE` file -> license badge (MIT, Apache-2.0, etc.)
   - Primary language(s) -> language/version badge
   - `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod` -> registry badges (npm, PyPI, crates.io) if published
   - `.github/workflows/*.yml` -> CI status badge; get the workflow file name for the URL
   - `codecov.yml`, `.coveralls.yml`, coverage config -> coverage badge
   - Docker / deploy targets -> platform badges
   - `git remote -v` -> the real `owner/repo` slug for dynamic badge URLs (badge URLs are case-sensitive on some services; copy the slug exactly)

2. **Suggest a small set, not the whole catalog.** Badges are claims; a row of 15 badges where half are noise reads worse than 4 honest ones. Default suggestion set:
   - License (if a LICENSE file exists)
   - Primary language/runtime version
   - CI status (only if workflows actually exist)
   - One distinguishing trait (zero dependencies, platform, maintained, etc.)

3. **Emit ready-to-paste markdown.** One badge per line, image wrapped in a link:

   ```markdown
   [![License: MIT](https://img.shields.io/github/license/OWNER/REPO)](LICENSE)
   ```

4. **Placement.** Default is a badge row directly under the H1 title, before the intro paragraph. If the README already has a badge section, match it. Ask before moving existing badges.

5. **Style consistency.** If the README already uses a style (`?style=flat-square`, `for-the-badge`, `social`), apply the same style to new badges.

## Common badges (copy-paste, replace OWNER/REPO)

```markdown
[![License](https://img.shields.io/github/license/OWNER/REPO)](LICENSE)
[![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/REPO/actions)
[![Release](https://img.shields.io/github/v/release/OWNER/REPO)](https://github.com/OWNER/REPO/releases)
[![Last commit](https://img.shields.io/github/last-commit/OWNER/REPO)](https://github.com/OWNER/REPO/commits)
```

For the full catalog (npm/PyPI/Docker versions, coverage, code quality, security, social, fun badges, shields.io style parameters), read `references/badges.md`.

## Notes

- Dynamic shields.io badges (`github/license`, `github/last-commit`, ...) only work on public repos. For private repos use static badges: `https://img.shields.io/badge/license-MIT-blue`.
- Static badge syntax: `https://img.shields.io/badge/LEFT-RIGHT-COLOR` where LEFT/RIGHT are the two text segments. Escape spaces as `%20` or use `_`.
- Prefer linking badges somewhere useful (LICENSE file, Actions page, registry page) rather than leaving them unlinked.
