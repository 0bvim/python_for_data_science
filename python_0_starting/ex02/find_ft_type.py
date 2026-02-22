from Utils import Utils


def all_thing_is_obj(object: any) -> int:
    Utils().check_version()
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
