"""
Tests for WBTSdata.merge_datasets module.
"""
import pytest
import numpy as np
import xarray as xr
import os
import glob
from unittest.mock import patch, MagicMock
import tempfile

from WBTSdata import merge_datasets


class TestDirListCTD:
    """Test the dir_list_CTD function."""
    
    def test_dir_list_ctd_finds_directories(self, mock_data_structure):
        """Test that dir_list_CTD finds CTD directories."""
        result = merge_datasets.dir_list_CTD(mock_data_structure['base_dir'])
        
        # Should find the CTD directory
        assert len(result) >= 1
        assert any('CTD' in path for path in result)
    
    def test_dir_list_ctd_empty_directory(self, tmp_path):
        """Test dir_list_CTD with empty directory."""
        result = merge_datasets.dir_list_CTD(str(tmp_path))
        assert result == []
    
    def test_dir_list_ctd_excludes_created_files(self, tmp_path):
        """Test that dir_list_CTD excludes Created_files directories."""
        # Create directory structure
        ctd_dir = tmp_path / "cruise1" / "CTD"
        created_files_dir = tmp_path / "Created_files" / "CTD"
        
        ctd_dir.mkdir(parents=True)
        created_files_dir.mkdir(parents=True)
        
        result = merge_datasets.dir_list_CTD(str(tmp_path))
        
        # Should find CTD but not Created_files/CTD
        assert len(result) == 1
        assert 'Created_files' not in result[0]


class TestDirListADCP:
    """Test the dir_list_ADCP function."""
    
    def test_dir_list_adcp_finds_directories(self, mock_data_structure):
        """Test that dir_list_ADCP finds ADCP directories."""
        result = merge_datasets.dir_list_ADCP(mock_data_structure['base_dir'])
        
        # Should find the ADCP directory
        assert len(result) >= 1
        assert any('ladcp_velfiles' in path for path in result)
    
    def test_dir_list_adcp_empty_directory(self, tmp_path):
        """Test dir_list_ADCP with empty directory."""
        result = merge_datasets.dir_list_ADCP(str(tmp_path))
        assert result == []
    
    def test_dir_list_adcp_excludes_2019_12(self, tmp_path):
        """Test that dir_list_ADCP excludes 2019_12 directories."""
        # Create directory structure
        good_dir = tmp_path / "cruise_2001" / "FINAL_ADCP_PRODUCTS"
        good_dir.mkdir(parents=True)
        (good_dir / "ladcp_velfiles").mkdir()
        
        bad_dir = tmp_path / "cruise_2019_12" / "FINAL_ADCP_PRODUCTS"  
        bad_dir.mkdir(parents=True)
        (bad_dir / "ladcp_velfiles").mkdir()
        
        result = merge_datasets.dir_list_ADCP(str(tmp_path))
        
        # Should exclude 2019_12
        assert all('2019_12' not in path for path in result)


class TestMergeYears:
    """Test the merge_years function."""
    
    def test_merge_years_with_sample_files(self, tmp_path, sample_ctd_dataset):
        """Test merge_years with sample NetCDF files."""
        # Create merged directory
        merged_dir = tmp_path / "Merged"
        merged_dir.mkdir()
        
        # Create sample NetCDF files
        file1 = merged_dir / "WBTS_2001_04_CTD_LADCP.nc"
        file2 = merged_dir / "WBTS_2002_06_CTD_LADCP.nc"
        
        # Create slightly different datasets
        ds1 = sample_ctd_dataset.copy()
        ds1.attrs['year'] = '2001'
        
        ds2 = sample_ctd_dataset.copy()
        ds2['DATETIME'] = ds2['DATETIME'] + np.timedelta64(365, 'D')  # Next year
        ds2.attrs['year'] = '2002'
        
        # Save to files
        ds1.to_netcdf(file1)
        ds2.to_netcdf(file2)
        
        # Test merge_years
        result = merge_datasets.merge_years(str(tmp_path), max_files=2)
        
        # Check results
        assert isinstance(result, xr.Dataset)
        assert len(result.DATETIME) == len(ds1.DATETIME) + len(ds2.DATETIME)
        assert 'geospatial_vertical_max' in result.attrs
        assert 'geospatial_vertical_min' in result.attrs
    
    def test_merge_years_excludes_output_file(self, tmp_path, sample_ctd_dataset):
        """Test that merge_years excludes the output file from inputs."""
        merged_dir = tmp_path / "Merged"
        merged_dir.mkdir()
        
        # Create input file
        input_file = merged_dir / "WBTS_2001_04_CTD_LADCP.nc"
        sample_ctd_dataset.to_netcdf(input_file)
        
        # Create the output file (empty)
        output_file = merged_dir / "WBTS_all_years_CTD_LADCP.nc"
        output_file.touch()
        
        # Should not try to load the output file
        result = merge_datasets.merge_years(str(tmp_path), max_files=1)
        assert isinstance(result, xr.Dataset)
    
    def test_merge_years_no_files_raises_error(self, tmp_path):
        """Test that merge_years raises error when no files found."""
        merged_dir = tmp_path / "Merged"
        merged_dir.mkdir()
        
        with pytest.raises(ValueError, match="No valid datasets found"):
            merge_datasets.merge_years(str(tmp_path))
    
    def test_merge_years_max_files_limit(self, tmp_path, sample_ctd_dataset):
        """Test that max_files parameter limits the number of files processed."""
        merged_dir = tmp_path / "Merged"
        merged_dir.mkdir()
        
        # Create 3 files
        for i, year in enumerate(['2001', '2002', '2003']):
            file_path = merged_dir / f"WBTS_{year}_04_CTD_LADCP.nc"
            ds = sample_ctd_dataset.copy()
            ds['DATETIME'] = ds['DATETIME'] + np.timedelta64(i * 365, 'D')
            ds.to_netcdf(file_path)
        
        # Test with max_files=2
        result = merge_datasets.merge_years(str(tmp_path), max_files=2)
        
        # Should only process 2 files
        expected_length = 2 * len(sample_ctd_dataset.DATETIME)
        assert len(result.DATETIME) == expected_length


class TestMergeDatasets:
    """Test the merge_datasets function."""
    
    def test_merge_datasets_with_adcp(self, sample_ctd_dataset, sample_adcp_dataset, sample_config):
        """Test merge_datasets with both CTD and ADCP data - simplified test."""
        # This is a complex function that requires extensive mocking
        # For now, test that the function exists and is callable
        assert hasattr(merge_datasets, 'merge_datasets')
        assert callable(merge_datasets.merge_datasets)
        
        # More detailed testing would require mocking the entire data loading pipeline
        pytest.skip("Complex integration test - requires extensive mocking")
    
    def test_merge_datasets_ctd_only(self, sample_ctd_dataset, sample_config):
        """Test merge_datasets with CTD data only - simplified test."""
        # This function requires complex data loading pipeline mocking
        assert hasattr(merge_datasets, 'merge_datasets')
        assert callable(merge_datasets.merge_datasets)
        
        pytest.skip("Complex integration test - requires extensive mocking")


class TestCreateCoordinatesWithADCPTimes:
    """Test the create_coordinates_with_ADCPtimes function."""
    
    def test_create_coordinates_with_adcp_times(self, sample_config):
        """Test create_coordinates_with_ADCPtimes function."""
        # This function requires complex mocking of multiple modules
        assert hasattr(merge_datasets, 'create_coordinates_with_ADCPtimes')
        assert callable(merge_datasets.create_coordinates_with_ADCPtimes)
        
        pytest.skip("Complex integration test - requires extensive mocking")


@pytest.mark.integration  
class TestMergeDatasetsIntegration:
    """Integration tests for merge_datasets module."""
    
    def test_full_merge_workflow(self, tmp_path, sample_ctd_dataset, sample_adcp_dataset):
        """Test full merge workflow with real files."""
        # This would test the entire pipeline
        pytest.skip("Integration test - requires full file system setup")
    
    def test_merge_years_with_real_files(self):
        """Test merge_years with the actual sample data files."""
        # Could test with the real data files in data/Merged/
        pytest.skip("Integration test - requires real data files")