import xml.etree.ElementTree as ET
from typing import List
from dataclasses import asdict
import json
from .model import *


def normalize_keys(d: dict) -> dict:
    return {k.replace("-", "_"): v for k, v in d.items()}


def parse_element_list(parent, tag, cls):
    return [cls(**normalize_keys(e.attrib)) for e in parent.findall(tag)]


def parse_manifest(path: str) -> Manifest:
    tree = ET.parse(path)
    root = tree.getroot()

    manifest = Manifest()

    if (notice := root.find('notice')) is not None:
        manifest.notice = notice.text

    manifest.remotes = [Remote(**normalize_keys(r.attrib), annotations=parse_element_list(r, 'annotation', Annotation)) for r in root.findall('remote')]

    if (default := root.find('default')) is not None:
        manifest.default = Default(**normalize_keys(default.attrib))

    manifest.submanifests = parse_element_list(root, 'submanifest', Submanifest)
    manifest.remove_projects = parse_element_list(root, 'remove-project', RemoveProject)
    manifest.extend_projects = parse_element_list(root, 'extend-project', ExtendProject)
    manifest.includes = parse_element_list(root, 'include', Include)

    repo_hooks = root.find('repo-hooks')
    if repo_hooks is not None:
        manifest.repo_hooks = RepoHooks(**normalize_keys(repo_hooks.attrib))

    superproject = root.find('superproject')
    if superproject is not None:
        manifest.superproject = SuperProject(**normalize_keys(superproject.attrib))

    contactinfo = root.find('contactinfo')
    if contactinfo is not None:
        manifest.contact_info = ContactInfo(**normalize_keys(contactinfo.attrib))

    for proj in root.findall('project'):
        project = Project(
            **normalize_keys(proj.attrib),
            annotations=parse_element_list(proj, 'annotation', Annotation),
            projects=[Project(**normalize_keys(sub.attrib)) for sub in proj.findall('project')],
            copyfiles=parse_element_list(proj, 'copyfile', CopyFile),
            linkfiles=parse_element_list(proj, 'linkfile', LinkFile),
        )
        manifest.projects.append(project)

    return manifest


def manifest_to_json(manifest: Manifest) -> str:
    return json.dumps(asdict(manifest), indent=2, ensure_ascii=False)
