from __future__ import annotations
from typing import *
from enum import Enum
from copy import deepcopy

K = TypeVar("K")
V = TypeVar("V")

class ExDictionary(Generic[K, V]):
    def __init__(self):
        super().__init__()
        self.__keys: list[K] = []
        self.__values: list[V] = []

    def get_count(self) -> int:
        if len(self.__keys) == len(self.__values):
            return len(self.__keys)
        
    def get_keys(self) -> list[K]:
        return deepcopy(self.__keys)
    
    def get_values(self) -> list[V]:
        return deepcopy(self.__values)
    
    def add(self, key: K, value: V):
        if self.contains_key(key):
            return
        
        self.__keys.append(key)
        self.__values.append(value)

    def set(self, key: K, value: V):
        if len(self.__keys) <= 0:
            return
        if self.contains_key(key):
            for i in range(len(self.__keys)):
                if self.__keys[i] == key:
                    self.__values[i] = value

    def get(self, key: K) -> V:
        if self.contains_key(key):
            for i in range(len(self.__keys)):
                if self.__keys[i] == key:
                    return self.__values[i]
        return None
    
    def remove(self, key: K) -> bool:
        for i in range(len(self.__keys)):
            if self.__keys[i] == key:
                self.__keys.pop(i)
                self.__values.pop(i)
                return True
        return False
    
    def clear(self):
        self.__keys = []
        self.__values = []


    def contains_key(self, key: K) -> bool:
        for i in range(len(self.__keys)):
            if self.__keys[i] == key:
                return True
        return False
    
    def contains_value(self, value: V) -> bool:
        for i in range(len(self.__values)):
            if self.__values[i] == value:
                return True
        return False
    
    def visit(self, visitor: Callable[[K, V], None]):
        if visitor is None:
            return None
        for i in range(len(self.__keys)):
            visitor(self.__keys[i], self.__values[i])

    def filter(self, f: Callable[[K, V], bool]) -> ExDictionary:
        if f is None:
            return
        result = ExDictionary[K, V]()
        for i in range(len(self.__keys)):
            if f(self.__keys[i], self.__values[i]):
                result.add(self.__keys[i], self.__values[i])
        return result
    
    def clone(self) -> ExDictionary:
        result = ExDictionary[K, V]()
        result.__keys = deepcopy(self.__keys)
        result.__values = deepcopy(self.__values)
        return result
    
    def to_list(self) -> list[tuple[K, V]]:
        result = []
        for i in range(len(self.__keys)):
            result.append((self.__keys[i], self.__values[i]))
        return result
    
