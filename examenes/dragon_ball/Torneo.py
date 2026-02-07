from abc import abstractmethod
from Persona import *

class iTorneo:

    @abstractmethod
    def iniciar_torneo(self):
        pass

    @abstractmethod
    def  add_participante(self, participante):
        pass

    @abstractmethod
    def ejecutar_ronda(self):
        pass

    @abstractmethod
    def get_participantes(self):
        pass

    @abstractmethod
    def get_winner(self):
        pass

class Torneo(iTorneo):
    def __init__(self):
        super().__init__()
        self.__list = []
    def iniciar_torneo(self):
        pass

    def add_participante(self, participante: Persona):
        self.__list.append(participante)

    def ejecutar_ronda(self):
        pass

    def get_participantes(self):
        pass

    def get_winner(self):
        pass