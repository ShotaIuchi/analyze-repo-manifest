from analyze_repo_manifest.parse import parse_manifest


def main():
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    manifest = parse_manifest(os.path.join(current_dir, os.path.pardir, "tests", "data", "manifests", "default.xml"))
    for remote in manifest.remotes:
        print(f"Remote name: {remote.name}, fetch: {remote.fetch}")
