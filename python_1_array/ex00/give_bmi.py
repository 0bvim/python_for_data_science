import numpy as np


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    if len(height) != len(weight):
        raise AssertionError(
            "list have different size. It must have same size."
        )

    h_arr = np.array(height)
    w_arr = np.array(weight)

    bmi = w_arr / (h_arr**2)

    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    check_value(bmi, "bmi")

    bmi_arr = np.array(bmi)

    return (bmi_arr > limit).tolist()


def check_value(lst: list[int | float], name: str) -> None:
    if not all(
        isinstance(x, (int, float)) and not isinstance(x, bool) for x in lst
    ):
        raise AssertionError(
            f"{name} list must contain only int or float values"
        )
