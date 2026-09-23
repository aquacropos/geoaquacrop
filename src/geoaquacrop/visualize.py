"""Result visualisation — :mod:`geoaquacrop.visualize`.

Façade over the ``geoaquacrop_visualize`` package::

    import geoaquacrop as gac

    gac.visualize.run()      # starts the dashboard, then open the printed URL
"""
from ._util import delegate

__all__ = ["run"]


def run(*args, **kwargs):
    """Start the interactive dashboard."""
    return delegate("visualize", "run")(*args, **kwargs)