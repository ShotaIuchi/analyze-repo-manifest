import sys
from analyze_repo_manifest.args import (
    parse_args,
    parse_set_fields,
)
from analyze_repo_manifest.display import (
    get_display_function,
)
from analyze_repo_manifest.manifest import (
    parse_manifest,
    search_manifest,
    update_elements,
    save_manifest,
)


def main():
    args = parse_args()

    tree, root = parse_manifest(args.manifest)

    filters = {
        "name": args.name,
        "path": args.path,
        "revision": args.revision,
        "remote": args.remote,
        "groups": args.groups,
        "alias": args.alias,
        "fetch": args.fetch,
        "pushurl": args.pushurl,
        "review": args.review,
        "manifest-name": args.manifest_name,
        "project": args.project,
    }

    elements = search_manifest(root, args.command, **{k: v for k, v in filters.items() if v is not None})

    if not elements:
        print("No matching elements found.", file=sys.stderr)
        sys.exit(1)

    if args.update:
        updates = parse_set_fields(args.set)
        update_elements(elements, updates)
        save_manifest(tree, args.manifest)
    else:
        display_func = get_display_function(args.display)
        display_func(elements, args.fields)


if __name__ == "__main__":
    main()
