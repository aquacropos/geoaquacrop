"""Sphinx configuration for the GeoAquaCrop documentation."""
import os
import sys

sys.path.insert(0, os.path.abspath("../src"))
from datetime import datetime

project = "GeoAquaCrop"
author = "Josias Lang-Ritter, Christopher Bowden, Seyed Hossein Hosseini, Henrikki Tenkanen, Timothy Foster"
copyright = f"{datetime.now():%Y}, {author}"
release = "0.1.0"
version = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
]

autodoc_member_order = "bysource"
autodoc_default_options = {"members": True, "show-inheritance": True}
# the stage packages need not be installed to build these docs
autodoc_mock_imports = ["geoaquacrop.preprocess", "geoaquacrop.simulate",
                        "geoaquacrop.visualize"]

intersphinx_mapping = {
    "preprocess": ("https://geoaquacrop-preprocess.readthedocs.io/en/stable/", None),
    "simulate": ("https://geoaquacrop-simulate.readthedocs.io/en/stable/", None),
    "visualize": ("https://geoaquacrop-visualize.readthedocs.io/en/latest/", None),
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_title = f"{project} {release}"
