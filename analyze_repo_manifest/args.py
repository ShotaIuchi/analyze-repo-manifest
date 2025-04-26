import argparse
from analyze_repo_manifest.display import get_display_names


def parse_args():
    parser = argparse.ArgumentParser(
        description="Analyze and update repo manifest XML (e.g. default.xml). Supports search, display, and update.",
        epilog="Examples:\n"
               "  analyze-repo-manifest default.xml project --name foo\n"
               "  analyze-repo-manifest default.xml project --name foo --update --set upstream=main\n",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("manifest", help="Path to manifest file (e.g. default.xml)")
    parser.add_argument("command", choices=["project", "remote", "submanifest"], help="Target element type to search or update")

    parser.add_argument("--fields", help="Comma-separated field names to display (default: all fields)")
    parser.add_argument("--display", choices=get_display_names(), help="Display style (default/json/yaml)")

    parser.add_argument("--update", action="store_true", help="Update matching items instead of displaying them")
    parser.add_argument("--set", nargs="+", metavar="KEY=VALUE", help="Fields to update. Used with --update. Example: --set path=foo/bar upstream=main")

    # common filters for all commands
    parser.add_argument("--name", help="Filter by name attribute")
    parser.add_argument("--path", help="Filter by path attribute")
    parser.add_argument("--revision", help="Filter by revision attribute")
    parser.add_argument("--remote", help="Filter by remote attribute")
    parser.add_argument("--groups", help="Filter by groups attribute")
    parser.add_argument("--alias", help="Filter by alias attribute (for remote)")
    parser.add_argument("--fetch", help="Filter by fetch attribute (for remote)")
    parser.add_argument("--pushurl", help="Filter by pushurl attribute (for remote)")
    parser.add_argument("--review", help="Filter by review attribute (for remote)")
    parser.add_argument("--manifest-name", help="Filter by manifest-name attribute (for submanifest)")
    parser.add_argument("--project", help="Filter by project attribute (for submanifest)")

    return parser.parse_args()


def parse_set_fields(set_args):
    """Parse --set KEY=VALUE args into a dict"""
    updates = {}
    for s in set_args or []:
        if "=" not in s:
            raise ValueError(f"Invalid --set format: {s}")
        key, value = s.split("=", 1)
        updates[key.replace("-", "_")] = value
    return updates
