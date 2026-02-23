def count_in_list(lst: list, item: object) -> int:
    """
    Counts the number of occurrences of a specified item in a list.

    Args:
        lst (list): The list in which to count occurrences.
        item (object): The item to count in the list.

    Returns:
        int: The number of times the item appears in the list.
    """
    return sum(1 for x in lst if x == item)
