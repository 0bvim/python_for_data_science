import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Convert the input sequence to a NumPy array, slice it, and return the slice as a Python list.

    This helper converts the provided `family` argument to a NumPy array, prints the array
    shape before and after slicing (for debugging), and returns the sliced portion as a list.
    Slicing uses standard NumPy indexing semantics (start inclusive, end exclusive), so negative
    indices are supported.

    Parameters
    ----------
    family : list
        A list or list-like object to be converted to a NumPy array and sliced.
    start : int
        Start index for the slice (inclusive). Supports negative indices.
    end : int
        End index for the slice (exclusive). Supports negative indices.

    Returns
    -------
    list
        The sliced portion of `family`, converted back to a Python list. If converting
        `family` to a NumPy array raises a ValueError, an empty list is returned.

    Notes
    -----
    The function prints the shapes of the array before and after slicing to standard output.
    These prints are intended for debugging and can be removed or replaced by proper logging
    in production code.

    Examples
    --------
    >>> slice_me([1, 2, 3, 4], 1, 3)
    My shape is : (4,)
    My new shape is : (2,)
    [2, 3]
    """ # noqa
    try:
        family_arr = np.array(family)
    except ValueError as e:
        print(f"Error: {e}")
        return []

    print(f"My shape is : {family_arr.shape}")

    sliced_family_array = family_arr[start:end]
    print(f"My new shape is : {sliced_family_array.shape}")

    return sliced_family_array.tolist()
