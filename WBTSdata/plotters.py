import numpy as np
import matplotlib.pyplot as plt


def plot_cast_over_time(ds_all):
    '''
    Plot the cast over time for the given dataset. The dataset should contain the following variables:
    - DATETIME: The datetime of the cast
    - LONGITUDE: The longitude of the cast
    - GC_STRING: The gc_string of the cast
    
    Parameters
    ----------
    ds_all : xarray.Dataset
        The dataset containing the data to plot.
        
    Returns
    -------
    fig, ax : matplotlib.figure.Figure, matplotlib.axes.Axes
        The figure and axes of the plot.
    '''
    fig, ax = plt.subplots(figsize=(15, 8))
    ax.set_title('Cast over Time', fontsize=15)

    # Plot the main data
    ax.plot(ds_all['DATETIME'], -ds_all['LONGITUDE'], marker='+', linestyle='None', label='Station')

    # Plot the unique gc_strings
    unique_gc_strings = np.unique(ds_all['GC_STRING'].values)
    for gc in unique_gc_strings:
        avg_datetime = ds_all['DATETIME'].where(ds_all['GC_STRING'] == gc).mean().values
        min_lon = ds_all['LONGITUDE'].where(ds_all['GC_STRING'] == gc).min().values - 2
        min_lon = 85
        ax.text(avg_datetime, min_lon, gc, rotation=90, fontsize=15)

    # Append °W to all the longitudes in the ytick label
    yticks = ax.get_yticks()
    ytick_labels = [f'{ytick}°W' for ytick in yticks]
    ax.set_yticks(yticks)  # Set the tick positions first
    ax.set_yticklabels(ytick_labels)

    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)
    ax.invert_yaxis()
    ax.set_xlabel('Year', fontsize=15)
    ax.set_ylabel('Longitude', fontsize=15)
    ax.legend(fontsize=15)
    
    return fig, ax
