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
        """
        Initialize the Calculator instance with a list of numbers.

        Args:
            numbers (list[float]): The list of numeric values.
        """
        self.numbers = numbers

    def __add__(self, object) -> None:
        """
        Add a scalar value to each element in the list.

        Args:
            object (float): The scalar value to add.
        """
        self.numbers = [num + object for num in self.numbers]
        print(self.numbers)

    def __mul__(self, object) -> None:
        """
        Multiply each element in the list by a scalar value.

        Args:
            object (float): The scalar value to multiply by.
        """
        self.numbers = [num * object for num in self.numbers]
        print(self.numbers)

    def __sub__(self, object) -> None:
        """
        Subtract a scalar value from each element in the list.

        Args:
            object (float): The scalar value to subtract.
        """
        self.numbers = [num - object for num in self.numbers]
        print(self.numbers)

    def __truediv__(self, object) -> None:
        """
        Divide each element in the list by a scalar value.

        Args:
            object (float): The scalar value to divide by.
        """
        if object == 0:
            print("Error: Division by zero")
            return
        self.numbers = [num / object for num in self.numbers]
        print(self.numbers)
