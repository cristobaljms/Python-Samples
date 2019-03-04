def buscar(arbol, valor):
    while(arbol != None):
        arbol = list(arbol)
        if(arbol[0] == valor):
            return True
        else:
            if arbol[0] >= valor:
                arbol = arbol[1]
            else: 
                arbol = arbol[2]
    return False

# tree = (3, (1, None, None), (8, None, (13, (9, None, None), None)))
# value = 10

# print buscar(tree, value)