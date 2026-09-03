GeoAquaCrop
===========

**GeoAquaCrop** is a toolchain for running
`AquaCrop-OSPy <https://github.com/aquacropos/aquacrop>`_ over large regions in gridded
format — from raw global datasets through to interactive exploration of
results.

It is distributed as three independent packages, plus a meta-package
(``geoaquacrop``) that installs all three together.

.. code-block:: text

   geoaquacrop_preproc  ->  geoaquacrop_simulate  ->  geoaquacrop_visualizer
   (download & harmonise)   (simulate & correct)  (explore results)

.. list-table::
   :header-rows: 1
   :widths: 22 50 28

   * - Package
     - What it does
     - Documentation
   * - **geoaquacrop.preprocess**
     - Downloads and harmonises climate, soil, crop calendar and crop area
       data onto a common grid for a given polygon and period
     - `readthedocs <https://geoaquacrop.preprocess.readthedocs.io/en/stable/>`_
   * - **geoaquacrop.simulate**
     - Runs AquaCrop per grid cell in parallel; optional yield bias-correction
       and calibration against observations
     - `readthedocs <https://geoaquacrop.simulate.readthedocs.io>`_
   * - **geoaquacrop_visualize**
     - Interactive Dash/Plotly dashboard for exploring simulation outputs and
       climate inputs
     - `github.io <https://sehohosseini.github.io/geoaquacrop.visualize/>`_

This site is an overview and signpost. Detailed installation, configuration and
API reference live with each package.

.. toctree::
   :caption: Contents
   :maxdepth: 1

   installation
   standard
   api
   walkthrough_TODO
