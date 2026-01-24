from typing import *

T = TypeVar("T")

class ExList(Generic(T)):
    def __init__(self):
        self.__list: list[T] = []
        self.__count = 0

    def get_count(self) -> int:
        return self.__count
    
    def get_capacity(self) -> int:
        return len(self.__list)
    
    def get_first(self) -> T:
        if self.get_capacity() <= 0:
            return
        return self.__list[0]
    
    def get_last(self) -> T:
        if self.get_capacity() <= 0:
            return []
        
        index = self.get_count()
        return self.__list[index - 1]
    
    def get_reversed(self) -> list[T]:
        if self.get_count <= 0:
            return []
        result = []
        for i in range(len(self.__list) -1, -1, -1):
            result.append(self.__list[i])

        return result