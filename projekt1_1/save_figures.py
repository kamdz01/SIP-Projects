import os
import matplotlib.pyplot as plt


def save_fig(
    fig,
    filename,
    directory="figures",
    dpi=300,
    formats=("png", "pdf"),
    bbox_inches="tight",
    transparent=False,
):
    """
    Save a figure in multiple formats with specified parameters.

    Parameters:
    -----------
    fig : matplotlib.figure.Figure
        The figure to save. If None, plt.gcf() will be used.
    filename : str
        The base filename without extension
    directory : str
        The directory to save the figure in
    dpi : int
        Resolution for the figure
    formats : tuple
        File formats to save the figure in
    bbox_inches : str
        How to handle the edges of the figure
    transparent : bool
        Whether to save with transparent background

    Returns:
    --------
    tuple
        Paths to the saved files
    """
    # Create directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

    # If no figure provided, use current figure
    if fig is None:
        fig = plt.gcf()

    saved_files = []

    # Save the figure in each format
    for fmt in formats:
        filepath = os.path.join(directory, f"{filename}.{fmt}")
        fig.savefig(filepath, dpi=dpi, bbox_inches=bbox_inches, transparent=transparent)
        saved_files.append(filepath)
        print(f"Figure saved: {filepath}")

    return saved_files
