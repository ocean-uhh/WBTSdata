.. WBTSdata documentation master file

========================================================
WBTSdata: Western Boundary Time Series Data Processing
========================================================

WBTSdata is a Python package for loading, processing, and visualizing data from the Western Boundary Time Series (WBTS) project. The package provides tools for handling oceanographic CTD and ADCP data with functions for data loading, conversion, plotting, and analysis.

Overview
--------

The WBTS is a comprehensive observational program designed to monitor the Atlantic Meridional Overturning Circulation (AMOC) and its associated boundary currents, such as the Florida and Antilles Currents. These observations are critical for understanding the role of ocean circulation in regulating global climate and assessing changes over time.

The program is primarily conducted by the National Oceanic and Atmospheric Administration (NOAA). Data are collected along hydrographic sections using ship-based methods, which include:

- **Lowered Acoustic Doppler Current Profiler (LADCP)**: Measures water velocity throughout the water column, providing detailed insights into the flow patterns of boundary currents.
- **Conductivity-Temperature-Depth (CTD)**: Measures the physical properties of seawater, such as temperature, salinity, and density, which are essential for characterizing oceanographic conditions.

The calibrated WBTS data, including LADCP and CTD measurements, are made publicly available through NOAA's Atlantic Oceanographic and Meteorological Laboratory (AOML) at https://www.aoml.noaa.gov/western-boundary-time-series/.

Key Features
------------

- Load and process CTD oceanographic data from NetCDF files
- Data conversion utilities for WBTS datasets  
- Visualization functions for time series and profile data
- Data merging and quality control tools
- Support for ADCP velocity data
- Integration with the scientific Python ecosystem (xarray, pandas, matplotlib)

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   Installation and Setup <installation>

.. toctree::
   :maxdepth: 1
   :caption: Examples

   demo-output.ipynb

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   WBTSdata

.. toctree::
   :maxdepth: 1
   :caption: Project Links

   GitHub Repository <https://github.com/ocean-uhh/WBTSdata>
   WBTS Data Portal <https://www.aoml.noaa.gov/western-boundary-time-series/>

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
