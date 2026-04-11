import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(default="")
    id: str = field(default=generate_id())

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.login = f"{self.name[0]}{self.surname.lower()}"
