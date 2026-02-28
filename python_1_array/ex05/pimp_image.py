import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    inverted_array = 255 - array

    plt.imshow(inverted_array)
    plt.show()

    return inverted_array


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Applies a red filter to the image received.
    """
    red_array = array * np.array([1, 0, 0])

    plt.imshow(red_array)
    plt.show()

    return red_array


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Applies a green filter to the image received.
    """
    green_array = array.copy()

    green_array[:, :, 0] = (
        green_array[:, :, 0] - green_array[:, :, 0]
    )  # red becomes 0

    green_array[:, :, 2] = (
        green_array[:, :, 2] - green_array[:, :, 2]
    )  # blue becomes 0

    plt.imshow(green_array)
    plt.show()

    return green_array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Applies a blue filter to the image received.
    """
    blue_array = array.copy()

    blue_array[:, :, 0] = 0  # red becomes 0
    blue_array[:, :, 1] = 0  # green becomes 0

    plt.imshow(blue_array)
    plt.show()

    return blue_array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Applies a green filter to the image received.
    """
    grey_array = array.copy()

    # Grayscale is normally (R+G+B)/3. Since we CANNOT use '+', we use np.sum()
    # as a function to handle the addition,
    # and then use our allowed '/' operator.
    grey_channel = np.sum(array, axis=2) / 3

    grey_array[:, :, 0] = grey_channel
    grey_array[:, :, 1] = grey_channel
    grey_array[:, :, 2] = grey_channel

    plt.imshow(grey_array)
    plt.show()

    return grey_array
