import sys
# Funcion que le das una lista y devuelve la lista inversa

def reverse_list(list1):
    if len(list1) == 0:
        return []
    return list1[::-1]


# Funcion que le paso un entero y me genera la siguiente serie
# 4 
# [1, 2, 3, 4]

def generate_serie_1(n: int):
    result = []
    i: int= 1
    while i <= n:
        result.append(i)
        i += 1
    return result


# Funcion que devuelve una serie con x numeros que d

def generate_serie_2(n: int):
    result = []
    i: int = 0
    contador = 0
    while contador < n:
        result.append(i)
        i += 2
        contador += 1

    return result

# Funcion que le das un numero y te devuelve la serie de potencias de 2

def generate_serie_3(n: int):
    result = []
    i: int = 0
    number: int = 1
    while i < n:
        result.append(number)
        number *= 2
        i += 1
    return result





# Funcion 
# 5
# [5, -4, 3, -2, 1]

def generate_serie_4(n: int):
    result = []
    i: int = 0
    number: int = n
    while i < n:
        if number < 0:
            result.append(number)
            number = number * (-1) -1
        else:
            result.append(number)
            number = (number - 1) *(-1)
        i += 1
    return result


# Funcion que le das un numero y te devuelve la serie de collatz

def es_par(n: int):
    if n % 2 == 0:
        return True
    return False

def generate_serie_5(n: int):
    result = [n]
    if n < 1:
        return []
    while n > 1:
        if es_par(n):
            n //= 2
            result.append(n)
        else:
            n *= 3 + 1
            result.append(n)
            
# Funcion que le paso un entero y me genera la siguiente serie
# 4 
# [1, 2, 3, 4]



# Le das un numero y te devuelvo ese numero de veces el fibonacci

def generate_serie_6(n:int):
    last_number = 0
    number = 1
    suma = 0
    result = [last_number, number]
    i = 2
    if n < 0:
        return []
    while i < n:
        suma = number + last_number
        last_number = number
        number = suma
        result.append(suma)
        i += 1
    return result


# Le das un numero y devuelve la posicion del fibonacci
def generate_serie_7(n:int):
    last_number = 0
    number = 1
    suma = 0
    i = 0
    if n < 0:
        return sys.maxsize
    while i < n:
        suma = number + last_number
        last_number = number
        number = suma
        i += 1
    return last_number



def middle_point(list):
    if len(list) < 1:
        return sys.maxsize
    return list[len(list)//2]
# Funcion que le das una lista y te devuelve el punto medio
