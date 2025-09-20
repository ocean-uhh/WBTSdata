Coding Conventions
==================

This document outlines the coding conventions and best practices for the WBTSdata project.

Code Style
----------

- **Python Code**: Follow PEP 8 style guidelines
- **Line Length**: Maximum 88 characters (Black formatter default)
- **Import Organization**: Use isort for consistent import ordering
- **Code Formatting**: Use Black for automatic code formatting

Documentation
-------------

- **Docstrings**: Use NumPy-style docstrings for all functions and classes
- **Type Hints**: Include type hints for function parameters and return values where appropriate
- **Comments**: Write clear, concise comments for complex logic

Example docstring format:

.. code-block:: python

    def load_ctd_data(file_path, quality_control=True):
        """
        Load CTD data from a NetCDF file.
        
        Parameters
        ----------
        file_path : str
            Path to the NetCDF file containing CTD data.
        quality_control : bool, optional
            Whether to apply automatic quality control, by default True.
            
        Returns
        -------
        xarray.Dataset
            CTD data with coordinates and attributes.
            
        Examples
        --------
        >>> ds = load_ctd_data('data/ctd_2023.nc')
        >>> print(ds.temperature.shape)
        """

Code Quality
------------

- **Pre-commit Hooks**: Use pre-commit for automatic code quality checks
- **Testing**: Write tests for new functionality using pytest
- **Error Handling**: Include appropriate error handling and informative error messages
- **Naming**: Use descriptive variable and function names

Git Workflow
------------

- **Commit Messages**: Write clear, descriptive commit messages
- **Branch Names**: Use descriptive branch names (e.g., `fix/ctd-loading-bug`, `feat/add-velocity-plots`)
- **Pull Requests**: Use the provided PR template and include tests for new features

Dependencies
------------

- **Core Dependencies**: Keep core dependencies minimal and well-justified
- **Version Pinning**: Pin development dependencies in requirements-dev.txt
- **Documentation**: Update requirements files when adding new dependencies

Data Handling
-------------

- **File Paths**: Use pathlib.Path for cross-platform compatibility
- **NetCDF Files**: Follow CF conventions for metadata and variable naming
- **Memory Management**: Be mindful of memory usage when processing large datasets
- **Data Validation**: Include checks for expected data formats and ranges