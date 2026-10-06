Installation
============

Everything at once (recommended)
--------------------------------

.. code-block:: bash

   conda create -n geoaquacrop python=3.11
   conda activate geoaquacrop
   python -m pip install geoaquacrop

This installs all three sub-packages.

Individual packages
-------------------

.. code-block:: bash

   python -m pip install geoaquacrop_preprocess      # data preparation only
   python -m pip install geoaquacrop_simulate          # simulation only
   python -m pip install geoaquacrop_visualize   # visualisation only

Which do I need?
----------------

* **Model outputs for a region, starting from nothing** — all three.
* **Already have gridded climate, soil and crop inputs** — ``gac.simulate``
  alone; see its documentation for the expected file layout.
* **Already have simulation outputs** — ``gac.visualize`` alone.
* **Building your own pipeline** — each package has a documented Python API and
  works independently.

Credentials
-----------

Downloading **past** climate data (AgERA5) needs a free
`Copernicus CDS account <https://cds.climate.copernicus.eu/>`_ and a personal
API token. Future climate projections (NASA NEX-GDDP-CMIP6) need no
credentials. See the
`preprocessing documentation <https://geoaquacrop_preprocessing.readthedocs.io/en/latest/installation.html>`_
for details.

Verify
------

.. code-block:: python

   import geoaquacrop as gac

   print(gac.__version__)
   print([stage for stage in dir(gac) if not stage.startswith("_")])
   # ['preprocess', 'simulate', 'visualize']

Each stage loads on first use, so this import stays fast however many stages
are installed.
