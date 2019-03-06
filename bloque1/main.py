#!/usr/bin/env python
# -*- coding: utf-8 -*-

# EJERCICIO 1: Manipulacion de secuencias

def splitN(L, n):
    args = [iter(L)] * n
    return zip(*args)

# EJERCICIO 2: Matriz de adyacencia

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

# EJERCICIO 3: Arboles binarios

class BinaryTree:
    def __init__(self): self.tree = EmptyNode()
    def getTree(self) : return self.tree.getNode()
    def insert(self, value): self.tree = self.tree.insert(value)

class EmptyNode:
    def getNode(self):
        return None
    def insert(self,value):
        return BinaryNode(value, self, self)

class BinaryNode:
    def __init__(self, value, left, right):
        self.data, self.left, self.right = value, left, right

    def insert(self, value):
        if self.data > value:
            self.left = self.left.insert(value)
        elif self.data < value:
            self.right = self.right.insert(value)
        return self

    def getNode(self): return (self.data, self.left.getNode(), self.right.getNode() )

def arbol_binario(L):
    x = BinaryTree()
    for i in L:
        x.insert(i)
    return x.getTree()


# EJERCICIO 4: Búsqueda en arbol

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

# EJERCICIO 5: Árbol a conjunto
def arbol_a_conjunto(arbol):
    paso1 = str(arbol).split('(')
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



# EJERCICIO 6: Mezcla de diccionarios

def mezcla(A,B):
    C = dict()
    for key, value in A.items():
        C[key]=value
    for key, value in B.items():
        if key in C:
            C[key] = (C[key], value)
        else:
            C[key]=value        
    return C

# EJERCICIO 7: Busqueda de ciclos

from collections import defaultdict

def dfs(x, col, adj, parent=None):
    if col[x] == 1: return True
    if col[x] == 2: return False
    col[x] = 1
    res = False
    for y in adj[x]:
        if y == parent: continue
        if dfs(y, col, adj, x): res = True
    col[x] = 2
    return res

def hay_ciclo(g):
    adj = defaultdict(set)
    col = defaultdict(int)
    for x, y in g:
        adj[x].add(y)
        adj[y].add(x)
    
    for x in adj:
        if dfs(x, col, adj):  
            return True      
    return False   

# EJERCICIO 8: 
import re

def replaceFirstPerson(word):
    return word[:-2]+"o"

def replaceSecondPerson(word):
    if re.match("\w*(ar)", word):
        return word[:-2]+"as"
    else:
        return word[:-2]+"es"
    
def replaceThirtyPerson(word):
    if re.match("\w*(ar)", word):
        return word[:-2]+"a"
    else:
        return word[:-2]+"e"

def replaceFortyPerson(word):
    if re.match("\w*(ar)", word):
        return word[:-2]+"amos"
    elif re.match("\w*(er)", word):
        return word[:-2]+"emos"
    else:
        return word[:-2]+"imos"

def replaceFivetyPerson(word):
    if re.match("\w*(ar)", word):
        return word[:-2]+"áis"
    elif re.match("\w*(er)", word):
        return word[:-2]+"éis"
    else:
        return word[:-2]+"ís"

def replaceSixtyPerson(word):
    if re.match("\w*(ar)", word):
        return word[:-2]+"an"
    elif re.match("\w*(er)", word):
        return word[:-2]+"en"
    else:
        return word[:-2]+"en"

def presente_indicativo(verbo):
    if re.match("\w*(ar|er|ir)", verbo):
        result = list()
        result.append(replaceFirstPerson(verbo))
        result.append(replaceSecondPerson(verbo))
        result.append(replaceThirtyPerson(verbo))
        result.append(replaceFortyPerson(verbo))
        result.append(replaceFivetyPerson(verbo))
        result.append(replaceSixtyPerson(verbo))
        return result

# EJERCICIO 9: Cuartiles

def cuartiles(L):
    L = list(L)
    L.sort()
    Q1 = 0
    posQ1 = (len(L)+1)/float(4) 
    decimal = posQ1 - int(posQ1)
    if decimal > 0:
        Q1 = L[int(posQ1)-1] + decimal*(L[int(posQ1)]-L[int(posQ1)-1])
    else:
        Q1 = L[int(posQ1)-1]

    Q2 = 0
    posQ2 = 2*(len(L)+1)/float(4) 
    decimal = posQ2 - int(posQ2)
    if decimal > 0:
        Q2 = L[int(posQ2)-1] + decimal*(L[int(posQ2)]-L[int(posQ2)-1])
    else:
        Q2 = L[int(posQ2)-1]

    Q3 = 0
    posQ3 = 3*(len(L)+1)/float(4) 
    decimal = posQ3 - int(posQ3)
    if decimal > 0:
        Q3 = L[int(posQ3)-1] + decimal*(L[int(posQ3)]-L[int(posQ3)-1])
    else:
        Q3 = L[int(posQ3)-1]

    Q4 = L[-1]

    return (Q1, Q2, Q3, Q4)

# EJERCICIO 10: Cambio de notación de RPN a notación algebraica
OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRIORITY = {'+':1, '-':1, '*':2, '/':2}


def rpn_to_algebraic(s):
    s = s.split(' ')
    stack = []
    prev_op = None
    for ch in s:
        if not ch in OPERATORS:
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            expr = '('+a + ' ' + ch + ' ' + b+')'
            stack.append(expr)
            prev_op = ch
    return stack[-1]


from unittest import TestCase, main

class Test(TestCase):
    def test_splitN(self):
        self.assertEqual(list(splitN(range(6),3)), [(0,1,2),(3,4,5)])
        self.assertEqual(list(splitN(range(6),2)), [(0,1),(2,3),(4,5)])
        self.assertEqual(list(splitN(range(3),3)), [(0,1,2)])
        self.assertEqual(list(splitN([],3)), [])

    def test_matriz_adj(self):
        self.assertEqual(matriz_adj([(2,3), (2,4), (4,5), (5,2)]),
                         ((0,0,0,1), (1,0,0,0), (1,0,0,0), (0,0,1,0)))
        self.assertEqual(matriz_adj([(5,3), (4,4)]),
                         ((0,0,1), (0,1,0), (0,0,0)))
        self.assertEqual(matriz_adj([(5,5), (4,4)]),
                         ((1,0), (0,1)))
        self.assertEqual(matriz_adj([(5,1), (4,2)]),
                         ((0,0,0,1), (0,0,1,0), (0,0,0,0), (0,0,0,0)))

    def test_arbol_binario(self):
        self.assertEqual(arbol_binario([3, 8, 1, 13, 5, 9]),
                         (3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None))))
        self.assertEqual(arbol_binario(range(5)),
                         (0, None, (1, None, (2, None, (3, None, (4, None, None))))))
        self.assertEqual(arbol_binario(list(reversed(range(5)))),
                         (4, (3, (2, (1, (0, None, None), None), None), None), None))
        self.assertEqual(arbol_binario([]), None)

    def test_buscar(self):
        self.assertTrue(buscar((3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None))),
                               13))
        self.assertFalse(buscar((3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None))),
                                12))
        self.assertTrue(buscar((4, (3, (2, (1, (0, None, None), None), None), None), None),
                               0))
        self.assertFalse(buscar(None, 0))

    def test_arbol_a_conjunto(self):
        self.assertEqual(arbol_a_conjunto(None), set())
        self.assertEqual(arbol_a_conjunto((5,None,None)), {5})
        self.assertEqual(arbol_a_conjunto((3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None)))),
                         {3,8,1,13,5,9})
        self.assertEqual(arbol_a_conjunto((4, (3, (2, (1, (0, None, None), None), None), None), None)),
                         {0,1,2,3,4})

    def test_mezcla(self):
        self.assertEqual(mezcla({'a':1}, {'b':2}), {'a':1,'b':2})
        self.assertEqual(mezcla({'a':1,'e':2}, {'a':1,'b':2}), {'a':(1,1),'b':2,'e':2})
        self.assertEqual(mezcla({}, {}), {})
        self.assertEqual(mezcla({1:2,2:3,3:4}, {1:1,2:2,3:3}), {1:(2,1),2:(3,2),3:(4,3)})

    def test_hay_ciclo(self):
        self.assertTrue(hay_ciclo([(1,1)]))
        self.assertTrue(hay_ciclo([(1,2),(3,4),(2,3),(4,1)]))
        self.assertFalse(hay_ciclo([(1,2),(3,4),(2,3),(4,11)]))
        self.assertFalse(hay_ciclo([(1,2),(3,4),(2,3),(3,4)]))

    def test_conjugacion(self):
        self.assertEqual(presente_indicativo('amar'),
                         ['amo', 'amas', 'ama', 'amamos', 'amáis', 'aman'])
        self.assertEqual(presente_indicativo('leer'),
                         ['leo', 'lees', 'lee', 'leemos', 'leéis', 'leen'])
        self.assertEqual(presente_indicativo('batir'),
                         ['bato', 'bates', 'bate', 'batimos', 'batís', 'baten'])
        self.assertEqual(presente_indicativo('ir'),
                         ['o', 'es', 'e', 'imos', 'ís', 'en'])

    def test_cuartiles(self):
        self.assertEqual(cuartiles((63,34,60,30,45,32,56,40,21,37,54,33,28,53,19,45,28,52,24,29)),
                         (28.25, 35.5, 52.75, 63))
        self.assertEqual(cuartiles(range(10)), (1.75, 4.5, 7.25, 9))
        self.assertEqual(cuartiles((1,2,3)), (1,2,3,3))
        self.assertEqual(cuartiles((1,1,1)), (1,1,1,1))

    def test_rpn_to_algebraic(self):        
        self.assertEqual(rpn_to_algebraic('12 3 - 2 5 * +'), '((12 - 3) + (2 * 5))')
        self.assertEqual(rpn_to_algebraic('1 2 3 4 - - -'), '(1 - (2 - (3 - 4)))')
        self.assertEqual(rpn_to_algebraic('1 2 - 3 - 4 -'), '(((1 - 2) - 3) - 4)')
        self.assertEqual(rpn_to_algebraic('1'), '1')

main()
