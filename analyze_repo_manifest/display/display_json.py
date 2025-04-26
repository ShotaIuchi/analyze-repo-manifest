def get_display_name():
    return "json"


def display(items, fields=None):
    import json
    dicts = []
    for elem in items:
        d = {k: v for k, v in elem.attrib.items()}
        if fields:
            field_list = fields.split(",")
            d = {k: v for k, v in d.items() if k in field_list}
        dicts.append(d)
    print(json.dumps(dicts, indent=2, ensure_ascii=False))
