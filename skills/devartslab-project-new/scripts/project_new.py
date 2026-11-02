#!/usr/bin/env python3
"""Scaffold a new project via copier + workspace store wiring.

Dry-run by default: prints the plan and writes nothing.
Pass --apply to write.

Usage:
  project_new.py --slug <slug> [--identity NAME|PATH] [--secrets a,b,c]
                 [--blueprint PATH|URL] [--dest DIR] [--root DIR] [--apply]
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

SLUG_RE = re.compile(r"^[a-z][a-z0-9-]{1,38}[a-z0-9]$")
RESERVED = {"_template", "default", "example", "all", "projects", "private", "shared", "config"}
BLUEPRINT_NAME = "project-blueprint"


def die(msg):
    sys.exit(f"error: {msg}")


def resolve_root(start):
    for var in ("WORKSPACE_HOME", "DEVARTSLAB_HOME"):
        env = os.environ.get(var)
        if env:
            p = Path(env).expanduser()
            if (p / ".workspace.json").is_file():
                return p
            die(f"{var}={p} has no .workspace.json")
    p = Path(start).resolve()
    for cand in [p, *p.parents]:
        if (cand / ".workspace.json").is_file():
            return cand
    die("no .workspace.json found upward from cwd; set WORKSPACE_HOME or pass --root")


def flatten_identity(manifest, schema):
    """Walk identity.schema.json; emit flat {copier_var: value} for keys
    annotated x-copier-var that are present in the manifest."""
    flat = {}

    def walk(props, node):
        for key, spec in props.items():
            if not isinstance(node, dict) or key not in node:
                continue
            var = spec.get("x-copier-var")
            if var is not None:
                flat[var] = node[key]  # None is kept: overrides marker defaults
            if spec.get("type") == "object":
                walk(spec.get("properties", {}), node[key])

    walk(schema.get("properties", {}), manifest)
    return flat


def load_identity(arg, store_root):
    id_dir = store_root / "identity"
    schema_path = id_dir / "identity.schema.json"
    if not schema_path.is_file():
        die(f"identity schema missing: {schema_path}")
    schema = json.loads(schema_path.read_text())

    def load(p):
        return p, flatten_identity(json.loads(p.read_text()), schema)

    if arg:
        p = Path(arg).expanduser()
        if p.suffix != ".json":
            p = id_dir / f"{p.stem}.json"
        if not p.is_file():
            die(f"identity manifest not found: {p}")
        return load(p)
    manifests = sorted(m for m in id_dir.glob("*.json") if not m.name.endswith(".schema.json"))
    if len(manifests) == 1:
        return load(manifests[0])
    if not manifests:
        die(f"no identity manifests in {id_dir}; pass --identity after creating one")
    die(f"multiple identity manifests; pick one: {[m.stem for m in manifests]}")


def blueprint_source(arg, manifest):
    if arg:
        return arg
    name = manifest.get("blueprint_repo", BLUEPRINT_NAME)
    org = manifest.get("github_org")
    if org:
        return f"gh:{org}/{name}"
    sibling = Path.cwd().resolve().parent / name
    if sibling.is_dir():
        return str(sibling)
    die("no --blueprint, no github_org in manifest, no sibling blueprint dir")


def render_env_local(example_path, out_path):
    lines = ["# Rendered by project-new scaffold. Gitignored; regenerate on demand.\n",
             "# Values: fill from the workspace store, never commit.\n"]
    if example_path.is_file():
        for line in example_path.read_text().splitlines(keepends=True):
            m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)=.*$", line)
            lines.append(f"{m.group(1)}=\n" if m else line)
    out_path.write_text("".join(lines))


def retire(args, root, store_root, env_root, slug):
    """Inverse of scaffold: remove all slug-keyed artifacts.
    Repo dir and Linear issue are listed, never deleted."""
    store = store_root / "projects" / slug
    env_dir = env_root / "projects" / slug
    registry = store_root / "registry.json"
    removed = []
    for p in (store, env_dir):
        if p.exists():
            shutil.rmtree(p)
            removed.append(str(p))
    if registry.is_file():
        reg = json.loads(registry.read_text())
        before = len(reg.get("secrets", {}))
        reg["secrets"] = {k: v for k, v in reg.get("secrets", {}).items()
                          if v.get("owner") != f"projects/{slug}"}
        if len(reg["secrets"]) != before:
            registry.write_text(json.dumps(reg, indent=2) + "\n")
            removed.append(f"registry: {before - len(reg['secrets'])} entries")
    lab_index = root / "LAB_INDEX.md"
    if lab_index.is_file() and slug in lab_index.read_text():
        removed.append(f"LAB_INDEX.md contains '{slug}' rows: remove manually")
    print("removed:" if removed else "nothing found.")
    for r in removed:
        print(f"  {r}")
    repo = root / slug
    if repo.exists():
        print(f"manual: repo dir not touched: {repo}")
    print("manual: close the tracking issue in Linear")


def plan_and_apply(args):
    root = Path(args.root).expanduser() if args.root else resolve_root(Path.cwd())
    marker_path = root / ".workspace.json"
    if not marker_path.is_file():
        die(f"no .workspace.json at {root}")

    slug = args.slug
    if not SLUG_RE.match(slug) or slug in RESERVED:
        die(f"invalid slug '{slug}' (pattern {SLUG_RE.pattern}; reserved: {sorted(RESERVED)})")

    marker = json.loads(marker_path.read_text())
    entities = marker.get("entities", ["projects"])
    if "projects" not in entities:
        die(f".workspace.json entities {entities} has no 'projects' type")
    store_root = root / marker.get("store", "config")
    env_root = root / marker.get("env", "config/env")

    if args.retire:
        store = store_root / "projects" / slug
        env_dir = env_root / "projects" / slug
        print("RETIRE PLAN" if not args.apply else "RETIRING")
        print(f"  remove store dirs  -> {store}/")
        print(f"  remove env dir     -> {env_dir}/")
        print(f"  prune registry     -> owner=projects/{slug} entries")
        print("  manual only        -> repo dir, LAB_INDEX rows, Linear issue")
        if not args.apply:
            print("\ndry-run. rerun with --apply to execute.")
            return
        retire(args, root, store_root, env_root, slug)
        return

    dest = Path(args.dest).expanduser() if args.dest else root / slug
    if dest.exists() and any(dest.iterdir()):
        die(f"destination exists and is not empty: {dest}")

    secrets = [s.strip() for s in args.secrets.split(",") if s.strip()] if args.secrets else []
    for s in secrets:
        if not re.match(r"^[a-z0-9][a-z0-9_-]*/[a-z0-9][a-z0-9_-]*/[A-Za-z_][A-Za-z0-9_]*$", s):
            die(f"secret id '{s}' must match <platform>/<env>/<NAME>")

    id_path, manifest = load_identity(args.identity, store_root)
    # governance defaults from the marker; manifest workspace overrides win;
    # explicit null removes the feature
    manifest = {k: v for k, v in
                {**marker.get("governance", {}), **manifest}.items()
                if v is not None}
    src = blueprint_source(args.blueprint, manifest)

    store = store_root / "projects" / slug
    env_dir = env_root / "projects" / slug
    registry = store_root / "registry.json"

    steps = [
        f"copier copy         -> {src} -> {dest}",
        f"identity manifest    -> {id_path.name} ({manifest.get('org_name', '?')})",
        f"project.json         -> slug + {len(secrets)} secret ids (rendered by copier)",
        f"create store dirs    -> {store}/{{secrets,config,data}}",
        f"create env dir       -> {env_dir}/",
        f"render .env.local    -> {env_dir}/.env.local (key names only)",
        f"update registry      -> {registry} ({len(secrets)} entries)",
        "git init             -> new repo (no commits)",
    ]
    print("PLAN" if not args.apply else "APPLYING")
    for s in steps:
        print(f"  {s}")
    if not args.apply:
        print("\ndry-run. rerun with --apply to write.")
        return

    answers = dict(manifest)
    answers.update({"slug": slug, "secrets": secrets})
    with tempfile.TemporaryDirectory() as tmp:
        data_file = Path(tmp) / "answers.json"
        data_file.write_text(json.dumps(answers))
        r = subprocess.run(
            ["copier", "copy", "--data-file", str(data_file), "--defaults",
             str(src), str(dest)],
            capture_output=True, text=True)
        if r.returncode != 0:
            die(f"copier failed: {r.stderr.strip() or r.stdout.strip()}")

    for d in ("secrets", "config", "data"):
        (store / d).mkdir(parents=True, exist_ok=True)
    env_dir.mkdir(parents=True, exist_ok=True)
    render_env_local(dest / ".dev.vars.example", env_dir / ".env.local")

    reg = json.loads(registry.read_text()) if registry.is_file() else {"schema": 1, "secrets": {}}
    for s in secrets:
        reg.setdefault("secrets", {}).setdefault(s, {
            "owner": f"projects/{slug}",
            "consumers": [f"projects/{slug}"],
            "registered": str(date.today()),
        })
    registry.write_text(json.dumps(reg, indent=2) + "\n")

    if not (dest / ".git").exists():
        subprocess.run(["git", "init", "-q"], cwd=dest, check=True)

    print(f"\ndone: {dest}")
    print("next:")
    print(f"  1. fill secret values in {store}/secrets/ and {env_dir}/.env.local")
    print("  2. blueprint evolves -> rerun: copier update <dest>")
    print("  3. regenerate indexes: run the update-index skill, then the lab index")
    print("  4. create a tracking issue for the project; commit yourself (agents do not commit)")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--identity", help="manifest name or path; default: sole file in <store>/identity/")
    ap.add_argument("--secrets", default="", help="comma list: <platform>/<env>/<NAME>")
    ap.add_argument("--blueprint", help="copier source: path, URL, or gh:org/repo; default from manifest")
    ap.add_argument("--dest", help="default: <workspace-root>/<slug>")
    ap.add_argument("--root", help="workspace root; default: resolve via .workspace.json")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--retire", action="store_true", help="inverse of scaffold: remove slug-keyed artifacts")
    args = ap.parse_args()
    plan_and_apply(args)


if __name__ == "__main__":
    main()
