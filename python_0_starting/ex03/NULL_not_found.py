import math


def NULL_not_found(object: any) -> int:
    """
    Check if the given object is a "NULL" value and print its type and name.

    NULL values include:
    - None
    - math.nan
    - 0
    - ""
    - False

    Args:
        object (any): The object to check.

    Returns:
        int: Returns 0 if the object is a recognized NULL value, 1 otherwise.
    """
    obj_type = type(object)

    if object is None:
        print(f"Nothing: None {obj_type}")
    elif isinstance(object, float) and math.isnan(object):
        print(f"Cheese: nan {obj_type}")
    elif obj_type is int and object == 0:
        print(f"Zero: {object} {obj_type}")
    elif obj_type is str and object == "":
        print(f"Empty: {obj_type}")
    elif obj_type is bool and object is False:
        print(f"Fake: False {obj_type}")
    else:
        print("Type not Found")
        return 1

    return 0
