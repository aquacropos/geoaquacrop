# GeoAquaCrop

> Run FAO AquaCrop over large regions in gridded format — from raw global datasets to interactive results.

![Python](https://img.shields.io/badge/python-3.11%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green)

**GeoAquaCrop** is a toolchain for gridded crop water productivity modelling. It is distributed as three independent packages plus this meta-package, which installs all three together.

```
geoaquacrop_preproc  ->  geoaquacrop_simulate  ->  geoaquacrop_visualizer
(download & harmonise)   (simulate & correct)  (explore results)
```

| Package | What it does | Docs |
| ------- | ------------ | ---- |
| [**geoaquacrop_preproc**](https://github.com/josiasritter/geoaquacrop_preproc-dev) | Downloads and harmonises climate, soil, crop calendar and crop area data onto a common grid for a given polygon and period | [readthedocs](https://geoaquacrop_preprocessing.readthedocs.io/en/stable/) |
| [**geoaquacrop_simulate**](https://github.com/<your-org>/geoaquacrop_simulate) | Runs AquaCrop per grid cell in parallel; optional yield bias-correction and calibration against observations | [readthedocs](https://geoaquacrop_simulate.readthedocs.io) |
| [**geoaquacrop_visualizer**](https://github.com/sehohosseini/geoaquacrop_visualize) | Interactive Dash/Plotly dashboard for exploring simulation outputs and climate inputs | [github.io](https://sehohosseini.github.io/geoaquacrop_visualize/) |

## Installation

```bash
conda create -n geoaquacrop python=3.11
conda activate geoaquacrop
python -m pip install --pre geoaquacrop
```

The `--pre` flag is needed while the toolchain is in beta (`0.1.0b1`); pip
skips pre-release versions otherwise.

That installs all three sub-packages. To install only what you need:

```bash
python -m pip install geoaquacrop_preproc      # data preparation only
python -m pip install geoaquacrop_simulate          # simulation only
python -m pip install geoaquacrop_visualizer   # visualisation only
```

**For past climate data** you also need a free [Copernicus CDS account](https://cds.climate.copernicus.eu/) and API token — see the preproc documentation.

## End-to-end example

A complete run for a region of interest, in three steps.

### 1. Prepare the input data

```python
from geoaquacrop_preproc import geoaquacrop_preproc

geoaquacrop_preproc(
    domain_shape_path='high_plains.geojson',   # polygon, EPSG:4326
    start_year=2008,
    end_year=2010,
    api_token='your-copernicus-api-token',
    cell_resolution=0.05,
    workingdirectory='/data/high_plains',
)
```

Writes harmonised NetCDF and GeoTIFF datasets to `/data/high_plains/processed/`.

### 2. Run the simulation

```python
from geoaquacrop_sim.run_aquacrop import main

# edit config_dict in run_aquacrop.py, pointing all four input paths at
# /data/high_plains/processed, then:
summary_file, daily_file = main()
```

Writes per-cell seasonal and daily results to `outputs/`.

### 3. Explore the results

```bash
python -m geoaquacrop_visualizer     # then open http://localhost:8050
```

Point the visualiser's configuration at the simulation `outputs/` folder and the preprocessing `processed/` folder.

## Which package do I need?

- **Just want model outputs for a region?** All three: preproc → sim → visualizer.
- **Already have gridded climate/soil/crop inputs?** `geoaquacrop_simulate` alone — see its documentation for the required file layout.
- **Already have simulation outputs?** `geoaquacrop_visualizer` alone.
- **Building your own pipeline?** Each package has a documented Python API and can be used independently.

## Documentation

This page is a signpost. Detailed installation, configuration and API reference live with each package:

- **Preprocessing** — <https://geoaquacrop_preprocessing.readthedocs.io/en/stable/>
- **Simulation** — <https://geoaquacrop_simulate.readthedocs.io>
- **Visualisation** — <https://sehohosseini.github.io/geoaquacrop_visualize/>

## Citation

If you use GeoAquaCrop in published work, please cite the toolchain and the underlying [FAO AquaCrop](https://www.fao.org/aquacrop) model.

## License

MIT — see [LICENSE](LICENSE).
