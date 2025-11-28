from abc import abstractmethod, ABC
from dataclasses import dataclass
from datetime import date

@dataclass(slots=True)
class User:
    id: int = -1
    name: str = ""
    birth_date: date = date.today()


class UsersService(ABC):
    @abstractmethod
    def create_user(self, user: User) -> int:
        pass

    @abstractmethod
    def read_user(self, id) -> User:
        pass

    @abstractmethod
    def update_user(self, id, user:User):
        pass

    @abstractmethod
    def delete_user(self, id):
        pass

    @abstractmethod
    def list_users(self, filter: UsersFilter, limit, offset) -> list[User]:
        pass