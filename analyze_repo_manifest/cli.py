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

    print_selected_fields(results, args.fields)


def print_selected_fields(obj_list, fields: str):
    if not obj_list:
        return

    if not fields:
        fields = ",".join(obj_list[0].__dataclass_fields__.keys())

    field_list = fields.split(",")

    for obj in obj_list:
        values = []
        for f in field_list:
            value = getattr(obj, f, None)
            if value is not None:
                values.append(f"{f}={value}")
        if values:
            print(", ".join(values))


if __name__ == "__main__":
    main()
