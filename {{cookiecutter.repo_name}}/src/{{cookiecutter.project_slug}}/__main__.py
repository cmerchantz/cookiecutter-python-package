"""The __main__ module.

The presence of this module allows the project to be invoked by the command
``python -m {{cookiecutter.project_slug}}``.
"""

from .cli import main

if __name__ == "__main__":
    main()
