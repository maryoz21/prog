import random
from Persona import *


class utils:
    @classmethod
    def humano_random(cls):
        energia = random.uniform(1000, 2000)
        deseo = random.uniform(0.1, 0.9)
        atk_golpes = random.uniform(0.1, 0.8)
        cap_esq = random.uniform(0.4, 0.6)
        cap_par = random.uniform(0.7, 0.9)
        return Humano("HumanoX", energia, deseo, atk_golpes, cap_esq, cap_par)

    @classmethod
    def guerrero_random(cls):
        energia = random.uniform(1000, 2000)
        deseo = random.uniform(0.1, 0.9)
        atk_rayo = random.uniform(0.3, 0.6)
        atk_golpes = random.uniform(0.1, 0.8)
        cap_esq = random.uniform(0.2, 0.4)
        cap_par = random.uniform(0.4, 0.9)
        return GuerreroDelEspacio("GuerreroX", energia, deseo, atk_rayo, atk_golpes, cap_esq, cap_par)

    @classmethod
    def super_random(cls):
        energia = random.uniform(1000, 2000)
        deseo = random.uniform(0.1, 0.9)
        atk_rayo = random.uniform(0.3, 0.6)
        atk_golpes = random.uniform(0.1, 0.8)
        cap_esq = random.uniform(0.2, 0.4)
        cap_par = random.uniform(0.4, 0.9)
        return SuperSaiyajin("SuperX", energia, deseo, atk_rayo, atk_golpes, cap_esq, cap_par)

    @classmethod
    def combate(cls, a: Persona, b: Persona):
        turno = 0
        while a.energia > 0 and b.energia > 0:
            if turno % 2 == 0:
                a.atacar(b)
            else:
                b.atacar(a)
            turno += 1
        return a if a.energia > 0 else b