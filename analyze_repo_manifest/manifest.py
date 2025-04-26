from lxml import etree


def parse_manifest(path: str):
    """Parse manifest XML and return (tree, root)"""
    tree = etree.parse(path)
    return tree, tree.getroot()


def search_manifest(root, command, **filters):
    """Search elements in manifest using filters"""
    xpath = _build_xpath(command, **filters)
    return root.xpath(xpath)


def update_elements(elements, updates: dict):
    """Update attributes of matched elements"""
    for elem in elements:
        for key, value in updates.items():
            elem.set(key.replace("_", "-"), value)


def save_manifest(tree, path: str):
    """Save the XML tree back to file with pretty print"""
    tree.write(path, pretty_print=True, encoding="utf-8", xml_declaration=True)


def _build_xpath(command, **filters):
    """[internal] Build XPath string based on command type and filter conditions"""
    if command == "project":
        base = "//project"
    elif command == "remote":
        base = "//remote"
    elif command == "submanifest":
        base = "//submanifest"
    else:
        raise ValueError(f"Unknown command: {command}")

    conds = []
    for key, value in filters.items():
        if value is not None:
            conds.append(f'@{key}="{value}"')

    if conds:
        return f'{base}[{" and ".join(conds)}]'
    else:
        return base
