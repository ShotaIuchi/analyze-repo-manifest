def get_display_name():
    return "yaml"


def display(items, fields=None):
    import yaml
    dicts = []
    for elem in items:
        d = {k: v for k, v in elem.attrib.items()}
        if fields:
            field_list = fields.split(",")
            d = {k: v for k, v in d.items() if k in field_list}
        dicts.append(d)
    print(yaml.safe_dump(dicts, allow_unicode=True, sort_keys=False))
