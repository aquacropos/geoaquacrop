"""Gridded AquaCrop simulation — :mod:`geoaquacrop.simulate`.

Thin façade over ``geoaquacrop.simulate``::

    import geoaquacrop as gac

    summary, daily = gac.simulate.run(config)
    gac.sim.build_reference(regions='provinces.geojson', region_id='NAME_LATN',
                            table='yields.csv', table_id='region',
                            year_col='year', value_col='yield_t_ha',
                            out='reference.geojson')
    gac.simulate.correct(config)                 # correct a saved run, no re-run
    gac.simulate.compare([...])                  # comparison figures + statistics
"""
from ._util import require



def _mod(name):
    import importlib
    require("geoaquacrop.simulate")
    return importlib.import_module(f"geoaquacrop.simulate.{name}")


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
    return _mod("run_aquacrop").run(config)


def example_config():
    """Return a copy of the example configuration, to edit and pass to
    :func:`run`."""
    import copy
    return copy.deepcopy(_mod("run_aquacrop").EXAMPLE_CONFIG)


def input_requirements():
    """Print the input files a simulation needs, with units and naming."""
    return _mod("run_aquacrop").print_input_requirements()


def build_reference(**kwargs):
    """Build a per-year, region-level yield reference from a boundary file and
    a statistics table. See ``geoaquacrop_sim.build_reference.build``."""
    return _mod("build_reference").build(**kwargs)


def correct(config, logger=None):
    """Bias-correct or calibrate an already-saved run, without re-simulating.

    Requires ``config['correction']['reuse_results']`` to be set.
    """
    return _mod("correction").correct_saved_run(config, logger=logger)


def compare(args=None):
    """Compare corrected runs against the reference: per-year maps, region
    difference maps, a domain time series and a statistics table."""
    return _mod("compare_corrections").main(args)


def load_results(path, value_col="Dry yield (tonne/ha)", start_year=None):
    """Load a saved ``summary_results_*.pkl`` as tidy per-year points
    ``[year, y, x, val]``."""
    import pickle
    correction = _mod("correction")
    with open(path, "rb") as fh:
        summary_results = pickle.load(fh)
    return correction.summary_to_points(summary_results, value_col, start_year)


__all__ = ["run", "example_config", "input_requirements", "build_reference",
           "correct", "compare", "load_results"]
