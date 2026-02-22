import sys

from ft_filter import ft_filter


def validate_arguments(arguments: list[str]) -> tuple[str, int]:
    """
    Validate command-line arguments for the filter program.

    Expects exactly two arguments: a string and an integer.

    Args:
        arguments: A list of string arguments to validate.

    Returns:
        A tuple containing the string argument and the integer argument.

    Raises:
        AssertionError: If the number of arguments is not 2,
                or if the second argument cannot be converted to an integer.
    """
    if len(arguments) != 2:
        raise AssertionError("the arguments are bad")

    try:
        string_arg = arguments[0]
        int_arg = int(arguments[1])

        if not isinstance(string_arg, str):
            raise ValueError("the arguments are bad")
        return string_arg, int_arg

    except ValueError:
        raise AssertionError("the arguments are bad")


def main():
    """
    Entry point for the filter program.

    Parses command-line arguments to extract a string and an integer,
    then filters the words in the string, keeping only those whose
    length is strictly greater than the given integer.

    Prints the resulting list of filtered words to standard output.

    Usage:
        python program.py <string> <integer>

    Raises:
        AssertionError: If the arguments are invalid (via validate_arguments).
    """
    args = sys.argv[1:]
    text, number = validate_arguments(args)

    words = text.split()
    filtered_words = ft_filter(lambda word: len(word) > number, words)
    print(list(filtered_words))


if __name__ == "__main__":
    main()
