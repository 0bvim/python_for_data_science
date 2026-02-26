import numpy as np


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """
    Compute body mass index (BMI) for corresponding height and weight lists.

    BMI is calculated as weight divided by the square of height (weight / height^2).
    Heights and weights must be provided as sequences of numeric values of the same length.
    Heights are expected to be in units that match the units used for weight such that
    the resulting BMI is meaningful (for example: weight in kilograms and height in meters).

    Parameters
    ----------
    height : list[int | float]
        Sequence of heights.
    weight : list[int | float]
        Sequence of weights corresponding to each height.

    Returns
    -------
    list[int | float]
        List of BMI values (one per input pair), returned as Python floats.

    Raises
    ------
    AssertionError
        If the input lists have different lengths.
    """ # noqa
    if len(height) != len(weight):
        raise AssertionError(
            "list have different size. It must have same size."
        )

    h_arr = np.array(height)
    w_arr = np.array(weight)

    bmi = w_arr / (h_arr**2)

    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a threshold to a sequence of BMI values.

    For each value in the input BMI list, determine whether it is strictly greater
    than the provided limit.

    Parameters
    ----------
    bmi : list[int | float]
        Sequence of BMI values to check. Each value must be an int or float.
    limit : int
        Numeric threshold to compare against.

    Returns
    -------
    list[bool]
        A list of booleans where each element is True if the corresponding BMI
        value is greater than the limit, otherwise False.

    Raises
    ------
    AssertionError
        If the bmi list contains non-numeric values.
    """ # noqa
    check_value(bmi, "bmi")

    bmi_arr = np.array(bmi)

    return (bmi_arr > limit).tolist()


def check_value(lst: list[int | float], name: str) -> None:
    """
    Validate that a list contains only numeric (int or float) values.

    Booleans are explicitly rejected because they are subclasses of int in Python.

    Parameters
    ----------
    lst : list[int | float]
        The list to validate.
    name : str
        Name of the list (used in the error message) for clearer diagnostics.

    Raises
    ------
    AssertionError
        If any element in lst is not an int or float, or if it is a bool.
    """ # noqa
    if not all(
        isinstance(x, (int, float)) and not isinstance(x, bool) for x in lst
    ):
        raise AssertionError(
            f"{name} list must contain only int or float values"
        )
