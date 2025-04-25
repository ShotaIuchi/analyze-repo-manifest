def get_display_name():
    return "default"


def display(items, fields=None):
    if not items:
        return

    if not fields:
        fields = ",".join(items[0].__dataclass_fields__.keys())

    field_list = fields.split(",")

    for item in items:
        values = []
        for f in field_list:
            value = getattr(item, f, None)
            if value is not None:
                values.append(f"{f}={value}")
        if values:
            print(", ".join(values))
