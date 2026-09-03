# GeoAquaCrop

> Run FAO AquaCrop over large regions in gridded format — from raw global datasets to interactive results.

![Python](https://img.shields.io/badge/python-3.11%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green)

## One import, three stages

```python
import geoaquacrop as gac

gac.preprocess.run(...)        # download & harmonise the input datasets
gac.simulate.run(config)       # run AquaCrop for every grid cell
gac.visualize.launch()         # explore the results
```

That is the whole API. Each stage is a separately maintained package, but you
never need to know their names: `geoaquacrop` presents them as one library.

```
gac.preprocess  ->  gac.simulate  ->  gac.visualize
```

| Stage | What it does | Documentation |
| ----- | ------------ | ------------- |
| `gac.preprocess` | Downloads and harmonises climate, soil, crop calendar and crop area data onto a common grid for a given polygon and period | [readthedocs](https://geoaquacrop-preprocessing.readthedocs.io/en/stable/) |
| `gac.simulate` | Runs AquaCrop per grid cell in parallel; optional yield bias-correction and calibration against observations | [readthedocs](https://geoaquacrop-simulate.readthedocs.io) |
| `gac.visualize` | Interactive Dash/Plotly dashboard for exploring simulation outputs and climate inputs | [github.io](https://sehohosseini.github.io/Geoaquacrop-visualizer/) |

## Installation

```bash
conda create -n geoaquacrop python=3.11
conda activate geoaquacrop
python -m pip install --pre geoaquacrop
```

The `--pre` flag is needed while the toolchain is in beta (`0.1.0b1`); pip skips
pre-release versions otherwise. This installs all three stages.

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
summary_file, daily_file = simulate.run(config)
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
config = gac.simulate.example_config()
config.update({
    'weather_path': '/data/high_plains/processed',
    'soil_path':    '/data/high_plains/processed',
    'pheno_path':   '/data/high_plains/processed',
    'spam_path':    '/data/high_plains/processed',
    'start_date':   '2011/01/01',
    'end_date':     '2013/12/31',
    'crop':         'Wheat_winter',
    'irrigation':   'rainfed',
    'output_dir':   'outputs',
})
summary_file, daily_file = gac.simulate.run(config)

# 3. explore the results
gac.visualize.launch()          # then open http://localhost:8050
```

## What each stage offers

```python
gac.preprocess.run(...)                 # prepare every dataset
gac.preprocess.weather(...)             # or re-run a single step
gac.preprocess.soil(...)
gac.preprocess.crop_calendar(...)
gac.preprocess.crop_area(...)

gac.simulate.run(config)                # simulate; returns (summary, daily)
gac.simulate.example_config()           # a config template to edit
gac.simulate.input_requirements()       # print required files and units
gac.simulate.build_reference(...)       # per-year, region-level yield reference
gac.simulate.correct(config)            # bias-correct a saved run, no re-run
gac.simulate.compare([...])             # comparison figures and statistics
gac.simulate.load_results(path)         # saved results as tidy per-year points

gac.visualize.launch()                  # start the dashboard
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
- **Preprocessing** — <https://geoaquacrop-preprocessing.readthedocs.io/en/stable/>
- **Simulation** — <https://geoaquacrop-simulate.readthedocs.io>
- **Visualisation** — <https://sehohosseini.github.io/Geoaquacrop-visualizer/>

Contributors: see [the stage package standard](https://geoaquacrop.readthedocs.io/en/latest/standard.html)
for the naming and API contract each stage follows.

## Citation

If you use GeoAquaCrop in published work, please cite the toolchain and the
underlying [FAO AquaCrop](https://www.fao.org/aquacrop) model.

## License

MIT — see [LICENSE](LICENSE).
