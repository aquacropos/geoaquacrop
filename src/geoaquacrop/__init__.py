"""GeoAquaCrop — gridded FAO AquaCrop from raw data to results.

A single, stable entry point to the three toolchain packages::

    import geoaquacrop as gac

    gac.preprocess.run(...)      # download & harmonise input datasets
    gac.simulate.run(config)          # simulate every grid cell
    gac.visualize.run(...)          # explore the results

Each stage is also installable and usable on its own
(``geoaquacrop_preproc``, ``geoaquacrop_sim``, ``geoaquacrop_visualizer``);
this package is a thin, curated façade over them, so the names here stay
stable even if the internals move.

Submodules are imported lazily: ``import geoaquacrop`` is cheap, and the heavy
dependencies of a stage are only loaded when you first touch that stage.
"""
from importlib import import_module as _import_module

__all__ = ["preprocess", "simulate", "visualize"]
__version__ = "0.1.0b1"

_SUBMODULES = frozenset(__all__)


def __getattr__(name):
    """Import a stage on first use (PEP 562)."""
    if name in _SUBMODULES:
        module = _import_module(f"{__name__}.{name}")
        globals()[name] = module
        return module
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    public = [k for k in globals() if not k.startswith("_")]
    return sorted(set(public) | _SUBMODULES)
