<p align="center">
  <img src="https://raw.githubusercontent.com/aquacropos/geoaquacrop/main/docs/_static/logo.png"
       alt="" width="360">
</p>

<p align="center">Run AquaCrop-OSPy over large regions in gridded format — from raw global datasets to interactive results.</p>

<p align="center">
  <a href="https://pypi.org/project/geoaquacrop/"><img src="https://img.shields.io/pypi/v/geoaquacrop" alt="PyPI"></a>
  <a href="https://pypi.org/project/geoaquacrop/"><img src="https://img.shields.io/pypi/pyversions/geoaquacrop" alt="Python"></a>
  <a href="https://geoaquacrop.readthedocs.io/en/stable/"><img src="https://img.shields.io/readthedocs/geoaquacrop" alt="Docs"></a>
  <a href="https://github.com/aquacropos/geoaquacrop/actions/workflows/tests.yml"><img src="https://github.com/aquacropos/geoaquacrop/actions/workflows/tests.yml/badge.svg" alt="Tests"></a>
  <a href="https://github.com/aquacropos/geoaquacrop/blob/main/LICENSE"><img src="https://img.shields.io/badge/licence-Apache%202.0-blue" alt="Licence"></a>
</p>

## One import, three stages

```python
import geoaquacrop as gac

gac.preprocess.run(...)        # download & harmonise the input datasets
gac.simulate.run(...)          # run AquaCrop for every grid cell
gac.visualize.run()         # explore the results
```

That is the whole API. Each stage is a separately maintained package, but you
never need to know their names: `geoaquacrop` presents them as one library.

```
gac.preprocess  ->  gac.simulate  ->  gac.visualize
```

| Stage | What it does | Repository | Documentation |
| ----- | ------------ | ---------- | ------------- |
| `gac.preprocess` | Downloads and harmonises climate, soil, crop calendar and crop area data onto a common grid for a given polygon and period | [geoaquacrop_preprocess](https://github.com/aquacropos/geoaquacrop_preprocess) | [readthedocs](https://geoaquacrop-preprocess.readthedocs.io/en/latest/) |
| `gac.simulate` | Runs AquaCrop per grid cell in parallel; optional yield bias-correction and calibration against observations | [geoaquacrop_simulate](https://github.com/aquacropos/geoaquacrop_simulate) | [readthedocs](https://geoaquacrop-simulate.readthedocs.io) |
| `gac.visualize` | Interactive Dash/Plotly dashboard for exploring simulation outputs and climate inputs | [geoaquacrop_visualize](https://github.com/aquacropos/geoaquacrop_visualize) | [readthedocs](https://geoaquacrop-visualize.readthedocs.io/en/latest/) |

## Installation

```bash
conda create -n geoaquacrop python=3.11
conda activate geoaquacrop
python -m pip install geoaquacrop
```

This installs all three stages.

**For past climate data** you also need a free [Copernicus CDS account](https://cds.climate.copernicus.eu/)
and API token — see the preprocessing documentation.

<details>
<summary>Installing a single stage</summary>

Each stage also works standalone, with the same function names:

```bash
python -m pip install geoaquacrop_preprocess    # data preparation only
python -m pip install geoaquacrop_simulate      # simulation only
python -m pip install geoaquacrop_visualize     # visualisation only
```

```python
import geoaquacrop_simulate as simulate
summary_file, daily_file = simulate.run(data_path='...', start_date='...',
                                        end_date='...', crop='Wheat_winter')
```

`gac.simulate.run` and `geoaquacrop_simulate.run` are the same function, so
code written against either keeps working.
</details>

## End-to-end example

A complete run for one region, using only `gac`.

```python
import geoaquacrop as gac

# 1. prepare the input data
gac.preprocess.run(
    domain_shape_path='high_plains.geojson',   # polygon, EPSG:4326
    start_year=2011,
    end_year=2013,
    api_token='your-copernicus-api-token',
    cell_resolution=0.05,
    workingdirectory='/data/high_plains',
)

# 2. run the simulation
summary_file, daily_file = gac.simulate.run(
    data_path='/data/high_plains/processed',   # fills all four input paths
    start_date='2011/01/01',
    end_date='2013/12/31',
    crop='Wheat_winter',
    irrigation='rainfed',
    output_dir='outputs',
)

# 3. explore the results
gac.visualize.run()          # then open http://localhost:8050
```

## What each stage offers

```python
gac.preprocess.run(...)                 # prepare every dataset
gac.preprocess.weather(...)             # or re-run a single step
gac.preprocess.soil(...)
gac.preprocess.crop_calendar(...)
gac.preprocess.crop_area(...)

gac.simulate.run(data_path=..., ...)    # simulate; returns (summary, daily)
gac.simulate.example_config()           # inspect every available setting
gac.simulate.input_requirements()       # print required files and units
gac.simulate.build_reference(...)       # per-year, region-level yield reference
gac.simulate.correct(config)            # bias-correct a saved run, no re-run
gac.simulate.compare([...])             # comparison figures and statistics
gac.simulate.load_results(path)         # saved results as tidy per-year points

gac.visualize.run()                  # start the dashboard
```

Importing `geoaquacrop` is cheap: each stage — and its dependencies — loads only
when you first use it. If a stage is not installed, calling it tells you exactly
what to install.

## Which stage do I need?

- **Model outputs for a region, starting from nothing** — all three.
- **Already have gridded climate, soil and crop inputs** — `gac.simulate` alone.
- **Already have simulation outputs** — `gac.visualize` alone.

## Documentation

- **This toolchain** — <https://geoaquacrop.readthedocs.io>
- **Preprocessing** — <https://geoaquacrop-preprocess.readthedocs.io/en/latest/>
- **Simulation** — <https://geoaquacrop-simulate.readthedocs.io>
- **Visualisation** — <https://geoaquacrop-visualize.readthedocs.io/en/latest/>

Contributors: see [the stage package standard](https://geoaquacrop.readthedocs.io/en/latest/standard.html)
for the naming and API contract each stage follows.

## Citation

If you use GeoAquaCrop in published work, please cite the toolchain and the
underlying [AquaCrop-OSPy](https://github.com/aquacropos/aquacrop) model.

A preprint will be published soon. Until then, please cite:

> Láng-Ritter, J., Bowden, C., Hosseini, S., Alkio, E., Tenkanen, H. & Foster, T. GeoAquaCrop: Large-scale agricultural crop modelling using open global data

## License

Apache-2.0 — see [LICENSE](LICENSE).
