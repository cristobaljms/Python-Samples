def arbol_a_conjunto(arbol):
    paso1 = str(tree).split('(')
    paso2 = list()
    for node in paso1:
        for v in node.split(')'):
            paso2.append(v)
    paso3 = list()
    for node in paso2:
        for v in node.split(','):
            paso3.append(v)
    paso4 = list()
    for node in paso3:
        for v in node.split('None'):
            paso4.append(v)
    paso5 = list()
    for node in paso4:
        for v in node.split(' '):
            paso5.append(v) 
    
    result = set()
    for v in paso5:
        if v != '':
            result.add(int(v))
    return result        

tree = (3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None)))


print (arbol_a_conjunto(tree))