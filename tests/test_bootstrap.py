"""Installer regression tests using only the Python standard library."""

from pathlib import Path
import os
import stat
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
PAYLOAD = {
    "AGENTS.md": "skeleton/AGENTS.md",
    ".agent-framework/workflow.md": "skeleton/.agent-framework/workflow.md",
    ".agent-framework/manager.md": "skeleton/.agent-framework/manager.md",
    ".agent-framework/implementer.md": "skeleton/.agent-framework/implementer.md",
    ".agent-framework/change-guidelines.md": "skeleton/.agent-framework/change-guidelines.md",
    "project.md": "skeleton/templates/project.md",
    "project-rules.md": "skeleton/templates/project-rules.md",
    "wip.md": "skeleton/templates/wip.md",
    ".agent-framework/templates/wip.md": "skeleton/templates/wip.md",
}


def snapshot(root):
    """Capture paths, types, permissions, contents, and links without following links."""
    entries = {}

    def visit(path):
        mode = path.lstat().st_mode
        name = str(path.relative_to(root))
        if stat.S_ISLNK(mode):
            entries[name] = (mode, os.readlink(path))
        elif stat.S_ISDIR(mode):
            entries[name] = (mode, None)
            for child in path.iterdir():
                visit(child)
        else:
            entries[name] = (mode, path.read_bytes())

    visit(root)
    return entries


class BootstrapTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="framework-bootstrap-test-")
        self.addCleanup(self.temp.cleanup)
        self.workspace = Path(self.temp.name)
        self.target = self.workspace / "project with spaces"

    def install(self):
        return subprocess.run(
            ["bash", str(ROOT / "bootstrap.sh"), str(self.target)],
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=10,
        )

    def assert_payload(self):
        files = {
            str(path.relative_to(self.target))
            for path in self.target.rglob("*")
            if path.is_file()
        }
        self.assertEqual(files, set(PAYLOAD))
        for destination, source in PAYLOAD.items():
            with self.subTest(destination=destination):
                installed = self.target / destination
                self.assertFalse(installed.is_symlink())
                self.assertEqual(installed.read_bytes(), (ROOT / source).read_bytes())

    def assert_rejected_unchanged(self):
        before = snapshot(self.workspace)
        result = self.install()
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertTrue(result.stderr.strip(), "Rejection should explain the failure")
        self.assertEqual(snapshot(self.workspace), before)

    def test_new_directory(self):
        result = self.install()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assert_payload()

    def test_empty_directory(self):
        self.target.mkdir()
        result = self.install()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assert_payload()

    def test_existing_file_in_directory(self):
        self.target.mkdir()
        (self.target / "notes.txt").write_text("Preserve these project notes.\n")
        self.assert_rejected_unchanged()

    def test_hidden_file_only(self):
        self.target.mkdir()
        (self.target / ".settings").write_text("Preserve hidden settings.\n")
        self.assert_rejected_unchanged()

    def test_hidden_directory_only(self):
        self.target.mkdir()
        (self.target / ".git").mkdir()
        self.assert_rejected_unchanged()

    def test_empty_subdirectory_only(self):
        self.target.mkdir()
        (self.target / "nested").mkdir()
        self.assert_rejected_unchanged()

    def test_dangling_link_inside_directory(self):
        self.target.mkdir()
        (self.target / ".link").symlink_to("missing")
        self.assert_rejected_unchanged()

    def test_file_target(self):
        self.target.write_text("Preserve this file.\n")
        self.assert_rejected_unchanged()

    def test_dangling_symlink_target(self):
        self.target.symlink_to("missing")
        self.assert_rejected_unchanged()

    def test_second_installation(self):
        result = self.install()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assert_payload()
        self.assert_rejected_unchanged()


if __name__ == "__main__":
    unittest.main(verbosity=2)
