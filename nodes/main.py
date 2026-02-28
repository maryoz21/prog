from node import Node

root = Node("root")
child1 = Node("child1")
child2 = Node("child2")
child3 = Node("child3")

child1.set_parent(root)
child2.set_parent(root)
child3.set_parent(child1)
print("Arbol inicial:")
root.visit(lambda node: print(node.item))

child3.get_root_recursive().item
child3.get_root_iterative().item
child1.unlink()
child3.get_root_recursive().item
child3.get_root_iterative().item
print("Arbol final:")
root.visit(lambda node: print(node.item))

