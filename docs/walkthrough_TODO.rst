End-to-end walkthrough
======================

A complete run for one region, in three steps. Each step links to the package
documentation for the full set of options.

1. Prepare the input data
-------------------------

.. code-block:: python

   from geoaquacrop_preproc import geoaquacrop_preproc

   geoaquacrop_preproc(
       domain_shape_path='high_plains.geojson',   # polygon, EPSG:4326
       start_year=2008,
       end_year=2010,
       api_token='your-copernicus-api-token',
       cell_resolution=0.05,
       workingdirectory='/data/high_plains',
   )

Writes harmonised climate, soil, crop calendar and crop area datasets to
``/data/high_plains/processed/``. The climate source is chosen automatically:
AgERA5 reanalysis for past periods, NASA NEX-GDDP-CMIP6 projections otherwise.

See the
`preprocessing quick start <https://geoaquacrop.preprocess.readthedocs.io/en/stable/quickstart.html>`_.

2. Run the simulation
---------------------

Point all four input paths at the ``processed`` folder from step 1:

.. code-block:: python

   config_dict = {
       'weather_path': '/data/high_plains/processed',
       'soil_path':    '/data/high_plains/processed',
       'pheno_path':   '/data/high_plains/processed',
       'spam_path':    '/data/high_plains/processed',
       'start_date':   '2008/01/01',
       'end_date':     '2010/12/31',
       'crop':         'Maize',
       'irrigation':   'rainfed',
       'output_dir':   'outputs',
   }

.. code-block:: python

   from geoaquacrop_sim.run_aquacrop import main

   summary_file, daily_file = main()

Writes per-cell seasonal and daily results to ``outputs/``. Optionally
bias-corrects or calibrates yields against an observational reference — see the
`simulation documentation <https://geoaquacrop.simulate.readthedocs.io>`_.

3. Explore the results
----------------------

.. code-block:: bash

   python -m geoaquacrop_visualizer

Then open http://localhost:8050. Point the visualiser's configuration at the
simulation ``outputs/`` folder and the preprocessing ``processed/`` folder.

See the
`visualiser overview <https://sehohosseini.github.io/geoaquacrop.visualize/overview.html>`_.

Keeping the pieces consistent
-----------------------------

* Use the **same grid resolution** throughout: the simulation inherits its grid
  from the preprocessing outputs, and the visualiser expects that same grid.
* Use the **same domain polygon** for preprocessing and for any reference
  dataset used in yield correction.
* The simulation period must fall inside the period the climate files cover.
