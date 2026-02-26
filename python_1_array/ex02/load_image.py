import numpy as np
from matplotlib import image as mpimg


def ft_load(path: str) -> np.ndarray:
    image = np.empty(0)
    try:
        image = mpimg.imread(path)
        print(f"The shape of image is: {image.shape}")
        print(image)
    except Exception as e:
        print(f"Error loading image '{path}': {e}")

    return image
