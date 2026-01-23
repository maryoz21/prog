from __future__ import annotations
from typing import *

T = TypeVar("T")

class Queue(Generic[T]):
    def __init__(self):
        self.__list: list[T] = []
    
    def element_count(self):
        return len(self.__list)
    
    def enqueue(self, element: T):
        self.__list.append(element)

    def top(self):
        if len(self.__list) > 0:
            return self.__list[0]
        
    def dequeue(self):
        if len(self.__list) > 0:
            return self.__list.pop[0] 
        
    def visit(self, visitor: Callable [[T], None]):
        if visitor is None:
            return
        for element in self.__list:
            visitor(element)

    def filter(self, f: Callable[[T], bool]):
        if f is None:
            return
        
        result = Queue[T]()
        for element in self.__list:
            if f(element):
                result.enqueue(element)
        return result