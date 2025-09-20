"""
Pytest configuration and fixtures for WBTSdata tests.
"""
import sys
import os
from pathlib import Path

# Add the project root to Python path so WBTSdata can be imported
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import pytest
import numpy as np
import xarray as xr
import tempfile
import yaml


@pytest.fixture
def sample_config():
    """Create a sample configuration dictionary for testing."""
    return {
        'input_dir': '../data/input',
        'output_dir': '../data',
        'GC_2001_04': {
            'Cruise': {
                'cruise_id': 'AB0104 / OC365-9',
                'start_date': '2001-04-26',
                'end_date': '2001-05-07',
                'ship': 'R/V OCEANUS',
                'sections': 'Abaco and Northwest Providence Channel Sections'
            }
        }
    }


@pytest.fixture
def sample_config_file(tmp_path, sample_config):
    """Create a temporary config.yaml file for testing."""
    config_file = tmp_path / "config.yaml"
    with open(config_file, 'w') as f:
        yaml.dump(sample_config, f)
    return str(config_file)


@pytest.fixture
def sample_ctd_dataset():
    """Create a sample CTD dataset for testing."""
    np.random.seed(42)  # For reproducible tests
    
    # Create sample dimensions
    n_time = 10
    n_depth = 50
    
    # Create coordinate arrays
    datetime = np.datetime64('2001-04-26T12:00:00') + np.arange(n_time) * np.timedelta64(1, 'h')
    depth = np.linspace(0, 500, n_depth)
    latitude = np.full(n_time, 26.5)
    longitude = np.full(n_time, -77.0)
    
    # Create sample data variables
    temp = 20 + 5 * np.random.random((n_time, n_depth))
    psal = 35 + 2 * np.random.random((n_time, n_depth))
    pres = np.broadcast_to(depth, (n_time, n_depth))
    
    # Create dataset
    ds = xr.Dataset(
        {
            'TEMP': (['DATETIME', 'DEPTH'], temp),
            'PSAL': (['DATETIME', 'DEPTH'], psal),
            'PRES': (['DATETIME', 'DEPTH'], pres),
        },
        coords={
            'DATETIME': datetime,
            'DEPTH': depth,
            'LATITUDE': (['DATETIME'], latitude),
            'LONGITUDE': (['DATETIME'], longitude),
        }
    )
    
    # Add attributes
    ds.attrs['title'] = 'Test CTD data'
    ds.attrs['instrument'] = 'CTD'
    ds['TEMP'].attrs = {'units': 'degree_C', 'long_name': 'Temperature'}
    ds['PSAL'].attrs = {'units': '1e-3', 'long_name': 'Practical Salinity'}
    ds['PRES'].attrs = {'units': 'dbar', 'long_name': 'Pressure'}
    
    return ds


@pytest.fixture
def sample_adcp_dataset():
    """Create a sample ADCP dataset for testing."""
    np.random.seed(42)
    
    # Create sample dimensions
    n_time = 10
    n_depth = 30
    
    # Create coordinate arrays
    datetime = np.datetime64('2001-04-26T12:00:00') + np.arange(n_time) * np.timedelta64(1, 'h')
    depth = np.linspace(10, 300, n_depth)
    latitude = np.full(n_time, 26.5)
    longitude = np.full(n_time, -77.0)
    
    # Create sample velocity data
    u_vel = 0.1 * np.random.random((n_time, n_depth)) - 0.05
    v_vel = 0.1 * np.random.random((n_time, n_depth)) - 0.05
    err_vel = 0.01 * np.random.random((n_time, n_depth))
    
    # Create dataset
    ds = xr.Dataset(
        {
            'U_WATER_VELOCITY': (['DATETIME', 'DEPTH'], u_vel),
            'V_WATER_VELOCITY': (['DATETIME', 'DEPTH'], v_vel),
            'ERROR_VELOCITY': (['DATETIME', 'DEPTH'], err_vel),
        },
        coords={
            'DATETIME': datetime,
            'DEPTH': depth,
            'LATITUDE': (['DATETIME'], latitude),
            'LONGITUDE': (['DATETIME'], longitude),
        }
    )
    
    # Add attributes
    ds.attrs['title'] = 'Test ADCP data'
    ds.attrs['instrument'] = 'LADCP'
    ds['U_WATER_VELOCITY'].attrs = {'units': 'm/s', 'long_name': 'Eastward velocity'}
    ds['V_WATER_VELOCITY'].attrs = {'units': 'm/s', 'long_name': 'Northward velocity'}
    ds['ERROR_VELOCITY'].attrs = {'units': 'm/s', 'long_name': 'Error velocity'}
    
    return ds


@pytest.fixture
def sample_netcdf_file(tmp_path, sample_ctd_dataset):
    """Create a temporary NetCDF file for testing."""
    nc_file = tmp_path / "test_data.nc"
    sample_ctd_dataset.to_netcdf(nc_file)
    return str(nc_file)


@pytest.fixture
def temp_directory():
    """Create a temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield tmp_dir


@pytest.fixture
def mock_data_structure(tmp_path):
    """Create a mock data directory structure for testing."""
    # Create directory structure
    base_dir = tmp_path / "test_data"
    ctd_dir = base_dir / "cruise_2001" / "CTD"
    adcp_dir = base_dir / "cruise_2001" / "FINAL_ADCP_PRODUCTS" / "ladcp_velfiles"
    merged_dir = base_dir / "Merged"
    
    for directory in [ctd_dir, adcp_dir, merged_dir]:
        directory.mkdir(parents=True, exist_ok=True)
    
    # Create some dummy files
    (ctd_dir / "test_ctd_001.cal").write_text("dummy ctd data")
    (adcp_dir / "test_001d.vel").write_text("dummy adcp data")
    
    return {
        'base_dir': str(base_dir),
        'ctd_dir': str(ctd_dir),
        'adcp_dir': str(adcp_dir),
        'merged_dir': str(merged_dir)
    }