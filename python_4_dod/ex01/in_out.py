def square(x: int | float) -> int | float:
    """
    Calculates the square of a number.

    This function takes a numeric value as input and returns its square by
    multiplying the number by itself.

    Args:
        x: A number to be squared. Can be of type int or float.

    Returns:
        The square of the input number, with the same type as the input (int or
        float).
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Calculates the result of a number raised to the power of itself.

    This function computes x raised to the power of x (x^x) and returns the
    result. The input x can be an integer or a float.

    Args:
        x (int | float): The number that will be raised to the power of itself.

    Returns:
        int | float: The result of x raised to the power of x.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Creates a closure that repeatedly applies a function to a value.

    This function returns an inner function that maintains state through
    closures. Each call to the inner function applies the given function to
    the current value of x and increments a counter.

    Args:
        x (int | float): The initial numeric value to be transformed.
        function: A callable that takes a numeric value and returns a
            numeric result.

    Returns:
        object: A callable inner function that applies the given function
            to x and returns the updated value on each invocation.
    """
    count = 0

    def inner() -> float:
        """
        Applies the outer function's given function to x.

        Increments the call counter and applies the transformation function
        to the current value of x, updating x with the result.

        Returns:
            float: The updated value of x after applying the function.
        """
        nonlocal x
        nonlocal count

        count += 1
        x = function(x)
        return x

    return inner
