GeoAquaCrop
===========

**GeoAquaCrop** runs `FAO AquaCrop <https://www.fao.org/aquacrop>`_ over large
regions in gridded format — from raw global datasets through to interactive
exploration of results.

One import, three stages
------------------------

.. code-block:: python

   import geoaquacrop as gac

   gac.preprocess.run(...)        # download & harmonise the input datasets
   gac.simulate.run(config)       # run AquaCrop for every grid cell
   gac.visualize.launch()         # explore the results

That is the whole API. Each stage is a separately maintained package, but you
never need to know their names: ``geoaquacrop`` presents them as one library.

.. code-block:: text

   gac.preprocess  ->  gac.simulate  ->  gac.visualize

.. list-table::
   :header-rows: 1
   :widths: 20 52 28

   * - Stage
     - What it does
     - Documentation
   * - ``gac.preprocess``
     - Downloads and harmonises climate, soil, crop calendar and crop area
       data onto a common grid for a given polygon and period
     - `readthedocs <https://geoaquacrop-preprocessing.readthedocs.io/en/stable/>`_
   * - ``gac.simulate``
     - Runs AquaCrop per grid cell in parallel; optional yield bias-correction
       and calibration against observations
     - `readthedocs <https://geoaquacrop-simulate.readthedocs.io>`_
   * - ``gac.visualize``
     - Interactive Dash/Plotly dashboard for exploring simulation outputs and
       climate inputs
     - `github.io <https://sehohosseini.github.io/Geoaquacrop-visualizer/>`_

Importing ``geoaquacrop`` is cheap: each stage -- and its dependencies -- loads
only when you first use it. If a stage is not installed, calling it tells you
exactly what to install.

Each stage also works standalone with the same function names, so
``gac.simulate.run`` and ``geoaquacrop_simulate.run`` are interchangeable.

.. toctree::
   :caption: Getting started
   :maxdepth: 1

   installation
   walkthrough_TODO

.. toctree::
   :caption: Reference
   :maxdepth: 1

   api
   standard

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
