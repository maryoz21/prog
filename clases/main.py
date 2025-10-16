from GameObject import GameObject
from typing import List

#Funcion que le pasas un nombre y te devuelve el objeto con ese nombre
def get_object(name: str, lista: list[GameObject] ) -> GameObject :
    for obj in lista:
        if obj.name == name:
            return obj
    return None

print(get_object("Player", [GameObject(1, "Player"), GameObject(2, "Enemy")]))