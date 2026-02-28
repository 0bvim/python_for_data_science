import matplotlib.pyplot as plt
from load_image import ft_load
from pimp_image import ft_blue, ft_green, ft_grey, ft_invert, ft_red


def main():
    """
    Loads an image, applies 5 color filters, prints the invert docstring,
    and displays all images in a 2x3 grid.
    """
    try:
        # Load the original image
        array = ft_load("landscape.jpg")

        if array is None:
            print("Failed to load image. Exiting.")
            return

        # Apply all the filters
        img_invert = ft_invert(array)
        img_red = ft_red(array)
        img_green = ft_green(array)
        img_blue = ft_blue(array)
        img_grey = ft_grey(array)

        # Print the docstring as requested by the subject
        if ft_invert.__doc__:
            print(ft_invert.__doc__.strip())

        # Set up a 2x3 grid for the images
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))

        # Figure VIII.1: Original
        axes[0, 0].imshow(array)
        axes[0, 0].set_title("Figure VIII.1: Original")
        axes[0, 0].axis("off")  # Hides the axis numbers for a cleaner look

        # Figure VIII.2: Invert
        axes[0, 1].imshow(img_invert)
        axes[0, 1].set_title("Figure VIII.2: Invert")
        axes[0, 1].axis("off")

        # Figure VIII.3: Red
        axes[0, 2].imshow(img_red)
        axes[0, 2].set_title("Figure VIII.3: Red")
        axes[0, 2].axis("off")

        # Figure VIII.4: Green
        axes[1, 0].imshow(img_green)
        axes[1, 0].set_title("Figure VIII.4: Green")
        axes[1, 0].axis("off")

        # Figure VIII.5: Blue
        axes[1, 1].imshow(img_blue)
        axes[1, 1].set_title("Figure VIII.5: Blue")
        axes[1, 1].axis("off")

        # Figure VIII.6: Grey
        # We pass cmap='gray' here so Matplotlib knows how to map the single-channel intensity
        axes[1, 2].imshow(img_grey, cmap="gray")
        axes[1, 2].set_title("Figure VIII.6: Grey")
        axes[1, 2].axis("off")

        # Adjust layout so titles don't overlap and display the window
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An unexpected error occurred in the tester: {e}")


if __name__ == "__main__":
    main()
