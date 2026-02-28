import gc
from node import Node

# ... (tu clase Node aquí arriba) ...

if __name__ == '__main__':
    # 1. Creamos la estructura del árbol
    root = Node("Raíz")
    child1 = Node("Hijo 1")
    child2 = Node("Hijo 2")
    grandchild = Node("Nieto")

    # 2. Conectamos los nodos
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(grandchild)

    # 3. Comprobamos que la navegación hacia arriba funciona
    print("--- Navegación ---")
    print(f"Padre del nieto: {grandchild.get_parent().item}")
    print(f"Raíz desde el nieto (iterativa): {grandchild.get_root_iterative().item}")
    print(f"Raíz desde el nieto (recursiva): {grandchild.get_root_recursive().item}")

    # 4. PRUEBA DE FUEGO: Comprobar el weakref y el recolector de basura
    print("\n--- Prueba de Memoria ---")
    print(f"Antes de borrar: El padre de '{child1.item}' existe? {'Sí' if child1.get_parent() is not None else 'No'}")
    
    # Borramos la variable original de la raíz
    del root
    
    # Forzamos al recolector de basura a limpiar la memoria sin uso
    gc.collect() 

    # Si usáramos referencias fuertes normales, la raíz seguiría viva en memoria
    # oculta dentro del atributo __parent de child1 y child2. 
    # Como usamos weakref, la raíz se destruye de verdad.
    padre_actual = child1.get_parent()
    if padre_actual is None:
        print("ÉXITO: La raíz fue destruida de la memoria. El weakref funciona perfectamente devolviendo None.")
    else:
        print("ERROR: La raíz sigue viva en la memoria.")