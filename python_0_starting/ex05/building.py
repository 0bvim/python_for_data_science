import string
import sys


def validate_arguments(arguments: list[str]) -> str:
    """
    Validate and process command line arguments for text analysis.

    If no arguments are provided or an empty argument is given, prompts the user
    to input text interactively. Handles EOF (Ctrl+D) and KeyboardInterrupt (Ctrl+C)
    gracefully by returning an empty string.

    Args:
        arguments (list[str]): List of command line arguments (sys.argv[1:])

    Returns:
        str: The text to be analyzed. Returns empty string if user presses Ctrl+D
        or Ctrl+C

    Raises:
        AssertionError: If more than one argument is provided

    Note:
        When prompting for input, carriage returns count as spaces. Use Ctrl+D
        to finish input without adding a newline, or Ctrl+C to cancel.
    """
    if len(arguments) == 0 or arguments[0] == "":
        try:
            text = input("What is the text to count?\n")
            return text
        except EOFError:
            return ""
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return ""
    assert len(arguments) == 1, "more than one argument is provided"
    return arguments[0]


def count_types(text: str) -> dict[str, int]:
    """
    Count different types of characters in the given text.

    Analyzes each character in the input text and categorizes them into:
    - upper: uppercase letters
    - lower: lowercase letters
    - punctuation: punctuation marks (as defined by string.punctuation)
    - spaces: whitespace characters (spaces, tabs, newlines, etc.)
    - digits: numeric digits (0-9)

    Args:
        text (str): The text to analyze

    Returns:
        dict[str, int]: Dictionary mapping character type names to their counts.
                       Only includes types that have at least one occurrence.

    Example:
        >>> count_types("Hello World! 123")
        {'upper': 2, 'lower': 8, 'spaces': 2, 'punctuation': 1, 'digits': 3}
    """
    types = {}
    for char in text:
        if char.isupper():
            types["upper"] = types.get("upper", 0) + 1
        elif char.islower():
            types["lower"] = types.get("lower", 0) + 1
        elif char in string.punctuation:
            types["punctuation"] = types.get("punctuation", 0) + 1
        elif char.isspace():
            types["spaces"] = types.get("spaces", 0) + 1
        elif char.isdigit():
            types["digits"] = types.get("digits", 0) + 1
        else:
            continue
    return types


def main():
    """
    Main function that orchestrates the text analysis program.

    Processes command line arguments, gets text input (either from arguments
    or user prompt), analyzes the text character composition, and displays
    a detailed report of character counts by type.

    The program can be used in two ways:
    1. With command line argument: python building.py "text to analyze"
    2. Interactive mode: python building.py (then enter text when prompted)

    Outputs a summary showing:
    - Total character count
    - Count of uppercase letters
    - Count of lowercase letters
    - Count of punctuation marks
    - Count of spaces/whitespace
    - Count of digits
    """
    arguments = sys.argv[1:]
    text = validate_arguments(arguments)

    if text == "":
        return

    types = count_types(text)

    print(f"The text contains {len(text)} characters:")
    print(f"{types.get('upper', 0)} upper letters")
    print(f"{types.get('lower', 0)} lower letters")
    print(f"{types.get('punctuation', 0)} punctuation marks")
    print(f"{types.get('spaces', 0)} spaces")
    print(f"{types.get('digits', 0)} digits")


if __name__ == "__main__":
    main()
