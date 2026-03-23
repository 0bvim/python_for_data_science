class Calculator:
    """
    Performs arithmetic operations on a list of numbers.

    The Calculator class allows users to perform arithmetic operations such
    as addition, multiplication, subtraction, and division on a list of
    numeric values. It is designed to support element-wise operations on
    the stored list of numbers.

    Attributes:
        numbers (list[float]): The list of numeric values to operate on.
    """

    def __init__(self, numbers: list[float]) -> None:
        self.numbers = numbers

    def __add__(self, object) -> None:
        self.numbers = [num + object for num in self.numbers]
        print(self.numbers)

    def __mul__(self, object) -> None:
        self.numbers = [num * object for num in self.numbers]
        print(self.numbers)

    def __sub__(self, object) -> None:
        self.numbers = [num - object for num in self.numbers]
        print(self.numbers)

    def __truediv__(self, object) -> None:
        if object == 0:
            print("Error: Division by zero")
            return
        self.numbers = [num / object for num in self.numbers]
        print(self.numbers)
