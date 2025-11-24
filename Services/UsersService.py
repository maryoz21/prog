from abc import abstractmethod
from dataclasses import dataclass
from datetime import date

@dataclass(slots=True)
class User:
    id: int = -1
    name: str = ""
    birth_date: date = date.today()


class UsersService:
    @abstractmethod
    def create_user(self, user: User) -> int:
        pass