"""Result visualisation — :mod:`geoaquacrop.visualize`.

Façade over the ``geoaquacrop_visualize`` package::

    import geoaquacrop as gac

    gac.visualize.launch()      # starts the dashboard, then open the printed URL
"""
from ._util import delegate

__all__ = ["launch", "run"]


def launch(*args, **kwargs):
    """Start the interactive dashboard."""
    return delegate("visualize", "launch", "run", "main", "run_app", "start")(
        *args, **kwargs)


def run(*args, **kwargs):
    """Alias for :func:`launch`, so every stage answers to ``run``."""
    return launch(*args, **kwargs)
