---
name: code-review
description: Pre-push code review and security gate. Run before every git push, pull request, or commit to a shared repo, and whenever the user asks to review changes, check security, or mentions Dependabot, leaked secrets, or security bots.
allowed-tools:
  - read
  - grep
  - glob
  - exec
---

<!-- author: Amir Olyaei | DevArts Lab | last_updated: 2026-10-16 -->

# DevArts Lab code review and pre-push security gate

Always run this review before any `git push` or PR creation (`/review` in any
session maps to this flow). The goal is to catch what GitHub Dependabot,
secret scanners, and security bots would flag, before it leaves the machine.

## 1. Diff review

1. Run `git status` and `git diff --staged` (or `git diff` if nothing is
   staged). Include untracked files that will be committed.
2. Check for logic errors or bugs, missing error handling at real boundaries,
   security issues, and style inconsistencies with surrounding code.
3. Flag files that should not be committed: `.env*`, `*.pem`, `*.key`,
   credentials, logs with tokens, OS junk (`.DS_Store`), local caches, and
   dated report/log files that must not be rewritten.

## 2. Secret scan (hard gate)

Scan the staged diff and any new commits since the upstream branch
(`git log origin/HEAD..HEAD -p`) for credential patterns:

- Cloud/SCM tokens: `ghp_`, `gho_`, `ghu_`, `ghs_`, `ghr_`, `github_pat_`,
  `glpat-`, `AKIA[0-9A-Z]{16}`, `xox[baprs]-`
- Provider keys: `sk_live_`, `rk_live_`, `sk_test_`, `rk_test_`, `sk-ant-`,
  `sk-proj-`, `AIza[0-9A-Za-z_-]{35}`, `-----BEGIN [A-Z ]*PRIVATE KEY-----`
- Generic: `password|secret|token|api[_-]?key` assigned to a quoted literal
  (exclude placeholders like `"..."`, `"<...>"`, `"YOUR_..."`, env lookups)

A live secret anywhere in the diff or unpushed history is a **blocker**: do
not push. Remove it from files and history, rotate the credential, and tell
the user. If a secret was already pushed to a remote, say so immediately:
treat it as compromised and rotate it.

## 3. Dependency and Dependabot check

- Audit manifests that changed or when pushing project work:
  `npm audit` / `pnpm audit` / `pip-audit` / `cargo audit` as applicable.
- Check open Dependabot alerts before pushing to GitHub:
  `gh api repos/{owner}/{repo}/dependabot/alerts --jq '.[] | select(.state=="open")'`
- Prefer minimal fixes that keep the current major version (npm `overrides`,
  targeted bumps). Never `--force` a breaking upgrade without asking.
- Keep lockfiles regenerated and consistent; do not hand-edit resolved
  entries.

## 4. Repo hygiene and bot-flag risks

- `.gitignore` covers env files, keys, build output, caches, and OS junk.
- No secrets vault content, OAuth tokens, or PII in committed data files.
- Large or generated blobs reviewed before commit (size, provenance).
- License, SECURITY.md, and repo metadata consistent with the repo's purpose
  when creating or renaming repos.

## 5. Verdict

- **Block** the push on: live secrets, known-compromised creds, or the user's
  explicit hold. Report exactly what and where.
- **Warn, then proceed**: fixable vulns with an available patch (offer the
  fix), style issues, missing tests.
- Summarize findings in a short table: severity, file:line, issue, fix.
