# Funcion que le das una lista y devuelve la lista inversa

def reverse_list(list1):
    if len(list1) == 0:
        return []
    return list1[::-1]

list1 = [5]
print(reverse_list(list1)) 