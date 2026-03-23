from abc import ABC, abstractmethod
from typing import Optional


class Character(ABC):
    """Abstract class for characters."""

    def __init__(self, first_name: str,
                 is_alive: Optional[bool] = True) -> None:
        """Initialize a Character instance."""
        self.first_name = first_name
        self.is_alive = is_alive

    def health_state(self) -> None:
        """Set the character's health state to False."""
        self.is_alive = False

    @abstractmethod
    def die(self) -> None:
        """Method to kill the character."""
        pass


class Stark(Character):
    """Class that inherits from Character and represents a Stark character."""

    def __init__(self, first_name: str,
                 is_alive: Optional[bool] = True) -> None:
        """Initialize a Stark instance."""
        super().__init__(first_name, is_alive)

    def die(self) -> None:
        """Kill the character."""
        self.health_state()
