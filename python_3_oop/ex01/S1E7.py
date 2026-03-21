from typing import Optional

from S1E9 import Character


class Baratheon(Character):
    """
    Represents a member of the Baratheon family.

    The Baratheon class is a subclass of Character, representing individuals belonging to
    the Baratheon family. Each Baratheon has specific characteristics such as
    a family name, eye color, and hair color. This class provides functionality to
    handle the character's death and string representations.

    Attributes:
        family_name (str): The family name of the character, default is "Baratheon".
        eyes (str): The eye color of the character, default is "brown".
        hairs (str): The hair color of the character, default is "dark".
    """

    def __init__(self, first_name: str, is_alive: Optional[bool] = True):
        """Initialize a Baratheon instance."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Kill the character."""
        self.health_state()

    def __str__(self):
        """Return a string representation of the Baratheon instance."""
        return super().__str__()

    def __repr__(self):
        """Return a string representation of the Baratheon instance."""
        return super().__repr__()

class Lannister(Character):
    """A class representing a member of the Lannister family.

    The Lannister class models a character from the Lannister family,
    extending the general `Character` class. It provides specific
    attributes and functionality related to this noble family in a
    fictional setting.

    Attributes:
        family_name (str): The family name of the character, which is
            always "Lannister" for instances of this class.
        eyes (str): The eye color of the character, which is "blue".
        hairs (str): The hair color of the character, which is "light".
    """

    def __init__(self, first_name: str, is_alive: Optional[bool] = True):
        """Initialize a Lannister instance."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Kill the character."""
        self.health_state()

    @staticmethod
    def create_lannister(first_name: str, is_alive: bool = True):
        """Create a Lannister instance."""
        return Lannister(first_name, is_alive)

    def __str__(self):
        """Return a string representation of the Lannister instance."""
        return super().__str__()

    def __repr__(self):
        """Return a string representation of the Lannister instance."""
        return super().__repr__()
