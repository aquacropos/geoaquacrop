"""Shared helper for the stage façades."""
from importlib import import_module

# stage -> (distribution name, import name, purpose)

STAGES = {
    "preprocess": {
        "distribution": "geoaquacrop_preprocess",
        "module": "geoaquacrop_preprocess",
        "purpose": "input data preparation",
    },
    "simulate": {
        "distribution": "geoaquacrop_simulate",
        "module": "geoaquacrop_simulate",
        "purpose": "gridded simulation",
    },
    "visualize": {
        "distribution": "geoaquacrop_visualize",
        "module": "geoaquacrop_visualize",
        "purpose": "result visualisation",
    },
}


def require(stage):
    """Import the package behind a stage, or explain how to install it.

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
    try:
        return import_module(spec["module"])
    except ImportError as exc:
        raise ImportError(
            f"{spec['distribution']} is required for {spec['purpose']} but is "
            f"not installed.\n"
            f"    python -m pip install {spec['distribution']}\n"
            f"or install the whole toolchain with:\n"
            f"    python -m pip install geoaquacrop"
        ) from exc


def delegate(stage, name):
    """Return the callable a stage package exports under ``name``.

    Stage packages export their public API at package level (see the stage
    standard), so the façade looks up exactly one name and fails loudly if it
    is absent or not callable.

    Parameters
    ----------
    stage : str
        One of ``"preprocess"``, ``"simulate"``, ``"visualize"``.
    name : str
        The attribute to fetch from that stage package.

    Returns
    -------
    callable

    Raises
    ------
    AttributeError
        If the stage package does not export ``name`` as a callable.
    """
    pkg = require(stage)
    fn = getattr(pkg, name, None)
    if not callable(fn):
        exported = ", ".join(sorted(getattr(pkg, "__all__", []))) or "nothing"
        raise AttributeError(
            f"{pkg.__name__} does not export a callable {name!r}. "
            f"It exports: {exported}. See the GeoAquaCrop stage standard."
        )
    return fn
