# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from datetime import datetime

thisyear = str(datetime.now().year)

project = "streamlitrunner"
copyright = f"{thisyear}, Diogo Rossi"
author = "Diogo Rossi"

import os
import sys

sys.path.insert(0, os.path.abspath("../../src/"))
import streamlitrunner

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "myst_parser",
    "sphinx_copybutton",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinxnotes.comboroles",
]

templates_path = ["_templates"]
exclude_patterns = []

maximum_signature_line_length = 70

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False

# Copy button settings
copybutton_exclude = ".linenos, .gp, .go"
copybutton_prompt_text = ">>> "

# Inter-sphinx settings
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

# Ext-links settings
extlinks = {
    "original": ("https://docs.python.org/3/library/argparse.html#%s", "%s"),
    "argument": ("2_available_functions.html#%s", "%s"),
}

# Combo-roles settings
comboroles_roles = {
    "original_link": ["literal", "original"],
    "argument_link": ["literal", "argument"],
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_title = '<p style="text-align: center"><b>streamlitrunner</b></p>'
html_static_path = ["_static"]

html_css_files = ["css/custom.css"]
html_logo = "../../streamlitrunner.png"

default_role = "code"
