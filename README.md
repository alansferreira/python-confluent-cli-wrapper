  # Confluent CLI Wraper for Python

## Installation

```bash
pip3 install poetry
poetry config virtualenvs.create true
poetry install
```

## Utils commands
```bash
# bumps project version and generates change log file
poetry run cz bump --check-consistency --changelog && poetry version $(poetry run cz version -p)

```

## Contributing

Check commit message formats on Conventional Commits, it's enable in this project with `commitzen`.

You can bypass conventional commits using `--no-verify` on `clone, push` commands of `git`.

