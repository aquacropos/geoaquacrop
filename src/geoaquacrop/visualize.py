"""Result visualisation — :mod:`geoaquacrop.visualize`.

Thin façade over ``geoaquacrop.visualize``::

    import geoaquacrop as gac

    gac.visualize.launch()        # starts the dashboard, then open the printed URL
"""
from ._util import require


def _pkg():
    return require("geoaquacrop.visualize")


def launch(*args, **kwargs):
    """Start the interactive dashboard."""
    pkg = _pkg()
    for name in ("launch", "main", "run", "run_app", "start"):
        fn = getattr(pkg, name, None)
        if callable(fn):
            return fn(*args, **kwargs)
    raise AttributeError(
        "geoaquacrop_visualizer exposes no launch/main/run entry point; "
        "run it directly with: python -m geoaquacrop_visualizer")


__all__ = ["launch"]
