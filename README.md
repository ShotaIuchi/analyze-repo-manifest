# analyze-repo-manifest

A command-line tool for exploring and filtering [Google repo manifest XML](https://gerrit.googlesource.com/git-repo/+/main/docs/manifest-format.md) files.

Easily search for projects, remotes, and submanifests — and display them in your preferred format (`default`, `json`, `yaml`, or custom).

---

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

---

## 🚀 Usage

### As installed CLI

```bash
analyze-repo-manifest <manifest.xml> <category> [filters] [--display FORMAT]
```

### Or run directly via Python

```bash
python -m analyze_repo_manifest.cli <manifest.xml> <category> [filters] [--display FORMAT]
```

---

## 🔍 Examples

### Search project by name

```bash
analyze-repo-manifest default.xml project --name platform/frameworks/base
```

### Show as JSON

```bash
analyze-repo-manifest default.xml project --name foo --display json
```

---

## 🧩 Output Formats

Use `--display` to customize output:

- `default`: key=value text (default)
- `json`: structured JSON
- `yaml`: YAML format (requires `pyyaml`)

---

## 🔌 Plugin Support

This tool supports pluggable output formats via Python entry points.

You can even create your own plugin by writing a Python package that exposes an entry point like this:

```toml
[project.entry-points."analyze_repo_manifest.display"]
markdown = "your_package.display:display"
```

Once installed with pip, your plugin becomes available:

```bash
analyze-repo-manifest default.xml project --display markdown
```

> 💡 Example plugins may be published in the future. Let us know if you build one!

---

## ❓ Help

```bash
analyze-repo-manifest --help
analyze-repo-manifest project --help
```
