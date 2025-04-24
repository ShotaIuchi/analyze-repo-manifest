from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Annotation:
    name: str
    value: str
    keep: Optional[str] = "true"


@dataclass
class CopyFile:
    src: str
    dest: str


@dataclass
class LinkFile:
    src: str
    dest: str


@dataclass
class Project:
    name: str
    path: Optional[str] = None
    remote: Optional[str] = None
    revision: Optional[str] = None
    dest_branch: Optional[str] = None
    groups: Optional[str] = None
    sync_c: Optional[str] = None
    sync_s: Optional[str] = None
    sync_tags: Optional[str] = None
    upstream: Optional[str] = None
    clone_depth: Optional[str] = None
    force_path: Optional[str] = None
    annotations: List[Annotation] = field(default_factory=list)
    projects: List['Project'] = field(default_factory=list)
    copyfiles: List[CopyFile] = field(default_factory=list)
    linkfiles: List[LinkFile] = field(default_factory=list)


@dataclass
class Remote:
    name: str
    fetch: str
    alias: Optional[str] = None
    pushurl: Optional[str] = None
    review: Optional[str] = None
    revision: Optional[str] = None
    annotations: List[Annotation] = field(default_factory=list)


@dataclass
class Default:
    remote: Optional[str] = None
    revision: Optional[str] = None
    dest_branch: Optional[str] = None
    upstream: Optional[str] = None
    sync_j: Optional[str] = None
    sync_c: Optional[str] = None
    sync_s: Optional[str] = None
    sync_tags: Optional[str] = None


@dataclass
class Submanifest:
    name: str
    remote: Optional[str] = None
    project: Optional[str] = None
    manifest_name: Optional[str] = None
    revision: Optional[str] = None
    path: Optional[str] = None
    groups: Optional[str] = None
    default_groups: Optional[str] = None


@dataclass
class RemoveProject:
    name: Optional[str] = None
    path: Optional[str] = None
    optional: Optional[str] = None
    base_rev: Optional[str] = None


@dataclass
class ExtendProject:
    name: str
    path: Optional[str] = None
    dest_path: Optional[str] = None
    groups: Optional[str] = None
    revision: Optional[str] = None
    remote: Optional[str] = None
    dest_branch: Optional[str] = None
    upstream: Optional[str] = None
    base_rev: Optional[str] = None


@dataclass
class RepoHooks:
    in_project: str
    enabled_list: str


@dataclass
class SuperProject:
    name: str
    remote: Optional[str] = None
    revision: Optional[str] = None


@dataclass
class ContactInfo:
    bugurl: str


@dataclass
class Include:
    name: str
    groups: Optional[str] = None
    revision: Optional[str] = None


@dataclass
class Manifest:
    notice: Optional[str] = None
    remotes: List[Remote] = field(default_factory=list)
    default: Optional[Default] = None
    submanifests: List[Submanifest] = field(default_factory=list)
    remove_projects: List[RemoveProject] = field(default_factory=list)
    projects: List[Project] = field(default_factory=list)
    extend_projects: List[ExtendProject] = field(default_factory=list)
    repo_hooks: Optional[RepoHooks] = None
    superproject: Optional[SuperProject] = None
    contact_info: Optional[ContactInfo] = None
    includes: List[Include] = field(default_factory=list)
