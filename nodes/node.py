from __future__ import annotations
from typing import *
import weakref
T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, item: T):
        super().__init__()
        self.item: T = item
        self.__parent: weakref.ref[Node[T]] = None
        self.__children: list[Node[T]] = []

    def get_root_recursive(self) -> Node[T]:
        if self.get_parent() is None:
            return self
        else:
            return self.get_parent().get_root_recursive()
    
    def get_root_iterative(self) -> Node[T]:
        node = self
        while node.get_parent() is not None:
            node = node.get_parent()
        return node

    def get_parent(self) -> Node[T]:
        if self.__parent is None:
            return None
        return self.__parent()
    
    def set_parent(self, node: Node[T]):
        if node is not None:
            node.add_child(self)
        elif self.__parent is not None:
            self.get_parent().remove_child(self)

    def add_child(self, node: Node[T]):
        if node is None: 
            return
        if node.get_parent() is self:
            return
        if node.get_parent() is not None:
            node.get_parent().remove_child(node)
        node.__parent = weakref.ref(self)
        self.__children.append(node)

    def remove_child(self, node: Node[T]):
        index = self.index_of_child(node)
        if index >= 0:
            self.__children.pop(index)
            node.__parent = None

    def index_of_child(self, node: Node[T]) -> int:
        for i in range(len(self.__children)):
            child = self.__children[i]
            if child is node:
                return i
        return -1
    
    def unlink(self):
        self.set_parent(None)

    def visit(self, visitor: Callable[[Node[T]], None]):
        if visitor is None:
            return
        visitor(self)
        for child in self.__children:
            child.visit(visitor)
    

