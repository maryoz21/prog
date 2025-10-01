# Le das un numero y devuelve la posicion del fibonacci
def generate_serie_6(n:int):
    last_number = 0
    number = 1
    suma = 0
    i = 0
    if n < 0:
        return -1
    while i < n:
        suma = number + last_number
        last_number = number
        number = suma
        i += 1
    return last_number
posicion = generate_serie_6(0)
print(posicion)
