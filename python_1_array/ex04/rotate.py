import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def main() -> None:
    """Load an image, extract a rectangular region and a single channel,
    transpose that region, and display it as a grayscale image.

    Detailed behavior:
    - Loads the image file "animal.jpeg" using ft_load (expected to return a NumPy
      array with shape (height, width, channels)).
    - Extracts a rectangular sub-region defined by rows 100..499 and columns 400..799,
      and selects the first channel. The slice image_array[100:500, 400:800, 0:1]
      therefore has shape (400, 400, 1).
    - Manually transposes the 2D channel by iterating over indices and building a
      new list-of-lists where the new element at (i, j) is taken from the original
      channel at (j, i). This demonstrates explicit element access and rearrangement.
    - Converts the transposed list back to a NumPy array, prints its shape and contents,
      then squeezes out the singleton channel dimension and displays the result with
      matplotlib using a grayscale colormap.
    - The function prints diagnostic information but does not return a value.

    Notes:
    - The manual transpose via Python loops is intentionally explicit for demonstration.
      For production code with NumPy arrays, using transposed_array = zoomed_array[:, :, 0].T
      or np.transpose would be more concise and faster.
    """
    image_path = "animal.jpeg"
    image_array = ft_load(image_path)

    zoomed_array = image_array[100:500, 400:800, 0:1]

    rows = len(zoomed_array[0])
    cols = len(zoomed_array[1])

    transposed_list = []
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(zoomed_array[j][i][0])
        transposed_list.append(new_row)

    # Convert back to a NumPy array so we can inspect shape and display it.
    transposed_array = np.array(transposed_list)
    print(f"New shape after transpose: {transposed_array.shape}")
    print(transposed_array)

    display_array = transposed_array.squeeze()
    plt.imshow(display_array, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
