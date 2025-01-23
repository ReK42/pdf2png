# PROJECT_NAME
[![PyPi Version](https://img.shields.io/pypi/v/PROJECT_NAME.svg)](https://pypi.python.org/pypi/PROJECT_NAME)
[![PyPI Status](https://img.shields.io/pypi/status/PROJECT_NAME.svg)](https://pypi.python.org/pypi/PROJECT_NAME)
[![Python Versions](https://img.shields.io/pypi/pyversions/PROJECT_NAME.svg)](https://pypi.python.org/pypi/PROJECT_NAME)
[![License](https://img.shields.io/github/license/ReK42/PROJECT_NAME)](https://github.com/ReK42/PROJECT_NAME/blob/main/LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/ReK42/PROJECT_NAME/main?logo=github)](https://github.com/ReK42/PROJECT_NAME/commits/main)
[![Build Status](https://img.shields.io/github/actions/workflow/status/ReK42/PROJECT_NAME/build.yml?logo=github)](https://github.com/ReK42/PROJECT_NAME/actions)

PROJECT_DESC

# TODO
1. Find & replace PROJECT_NAME with the CLI command/PyPI project/Github repo name.
1. Find & replace MODULE_NAME with the project's Python root module name (`src/MODULE_NAME)`.
1. Find & replace PROJECT_DESC with the one-line project description.
1. Update `src/MODULE_NAME/__init__.py`
1. Begin coding...

## Installation
Install [Python](https://www.python.org/downloads/), then install [pipx](https://github.com/pypa/pipx) and use it to install `PROJECT_NAME`:
```sh
pipx install PROJECT_NAME
```

## Usage
For all options, run `PROJECT_NAME <COMMAND> --help`

## Development Environment
### Installation
```sh
git clone https://github.com/ReK42/PROJECT_NAME.git
cd PROJECT_NAME
python -m venv .env
source .env/bin/activate
python -m pip install --upgrade pip pre-commit
pre-commit install
pip install -e .[test]
```

### Manual Testing
To check:
```sh
mypy src
ruff check src
ruff format --diff src
```

To auto-fix/format:
```sh
ruff check --fix src
ruff format src
```

### Manual Building
```sh
pip install -e .[build]
python -m build
```
