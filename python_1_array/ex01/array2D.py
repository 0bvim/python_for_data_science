import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        family_arr = np.array(family)
    except ValueError as e:
        print(f"Error: {e}")
        return []
    
    print(f"My shape is : {family_arr.shape}")
    
    sliced_family_array = family_arr[start:end]
    print(f"My new shape is : {sliced_family_array.shape}")
    
    return sliced_family_array.tolist()
    
