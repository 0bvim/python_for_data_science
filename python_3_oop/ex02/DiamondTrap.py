from typing import Optional

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A class representing a fake King."""

    def __init__(self, first_name: str,
                 is_alive: Optional[bool] = True) -> None:
        """
        Initializes a new instance of the class with given attributes.

        Args:
            first_name (str): The first name of the individual.
            is_alive (Optional[bool]): Status indicating if the individual is
                alive. Defaults to True.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def set_eyes(self, eyes: str) -> None:
        """
        Sets the value of the eyes attribute.

        Args:
            eyes (str): The eye color or description to be set.
        """
        self.eyes = eyes

    def set_hairs(self, hairs: str) -> None:
        """
        Sets the number or type of hairs for the object.

        This method allows the modification or updating of the 'hairs'
        attribute of the object. It is intended to set a specific number or
        description of hairs based on the provided input.

        Args:
            hairs (str): The number or description of hairs to set for the
                object.
        """
        self.hairs = hairs

    def get_eyes(self) -> str:
        """
        Gets the value of the eyes attribute.

        Returns:
            str: The eye color or description.
        """
        return self.eyes

    def get_hairs(self) -> str:
        """
        Gets the value of the hairs attribute.

        Returns:
            str: The number or description of hairs.
        """
        return self.hairs

    def die(self) -> None:
        """Kill the character."""
        self.health_state()
