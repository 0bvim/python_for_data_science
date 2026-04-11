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
    Applies a given function to a value with a closure maintaining state.

    This function returns a closure that, when called, applies the input
    function to the initial value and updates the value and call count.
    The closure ensures the state is retained between calls.

    Args:
        x: The initial value to which the function will be applied. Can be an integer or a float.
        function: A callable that takes one argument and performs an operation on the provided value.

    Returns:
        A closure (inner function) that, when invoked, applies the provided function to the maintained
        state value and returns the updated value.
    """
    count = 0

    def inner() -> float:
        nonlocal x
        nonlocal count

        count += 1
        x = function(x)
        return x

    return inner
