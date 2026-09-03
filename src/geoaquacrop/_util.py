"""Shared helper for the stage façades."""
import importlib

# stage -> (distribution name, what it is needed for)
_DISTRIBUTIONS = {
    "geoaquacrop_preproc": ("geoaquacrop-preproc", "input data preparation"),
    "geoaquacrop_sim": ("geoaquacrop-sim", "gridded simulation"),
    "geoaquacrop_visualizer": ("geoaquacrop-visualizer", "result visualisation"),
}


def require(module_name):
    """Import a stage package, or explain how to install it.

    The three stages are independently installable, so a missing one is a
    normal situation rather than a bug -- this turns an opaque ImportError
    into an actionable message.
    """
    try:
        return importlib.import_module(module_name)
    except ImportError as exc:  # pragma: no cover - depends on environment
        dist, purpose = _DISTRIBUTIONS.get(module_name, (module_name, "this stage"))
        raise ImportError(
            f"{dist} is required for {purpose} but is not installed.\n"
            f"    python -m pip install {dist}\n"
            f"or install the whole toolchain with:\n"
            f"    python -m pip install --pre geoaquacrop"
        ) from exc
