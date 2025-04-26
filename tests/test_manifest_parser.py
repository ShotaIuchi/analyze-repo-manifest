import unittest
import os
from lxml import etree
from analyze_repo_manifest.manifest import parse_manifest


class TestManifestParser(unittest.TestCase):
    def setUp(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.manifest_path = os.path.join(current_dir, "data", "manifests", "default.xml")

    def test_parse_remotes(self):
        tree, root = parse_manifest(self.manifest_path)
        remotes = root.xpath("//remote")
        self.assertEqual(len(remotes), 2)

    def test_parse_default(self):
        tree, root = parse_manifest(self.manifest_path)
        defaults = root.xpath("//default")
        self.assertEqual(len(defaults), 1)

    def test_parse_projects(self):
        tree, root = parse_manifest(self.manifest_path)
        projects = root.xpath("//project")
        self.assertEqual(len(projects), 8)

    def test_parse_alpha_project(self):
        tree, root = parse_manifest(self.manifest_path)
        alpha = root.xpath("//project[@name='alpha']")[0]
        self.assertEqual(alpha.get("path"), "src/alpha")
        self.assertEqual(alpha.get("revision"), "dev")

        annotations = alpha.xpath("annotation")
        self.assertEqual(len(annotations), 1)
        self.assertEqual(annotations[0].get("name"), "maintainer")
        self.assertEqual(annotations[0].get("value"), "alice")

    def test_parse_beta_project(self):
        tree, root = parse_manifest(self.manifest_path)
        beta = root.xpath("//project[@name='beta']")[0]
        self.assertEqual(beta.get("path"), "src/beta")

        annotations = beta.xpath("annotation")
        self.assertEqual(len(annotations), 0)

        subprojects = beta.xpath("project")
        self.assertEqual(len(subprojects), 0)

    def test_parse_duplicate_projects(self):
        tree, root = parse_manifest(self.manifest_path)
        echoes = root.xpath("//project[@name='echo']")
        self.assertEqual(len(echoes), 2)

        revisions = sorted([e.get("revision") for e in echoes])
        self.assertEqual(revisions, ["main", "sub"])

    def test_parse_gamma_multiple_annotations(self):
        tree, root = parse_manifest(self.manifest_path)
        gamma = root.xpath("//project[@name='gamma']")[0]
        annotations = gamma.xpath("annotation")
        self.assertEqual(len(annotations), 2)

        names = sorted([a.get("name") for a in annotations])
        self.assertEqual(names, ["maintainer", "reviewer"])

    def test_parse_submanifests(self):
        tree, root = parse_manifest(self.manifest_path)
        submanifests = root.xpath("//submanifest")
        self.assertEqual(len(submanifests), 4)

        subA = root.xpath("//submanifest[@name='subA']")[0]
        self.assertEqual(subA.get("path"), "vendor/subA")
        self.assertEqual(subA.get("manifest-name"), "subA.xml")

    def test_comments_are_ignored(self):
        tree, root = parse_manifest(self.manifest_path)
        comments = [e for e in root.iter() if isinstance(e, etree._Comment)]
        self.assertGreaterEqual(len(comments), 1)


if __name__ == "__main__":
    unittest.main()
