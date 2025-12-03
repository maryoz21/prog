from UsersService import *
from UsersFilter import *
import copy

class UsersServiceImpl(UsersService):
    def __init__(self):
        super().__init__()
        self.__users: list[User]  = []
        self.__count: int = 0

    def create_user(self, user: User) -> int:
        if user is None:
            return -1
        id = self.__count
        user.id = id
        self.__count += 1
        self.__users.append(copy.deepcopy(user))
        return id
    
    def read_user(self, id: int) -> User | None :
        if id is None:
            return None
        for user in self.__users:
            if id == user.id:
                return user
        return None
    
    def update_user(self, id, user):
        if id is None or user is None:
            return None
        result = self.read_user(id)
        if result is None:
            return None
        result.name = user.name
        result.birth_date = user.birth_date
        return result
    
    def delete_user(self, id: int):
        if id is None:
            return
        index = 0
        for u in self.__users:
            if u.id == id:
                self.__users.pop(index)
                return
            index += 1

    def list_users(self, filter: UsersFilter, offset, limit):
        l = self.__users
        if filter.match_pattern is not None:
            l = filter_user_with_name(filter.match_pattern, l)
        if filter.min_age > -1:
            l = filter_user_with_age(filter.min_age, l)
        return copy.deepcopy(l[offset: offset + limit])