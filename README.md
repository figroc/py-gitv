# Git Versioning for Python Project

A biased git versioning tool. It versions as following:

- On `v*` tag: version as tag if not `sticky`

  i.e. `0.1.0`

- On `main` or `master` branch: version as *rc*

  i.e. `0.1.0-rc{BUILD_NUMBER}+{GIT_COMMIT_SHORT_SHA}`

- Others: version as *dev*

  i.e. `0.1.0-dev{BUILD_NUMBER}+{GIT_COMMIT_SHORT_SHA}`

If env `VERSIONING_GIT_BRANCH` is set, it will be used instead of `git branch --show-current`.

## Usage

It currently support *setuptools*, *hatch* and *poetry*.

### setuptools

```python
setuptools.setup(
  version="0.1.0",
  setup_requires=["gitv"]
)
  ```

### hatch

```toml
[build-system]
requires = ["hatchling", "gitv"]

[project]
dynamic = ["version"]

[tool.hatch.version]
version = "0.1.0"
source = "vcs"
```

### poetry

```toml
[build-system]
requires = ["poetry-core", "gitv"]

[tool.poetry]
version = "0.1.0"
```

