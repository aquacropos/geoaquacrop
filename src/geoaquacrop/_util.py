"""Shared helper for the stage façades."""
from importlib import import_module

# stage -> (distribution name, import name, purpose, legacy import names)
#
# The legacy names let the façade keep working while the stage repositories
# migrate to the standard naming (see docs/standard.rst). Remove them once all
# three have migrated.
STAGES = {
    "preprocess": {
        "distribution": "geoaquacrop_preprocess",
        "module": "geoaquacrop_preprocess",
        "purpose": "input data preparation",
        "legacy": ("geoaquacrop_preproc",),
    },
    "simulate": {
        "distribution": "geoaquacrop_simulate",
        "module": "geoaquacrop_simulate",
        "purpose": "gridded simulation",
        "legacy": ("geoaquacrop_sim",),
    },
    "visualize": {
        "distribution": "geoaquacrop_visualize",
        "module": "geoaquacrop_visualize",
        "purpose": "result visualisation",
        "legacy": ("geoaquacrop_visualizer",),
    },
}


def require(stage):
    """Import the package behind a stage, or explain how to install it.

    Tries the standard module name first, then any legacy name, so the façade
    works both before and after a stage repository migrates.

    Parameters
    ----------
    stage : str
        One of ``"preprocess"``, ``"simulate"``, ``"visualize"``.

    Returns
    -------
    module
        The imported stage package.

    Raises
    ------
    ImportError
        If the stage is not installed, with the command needed to install it.
    """
    spec = STAGES[stage]
    for name in (spec["module"], *spec["legacy"]):
        try:
            return import_module(name)
        except ImportError:
            continue
    raise ImportError(
        f"{spec['distribution']} is required for {spec['purpose']} but is not "
        f"installed.\n"
        f"    python -m pip install {spec['distribution']}\n"
        f"or install the whole toolchain with:\n"
        f"    python -m pip install --pre geoaquacrop"
    )


def delegate(stage, *candidates):
    """Return the first callable a stage package exposes from ``candidates``.

    Stage packages are expected to export their public API at package level
    (see docs/standard.rst). The candidate list tolerates a stage that has not
    migrated yet, and produces an explicit error when none is found.
    """
    pkg = require(stage)
    for name in candidates:
        fn = getattr(pkg, name, None)
        if callable(fn):
            return fn
    raise AttributeError(
        f"{pkg.__name__} exposes none of {candidates!r}. Its installed version "
        f"may not provide this step; see the GeoAquaCrop stage standard."
    )
