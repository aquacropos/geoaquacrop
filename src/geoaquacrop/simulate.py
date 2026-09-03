"""Gridded AquaCrop simulation — :mod:`geoaquacrop.simulate`.

Façade over the ``geoaquacrop_simulate`` package::

    import geoaquacrop as gac

    summary_file, daily_file = gac.simulate.run(
        data_path='/data/region/processed',
        start_date='2011/01/01', end_date='2013/12/31',
        crop='Wheat_winter', irrigation='rainfed')

Every name here is re-exported from ``geoaquacrop_simulate``; the two are
interchangeable, so code written against either keeps working.
"""
from ._util import delegate, require

__all__ = ["run", "example_config", "input_requirements", "build_reference",
           "correct", "compare", "load_results"]


def run(config=None, **kwargs):
    """Run a simulation for every cell in the domain.

    Settings are given as keyword arguments::

        gac.simulate.run(data_path='/data/region/processed',
                         start_date='2011/01/01', end_date='2013/12/31',
                         crop='Wheat_winter', irrigation='rainfed')

    ``data_path`` fills all four input paths at once. See
    :func:`example_config` for every available setting, or the stage
    documentation for the full reference.

    Parameters
    ----------
    config : dict, optional
        A configuration dictionary to start from, for programmatic use; any
        keyword argument overrides the matching entry.
    **kwargs
        Simulation settings such as ``data_path``, ``start_date``,
        ``end_date``, ``crop``, ``irrigation``, ``output_dir``, ``correction``.

    Returns
    -------
    tuple
        ``(summary_file, daily_file)``, or ``(None, None)`` if the call only
        corrected an already-saved run.
    """
    return delegate("simulate", "run")(config, **kwargs)


def example_config():
    """Return the example configuration, to inspect the available settings.

    Not a required step: :func:`run` takes the same settings as keyword
    arguments. Useful for seeing every key and its default.
    """
    return delegate("simulate", "example_config")()


def input_requirements():
    """Print the input files a simulation needs, with units and naming."""
    return delegate("simulate", "input_requirements",
                    "print_input_requirements")()


def build_reference(**kwargs):
    """Build a per-year, region-level yield reference from a boundary file and
    a statistics table."""
    return delegate("simulate", "build_reference")(**kwargs)


def correct(config, logger=None):
    """Bias-correct or calibrate an already-saved run, without re-simulating."""
    return delegate("simulate", "correct")(config, logger=logger)


def compare(args=None):
    """Compare corrected runs against the reference: per-year maps, region
    difference maps, a domain time series and a statistics table."""
    return delegate("simulate", "compare")(args)


def load_results(path, value_col="Dry yield (tonne/ha)", start_year=None):
    """Load a saved ``summary_results_*.pkl`` as tidy per-year points."""
    return delegate("simulate", "load_results")(path, value_col, start_year)
