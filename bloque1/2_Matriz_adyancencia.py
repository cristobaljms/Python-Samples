def matriz_adj(g):
    l = list()
    for n in g:
        for v in n:
            if not v in l:
                l.append(v)
    l.sort()

    matrix = list()
    for i in l:
        a = list()
        for j in l:
            a.append(0)
        matrix.append(a)

    for n in g:
        posi = l.index(n[0])
        posj = l.index(n[1])
        matrix[posj][posi] = 1
    
    for i in range(len(matrix)):
        matrix[i] = tuple(matrix[i])
        
    return tuple(matrix)