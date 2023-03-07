  # Confluent CLI Wraper for Python

## Installation

```bash
pip3 install poetry
poetry config virtualenvs.create true
poetry install
```

## Utils commands

### Publish new version

```bash
git mkver patch 
# Use Poetry to sync 'pyproject.toml' version with new '.semver' value
poetry version $(cat .semver)
# Commit Bumped files
git add .semver pyproject.toml
git commit -m "build: bumping to $(cat .semver)"
git mkver tag

# Push your(s) tag(s) to remote
git push --follow-tags

poetry build && poetry publish

```



## Contributing

See https://github.com/alansferreira/git-mkver-with-poetry to bump versions.

