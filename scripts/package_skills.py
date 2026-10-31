#!/usr/bin/env python3
"""Build relocatable local skill snapshots; no downloads or client configuration."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT_FILES = (
    "README.md", "LICENSE", "vibe-engineering-bible.md", "usage.md", "CLAUDE.md",
    "patterns.md", "registry.md", "CONTRIBUTING.md", "AGENTS.md",
    "scripts/package_skills.py", "tests/test_package_skills.py",
)
RESOURCE_DIRS = ("playbooks", "templates", "docs/adr", "examples/audit", "assets")
PLAYBOOKS = (
    "init-project.md", "audit-project.md", "review-pr.md", "propose-bible-change.md",
)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def resources(source: Path) -> dict[str, bytes]:
    paths = [source / name for name in ROOT_FILES]
    for name in RESOURCE_DIRS:
        directory = source / name
        if directory.is_symlink() or not directory.is_dir():
            raise ValueError(f"Missing directory or symlink: {name}")
        for p in sorted(directory.rglob("*")):
            if p.is_symlink():
                raise ValueError(f"Resource symlink is not packaged: {p.relative_to(source)}")
            if p.is_file() and not any(part.startswith(".") for part in p.relative_to(directory).parts):
                suffixes = {".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif"} if name == "assets" else {".md"}
                if p.suffix.lower() in suffixes:
                    paths.append(p)
    result = {}
    for p in sorted(paths):
        if p.is_symlink() or any(parent.is_symlink() for parent in p.parents if parent != source and source in parent.parents) or not p.is_file():
            raise ValueError(f"Missing resource or symlink: {p.relative_to(source)}")
        result[str(p.relative_to(source))] = p.read_bytes()
    return result


def package(source: Path, output: Path) -> list[str]:
    source = source.resolve()
    # A destination inside resources would become input on a later build.
    for name in RESOURCE_DIRS:
        if output.resolve().is_relative_to(source / name):
            raise ValueError("Output must be outside source resource directories")
    if output.is_symlink():
        raise ValueError("Output directory must not be a symlink")
    data = resources(source)
    try:
        top = subprocess.check_output(["git", "-C", str(source), "rev-parse", "--show-toplevel"], stderr=subprocess.DEVNULL, text=True).strip()
        base = subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], stderr=subprocess.DEVNULL, text=True).strip() if Path(top).resolve() == source else None
    except (subprocess.CalledProcessError, FileNotFoundError):
        base = None
    source_hash = sha(json_bytes({name: sha(body) for name, body in data.items()}))
    plans = {}
    for playbook in PLAYBOOKS:
        raw = data["playbooks/" + playbook].decode()
        front = re.match(r"\A---\n(.*?)\n---(?:\n|$)", raw, re.S)
        if not front:
            raise ValueError(f"Missing YAML frontmatter: {playbook}")
        name_match = re.search(r"^name: ([a-z0-9]+(?:-[a-z0-9]+)*)$", front[1], re.M)
        description = re.search(r"^description: (.+)$", front[1], re.M)
        if not name_match or not description or len(name_match[1]) > 64 or len(description[1]) > 1024:
            raise ValueError(f"Invalid name/description: {playbook}")
        name = name_match[1]
        if name in plans:
            raise ValueError(f"Duplicate skill: {name}")
        if (output / name).exists() or (output / name).is_symlink():
            raise ValueError(f"Existing skill is never overwritten: {output / name}")
        entry = ("---\n" + front[1] + "\n---\n\n"
                 + "# " + name + "\n\n"
                 + "Read the [source playbook](references/bible/playbooks/" + playbook + ") and follow it within the user's request.\n\n"
                 + "The Bible root is `references/bible/` next to this `SKILL.md`. Resolve canon, template and playbook paths from that root; the target project path is a separate input. Read the sections and resources the playbook needs.\n\n"
                 + "Create output files only in the project or destination named by the user, outside skill resources. This skill grants no additional permission for external actions or environment changes. File versions and hashes are in `SOURCE.json`.\n")
        files = {"SKILL.md": entry.encode()}
        files.update({"references/bible/" + path: body for path, body in data.items()})
        manifest = {"kind": "local-snapshot", "base_commit": base,
                    "source_snapshot_sha256": source_hash, "playbook": "playbooks/" + playbook,
                    "builder_sha256": sha(Path(__file__).read_bytes()),
                    "files": {path: sha(body) for path, body in sorted(files.items())}}
        files["SOURCE.json"] = json_bytes(manifest)
        plans[name] = files
    # Validate every dependency/name/collision before writing any package.
    for name, files in plans.items():
        dest = output / name
        dest.mkdir(parents=True, exist_ok=False)
        for path, body in files.items():
            target = dest / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
    return list(plans)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1], help="Bible checkout or unpacked source snapshot")
    parser.add_argument("--output", type=Path, required=True, help="Parent directory for the four new skill folders; existing skills are never replaced")
    args = parser.parse_args()
    try:
        names = package(args.source, args.output)
    except (OSError, ValueError, KeyError, UnicodeError) as error:
        print(f"Packaging failed: {error}", file=sys.stderr)
        return 1
    print("Created: " + ", ".join(names))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
