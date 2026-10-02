End-to-end walkthrough
======================

.. note::

   Draft. The commands below are correct but have not yet been run end to end
   on a fresh machine.

A complete run for one region, using only ``gac``. Each step links to the stage
documentation for the full set of options.

.. code-block:: python

   import geoaquacrop as gac

1. Prepare the input data
-------------------------

.. code-block:: python

   gac.preprocess.run(
       domain_shape_path='region.geojson',   # polygon, EPSG:4326
       start_year=2011,
       end_year=2013,
       api_token='your-copernicus-api-token',
       cell_resolution=0.05,
       workingdirectory='/data/region',
   )

Writes harmonised climate, soil, crop calendar and crop area datasets to
``/data/region/processed/``. The climate source is chosen automatically:
AgERA5 reanalysis for past periods, NASA NEX-GDDP-CMIP6 projections otherwise.

To re-run a single dataset rather than all of them:

.. code-block:: python

   gac.preprocess.soil(...)
   gac.preprocess.weather(...)

See the `preprocessing quick start
<https://geoaquacrop-preprocessing.readthedocs.io/en/stable/quickstart.html>`_.

2. Run the simulation
---------------------

Point all four input paths at the ``processed`` folder from step 1:

.. code-block:: python

   summary_file, daily_file = gac.simulate.run(
       data_path='/data/region/processed',   # fills all four input paths
       start_date='2011/01/01',
       end_date='2013/12/31',
       crop='Wheat_winter',
       irrigation='rainfed',
       output_dir='outputs',
   )

``gac.simulate.input_requirements()`` prints the files this expects, with units
and naming, if you want to check the preprocessing output first.

Optionally bias-correct or calibrate the yields against observations:

.. code-block:: python

   gac.simulate.build_reference(
       regions='provinces.geojson', region_id='NAME_LATN',
       table='yields.csv', table_id='region',
       year_col='year', value_col='yield_t_ha',
       out='reference.geojson')

See the `simulation documentation <https://geoaquacrop-simulate.readthedocs.io>`_.

3. Explore the results
----------------------

.. code-block:: python

   gac.visualize.run()      # then open http://localhost:8050

Point the visualiser's configuration at the simulation ``outputs/`` folder and
the preprocessing ``processed/`` folder.

See the `visualiser overview
<https://geoaquacrop-visualize.readthedocs.io/en/latest/>`_.

Keeping the stages consistent
-----------------------------

* Use the **same grid resolution** throughout: the simulation inherits its grid
  from the preprocessing outputs, and the visualiser expects that same grid.
* Use the **same domain polygon** for preprocessing and for any reference
  dataset used in yield correction.
* The simulation period must fall inside the period the climate files cover.
