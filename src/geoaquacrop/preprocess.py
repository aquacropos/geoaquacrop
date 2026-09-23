"""Input data preparation — :mod:`geoaquacrop.preprocess`.

Façade over the ``geoaquacrop_preprocess`` package::

    import geoaquacrop as gac

    gac.preprocess.run(domain_shape_path='region.geojson', start_year=2011,
                       end_year=2013, api_token='...', cell_resolution=0.05,
                       workingdirectory='/data/region')

:func:`run` prepares every dataset a simulation needs. The per-dataset helpers
re-run a single step; each requires the stage package to export that step at
package level (see the stage standard), and raises an explicit error if the
installed version does not.
"""
from ._util import delegate

__all__ = ["run", "weather", "soil", "crop_calendar", "crop_area"]


def run(*args, **kwargs):
    """Download and harmonise every input dataset for a domain and period."""
    return delegate("preprocess", "run")(
        *args, **kwargs)


def weather(*args, **kwargs):
    """Prepare the climate inputs only."""
    return delegate("preprocess", "weather")(*args, **kwargs)


def soil(*args, **kwargs):
    """Prepare the soil inputs only."""
    return delegate("preprocess", "soil")(*args, **kwargs)


def crop_calendar(*args, **kwargs):
    """Prepare the crop calendar (planting day, season length) only."""
    return delegate("preprocess", "crop_calendar")(*args, **kwargs)


def crop_area(*args, **kwargs):
    """Prepare the crop area mask only."""
    return delegate("preprocess", "crop_area")(*args, **kwargs)
