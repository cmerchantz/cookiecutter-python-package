"""The setup script for building the package."""

from setuptools import find_packages, setup

import versioneer

NAME = "{{cookiecutter.project_slug}}"
VERSION = versioneer.get_version()

# The long description is read from the README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    author="{{cookiecutter.full_name}}",
    url="github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}",
    version=VERSION,
    description="{{cookiecutter.project_short_description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=[],
    cmdclass=versioneer.get_cmdclass(),
)
