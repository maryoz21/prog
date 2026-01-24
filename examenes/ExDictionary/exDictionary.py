from __future__ import annotations
from typing import *

K = TypeVar("K")
V = TypeVar("V")

class ExDictionary(Generic[K, V]):
    def __init__(self):
        self.__items: list[tuple[K, V]] = []

    def get_count(self) -> int:
        return len(self.__items)
    
    def get_keys(self) -> list[K]:
        if len(self.__items) <= 0:
            return []
        result = []

        for k, _ in self.__items:
            result.append(k)
        return result
    
    def get_values(self) -> list[V]:
        if len(self.__items) <= 0:
            return []
        result = []

        for _, v in self.__items:
            result.append(v)
        return result
    
    def add_key(self, key: K, value: V):
        if self.contains_key(key):
            return
        self.__items.append((key, value))

    def set(self, key: K, value: V):
        if self.get(key) is None:
            return
        
        for i in range(len(self.__items)):
            current_tuple = self.__items[i]

            if current_tuple[0] == key:
                self.__items[i] = (key, value)
                return
            
    def get(self, key: K) -> V | None:
        for i in range(len(self.__items)):
            current_tuple = self.__items[i]

            if current_tuple[0] == key:
                return current_tuple[1]
            
        return None
    
    def remove(self, key: K) -> bool:
        for i in range(len(self.__items)):
            current_tuple = self.__items[i]

            if current_tuple[0] == key:
                self.__items.pop(i)
                return True
        return False
            
    def clear(self):
        self.__items = []

    def contains_key(self, key: K) -> bool:
        for i in range(len(self.__items)):
            current_tuple = self.__items[i]

            if current_tuple[0] == key:
                return True
            
        return False
    
    def contains_value(self, value: V) -> bool:
        for i in range(len(self.__items)):
            current_tuple = self.__items[i]

            if current_tuple[1] == value:
                return True
            
        return False
    
    def visit(self, visitor: Callable[[K, V], None]):
        if visitor is None:
            return
        if len(self.__items) <= 0:
            return
        for i in range(len(self.__items)):
            current_tuple = self.__items[i]
            visitor(current_tuple[0], current_tuple[1])

    def filter(self, f: Callable[[K, V], bool]) -> ExDictionary:
        if f is None:
            return
        if len(self.__items) <= 0:
            return
        result = ExDictionary[K, V]()
        for i in range(len(self.__items)):
            current_tuple = self.__items[i]
            k = current_tuple[0]
            v = current_tuple[1]

            if f(k, v):
                result.add_key(k, v)
        
        return result
    
    def clone(self) -> ExDictionary:
        result = ExDictionary[K, V]()
        for i in range(len(self.__items)):
            current_tuple = self.__items[i]
            result.add_key(current_tuple[0], current_tuple[1])

        return result

    def to_list(self) -> list[tuple[K, V]]:
        result = []
        for i in range(len(self.__items)):
            result.append(self.__items[i])
        
        return result