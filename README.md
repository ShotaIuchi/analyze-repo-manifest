# analyze-repo-manifest

A command-line and library tool for exploring, filtering, **and updating** [Google repo manifest XML](https://gerrit.googlesource.com/git-repo/+/main/docs/manifest-format.md) files.

Easily search for projects, remotes, and submanifests — display them in your preferred format (`default`, `json`, `yaml`, `xml`, or custom), and even **update attributes** in-place.

## 🔧 Installation

### 🔹 Not on PyPI (yet)

This tool is not published to PyPI yet.
You can install it locally by cloning the repository:

```bash
git clone https://github.com/yourname/analyze-repo-manifest.git
cd analyze-repo-manifest
pip install -e .
```

> For YAML output, install `pyyaml`:
>
> ```bash
> pip install pyyaml
> ```

> For XML pretty printing, install `lxml`:
>
> ```bash
> pip install lxml
> ```

## 🚀 Usage

### As installed CLI

```bash
analyze-repo-manifest <manifest.xml> <category> [filters] [--display FORMAT] [--update --set KEY=VALUE ...]
```

### Or run directly via Python

```bash
python -m analyze_repo_manifest.cli <manifest.xml> <category> [filters] [--display FORMAT] [--update --set KEY=VALUE ...]
```

### As Python library

You can also use it directly from Python:

```python
from analyze_repo_manifest.manifest import parse_manifest, search_manifest, update_elements, save_manifest

tree, root = parse_manifest("default.xml")
projects = search_manifest(root, "project", name="foo")
update_elements(projects, {"upstream": "main"})
save_manifest(tree, "default.xml")
```

## 🔍 Examples

### Search project by name

```bash
analyze-repo-manifest default.xml project --name platform/frameworks/base
```

### Show as JSON

```bash
analyze-repo-manifest default.xml project --name foo --display json
```

### Show as raw XML

```bash
analyze-repo-manifest default.xml project --name foo --display xml
```

### Update project upstream

```bash
analyze-repo-manifest default.xml project --name foo --update --set upstream=main
```

> 💡 Updates will modify the original manifest file in-place!

## 🧩 Output Formats

Use `--display` to customize output:

- `default`: key=value text (default)
- `json`: structured JSON
- `yaml`: YAML format (requires `pyyaml`)
- `xml`: Raw XML element format (pretty-printed)

## ✍️ Update Support

You can update fields of matching elements using `--update` and `--set`:

```bash
analyze-repo-manifest default.xml project --name foo --update --set upstream=dev path="new/path/"
```

Multiple fields can be updated at once.
The original file will be updated **in-place**.

## 🔌 Plugin Support

This tool supports pluggable output formats via Python entry points.

You can create your own plugin like this:

```toml
[project.entry-points."analyze_repo_manifest.display"]
markdown = "your_package.display:display"
```

Once installed, your plugin becomes available:

```bash
analyze-repo-manifest default.xml project --display markdown
```

> 💡 Example plugins may be published in the future. Let us know if you build one!

## 🧪 Testing

We use `unittest` and optionally `pytest` for testing.

To run tests:

```bash
python -m unittest discover tests
```

Or with pytest:

```bash
pytest
```

## ❓ Help

```bash
analyze-repo-manifest --help
analyze-repo-manifest project --help
```
