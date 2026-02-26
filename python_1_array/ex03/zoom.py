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
    image_array = ft_load(image_path)

    zoomed_array = image_array[100:500, 400:800, 0:1]
    print(f"New shape after slicing: {zoomed_array.shape}")
    print(zoomed_array)

    display_array = zoomed_array.squeeze()
    plt.imshow(display_array, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
