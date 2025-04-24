import unittest
import os
from analyze_repo_manifest.parse import parse_manifest
from analyze_repo_manifest.model import Manifest, Project


class TestManifestParser(unittest.TestCase):
    def test_parse_manifest(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        manifest_path = os.path.join(current_dir, "data", "manifests", "default.xml")
        manifest: Manifest = parse_manifest(manifest_path)

        self.assertTrue(len(manifest.remotes) > 0)
        self.assertIsNotNone(manifest.default)
        self.assertTrue(len(manifest.projects) > 0)
        self.assertEqual(len(manifest.projects), 6)

        alpha: Project = manifest.projects[0]
        self.assertEqual(alpha.name, "alpha")
        self.assertEqual(alpha.path, "src/alpha")
        self.assertEqual(alpha.revision, "dev")
        self.assertTrue(len(alpha.annotations) > 0)
        self.assertEqual(alpha.annotations[0].name, "maintainer")

        beta: Project = manifest.projects[1]
        self.assertEqual(beta.name, "beta")
        self.assertEqual(beta.path, "src/beta")
        self.assertEqual(len(beta.annotations), 0)
        self.assertEqual(len(beta.projects), 0)


if __name__ == "__main__":
    unittest.main()
