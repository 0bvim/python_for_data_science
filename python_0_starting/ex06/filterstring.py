import sys

from ft_filter import ft_filter


def validate_arguments(arguments: list[str]) -> tuple[str, int]:
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
    args = sys.argv[1:]
    text, number = validate_arguments(args)

    words = text.split()
    filtered_words = ft_filter(lambda word: len(word) > number, words)
    print(list(filtered_words))


if __name__ == "__main__":
    main()
