# pdf2png
[![PyPi Version](https://img.shields.io/pypi/v/pdf2png.svg)](https://pypi.python.org/pypi/pdf2png)
[![PyPI Status](https://img.shields.io/pypi/status/pdf2png.svg)](https://pypi.python.org/pypi/pdf2png)
[![Python Versions](https://img.shields.io/pypi/pyversions/pdf2png.svg)](https://pypi.python.org/pypi/pdf2png)
[![License](https://img.shields.io/github/license/ReK42/pdf2png)](https://github.com/ReK42/pdf2png/blob/main/LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/ReK42/pdf2png/main?logo=github)](https://github.com/ReK42/pdf2png/commits/main)
[![Build Status](https://img.shields.io/github/actions/workflow/status/ReK42/pdf2png/build.yml?logo=github)](https://github.com/ReK42/pdf2png/actions)

CLI utility to convert PDF pages to PNG images.

## Installation
1. Install [Python](https://www.python.org/downloads/).
1. Install [pipx](https://github.com/pypa/pipx).
1. Install [Ghostscript](https://www.ghostscript.com/releases/gsdnld.html).
1. Install ImageMagick according to the instructions [here](https://docs.wand-py.org/en/latest/guide/install.html).
1. Use `pipx` to install `pdf2png`:
```sh
pipx install pdf2png
```

## Usage
For all options, run `pdf2png --help`

## Development Environment
### Installation
```sh
git clone https://github.com/ReK42/pdf2png.git
cd pdf2png
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
