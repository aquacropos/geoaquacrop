"""Input data preparation — :mod:`geoaquacrop.preprocess`.

Thin façade over ``geoaquacrop.preprocess``::

    import geoaquacrop as gac

    gac.preprocess.run(domain_shape_path='region.geojson', start_year=2011,
                       end_year=2013, api_token='...', cell_resolution=0.05,
                       workingdirectory='/data/region')

`run` prepares every dataset a simulation needs. The per-dataset helpers
(:func:`weather`, :func:`soil`, :func:`crop_calendar`, :func:`crop_area`) are
provided for re-running a single stage; each maps to the corresponding
function in ``geoaquacrop_preproc``, and raises a clear error if that version
of the package does not expose it separately.
"""
from ._util import require


def _pkg():
    return require("geoaquacrop.preprocess")


def _call(candidates, *args, **kwargs):
    """Call the first attribute that exists, so the façade tolerates the
    upstream package renaming its entry points."""
    pkg = _pkg()
    for name in candidates:
        fn = getattr(pkg, name, None)
        if callable(fn):
            return fn(*args, **kwargs)
    raise AttributeError(
        f"geoaquacrop_preproc exposes none of {candidates}. It may not provide "
        f"this step as a separate function in the installed version; use "
        f"geoaquacrop.preprocess.run(...) to prepare all datasets together.")


def run(*args, **kwargs):
    """Download and harmonise every input dataset for a domain and period."""
    return _call(("geoaquacrop.preprocess", "preprocess", "run", "main"),
                 *args, **kwargs)


def weather(*args, **kwargs):
    """Prepare the climate inputs only."""
    return _call(("weather", "preprocess_weather", "climate"), *args, **kwargs)


def soil(*args, **kwargs):
    """Prepare the soil inputs only."""
    return _call(("soil", "preprocess.soil"), *args, **kwargs)


def crop_calendar(*args, **kwargs):
    """Prepare the crop calendar (planting day, season length) only."""
    return _call(("crop_calendar", "preprocess.crop_calendar", "phenology"),
                 *args, **kwargs)


def crop_area(*args, **kwargs):
    """Prepare the crop area mask only."""
    return _call(("crop_area", "preprocess.crop_area", "spam"), *args, **kwargs)


__all__ = ["run", "weather", "soil", "crop_calendar", "crop_area"]
