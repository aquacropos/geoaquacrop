"""Gridded AquaCrop simulation — :mod:`geoaquacrop.simulate`.

Façade over the ``geoaquacrop_simulate`` package::

    import geoaquacrop as gac

    config = gac.simulate.example_config()
    summary_file, daily_file = gac.simulate.run(config)

Every name here is re-exported from ``geoaquacrop_simulate``; the two are
interchangeable, so code written against either keeps working.
"""
from ._util import delegate, require

__all__ = ["run", "example_config", "input_requirements", "build_reference",
           "correct", "compare", "load_results"]


def run(config=None):
    """Run a simulation for every cell in the domain.

    Parameters
    ----------
    config : dict, optional
        Simulation configuration; see :func:`example_config`. Defaults to the
        built-in example, which is only useful as a template.

    Returns
    -------
    tuple
        ``(summary_file, daily_file)``, or ``(None, None)`` if the call only
        corrected an already-saved run.
    """
    return delegate("simulate", "run")(config)


def example_config():
    """Return an editable copy of the example simulation configuration."""
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
