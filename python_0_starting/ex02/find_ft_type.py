def all_thing_is_obj(object: any) -> int:
    """
    Identifies the type of object and prints it.

    For basic data structures (list, tuple, set, dict), it prints its
    internal name and type. For strings, it prints a special message.

    Args:
        object (any): The object whose type is to be identified.

    Returns:
        int: Always returns 42.
    """
    obj_type = type(object)
    type_name = obj_type.__name__

    type_map = {"list": "List", "tuple": "Tuple", "set": "Set", "dict": "Dict"}

    if type_name in type_map:
        print(f"{type_map[type_name]} : {obj_type}")
    elif type_name == "str":
        print(f"{object} is in the kitchen : {obj_type}")
    else:
        print("Type not found")

    return 42
