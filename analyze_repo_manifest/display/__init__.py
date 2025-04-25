from importlib.metadata import entry_points
from .display_default import display as default_display


def get_display_names():
    """Returns a list of all available display plugin names."""
    try:
        return [ep.name for ep in entry_points(group="analyze_repo_manifest.display")]
    except Exception:
        return ["default"]


def get_display_function(name: str):
    """Loads and returns the display function for the given plugin name."""
    if not name:
        return default_display

    for ep in entry_points(group="analyze_repo_manifest.display"):
        if ep.name == name:
            return ep.load()

    raise ValueError(f"Display plugin '{name}' not found")
