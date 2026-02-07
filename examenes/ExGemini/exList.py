from __future__ import annotations
from typing import *

T = TypeVar("T")
U = TypeVar("U")

class TwinList(Generic[T, U]):
    def __init__(self, inital_capicity: int = 10):
        super().__init__()
        self.__list: list[tuple[T, U]] = [None] * inital_capicity
        self.__count = 0

    def count(self) -> int:
        return self.__count
    
    def capacity(self) -> int:
        return len(self.__list)
    
    def first(self) -> tuple[T, U]:
        if self.count() <= 0:
            return
        return self.__list[0]
    
    def last(self) -> tuple[T, U]:
        if self.__count() <= 0:
            return
        return self.__list[self.__count - 1]
    
    def is_empty(self) -> bool:
        if self.__count <= 0:
            return True
        return False
    
    def add(self, item_t: T, item_u: U):
        if self.__count == self.capacity():
            result: list[tuple[T, U]] = [None] * (self.capacity() * 2)
            for i in range(len(self.__list)):
                result[i] = self.__list[i]
            self.__list = result
        self.__list[self.__count] = [item_t, item_u]
        self.__count += 1

    def get_at(self, index: int) -> tuple[T, U]:
        if 0 > index or index >= self.__count:
            return
        return self.__list[index]
    
    def set_at(self, index: int, item_t: T, item_u: U):
        if 0 > index or index >= self.__count:
            return
        self.__list[index] = [item_t, item_u]

    def clear(self):
        self.__count = 0
        self.__list = [None] * self.capacity()

    def remove_at(self, index: int):
        if 0 > index or index > self.__count:
            return
        n = self.count()
        for i in range(index, n - 1):
            self.__list[i] = self.__list[i + 1]

        self.__count -= 1
        self.__list[self.__count] = None

    def insert(self, index: int, item_t: T, item_u: U):
        if 0 > index or index > self.__count:
            return
        n = self.count()
        result = []
        if self.count() == self.capacity():
            if self.capacity <= 0:
                result = [None]
            else:
                result = [None] * (self.capacity() * 2)
            for i in range(self.count()):
                result[i] = self.__list[i]  
            self.__list = result

        for i in range(n, index, -1):
            self.__list[i] = self.__list[i - 1]

        self.__list[index] = [item_t, item_u]
        self.__count += 1

    def find(self, predicate: Callable[[T, U], bool]) -> tuple[T, U] | None:
        if predicate is None:
            return
        for i in range(self.count()):
            item = self.__list[i]
            if predicate((item[0], item[1])):
                return item
            
    def exists(self, predicate: Callable[[T, U], bool]) -> bool:
        if predicate is None:
            return
        for i in range(self.count()):
            item = self.__list[i]
            if predicate((item[0], item[1])):
                return True
        return False
    