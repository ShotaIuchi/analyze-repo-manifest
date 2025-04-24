from .model import Manifest, Project, Remote, Submanifest
from typing import List


def filter_projects(manifest: Manifest, **kwargs) -> List[Project]:
    return filter_items(manifest.projects, **kwargs)


def filter_remotes(manifest: Manifest, **kwargs) -> List[Remote]:
    return filter_items(manifest.remotes, **kwargs)


def filter_submanifests(manifest: Manifest, **kwargs) -> List[Submanifest]:
    return filter_items(manifest.submanifests, **kwargs)


def filter_items(items, **criteria):
    results = []
    for item in items:
        match = True
        for key, val in criteria.items():
            if val is not None and getattr(item, key, None) != val:
                match = False
                break
        if match:
            results.append(item)
    return results
