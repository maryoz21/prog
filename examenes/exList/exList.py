from __future__ import annotations
from typing import *

T = TypeVar("T")

class ExList(Generic[T]):
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
            return
        
        index = self.get_count()
        return self.__list[index - 1]
    
    def get_reversed(self) -> list[T]:
        if self.get_count() <= 0:
            return []
        result = []
        for i in range(self.get_count() -1, -1, -1):
            result.append(self.__list[i])

        return result
    
    def getElementAt(self, index: int) -> T:
        if 0 <= index < self.get_count():
            return self.__list[index]
            
    def setElementAt(self, index: int, element: T):
        if 0 <= index < self.get_count():
            self.__list[index] = element
    
    def add(self, element: T):
        capacity = self.get_capacity()
        count = self.get_count()

        if count == capacity:
            result = [None] * (capacity + 1)

            for i in range(count):
                result[i] = self.__list[i]
            self.__list = result

        self.__list[count] = element
        self.__count += 1

    def removeAt(self, index: int):
        if 0 <= index < self.__count:
            for i in range(index, self.__count - 1):
                self.__list[i] = self.__list[i + 1]
            
            self.__list[self.__count - 1] = None
            self.__count -= 1

    def clear(self):
        capacity = self.get_capacity()
        self.__list = [None] * capacity
        self.__count = 0

    def insert(self, index: int, element: T):
        if 0 <= index <= self.__count:

            capacity = self.get_capacity()
            count = self.get_count()

            if count == capacity:
                result = [None] * (capacity + 1)

                for i in range(count):
                    result[i] = self.__list[i]

                self.__list = result
            
            for i in range(count, index, -1):
                self.__list[i] = self.__list[i - 1]
            
            self.__list[index] = element
            self.__count += 1

    def indexOf(self, element: T) -> int:
        for i in range(self.__count):
            if self.__list[i] == element:
                return i
        return -1
    
    def contains(self, element: T) -> bool:
        return self.indexOf(element) != -1

    def indexOfDelegate(self, index: Callable[[T], bool]) -> int:
        if index is None:
            return -1
        for i in range(len(self.__list)):
            if index(self.__list[i]):
                return i
        return -1

    def containsDelegate(self, container: Callable[[T], bool]) -> bool:
        return self.indexOfDelegate(container) >= 0
    
    def visit(self, visitor: Callable[[T], None]):
        if visitor is None:
            return
        for i in range(len(self.__list)):
            visitor(self.__list[i])

    def sort(self, sorter: Callable[[T, T], None]):
        if sorter is None:
            return
        
        length = self.__count
        for i in range(length):
            for j in range(0, length - i - 1):
                if sorter(self.__list[j], self.__list[j + 1]) > 0:
                    aux = self.__list[j]
                    self.__list[j] = self.__list[j + 1]
                    self.__list[j + 1] = aux
        
    def filter(self, fil: Callable[[T], bool]) -> ExList[T]:
        if fil is None:
            return
        result = ExList[T]()
        for i in range(len(self.__list)):
            if fil(self.__list[i]):
                result.add(self.__list[i])
        return result
    
    def reverse(self):
        n = self.__count
        for i in range( n // 2):
            aux = self.__list[i]
            self.__list[i] = self.__list[n -i -1]
            self.__list[n -i -1] = aux

    def clone(self) -> ExList[T]:
        result = ExList[T]()
        for i in range(self.__count):
            result.add(self.__list[i])
        return result
        

# --- MAIN DE PRUEBA ---
if __name__ == "__main__":
    lista = ExList[str]()
    
    print("Añadiendo elementos...")
    lista.add("Hola")  # Capacity 0 -> 1
    lista.add("Mundo") # Capacity 1 -> 2
    lista.add("Python") # Capacity 2 -> 3
    
    print(f"Count: {lista.get_count()} (Esperado 3)")
    print(f"Capacity: {lista.get_capacity()}")
    
    print(f"Primero: {lista.get_first()}")
    print(f"Último: {lista.get_last()}")
    
    print(f"Reversed: {lista.get_reversed()}")
    
    lista.setElementAt(1, "CAMBIADO")
    print(f"Elemento 1 cambiado: {lista.getElementAt(1)}")