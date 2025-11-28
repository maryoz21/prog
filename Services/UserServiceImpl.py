from UsersService import UsersService, User
from copy import deepcopy

class UsersServiceImpl(UsersService):
    def __init__(self):
        super().__init__()
        self.__users: list[User]  = []
        self.__count: int = 0

    def create_user(self, user):
        return super().create_user(user)

