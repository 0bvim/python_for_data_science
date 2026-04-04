import os
import subprocess
import sys

import matplotlib.pyplot as plt
from load_image import ft_load


def main() -> None:
    """Load an image, extract a grayscale zoomed region, and display it.

    This function performs the following steps:
    - Loads an image from the hard-coded path "animal.jpeg" using ft_load.
    - Extracts a sub-region (rows 100 to 499, columns 400 to 799) and
      selects the first channel (slice 0:1), resulting in an array with a
      singleton third dimension.
    - Prints the new shape of the sliced array and the array contents.
    - Removes the singleton channel dimension with squeeze() to obtain a 2D
      array suitable for grayscale display.
    - Displays the resulting 2D array using matplotlib.pyplot.imshow with a
      grayscale colormap.

    Notes:
    - The function has no parameters and returns None.
    - It performs I/O (loading an image file and opening a plot window).
    - Exceptions may be raised if the image file is missing, unreadable, or
      if ft_load returns an array with unexpected dimensions.
    """
    image_path = "animal.jpeg"
    file_name = "zoomed_animal.png"
    image_array = ft_load(image_path)

    zoomed_array = image_array[100:500, 400:800, 0:1]
    print(f"New shape after slicing: {zoomed_array.shape}")
    print(zoomed_array)

    display_array = zoomed_array.squeeze()
    plt.imshow(display_array, cmap="gray")
    plt.title("Cropped Zoomed Animal")
    plt.savefig(file_name)

    open_file(file_name)


def open_file(file_path: str) -> None:
    file_path = "zoomed_animal.png"
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


if __name__ == "__main__":
    main()
