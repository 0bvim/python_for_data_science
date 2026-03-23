class Calculator:
    """
    Provides methods to perform basic vector operations such as dot product,
    addition, and subtraction.

    This class is designed for simple mathematical operations with vectors.
    It includes static methods to avoid the need to instantiate the class
    when performing these operations, enabling straightforward integration into
    other workflows or computational pipelines.
    """

    def __init__(self) -> None:
        """Initialize the Calculator instance."""
        pass

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate and print the dot product of two vectors.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        print(sum(x * y for x, y in zip(V1, V2, strict=True)))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculate and print the sum of two vectors.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        print([float(x + y) for x, y in zip(V1, V2, strict=True)])

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculate and print the subtraction of two vectors.

        Args:
            V1 (list[float]): The first vector.
            V2 (list[float]): The second vector.
        """
        print([float(x - y) for x, y in zip(V1, V2, strict=True)])
