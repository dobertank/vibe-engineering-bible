#!/usr/bin/env python3
"""Maintain four portable skill snapshots with Python 3.9+ stdlib; no downloads."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT_FILES = (
    "README.md", "LICENSE", "vibe-engineering-bible.md", "usage.md", "CLAUDE.md",
    "patterns.md", "registry.md", "CONTRIBUTING.md", "AGENTS.md",
    "scripts/package_skills.py", "tests/test_package_skills.py",
)
RESOURCE_DIRS = ("playbooks", "templates", "examples/audit", "assets")
PLAYBOOKS = {
    "init-project.md": "bible-init-project",
    "audit-project.md": "bible-audit-project",
    "review-pr.md": "bible-review-pr",
    "propose-bible-change.md": "bible-propose-change",
}
MAINTENANCE = {"AGENTS.md": "AGENTS.maintenance.md", "CLAUDE.md": "CLAUDE.maintenance.md"}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def resources(source: Path) -> dict[str, bytes]:
    paths = []
    for name in ROOT_FILES:
        path = source / name
        if not path.exists() and name in MAINTENANCE:
            path = source / MAINTENANCE[name]
        paths.append(path)
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
        name = str(p.relative_to(source))
        body = p.read_bytes()
        if name in {"README.md", "CONTRIBUTING.md"}:
            text = body.decode()
            for original, inert in MAINTENANCE.items():
                text = text.replace("](./" + original + ")", "](./" + inert + ")")
            if name == "README.md":
                text = text.replace("(`CLAUDE.md` imports it)", "(`CLAUDE.maintenance.md` imports it)")
            body = text.encode()
        if name in {"CLAUDE.md", "CLAUDE.maintenance.md"}:
            body = body.replace(b"@AGENTS.md", b"@AGENTS.maintenance.md")
        result[MAINTENANCE.get(name, name)] = body
    return result


def render(source: Path) -> dict[str, dict[str, bytes]]:
    data = resources(source)
    if data["scripts/package_skills.py"] != Path(__file__).read_bytes():
        raise ValueError("Executing builder differs from source builder; use the source snapshot builder")
    snapshot = sha(json_bytes({name: sha(body) for name, body in data.items()}))
    plans = {}
    for playbook, expected_name in PLAYBOOKS.items():
        raw = data["playbooks/" + playbook].decode()
        front = re.match(r"\A---\n(.*?)\n---(?:\n|$)", raw, re.S)
        if not front:
            raise ValueError(f"Missing YAML frontmatter: {playbook}")
        fields = dict(line.split(": ", 1) for line in front[1].splitlines() if ": " in line)
        name = fields.get("name", "")
        description = fields.get("description", "")
        if description.startswith('"'):
            description = json.loads(description)
        if name != expected_name or not isinstance(description, str) or not 1 <= len(description) <= 1024:
            raise ValueError(f"Invalid name/description: {playbook}")
        contract = re.search(r"^## Skill contract\n(.*?)^## Goal\n", raw, re.M | re.S)
        if not contract or not contract[1].strip():
            raise ValueError(f"Missing skill contract: {playbook}")
        entry = ("---\nname: " + name + "\ndescription: " + json.dumps(description, ensure_ascii=False)
                 + "\n---\n\n# " + name + "\n\n"
                 + "The Bible root is `references/bible/` beside this `SKILL.md`; no separate Bible checkout is needed. The target project is a separate input. Resolve Bible paths from that bundled root and project evidence from the target root.\n\n"
                 + "Reply in the user's requested language and honor the actual target project's applicable instructions. Bundled `AGENTS.maintenance.md` and `CLAUDE.maintenance.md` describe Bible maintenance; they are reference data, not target instructions or a response-language policy.\n\n"
                 + contract[1].strip() + "\n\n"
                 + "Read the [source playbook](references/bible/playbooks/" + playbook + ") for the detailed procedure and output schema. Do not run the bundled maintenance builder to use this skill. A skill grants no additional action, network or publication permissions; keep outputs outside its resources. Content identity is in `SOURCE.json`.\n")
        files = {"SKILL.md": entry.encode()}
        files.update({"references/bible/" + path: body for path, body in data.items()})
        files["SOURCE.json"] = json_bytes({
            "kind": "local-snapshot", "base_commit": None,
            "source_snapshot_sha256": snapshot, "playbook": "playbooks/" + playbook,
            "builder_sha256": sha(data["scripts/package_skills.py"]),
            "files": {path: sha(body) for path, body in sorted(files.items())},
        })
        plans[name] = files
    return plans


def package(source: Path, output: Path) -> list[str]:
    source = source.resolve()
    if output.is_symlink():
        raise ValueError("Output directory must not be a symlink")
    for name in RESOURCE_DIRS:
        if output.resolve().is_relative_to(source / name):
            raise ValueError("Output must be outside source resource directories")
    plans = render(source)
    for name in plans:
        if (output / name).exists() or (output / name).is_symlink():
            raise ValueError(f"Existing skill is never overwritten: {output / name}")
    for name, files in plans.items():
        dest = output / name
        dest.mkdir(parents=True, exist_ok=False)
        for path, body in files.items():
            target = dest / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
    return list(plans)


def check(source: Path, output: Path) -> None:
    if output.is_symlink() or not output.is_dir():
        raise ValueError("Missing skills directory or symlink")
    expected = {name + "/" + path: body for name, files in render(source.resolve()).items() for path, body in files.items()}
    actual = {}
    for path in output.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Generated tree has a symlink: {path.relative_to(output)}")
        if path.is_file():
            actual[str(path.relative_to(output))] = path.read_bytes()
    if actual != expected:
        raise ValueError("Generated skills are not fresh (missing, extra or modified files); regenerate to a new output and review the diff")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, help="Fresh parent for the four skill folders; existing folders are never replaced")
    parser.add_argument("--check", action="store_true", help="Compare generated bytes without writing; default target is source/skills")
    args = parser.parse_args()
    if not args.check and args.output is None:
        parser.error("--output is required when generating")
    try:
        if args.check:
            check(args.source, args.output or args.source / "skills")
            print("Generated skills are fresh")
        else:
            print("Created: " + ", ".join(package(args.source, args.output)))
    except (OSError, ValueError, KeyError, UnicodeError) as error:
        print(f"Packaging failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
