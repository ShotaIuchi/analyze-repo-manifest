def get_display_name():
    return "yaml"


def display(items, fields=None):
    import yaml
    from dataclasses import asdict
    dicts = [asdict(i) for i in items]
    if fields:
        field_list = fields.split(",")
        dicts = [
            {k: v for k, v in d.items() if k in field_list and v is not None}
            for d in dicts
        ]
    print(yaml.safe_dump(dicts, allow_unicode=True, sort_keys=False))
