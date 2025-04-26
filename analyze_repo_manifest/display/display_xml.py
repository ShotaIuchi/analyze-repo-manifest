from lxml import etree


def get_display_name():
    return "xml"


def display(items, fields=None):
    if not items:
        return
    for elem in items:
        print(etree.tostring(elem, pretty_print=True, encoding="unicode").strip())
