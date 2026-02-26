import os

import numpy as np
from matplotlib import image as mpimg


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from disk into a NumPy array.

    This function uses matplotlib.image.imread to read the image file at the
    provided path and returns it as a NumPy array. The returned array shape
    depends on the image type: grayscale images will typically have shape
    (H, W), RGB images (H, W, 3), and RGBA images (H, W, 4). The array dtype
    depends on the image file and matplotlib's backend (for example, PNGs may
    be loaded as float arrays with values in [0, 1], while JPEGs may be
    uint8).

    Parameters
    ----------
    path : str
        Filesystem path to the image to load.

    Returns
    -------
    numpy.ndarray
        The image data as a NumPy array.

    Raises
    ------
    FileNotFoundError
        If the path does not exist.
    Exception
        Any exception raised by matplotlib.image.imread is propagated.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Image not found: {path}")

    image = np.empty(0)
    try:
        image = mpimg.imread(path)
        print(f"The shape of image is: {image.shape}")
        print(image)
    except Exception:
        raise

    return image
