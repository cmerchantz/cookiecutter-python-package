"""This file configures how the Sphinx documentation is built."""

import sys
from os.path import abspath, join

sys.path.insert(0, abspath("../.."))
import {{cookiecutter.project_slug}}

# Sphinx configuration
# ====================
# Project information
# -------------------
project = "{{cookiecutter.project_name}}"
copyright = "{{cookiecutter.year}}, {{cookiecutter.full_name}}"
author = "{{cookiecutter.full_name}}"

# We needed to import the project to dynamically get its version.
release = {{cookiecutter.project_slug}}.__version__

# Other Sphinx configuration
# --------------------------
# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and directories to ignore when
# looking for source files. This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Extensions
# ----------
extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.doctest",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "autoapi.extension",
    "sphinx_rtd_theme",
]

# HTML options
# ------------
html_theme = "sphinx_rtd_theme"
html_title = f"{project} Documentation"
html_short_title = f"{project} Docs"

# Path(s) to directory containing static files (e.g. stylesheets)
html_static_path = ["_static"]

# Path(s) to CSS files that are either relative to html_static_path or fully qualified paths (e.g.
# starting with https://...)
html_css_files = ["custom.css"]

html_theme_options = {
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": True,
    "collapse_navigation": True,
    "navigation_depth": -1,
    "includehidden": True,
    "titles_only": True,
}

# Extension-specific configuration
# ================================

# intersphinx configuration
# -------------------------
intersphinx_mapping = {"python": ("https://docs.python.org/3/", None)}

# autosectionlabel configuration
# ------------------------------
# Prefix each section label with the name of the document it lives in. Helpful for uniquely
# identifying the same section name in different documents. For example, a section called
# "Introduction" in the file index.rst would be identified by "index:Introduction".
autosectionlabel_prefix_document = True

# autoapi configuration
# ---------------------
autoapi_type = "python"
autoapi_dirs = [join(abspath("../.."), "src")]
autoapi_template_dir = "_autoapi_templates"
autoapi_autoapi_add_toctree_entry = False
autoapi_options = ["members", "undoc-members", "show-inheritance"]

# Setting this to True can help with debugging
autoapi_keep_files = False

# Make sure the autoapi templates are included in the list of templates that Sphinx cares about
templates_path.append(autoapi_template_dir)

# To include __init__ methods explicitly, tell autoapi just to handle class docstrings, and then
# manually override the mechanism that ignores __init__ methods to have them documented just like
# any other instance method
autoapi_python_class_content = "class"


def keep_init_functions(app, what, name, obj, skip, options):
    """A custom handler for not ignoring class __init__ functions.

    Parameters
    ----------
    app
        The Sphinx application object
    what
        The type of the object which the docstring belongs to (one of "module", "class",
        "exception", "function", "method", "attribute")
    name
        The fully qualified name of the object
    obj
        The object itself
    skip
        A boolean indicating if autodoc will skip this member if the user handler does not override
        the decision
    options
        The options given to the directive: an object with attributes inherited_members,
        undoc_members, show_inheritance and noindex that are true if the flag option of same name
        was given to the auto directive
    """

    if what == "method" and name.split(".")[-1] == "__init__":
        return False


def setup(app):
    app.connect("autoapi-skip-member", keep_init_functions)
