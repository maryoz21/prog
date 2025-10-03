# Funcion que le das una lista y te devuelva el valor medio entre el meno y el mayor

def smallest(list1):
    if len(list1) < 1:
        return sys.maxsize
    i = 1
    smallest = list1[0]
    while i < len(list1):
        if list1[i] < smallest:
            smallest = list1[i]
        i += 1
    return smallest

def greatest(list1):
    if len(list1) < 1:
        return sys.maxsize
    greatest = list1[0]
    i = 1
    while i < len(list1):
        if list1[i] > greatest:
            greatest = list1[i]
        i += 1
    return greatest

def middle_point(list1):
    if len(list1) < 1:
        return 0
    return (smallest(list1) + greatest(list1)) / 2

# Funcion que le das un numero y te devuelve la cantidad de veces ese numero al lista de fibonacci

def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)



# Funcion que le das un numero y imprime la tabla de multiplicar de ese numero 
# sin uar listas ejemplo: 7 devuelve 7x1=7, 7x2=14, 7x3=21...7x10=70
 
def tabla_multiplicar(n: int):
    if n < 1:
        return ""
    result = ""
    for i in range(1, 11):
        result += f"{n}x{i}={n*i}\n"
    return result

# Productorio de un numero
def productory(n: int):
    if n < 0:
        return sys.maxsize
    result = 1
    for i in range(1, n+1):
        result *= i
    return result