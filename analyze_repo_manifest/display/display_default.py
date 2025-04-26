def get_display_name():
    return "default"


def display(items, fields=None):
    if not items:
        return
    for elem in items:
        if fields:
            field_list = fields.split(",")
        else:
            field_list = elem.attrib.keys()
        parts = []
        for f in field_list:
            value = elem.get(f)
            if value is not None:
                parts.append(f"{f}={value}")
        print(", ".join(parts))
