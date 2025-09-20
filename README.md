# WBTSdata

[![Documentation Status](https://github.com/ocean-uhh/WBTSdata/actions/workflows/docs_deploy.yml/badge.svg)](https://ocean-uhh.github.io/WBTSdata/)

A Python package for loading, processing, and visualizing data from the WBTS (Western Boundary Time Series) project. This package provides tools for handling oceanographic CTD (Conductivity-Temperature-Depth) data with functions for data loading, conversion, plotting, and analysis.

## Features

- Load and process CTD oceanographic data from NetCDF files
- Data conversion utilities for WBTS datasets
- Visualization functions for time series and profile data
- Data merging and quality control tools
- Support for ADCP velocity data
- Integration with the scientific Python ecosystem (xarray, pandas, matplotlib)

## Installation

### Using pip (recommended)

Clone the repository and install in development mode:

```bash
git clone https://github.com/ocean-uhh/WBTSdata.git
cd WBTSdata
pip install -e .
```

### Using conda/mamba

Create a conda environment with all dependencies:

```bash
git clone https://github.com/ocean-uhh/WBTSdata.git
cd WBTSdata
conda env create -f environment.yml
conda activate WBTSdata
pip install -e . --no-deps
```

## Quick Start

```python
from WBTSdata import plotters, tools, convert

# Load and plot oceanographic data
# (See notebooks/ directory for detailed examples)
```

## Documentation

- **API Documentation**: [https://ocean-uhh.github.io/WBTSdata/](https://ocean-uhh.github.io/WBTSdata/)
- **Examples**: See the `notebooks/` directory for Jupyter notebook examples
- **Data**: Example datasets are available in the `data/` directory

## Project Structure

```
WBTSdata/
├── WBTSdata/           # Main package
│   ├── plotters.py     # Visualization functions
│   ├── convert.py      # Data conversion utilities  
│   ├── tools.py        # General utility functions
│   ├── load_vel_files.py # Velocity data loading
│   └── merge_datasets.py # Dataset merging
├── notebooks/          # Example Jupyter notebooks
├── data/              # Data files
├── docs/              # Documentation source
└── tests/             # Test suite
```

## Development

### Setting up development environment

```bash
git clone https://github.com/ocean-uhh/WBTSdata.git
cd WBTSdata
pip install -r requirements-dev.txt
pip install -e .
```

### Running tests

```bash
pytest
```

### Building documentation

```bash
cd docs/
make html
```

The built documentation will be available in `docs/build/html/`.

### Code formatting

This project uses pre-commit hooks for code quality:

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes
4. Run tests and ensure code passes pre-commit checks
5. Commit your changes (`git commit -m 'Add new feature'`)
6. Push to the branch (`git push origin feature/new-feature`)
7. Open a Pull Request

## Citation

If you use this software in your research, please cite it:

```bibtex
@software{wbtsdata,
  author = {Moritz, Till and Frajka-Williams, Eleanor},
  title = {WBTSdata},
  version = {0.0.1},
  year = {2025},
  url = {https://github.com/ocean-uhh/WBTSdata}
}
```

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

## Authors

- **Till Moritz** - University of Hamburg
- **Eleanor Frajka-Williams** - University of Hamburg

## Acknowledgments

- Western Boundary Time Series project
- AOML/NOAA for data provision
- University of Hamburg - Institute of Oceanography