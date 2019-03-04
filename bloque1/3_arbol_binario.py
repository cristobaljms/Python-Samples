class BinaryTree:
    def __init__(self): self.tree = EmptyNode()
    def __repr__(self): return '{}'.format(self.tree)
    def insert(self, value): self.tree = self.tree.insert(value)

class EmptyNode:
    def __repr__(self):
        return 'None'
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

    def __repr__(self):
        return '({}, {}, {})'.format(self.data, self.left, self.right )

def arbol_binario(L):
    x = BinaryTree()
    for i in L:
        x.insert(i)
    return x

L = [3, 8, 1, 13, 5, 9]
print(arbol_binario(L))