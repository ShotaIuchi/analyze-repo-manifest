def get_display_name():
    return "json"


def display(items, fields=None):
    import json
    from dataclasses import asdict
    dicts = [asdict(i) for i in items]
    if fields:
        field_list = fields.split(",")
        dicts = [
            {k: v for k, v in d.items() if k in field_list and v is not None}
            for d in dicts
        ]
    print(json.dumps(dicts, indent=2, ensure_ascii=False))
