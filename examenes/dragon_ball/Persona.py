from enum import Enum
from abc import abstractmethod
from __future__ import annotations
import random

class Raza(Enum):
    Persona = 1
    Humano = 2
    GuerreroDelEspacio = 3
    SuperSaiyajin = 4


class Persona:
    def __init__(self, name: str, energia: float, deseo: float):
        self.__name: str = name
        self.__raza: Raza = Raza.Persona
        self.__energia: float = energia
        self.__deseo_de_esquivo: float = deseo

    def quitar_energia(self, energia: float):
        self.__energia -= energia

    @abstractmethod 
    def atacar(self, persona: Persona):
        pass

    @abstractmethod 
    def obtener_capacidad_de_esquiva(self) -> float:
        pass

    @abstractmethod
    def obtener_capacidad_de_parada(self) -> float:
        pass

    def quiere_esquivar(self) -> bool:
        pass     

class Humano(Persona):
    def __init__(self, name: str, energia: float, deseo: float, ataque: float, capacidad_esquiva: float, capacidad_parar: float):
        super().__init__(name, Raza.Humano, energia, deseo)
        self.__ataque_con_golpes = ataque
        self.__capacidad_de_esquiva = capacidad_esquiva
        self.__capacidad_de_parar = capacidad_parar

    def atacar(self, other: Persona):
        if self.__energia <= 0:
            return
        self.quitar_energia(1.0)
        if other.quiere_esquivar():
            if other.obtener_capacidad_de_esquiva() > random.random():
                return
        if other.obtener_capacidad_de_parada() > random.random():
            other.quitar_energia(0.5)
        else:
            other.quitar_energia(5.0)
        

    def obtener_capacidad_de_esquiva(self) -> float:
        return self.__capacidad_de_esquiva

    def obtener_capacidad_de_parada(self) -> float:
        return self.__capacidad_de_parar

class GuerreroDelEspacio(Persona):
    def __init__(self, name: str, energia: float, deseo: float, ataque_con_rayo: float, ataque_con_golpes: float, capacidad_de_esquivar: float, capacidad_de_parar: float):
        super().__init__(name, Raza.GuerreroDelEspacio, energia, deseo)
        self.__ataque_con_rayo = ataque_con_rayo
        self.__ataque_con_golpes = ataque_con_golpes
        self.__capacidad_de_esquivar = capacidad_de_esquivar
        self.__capacidad_de_parar = capacidad_de_parar

    def atacar(self):
        if random.random < 0.5:
            self.atacar_con_golpe()
        else:
            self.atacar_con_rayo()

    def atacar_con_rayo(self, other: Persona):
        if self.__energia <= 100:
            return
        self.quitar_energia(100.0)
        if other.quiere_esquivar():
            if other.obtener_capacidad_de_esquiva > random.random():
                return
        if other.obtener_capacidad_de_parada() > random.random():
            other.quitar_energia(25.0)
        else:
            other.quitar_energia(300.0)

    def atacar_con_golpe(self, other: Persona):
        if self.__energia <= 5.0:
            return
        self.quitar_energia(5.0)
        if other.quiere_esquivar():
            if other.obtener_capacidad_de_esquiva > random.random():
                return
        if other.obtener_capacidad_de_parada() > random.random():
            other.quitar_energia(2.0)
        else:
            other.quitar_energia(7.0)

    def obtener_capacidad_de_esquiva(self) -> float:
        return self.__capacidad_de_esquivar

    def obtener_capacidad_de_parada(self) -> float:
        return self.__capacidad_de_parar

class SuperSaiyajin(GuerreroDelEspacio):
    def __init__(self, name: str, energia: float, deseo: float, ataque_con_rayo: float, ataque_con_golpes: float, capacidad_de_esquivar: float, capacidad_de_parar: float):
        super().__init__(name, Raza.SuperSaiyajin, energia, deseo, ataque_con_rayo, ataque_con_golpes, capacidad_de_esquivar, capacidad_de_parar)

    def atacar(self, other: Persona):
        n = random.randint(1, 3)
        for _ in range(n):
            if self.__energia <= 0:
                return
            if random.random() < 0.5:
                self.atacar_con_rayo(other)
            else:
                self.atacar_con_golpe(other)


    def atacar_con_rayo(self, other: Persona):
        if self.__energia <= 100:
            return
        self.quitar_energia(100.0)
        if other.quiere_esquivar():
            if other.obtener_capacidad_de_esquiva > random.random():
                return
        if other.obtener_capacidad_de_parada() > random.random():
            other.quitar_energia(50.0)
        else:
            other.quitar_energia(600.0)

    def atacar_con_golpe(self, other: Persona):
        if self.__energia <= 5.0:
            return
        self.quitar_energia(5.0)
        if other.quiere_esquivar():
            if other.obtener_capacidad_de_esquiva > random.random():
                return
        if other.obtener_capacidad_de_parada() > random.random():
            other.quitar_energia(4.0)
        else:
            other.quitar_energia(14.0)

def generar_persona(nombre: str) -> Persona:
    n = random.randint(1, 3)
    if n < 1.5:
        return Humano( nombre, random.uniform(1000, 2000), random.uniform(0.1, 0.9), random.uniform(0.1, 0.8), random.uniform(0.4, 0.6), random.uniform(0.7, 0.9) )
    elif n > 2.5:
        return GuerreroDelEspacio( nombre, random.uniform(1000, 2000), random.uniform(0.1, 0.9), random.uniform(0.3, 0.6), random.uniform(0.1, 0.8), random.uniform(0.2, 0.4), random.uniform(0.4, 0.9) )
    else:
        return SuperSaiyajin( nombre, random.uniform(1000, 2000), random.uniform(0.1, 0.9), random.uniform(0.3, 0.6), random.uniform(0.1, 0.8), random.uniform(0.2, 0.4), random.uniform(0.4, 0.9))



def crear_humano_random(nombre: str) -> Humano:
    return Humano( nombre, random.uniform(1000, 2000), random.uniform(0.1, 0.9), random.uniform(0.1, 0.8), random.uniform(0.4, 0.6), random.uniform(0.7, 0.9) )

def crear_guerrero_espacial_random(nombre: str) -> GuerreroDelEspacio: 
    return GuerreroDelEspacio( nombre, random.uniform(1000, 2000), random.uniform(0.1, 0.9), random.uniform(0.3, 0.6), random.uniform(0.1, 0.8), random.uniform(0.2, 0.4), random.uniform(0.4, 0.9) )

def crear_supersaiyajin_random(nombre: str) -> SuperSaiyajin: 
    return SuperSaiyajin( nombre, random.uniform(1000, 2000), random.uniform(0.1, 0.9), random.uniform(0.3, 0.6), random.uniform(0.1, 0.8), random.uniform(0.2, 0.4), random.uniform(0.4, 0.9))