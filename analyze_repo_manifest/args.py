import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Repo manifest analysis CLI")
    parser.add_argument("manifest", help="Path to manifest file (e.g. default.xml)")

    # Subcoommand
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: project
    project_parser = subparsers.add_parser("project", help="Search projects")
    project_parser.add_argument("--name", help="Project name")
    project_parser.add_argument("--path", help="Project path")
    project_parser.add_argument("--revision", help="Revision")
    project_parser.add_argument("--remote", help="Remote")
    project_parser.add_argument("--groups", help="Groups")
    project_parser.add_argument("--fields", help="Comma-separated fields to display")

    # Subcommand: remote
    remote_parser = subparsers.add_parser("remote", help="Search remotes")
    remote_parser.add_argument("--name", help="Remote name")
    remote_parser.add_argument("--alias", help="Alias")
    remote_parser.add_argument("--fetch", help="Fetch URL")
    remote_parser.add_argument("--pushurl", help="Push URL")
    remote_parser.add_argument("--review", help="Review server")
    remote_parser.add_argument("--revision", help="Revision")
    remote_parser.add_argument("--fields", help="Comma-separated fields")

    # Subcommand: submanifest
    submanifest_parser = subparsers.add_parser("submanifest", help="Search submanifests")
    submanifest_parser.add_argument("--name", help="Name")
    submanifest_parser.add_argument("--project", help="Project name")
    submanifest_parser.add_argument("--path", help="Path")
    submanifest_parser.add_argument("--revision", help="Revision")
    submanifest_parser.add_argument("--groups", help="Groups")
    submanifest_parser.add_argument("--fields", help="Comma-separated fields")

    return parser.parse_args()
