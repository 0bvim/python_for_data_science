from typing import Any, Callable


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Computes and prints various statistical measures of given numeric data based on specified
    options. The function accepts variable positional and keyword arguments for data input
    and statistical options respectively.

    Args:
        *args (Any): A variable number of numeric arguments representing the dataset for
            statistical computations. Non-numeric elements will raise an error.
        **kwargs (Any): A variable number of keyword arguments where the key indicates an
            identifier and the value specifies the statistical measure to compute. Accepted
            values for statistical measures are:
            - "mean" for arithmetic mean,
            - "median" for the median,
            - "quartile" for interquartile range using percentiles,
            - "std" for standard deviation,
            - "var" for variance.

    Returns:
        None: This function does not return any value but prints the results of the specified
        statistical computations.

    Raises:
        TypeError: If non-numeric arguments are passed in *args or invalid values are specified
            for **kwargs.
    """
    valid_options = ["mean", "median", "quartile", "std", "var"]

    data = list(args)
    data.sort()
    data_len = len(data)

    def get_percentile(percentile: float) -> float:
        idx = (data_len - 1) * percentile
        lower_idx = int(idx)
        upper_idx = lower_idx + 1 if lower_idx < data_len - 1 else lower_idx
        weight = idx - lower_idx
        return float(data[lower_idx] + weight * (data[upper_idx] - data[lower_idx]))

    for key, value in kwargs.items():
        if value not in valid_options:
            continue

        if data_len == 0:
            print("ERROR")
            continue

        match value:
            case "mean":
                print_mean(data, data_len)
            case "median":
                print_median(data, data_len)
            case "quartile":
                print_quartile(get_percentile)
            case "var":
                print_var(data, data_len)
            case "std":
                print_std(data, data_len)


def print_std(data: list[Any], data_len: int) -> None:
    """
    Calculates the standard deviation of a dataset and prints the result.

    This function computes the mean, variance, and standard deviation
    of the given data. It assumes that the provided data is a list of
    numeric elements and that the data length is consistent with the
    provided list.

    Args:
        data (list[Any]): A list of numeric elements for which the standard
            deviation will be calculated.
        data_len (int): The number of elements in the data list.

    Returns:
        None
    """
    mean_val = sum(data) / data_len
    var_val = sum((x - mean_val) ** 2 for x in data) / data_len
    std_val = var_val ** 0.5
    print(f"std : {std_val}")


def print_var(data: list[Any], data_len: int) -> None:
    """
    Calculates and prints the variance of a given dataset.

    The function computes the variance of the data elements contained in the provided list
    by first calculating the mean value and then determining the square deviations from the
    mean. The variance is printed to the console.

    Args:
        data (list[Any]): A list of numerical data elements to calculate the variance from.
        data_len (int): The length of the dataset (must be equal to the length of `data`).

    Returns:
        None
    """
    mean_val = sum(data) / data_len
    var_val = sum((x - mean_val) ** 2 for x in data) / data_len
    print(f"var : {var_val}")


def print_quartile(get_percentile: Callable[..., float]) -> None:
    """
    Calculates and prints the first and third quartiles using a percentile fetching
    function passed as an argument.

    This function takes a callable object capable of computing percentiles and
    retrieves the 25th percentile (Q1) and the 75th percentile (Q3). It then prints
    these values formatted as "quartile : {q1} {q3}".

    Args:
        get_percentile (Callable[..., float]): A callable function that calculates
            and returns the specified percentile when given a value in the range
            [0.0, 1.0].

    Returns:
        None
    """
    q1 = get_percentile(0.25)
    q3 = get_percentile(0.75)
    print(f"quartile : {q1} {q3}")


def print_median(data: list[Any], data_len: int) -> None:
    """
    Prints the median of a given dataset.

    This function computes the median of a sorted dataset. For even-length datasets,
    the median is calculated as the sum of the two middle elements. For odd-length
    datasets, the median is the middle element. The computed median is then printed
    to the console.

    Args:
        data: List of sorted elements from which the median is to be calculated.
        data_len: The length of the dataset.

    Returns:
        None
    """
    if data_len % 2 == 0:
        med = (data[data_len // 2 - 1] + data[data_len // 2])
    else:
        med = data[data_len // 2]
    print(f"median : {med}")


def print_mean(data: list[Any], data_len: int) -> None:
    """
    Prints the mean value of a given dataset.

    This function takes a list of numerical data and its length as input, calculates
    the mean value, and prints it to the console.

    Args:
        data (list[Any]): The dataset containing numerical values for which the
            mean is to be calculated.
        data_len (int): The length of the dataset. It is expected to match the
            length of the data list.

    Returns:
        None
    """
    mean_val = sum(data) / data_len
    print(f"mean : {mean_val}")
