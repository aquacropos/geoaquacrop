"""Sphinx configuration for the GeoAquaCrop documentation."""
import os
import sys

sys.path.insert(0, os.path.abspath("../src"))
from datetime import datetime

project = "GeoAquaCrop"
author = "Josias Ritter, Chris Bowden, Seho Hosseini"
copyright = f"{datetime.now():%Y}, {author}"
release = "0.1.0b1"
version = "0.1.0b1"

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
    "preprocess": ("https://geoaquacrop-preprocessing.readthedocs.io/en/stable/", None),
    "simulate": ("https://geoaquacrop-simulate.readthedocs.io/en/stable/", None),
    "visualize": ("https://geoaquacrop-visualize.readthedocs.io/en/latest/", None),
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_title = f"{project} {release}"
