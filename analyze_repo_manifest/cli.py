from analyze_repo_manifest.display import get_display_function
from .args import parse_args
from .parse import parse_manifest
from .search import (
    filter_projects,
    filter_remotes,
    filter_submanifests,
)


def main():
    args = parse_args()
    manifest = parse_manifest(args.manifest)

    if args.command == "project":
        results = filter_projects(
            manifest,
            name=args.name,
            path=args.path,
            revision=args.revision,
            remote=args.remote,
            groups=args.groups,
        )

    elif args.command == "remote":
        results = filter_remotes(
            manifest,
            name=args.name,
            alias=args.alias,
            fetch=args.fetch,
            pushurl=args.pushurl,
            review=args.review,
            revision=args.revision,
        )

    elif args.command == "submanifest":
        results = filter_submanifests(
            manifest,
            name=args.name,
            project=args.project,
            path=args.path,
            revision=args.revision,
            groups=args.groups,
        )

    display_func = get_display_function(args.display)
    display_func(results, args.fields)


if __name__ == "__main__":
    main()
