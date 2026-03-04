from __future__ import annotations
from typing import *


T = TypeVar("T")

class ExList(Generic[T]):
    def __init__(self):
        super().__init__()
        self.__list: list[T] = []
        self.__count = 0

    

    def get_count(self) -> int:
        return self.__count
    
    def get_capacity(self) -> int:
        return len(self.__list)
    
    def get_first(self) -> T:
        if self.get_count() <= 0:
            return None
        return self.__list[0]
    
    def get_last(self) -> T:
        if self.get_count() <= 0:
            return None
        return self.__list[self.get_count() - 1]

    def get_reversed(self) -> ExList:

        result = ExList[T]()
        if self.get_capacity() <= 0:
            return result
        
        for i in range(self.get_count() -1, -1, -1):
            result.add(self.__list[i])

        return result


    def getElementAt(self, index: int) -> T | None:
        n = self.get_capacity()
        if 0 <= index <= n:
            return self.__list[index]
        return None



    def setElementAt(self, index: int, element: T):
        n = self.get_count()
        if 0 <= index <= n:
            self.__list[index] = element

        

    def add(self, element: T):
        if self.get_capacity() == self.get_count():
            result: list[T] = [None] * (self.get_capacity() + 1)
            for i in range(self.get_count()):
                result[i] = self.__list[i]
            self.__list = result
        self.__list[self.get_count()] = element
        self.__count += 1

    def removeAt(self, index: int):
        
        
    def clear(self):
        pass

    def insert(self, index: int, element: T):
        pass

    def indexOf(self, element: T) -> int:
        pass

    def contains(self, element: T) -> bool:
        pass

    def indexOf(self, element: T, f: Callable[[T], bool]) -> int:
        pass 

    def contains(self, element: T, f: Callable[[T], bool]) -> bool:
        pass

    def visit(self, vis: Callable[[T], None]):
        pass

    def sort(self, s: Callable[[T], None]):
        pass

    def filter(self, f: Callable[[T], bool]) -> ExList:
        pass

    def reverse(self):
        pass

    def clone(self) -> ExList:
        result = ExList[T]()
        n = self.get_count()
        for i in range(n):
            result.add(self.__list[i])


