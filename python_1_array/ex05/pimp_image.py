import os
import subprocess
import sys

import matplotlib.pyplot as plt
import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    file_name = "inverted.png"
    inverted_array = 255 - array

    plt.imshow(inverted_array)
    plt.title("Inverted Image")
    plt.savefig(file_name)

    open_file(file_name)

    return inverted_array


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Applies a red filter to the image received.
    """
    red_array = array * np.array([1, 0, 0])
    file_name = "red.png"

    plt.imshow(red_array)
    plt.title("Red Filter")
    plt.savefig(file_name)

    open_file(file_name)

    return red_array


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Applies a green filter to the image received.
    """
    green_array = array.copy()
    file_name = "green.png"

    green_array[:, :, 0] = green_array[:, :, 0] - green_array[:, :, 0]  # red becomes 0

    green_array[:, :, 2] = green_array[:, :, 2] - green_array[:, :, 2]  # blue becomes 0

    plt.imshow(green_array)
    plt.title("Green Filter")
    plt.savefig(file_name)

    open_file(file_name)

    return green_array


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Applies a blue filter to the image received.
    """
    blue_array = array.copy()
    file_name = "blue.png"

    blue_array[:, :, 0] = 0  # red becomes 0
    blue_array[:, :, 1] = 0  # green becomes 0

    plt.imshow(blue_array)
    plt.title("Blue Filter")
    plt.savefig(file_name)

    open_file(file_name)

    return blue_array


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Applies a green filter to the image received.
    """
    grey_array = array.copy()
    file_name = "grey.png"

    # Grayscale is normally (R+G+B)/3. Since we CANNOT use '+', we use np.sum()
    # as a function to handle the addition,
    # and then use our allowed '/' operator.
    grey_channel = np.sum(array, axis=2) / 3

    grey_array[:, :, 0] = grey_channel
    grey_array[:, :, 1] = grey_channel
    grey_array[:, :, 2] = grey_channel

    plt.imshow(grey_array)
    plt.title("Grey Filter")
    plt.savefig(file_name)

    open_file(file_name)

    return grey_array


def open_file(file_path: str) -> None:
    try:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
        else:
            if sys.platform.startswith("win"):
                # Windows
                os.startfile(file_path)
            elif sys.platform == "darwin":
                # macOS
                subprocess.run(["open", file_path], check=False)
            else:
                # Linux/Unix (xdg-open is the common tool)
                subprocess.run(["xdg-open", file_path], check=False)
    except Exception as e:
        print(f"Could not open {file_path}: {e}")
