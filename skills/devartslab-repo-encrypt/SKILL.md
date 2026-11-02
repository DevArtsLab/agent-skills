---
name: devartslab-repo-encrypt
description: Set up git-crypt encryption for a DevArts Lab repo so file contents are ciphertext on GitHub. Use whenever the user asks to encrypt a repo, add a vault, protect PII or private content before pushing, match another repo's security level, mentions git-crypt, a .git-crypt.key file, or unlocking an encrypted clone.
---

<!-- author: Amir Olyaei | DevArts Lab | created: 2026-11-02 | last_updated: 2026-11-02 -->

# Repo encryption via git-crypt

Lab pattern: git-crypt encrypts file contents at rest in git. Paths and
filenames stay visible on GitHub; only blob contents are ciphertext.
Plaintext exists only in unlocked working trees.

## Keys

Keys live in the lab key store. Never write the store location into this
skill, docs, or any file that can reach a public repo: agent-skills is
public on GitHub. Ask the user for the key path, or read it from the
unlock instructions in the target repo's vault README (e.g.
devarts-business `vault/README.md` points at the team password manager).
Naming convention: `<repo>.git-crypt.key`.

Two modes:

- Shared key (default for single-owner lab repos):
  `git-crypt unlock <key-path>/<existing>.git-crypt.key`
  Installs the existing key and filter config; no `git-crypt init` needed.
  Trade-off: one key compromise or rotation spans every repo sharing it.
- Per-repo key: `git-crypt init`, then
  `git-crypt export-key <key-path>/<repo>.git-crypt.key`.
  Use when the repo may get collaborators or a different trust boundary.

## Scope patterns

Pick one, then write `.gitattributes` at repo root.

Encrypted subtree (public docs stay readable; used by devarts-business):

```gitattributes
vault/** filter=git-crypt diff=git-crypt merge=git-crypt
```

Encrypt everything except an allowlist (PII-heavy repos; used by career-dev):

```gitattributes
* filter=git-crypt diff=git-crypt merge=git-crypt
.gitattributes -filter -diff -merge
.gitignore -filter -diff -merge
AGENTS.md -filter -diff -merge
.agents/** -filter -diff -merge
```

`.gitattributes`, `.gitignore`, and anything agents or GitHub must read
unencrypted must stay on the allowlist. Keep tracked filenames free of
sensitive details: names are never encrypted.

## Verify

```bash
git-crypt status | sort | uniq -c
git-crypt status | grep "not encrypted"
```

Second line must list allowlisted files only.

`*** WARNING: staged/committed version is NOT ENCRYPTED ***` means the
blob in history is still plaintext: expected until re-staged. After
`git add`, warnings must be gone before committing.

## Re-encrypt already-tracked files

`.gitattributes` alone does not convert blobs already committed; only
new writes get encrypted. Re-run the clean filter across the full tree:

```bash
git add --renormalize .
git-crypt status | grep WARNING
git commit -m "Re-encrypt tracked files under git-crypt"
git push
```

WARNING output must be empty before committing.

One commit converts every tracked file. Old commits keep plaintext; see
below.

## Existing plaintext history

git-crypt only encrypts new blobs. Any history already pushed stays
readable on the remote. Options:

- Orphan squash + force-push:

  ```bash
  git checkout --orphan clean-main
  git add -A
  git-crypt status | grep WARNING
  git commit -m "Reinitialize with git-crypt encryption"
  git branch -D main && git branch -m main
  git push --force origin main
  ```

  WARNING output must be empty before committing.

- Zero retention: delete and recreate the GitHub repo. Force-push leaves
  unreachable objects until GitHub GC; recreate only if old content was
  genuinely sensitive and repo has no stars/PRs/issues to lose.

`git filter-repo` alone does not help: it rewrites hashes but keeps blob
content as-is, so plaintext survives the rewrite.

Commit policy: the user runs all stage/commit/push commands. Prepare
`.gitattributes`, run unlock, verify status, then hand the user the exact
command block above.

## Unlock on a new clone

```bash
brew install git-crypt
git-crypt unlock <key-path>/<repo>.git-crypt.key
```

## Gotchas

- Untracked/ignored dirs (`.remember/`, `config/`) are unaffected; check
  `.gitignore` covers local-only PII dirs before trusting coverage.
- `.obsidian/` churn inside an encrypted vault is fine to encrypt; ignore
  per-device files (`workspace.json`, `cache/`, `.trash/`) via `.gitignore`.
- Symlinks under encrypted patterns encrypt the link blob, which breaks
  the link in locked clones; keep skill/provider symlink dirs on the
  allowlist.
- Paste command blocks line by line: a trailing `# comment` on the same
  line becomes an argument (`git add --renormalize . # note` fails with
  `pathspec '#' did not match`), and later commands then run against a
  stale index.
