"""Run with python3 -m unittest discover -s tests -v (stdlib only)."""
import hashlib
import json
import re
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts/package_skills.py"
PLAYBOOKS = {
    "init-project.md": "bible-init-project",
    "audit-project.md": "bible-audit-project",
    "review-pr.md": "bible-review-pr",
    "propose-bible-change.md": "bible-propose-change",
}


class PackageSkillsTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)
        self.source = self.work / "source"
        self.source.mkdir()
        for rel in ["README.md", "LICENSE", "vibe-engineering-bible.md", "usage.md",
                    "patterns.md", "registry.md", "CLAUDE.md",
                    "CONTRIBUTING.md", "AGENTS.md"]:
            (self.source / rel).write_text("# Example\nSnapshot content: " + rel + "\n")
        for rel in ["playbooks", "templates", "examples/audit", "assets"]:
            (self.source / rel).mkdir(parents=True)
        for file, name in PLAYBOOKS.items():
            (self.source / "playbooks" / file).write_text(
                "---\nname: " + name + "\ndescription: Use when this workflow is requested.\n---\n\n# Workflow\n\n## Skill contract\nUse this workflow only when requested. Read templates/report.md.\n\n## Goal\nFollow the contract.\n")
        (self.source / "templates/report.md").write_text("# Report\nExpected result\n")
        (self.source / "examples/audit/README.md").write_text("# Example\n")
        (self.source / "assets/example.svg").write_text("<svg/>\n")
        (self.source / "scripts").mkdir()
        if BUILDER.exists():
            shutil.copyfile(BUILDER, self.source / "scripts/package_skills.py")
        (self.source / "tests").mkdir()
        shutil.copyfile(Path(__file__), self.source / "tests/test_package_skills.py")
        (self.source / "CLAUDE.md").write_text("@AGENTS.md\n")
        self.output = self.work / "installed"

    def build(self, output=None):
        self.assertTrue(BUILDER.is_file(), "No reproducible builder / discoverable SKILL packages yet")
        return subprocess.run([sys.executable, str(BUILDER), "--source", str(self.source),
                               "--output", str(output or self.output)], capture_output=True, text=True)

    def test_four_relocatable_packages_with_exact_resources_and_integrity(self):
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        relocated = self.work / "relocated"
        shutil.move(self.output, relocated)
        for file, name in PLAYBOOKS.items():
            package = relocated / name
            entry = (package / "SKILL.md").read_text()
            self.assertIn("name: " + name, entry)
            self.assertIn("references/bible/playbooks/" + file, entry)
            self.assertNotIn(str(self.source), entry)
            self.assertIn("Read the [source playbook]", entry)
            self.assertIn("references/bible/", entry)
            self.assertEqual((package / "references/bible/playbooks" / file).read_bytes(),
                             (self.source / "playbooks" / file).read_bytes())
            self.assertEqual((package / "references/bible/templates/report.md").read_text(),
                             "# Report\nExpected result\n")
            manifest = json.loads((package / "SOURCE.json").read_text())
            actual = {str(p.relative_to(package)): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in package.rglob("*") if p.is_file() and p.name != "SOURCE.json"}
            self.assertEqual(manifest["files"], actual)
            self.assertEqual(manifest["kind"], "local-snapshot")
            self.assertIsNone(manifest["base_commit"])

    def test_packaged_build_instructions_keep_the_builder_dependency(self):
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in PLAYBOOKS.values():
            self.assertTrue((self.output / name / "references/bible/scripts/package_skills.py").is_file(), "Packaged build instructions lose their builder dependency")
            self.assertTrue((self.output / name / "references/bible/tests/test_package_skills.py").is_file())
            self.assertEqual((self.output / name / "references/bible/scripts/package_skills.py").read_bytes(),
                             (self.source / "scripts/package_skills.py").read_bytes())

    def test_reproducible_and_changes_are_content_addressed(self):
        self.assertEqual(self.build().returncode, 0)
        second = self.work / "second"
        self.assertEqual(self.build(second).returncode, 0)
        tree = lambda root: {str(p.relative_to(root)): p.read_bytes()
                             for p in root.rglob("*") if p.is_file()}
        self.assertEqual(tree(self.output), tree(second))
        (self.source / "vibe-engineering-bible.md").write_text("# Changed canon snapshot\n")
        third = self.work / "third"
        self.assertEqual(self.build(third).returncode, 0)
        get = lambda root: json.loads((root / "bible-audit-project/SOURCE.json").read_text())["source_snapshot_sha256"]
        self.assertNotEqual(get(self.output), get(third))

    def test_existing_skill_is_not_overwritten_or_partially_installed(self):
        existing = self.output / "bible-review-pr"
        existing.mkdir(parents=True)
        (existing / "SKILL.md").write_text("USER CONTENT")
        result = self.build()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((existing / "SKILL.md").read_text(), "USER CONTENT")
        self.assertEqual(list(self.output.iterdir()), [existing])

    def test_unrelated_files_and_secret_shaped_files_are_not_packaged(self):
        (self.source / ".env").write_text("SYNTHETIC TEST ONLY")
        (self.source / "templates/.env").write_text("SYNTHETIC TEST ONLY")
        (self.source / "docs").mkdir()
        (self.source / "docs/private-draft.md").write_text("NOT A RESOURCE")
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        for p in self.output.rglob("*"):
            self.assertNotIn(p.name, [".env", "private-draft.md"])

    def test_symlink_escape_is_rejected_before_install(self):
        outside = self.work / "outside.md"
        outside.write_text("OUTSIDE")
        (self.source / "templates/escape.md").symlink_to(outside)
        result = self.build()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("symlink", result.stderr.lower())
        self.assertFalse(self.output.exists())

    def test_required_resource_cannot_escape_through_parent_symlink(self):
        outside = self.work / "outside-scripts"
        shutil.move(self.source / "scripts", outside)
        (self.source / "scripts").symlink_to(outside, target_is_directory=True)
        result = self.build()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("symlink", result.stderr.lower())
        self.assertFalse(self.output.exists())

    def test_output_symlink_is_rejected_without_writing_its_target(self):
        target = self.work / "outside-output"
        target.mkdir()
        self.output.symlink_to(target, target_is_directory=True)
        result = self.build()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("symlink", result.stderr.lower())
        self.assertEqual(list(target.iterdir()), [])

    def test_frontmatter_error_prevents_partial_install(self):
        (self.source / "playbooks/review-pr.md").write_text(
            "---\nname: bible-review-pr\ndescription: \n---\n")
        result = self.build()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.output.exists())

    def test_license_notice_is_preserved_and_hashed_in_every_package(self):
        notice = b"MIT License\n\nCopyright (c) 2026 Synthetic Test Authors\n\nSYNTHETIC TEST FIXTURE\n"
        (self.source / "LICENSE").write_bytes(notice)
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in PLAYBOOKS.values():
            package = self.output / name
            license_file = package / "references/bible/LICENSE"
            self.assertTrue(license_file.is_file(), "Distributed package lost the license notice")
            self.assertEqual(license_file.read_bytes(), notice)
            manifest = json.loads((package / "SOURCE.json").read_text())
            self.assertEqual(manifest["files"]["references/bible/LICENSE"],
                             hashlib.sha256(notice).hexdigest())

    def test_missing_license_is_rejected_before_install(self):
        (self.source / "LICENSE").unlink()
        result = self.build()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.output.exists())

    def test_local_decision_records_are_not_required_or_distributed(self):
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        local_records = self.source / "docs" / "adr"
        local_records.mkdir(parents=True)
        (local_records / "local-note.md").write_text("LOCAL TEST NOTE; NOT A PUBLIC RESOURCE\n")
        second = self.work / "with-local-records"
        result = self.build(second)
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in PLAYBOOKS.values():
            for output in [self.output, second]:
                package = output / name
                self.assertFalse((package / "references/bible/docs/adr").exists())
                manifest = json.loads((package / "SOURCE.json").read_text())
                self.assertFalse(any(path.startswith("references/bible/docs/adr/")
                                     for path in manifest["files"]))

    def tree(self, root):
        return {str(p.relative_to(root)): p.read_bytes()
                for p in root.rglob("*") if p.is_file()}

    def check(self, output=None):
        args = [sys.executable, str(BUILDER), "--source", str(self.source), "--check"]
        if output is not None:
            args += ["--output", str(output)]
        return subprocess.run(args, capture_output=True, text=True)

    def test_maintenance_files_are_inert_with_resolved_links(self):
        (self.source / "README.md").write_text("[Maintenance](./AGENTS.md)\n")
        (self.source / "CONTRIBUTING.md").write_text("[Instructions](./AGENTS.md)\n")
        original = (self.source / "AGENTS.md").read_bytes()
        self.assertEqual(self.build().returncode, 0)
        for name in PLAYBOOKS.values():
            bundle = self.output / name / "references/bible"
            self.assertFalse((bundle / "AGENTS.md").exists())
            self.assertFalse((bundle / "CLAUDE.md").exists())
            self.assertEqual((bundle / "AGENTS.maintenance.md").read_bytes(), original)
            self.assertEqual((bundle / "CLAUDE.maintenance.md").read_text(), "@AGENTS.maintenance.md\n")
            self.assertTrue((bundle / "AGENTS.maintenance.md").is_file())
            self.assertIn("(./AGENTS.maintenance.md)", (bundle / "README.md").read_text())
        self.assertEqual((self.source / "AGENTS.md").read_bytes(), original)

    def test_content_identity_survives_git_commits_and_unpacked_source(self):
        self.assertEqual(self.build().returncode, 0)
        expected = self.tree(self.output)
        def git(*args):
            result = subprocess.run(["git", "-C", str(self.source), "-c", "core.hooksPath=/dev/null",
                                     "-c", "user.name=Synthetic Test Author", "-c", "user.email=test@example.com",
                                     *args], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
        git("init")
        git("add", ".")
        git("commit", "-m", "Synthetic input")
        for index in range(2):
            git("commit", "--allow-empty", "-m", "Synthetic history only")
            out = self.work / ("git-build-" + str(index))
            self.assertEqual(self.build(out).returncode, 0)
            self.assertEqual(self.tree(out), expected)
        for name in PLAYBOOKS.values():
            manifest = json.loads((self.output / name / "SOURCE.json").read_text())
            self.assertIsNone(manifest["base_commit"])

    def test_source_contract_changes_reach_the_entrypoint(self):
        path = self.source / "playbooks/audit-project.md"
        path.write_text(path.read_text().replace("Use this workflow only when requested.", "SCOPE_SENTINEL: inspect only the supplied diff."))
        self.assertEqual(self.build().returncode, 0)
        self.assertIn("SCOPE_SENTINEL: inspect only the supplied diff.",
                      (self.output / "bible-audit-project/SKILL.md").read_text())

    def test_check_reports_missing_extra_modified_and_symlinks_without_writing(self):
        self.assertEqual(self.build().returncode, 0)
        self.assertEqual(self.check(self.output).returncode, 0)
        package = self.output / "bible-audit-project"
        target = package / "SKILL.md"
        original = target.read_bytes()
        mutations = ["modified", "missing", "extra", "symlink"]
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                if mutation == "modified": target.write_bytes(b"USER CHANGE")
                elif mutation == "missing": target.unlink()
                elif mutation == "extra": (package / "unexpected.txt").write_text("USER FILE")
                else:
                    target.unlink()
                    target.symlink_to(self.source / "README.md")
                before = self.tree(self.output)
                self.assertNotEqual(self.check(self.output).returncode, 0)
                self.assertEqual(self.tree(self.output), before)
                if target.is_symlink(): target.unlink()
                target.write_bytes(original)
                if (package / "unexpected.txt").exists(): (package / "unexpected.txt").unlink()
        self.assertEqual(self.check(self.output).returncode, 0)

    def test_default_check_and_generated_trees_never_become_inputs(self):
        checked_in = self.source / "skills"
        self.assertEqual(self.build(checked_in).returncode, 0)
        self.assertEqual(self.check().returncode, 0)
        self.assertEqual(self.build().returncode, 0)
        self.assertEqual(self.tree(checked_in), self.tree(self.output))
        (checked_in / "extra-root.txt").write_text("UNKNOWN FILE")
        self.assertNotEqual(self.check().returncode, 0)
        self.assertEqual((checked_in / "extra-root.txt").read_text(), "UNKNOWN FILE")

    def test_packaged_source_rebuilds_without_the_original_checkout(self):
        self.assertEqual(self.build().returncode, 0)
        bundle = self.output / "bible-audit-project/references/bible"
        output = self.work / "standalone"
        result = subprocess.run([sys.executable, str(bundle / "scripts/package_skills.py"),
                                 "--output", str(output)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.tree(output), self.tree(self.output))

    def test_checked_in_real_packages_are_fresh_complete_and_inert(self):
        if (ROOT / "AGENTS.maintenance.md").is_file() and not (ROOT / "AGENTS.md").exists():
            self.skipTest("Checkout-only freshness; the standalone bundle has no recursive generated skills tree")
        result = subprocess.run([sys.executable, str(BUILDER), "--check"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        names = set(PLAYBOOKS.values())
        self.assertEqual({p.name for p in (ROOT / "skills").iterdir()}, names)
        for name in names:
            package = ROOT / "skills" / name
            text = (package / "SKILL.md").read_text()
            front = text.split("---\n", 2)[1]
            fields = dict(line.split(": ", 1) for line in front.strip().splitlines())
            self.assertEqual(fields["name"], name)
            self.assertRegex(name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
            self.assertTrue(0 < len(json.loads(fields["description"])) <= 1024)
            bundle = package / "references/bible"
            for file in ["LICENSE", "vibe-engineering-bible.md", "assets/banner-en.jpg"]:
                self.assertEqual((bundle / file).read_bytes(), (ROOT / file).read_bytes())
            self.assertFalse(any(p.name in {"AGENTS.md", "CLAUDE.md"} for p in package.rglob("*")))
            self.assertFalse((bundle / "docs/adr").exists())
            manifest = json.loads((package / "SOURCE.json").read_text())
            actual = {str(p.relative_to(package)): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in package.rglob("*") if p.is_file() and p.name != "SOURCE.json"}
            self.assertEqual(manifest["files"], actual)
            self.assertIsNone(manifest["base_commit"])
            self.assertNotIn("SOURCE.json", manifest["files"])

    def test_different_source_builder_is_rejected_before_install(self):
        path = self.source / "scripts/package_skills.py"
        path.write_bytes(path.read_bytes() + b"\n# Synthetic different source builder\n")
        result = self.build()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("builder", result.stderr.lower())
        self.assertFalse(self.output.exists())

    def test_missing_dependency_is_rejected_before_install(self):
        (self.source / "vibe-engineering-bible.md").unlink()
        result = self.build()
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.output.exists())


if __name__ == "__main__":
    unittest.main()
