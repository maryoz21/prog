from __future__ import annotations
from typing import *
import copy

K = TypeVar("K")
V = TypeVar("V")

class ExDictionary(Generic[K, V]):

    def __init__(self):
        super().__init__()
        self.__keys: list[K] = []
        self.__values: list[V] = []
