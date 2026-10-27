---
name: update-index
description: Regenerate REPO_INDEX.md after adding/removing/changing repo content
---

Run this whenever files or folders have been added, removed, renamed, or substantially
rewritten since `REPO_INDEX.md` was last updated.

1. Run `git rev-parse --show-toplevel` to locate the repo root, then read `REPO_INDEX.md` in full from that root.
2. List the top-level directory and any subdirectories that look new or changed since the
   index was last updated (compare against what's already documented in the index).
   - Use `list_dir` on the repo root, then drill into any folder not already described,
     or any folder whose item count changed.
3. For each new/changed file, skim just enough to write a one-line description (topic,
   purpose). Do NOT read entire large files (PDFs, spreadsheets, long docs) — a filename-based
   description is fine for reference material.
4. For versioned docs (`_v1`, `_v2`, `_v3`, ...), only update the "current version" pointer to
   the highest version number found; don't add a new row per version.
5. Update `REPO_INDEX.md`:
   - Add new rows/bullets for new content.
   - Remove rows for deleted content.
   - Update the "Last updated" date at the top to today's date (format: "YYYY-MM-DD at H:MM AM/PM EDT" per terminology guidelines).
6. Save the file. Do not create additional index files — `REPO_INDEX.md` is the single
   source of truth.
