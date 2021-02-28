# cookiecutter-python-package

My Python package template. There are many like it, but this one is mine.

## Summary of features

* All automated with [Tox](https://tox.readthedocs.io):
	* Testing: [Pytest](https://docs.pytest.org)
	* Test Coverage: [coverage.py](https://coverage.readthedocs.io/) via [pytest-cov](https://pytest-cov.readthedocs.io)
	* Documentation: [Sphinx](https://www.sphinx-doc.org)
		* Some of my personal tweaks to the defaults
* Version management: [versioneer](https://github.com/python-versioneer/python-versioneer)
* Pre-commit hooks: [pre-commit](https://pre-commit.com/)
	* Code formatting: [Black](https://black.readthedocs.io)
	* Linting: [Flake8](https://flake8.pycqa.org)
	* Automatic import sorting: [isort](https://pycqa.github.io/isort/)
* Choice of license, inspired by [audreyfeldroy's ultimate Python project template](https://github.com/audreyfeldroy/cookiecutter-pypackage)

## Usage

Install cookiecutter, if you haven't already

```
python -m pip install cookiecutter
```

Cookie-cut this repo

```
cookiecutter gh:cmerchantz/cookiecutter-python-package
```

Once your project is under version control, install pre-commit hooks from within the project directory:

```
pre-commit install
```