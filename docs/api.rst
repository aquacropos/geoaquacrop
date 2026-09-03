Unified API
===========

Installing ``geoaquacrop`` gives one import that reaches all three stages::

    import geoaquacrop as gac

    gac.preprocess.run(...)      # download & harmonise input datasets
    gac.simulate.run(config)          # simulate every grid cell
    gac.visualize.run()             # explore the results

The stage packages remain fully usable on their own -- this is a thin,
curated façade whose names stay stable even if the internals move. Submodules
load lazily, so ``import geoaquacrop`` is cheap and a stage's dependencies are
only imported when you first touch that stage. If a stage is not installed,
using it raises an error telling you what to install.

preprocess
----------

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Call
     - Purpose
   * - ``gac.preprocess.run(...)``
     - Prepare every input dataset for a domain and period
   * - ``gac.preprocess.weather(...)``
     - Climate inputs only
   * - ``gac.preprocess.soil(...)``
     - Soil inputs only
   * - ``gac.preprocess.crop_calendar(...)``
     - Planting day and season length only
   * - ``gac.preprocess.crop_area(...)``
     - Crop area mask only

simulate
---

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Call
     - Purpose
   * - ``gac.simulate.run(config)``
     - Run the simulation; returns ``(summary_file, daily_file)``
   * - ``gac.simulate.example_config()``
     - A configuration template to edit and pass to ``run``
   * - ``gac.simulate.input_requirements()``
     - Print the required input files, units and naming
   * - ``gac.simulate.build_reference(...)``
     - Build a per-year, region-level yield reference
   * - ``gac.simulate.correct(config)``
     - Bias-correct a saved run without re-simulating
   * - ``gac.simulate.compare([...])``
     - Comparison figures and statistics against the reference
   * - ``gac.simulate.load_results(path)``
     - Load saved results as tidy per-year points

visualize
---

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Call
     - Purpose
   * - ``gac.visualize.launch()``
     - Start the interactive dashboard

Example
-------

.. code-block:: python

   import geoaquacrop as gac

   # 1. prepare inputs
   gac.preprocess.run(domain_shape_path='region.geojson',
                      start_year=2011, end_year=2013,
                      api_token='...', cell_resolution=0.05,
                      workingdirectory='/data/region')

   # 2. simulate
   config = gac.simulate.example_config()
   config.update({
       'weather_path': '/data/region/processed',
       'soil_path':    '/data/region/processed',
       'pheno_path':   '/data/region/processed',
       'spam_path':    '/data/region/processed',
       'start_date':   '2011/01/01',
       'end_date':     '2013/12/31',
       'crop':         'Wheat_winter',
       'irrigation':   'rainfed',
       'output_dir':   'outputs',
   })
   summary_file, daily_file = gac.simulate.run(config)

   # 3. explore
   gac.visualize.launch()

Reference
---------

.. automodule:: geoaquacrop
   :members:

.. automodule:: geoaquacrop.simulate
   :members:

.. automodule:: geoaquacrop.preprocess
   :members:

.. automodule:: geoaquacrop.visualize
   :members:
